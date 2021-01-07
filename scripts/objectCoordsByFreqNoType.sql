-- List coordinates of all objects sorted by frequency

.headers on
.mode csv
.once scripts/out/objectCoordsByFreqNoType.csv

SELECT x, y, COUNT(*) as freq
FROM objects
WHERE
  beatmap_id NOT IN (
    SELECT beatmap_id
    FROM beatmaps_web
    WHERE status = 'loved'
  )
  AND type != 'spinner'
GROUP BY x, y
ORDER BY freq DESC;
