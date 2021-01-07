import sqlite3

print('Building coords...')
circles = [None] * 513
for i in range(len(circles)):
  circles[i] = [0] * 385

sliders = [None] * 513
for i in range(len(sliders)):
  sliders[i] = [0] * 385

conn = sqlite3.connect('mapdata.db')
conn.row_factory = sqlite3.Row

print('Running query...')
c = conn.cursor()
c.execute('''
  SELECT x, y, type, COUNT(*) as freq
  FROM objects
  WHERE beatmap_id NOT IN (
    SELECT beatmap_id
    FROM beatmaps_web
    WHERE status = 'loved'
  )
  AND type != 'spinner'
  GROUP BY x, y, type;
''')

print('Updating coords...')
for row in c:
  try:
    if row['type'] == 'circle':
      circles[row['x']][row['y']] = int(row['freq'])
    else:
      sliders[row['x']][row['y']] = int(row['freq'])
  except:
    print('skipped {} {}'.format(row['x'], row['y']))

print('Getting...')
for i, arr in enumerate([circles, sliders]):
  for x, ys in enumerate(arr):
    lows = [[y, freq] for y, freq in enumerate(ys) if freq == 0]

    if len(lows) > 0:
      objectType = 'circle' if i == 0 else 'slider'

      for y, freq in lows:
        print('{}, {}, {}, {}'.format(x, y, freq, objectType))
