-- List coordinates of first non-spinner objects

.headers on
.mode csv
.once scripts/out/firstObjectCoords.csv

SELECT x, y
FROM (
  SELECT beatmap_id, x, y, MIN(object_number)
  FROM objects
  WHERE type != 'spinner'
  GROUP BY beatmap_id
)
WHERE
  beatmap_id NOT IN (
    SELECT beatmap_id
    FROM beatmaps_web
    WHERE status = 'loved'
  )
