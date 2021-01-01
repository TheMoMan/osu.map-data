-- List coordinates of the first object of a map sorted by frequency

.once scripts/out/firstObjectCoordsByFreq.txt

SELECT x, y, COUNT(*) as freq
FROM objects
WHERE object_number = 0
GROUP BY x, y
ORDER BY freq DESC
LIMIT 1000;
