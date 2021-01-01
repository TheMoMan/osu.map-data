-- List coordinates of all objects sorted by frequency

.once scripts/out/objectCoordsByFreq.txt

SELECT x, y, type, COUNT(*) as freq
FROM objects
GROUP BY x, y, type
ORDER BY freq DESC;
