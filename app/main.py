import sqlite3
import os
import time
from app import parseOsu
from app.lib import objects, beatmap

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
  print('Processing map {} of {}'.format(fileNumber, numberOfFiles))

  path = pathToMaps + file

  with open(path, 'r') as f:
    beatmap = [line.rstrip() for line in f]
  
  # Skip non-standard gamemodes for now
  mode = parseOsu.getMode(beatmap)
  if mode != '0':
    print('Skipped {} as not osu! standard gamemode'.format(file))
    continue

  # Add Mapset Data
  mapsetData = parseOsu.parseMapsetData(beatmap)

  try:
    with conn:
      c.execute('INSERT INTO beatmap_sets values (?, ?, ?, ?, ?, ?, ?, ?);', mapsetData)
  except sqlite3.IntegrityError:
    print('Skipped adding new mapset for {}'.format(file))
  
  # Add Map Data
  mapData = parseOsu.parseMapData(beatmap)
  beatmapId = mapData[0]

  try:
    with conn:
      c.execute('INSERT INTO beatmaps values (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);', mapData)
  except sqlite3.IntegrityError:
    print('Skipped adding new map for {}'.format(file))
    continue

  # Add Map Objects
  index = beatmap.index('[HitObjects]')

  with conn:
    for i, objectLine in enumerate(beatmap[index+1:]):
      hitObject = parseOsu.parseObject(objectLine, i, beatmapId)

      if hitObject[2] == 'circle':
        c.execute('REPLACE INTO objects (object_number, beatmap_id, type, time, x, y, new_combo) values (?, ?, ?, ?, ?, ?, ?);', hitObject)
      
      if hitObject[2] == 'slider':
        c.execute('REPLACE INTO objects values (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);', hitObject)
      
      if hitObject[2] == 'spinner':
        c.execute('REPLACE INTO objects (object_number, beatmap_id, type, time, x, y, new_combo, length) values (?, ?, ?, ?, ?, ?, ?, ?);', hitObject)

print('Finished in {}'.format(time.time() - timeStart))
