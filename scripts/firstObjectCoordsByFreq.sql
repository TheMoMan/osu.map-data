-- List coordinates of the first non-spinner object of a map sorted by frequency

-- .output csv
-- .once scripts/out/firstObjectCoordsByFreq.csv
.once scripts/out/firstObjectCoordsByFreq.txt

SELECT x, y, COUNT(*) as freq
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
GROUP BY x, y
ORDER BY freq DESC;
