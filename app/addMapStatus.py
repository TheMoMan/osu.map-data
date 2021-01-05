import sqlite3
import json
from app.utils import log

conn = sqlite3.connect('mapdata.db')

with open('inputs/lovedMaps.json') as f:
  mapIds = json.load(f)

beatmapWebs = [(int(mapId), 'loved',) for mapId in mapIds]

log('Adding loved status data...')
try:
  with conn:
    conn.executemany('REPLACE INTO beatmaps_web (beatmap_id, status) values (?, ?)', beatmapWebs)
