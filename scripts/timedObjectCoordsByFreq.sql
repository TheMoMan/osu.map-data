-- List time and coordinates of all objects sorted by frequency

.width 4 4 8 8 5
.once scripts/out/timedObjectCoordsByFreq.txt

SELECT x, y, time, type, COUNT(*) as freq
FROM objects
WHERE
  type != 'spinner'
  AND beatmap_id NOT IN (
    SELECT beatmap_id
    FROM beatmaps_web
    WHERE status = 'loved'
  )
GROUP BY x, y, time, type
ORDER BY freq DESC
LIMIT 1000;
