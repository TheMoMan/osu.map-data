-- List coordinates of all objects

.headers on
.mode csv
.once scripts/out/objectCoords.csv

SELECT x, y
FROM objects
WHERE
  beatmap_id NOT IN (
    SELECT beatmap_id
    FROM beatmaps_web
    WHERE status = 'loved'
  )
  AND type != 'spinner';
