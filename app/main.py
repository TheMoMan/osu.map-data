import sqlite3
import os
import time
from app import parseOsu
from app.lib import objects, beatmap
from app.utils import log

###
pathToMaps = 'maps/'
###

timeStart = time.time()

conn = sqlite3.connect('mapdata.db')
c = conn.cursor()

files = [file for file in os.listdir(pathToMaps)]
numberOfFiles = len(files)
fileNumber = 0

for file in files:
  fileNumber += 1
  print('Processing map {} of {} ({})'.format(fileNumber, numberOfFiles, file))

  path = pathToMaps + file

  with open(path, 'r') as f:
    beatmap = [line.rstrip() for line in f]
  
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
      c.execute('INSERT INTO beatmap_sets values (?, ?, ?, ?, ?, ?, ?, ?);', mapsetData)
  except sqlite3.IntegrityError:
    log('Skipped adding new mapset for {}'.format(file))
  
  # Add Map Data
  mapData = parseOsu.parseMapData(beatmap, file)
  beatmapId = mapData[0]

  try:
    with conn:
      c.execute('INSERT INTO beatmaps values (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);', mapData)
  except sqlite3.IntegrityError:
    log('Skipped adding new map for {}'.format(file))
    continue

  # Add Map Objects
  try:
    index = beatmap.index('[HitObjects]')
  except ValueError:
    log('Skipped adding objects for {}, cannot find objects'.format(file))

  with conn:
    for i, objectLine in enumerate(beatmap[index+1:]):
      hitObject = parseOsu.parseObject(objectLine, i, beatmapId)

      if hitObject[2] == 'circle':
        c.execute('REPLACE INTO objects (object_number, beatmap_id, type, time, x, y, new_combo) values (?, ?, ?, ?, ?, ?, ?);', hitObject)
      
      if hitObject[2] == 'slider':
        c.execute('REPLACE INTO objects values (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);', hitObject)
      
      if hitObject[2] == 'spinner':
        c.execute('REPLACE INTO objects (object_number, beatmap_id, type, time, x, y, new_combo, length) values (?, ?, ?, ?, ?, ?, ?, ?);', hitObject)

log('Finished in {}'.format(time.time() - timeStart))
