import sqlite3

print('Building coords...')
coords = [None] * 513
for i in range(len(coords)):
  coords[i] = [0] * 385

conn = sqlite3.connect('mapdata.db')
conn.row_factory = sqlite3.Row

print('Running query...')
c = conn.cursor()
c.execute('''
  SELECT x, y, COUNT(*) as freq
  FROM objects
  WHERE beatmap_id NOT IN (
    SELECT beatmap_id
    FROM beatmaps_web
    WHERE status = 'loved'
  )
  GROUP BY x, y;
''')

print('Updating coords...')
for row in c:
  try:
    coords[row['x']][row['y']] = int(row['freq'])
  except:
    print('skipped {} {}'.format(row['x'], row['y']))

print('Getting...')
for x, ys in enumerate(coords):
  lows = [[y, freq] for y, freq in enumerate(ys) if freq < 4]

  if len(lows) > 0:
    for y, freq in lows:
      print('{}, {}, {}'.format(x, y, freq))
