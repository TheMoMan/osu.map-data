import sqlite3
import os
import time
from app import parseOsu
from app.lib import objects, beatmap
from app.utils import log

###
pathToMaps = 'maps/'
databaseFile = 'mapdata.db'
###

timeStart = time.time()

conn = sqlite3.connect(databaseFile)

files = [file for file in os.listdir(pathToMaps)]
numberOfFiles = len(files)
fileNumber = 0

circles = []
sliders = []
spinners = []

for file in files:
  fileNumber += 1
  log('Processing map {} of {} ({})'.format(fileNumber, numberOfFiles, file))

  path = pathToMaps + file

  try:
    with open(path, 'r') as f:
      beatmap = [line.rstrip() for line in f]
  except:
    log('Couldn\'t read file {}, check encoding?'.format(file))
    continue
  
  if len(beatmap) == 0:
    log('Skipped {} as file was empty'.format(file))
    continue

  # Skip non-standard gamemodes for now
  mode = parseOsu.getMode(beatmap)
  if mode != '0':
    log('Skipped {} as not osu! standard gamemode'.format(file))
    continue

  # Add Mapset Data
  mapsetData = parseOsu.parseMapsetData(beatmap)

  try:
    with conn:
      conn.execute('INSERT INTO beatmap_sets values (?, ?, ?, ?, ?, ?, ?, ?);', mapsetData)
  except sqlite3.IntegrityError:
    log('Skipped adding new mapset for {}'.format(file))
  
  # Add Map Data
  mapData = parseOsu.parseMapData(beatmap, file)
  beatmapId = mapData[0]

  try:
    with conn:
      conn.execute('INSERT INTO beatmaps values (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);', mapData)
  except sqlite3.IntegrityError:
    log('Skipped adding new map for {}'.format(file))
    continue

  # Add Map Objects
  try:
    index = beatmap.index('[HitObjects]')
  except ValueError:
    log('Skipped adding objects for {}, cannot find objects'.format(file))
    continue

  for i, objectLine in enumerate(beatmap[index+1:]):
    try:
      hitObject = parseOsu.parseObject(objectLine, i, beatmapId)
    except:
      log('Couldn\'t parse object number {} for {}'.format(i, file))
      continue

    if hitObject[2] == 'circle':
      circles.append(hitObject)
    
    if hitObject[2] == 'slider':
      sliders.append(hitObject)
  
    if hitObject[2] == 'spinner':
      spinners.append(hitObject)

  # Batch insert
  if fileNumber % 5000 == 0 or fileNumber == numberOfFiles:
    with conn:
      log('Inserting circles...')
      conn.executemany('INSERT INTO objects (object_number, beatmap_id, type, time, x, y, new_combo) VALUES (?, ?, ?, ?, ?, ?, ?);', circles)

      log('Inserting sliders...')
      conn.executemany('INSERT INTO objects VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);', sliders)

      log('Inserting spinners...')
      conn.executemany('INSERT INTO objects (object_number, beatmap_id, type, time, x, y, new_combo, length) VALUES (?, ?, ?, ?, ?, ?, ?, ?);', spinners)

    circles = []
    sliders = []
    spinners = []

log('Finished in {}'.format(time.time() - timeStart))
