import sqlite3
import json

conn = sqlite3.connect('mapdata.db')

with open('inputs/lovedMaps.json') as f:
  mapIds = json.load(f)

beatmapWebs = [(int(mapId), 'loved',) for mapId in mapIds]
# test = (int(mapIds[0]), 'loved')

with conn:
  conn.executemany('INSERT INTO beatmaps_web (beatmap_id, status) values (?, ?)', beatmapWebs)
