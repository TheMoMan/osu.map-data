-- List time and coordinates of all objects sorted by frequency

.once scripts/out/timedObjectCoordsByFreq.txt

SELECT x, y, time, type, COUNT(*) as freq
FROM objects
GROUP BY x, y, time, type
ORDER BY freq DESC
LIMIT 1000;
