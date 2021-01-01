-- Finds the most common circle by x and y
SELECT time, x, y, type, COUNT(*) as freq FROM objects
GROUP BY x, y
HAVING freq = (
  SELECT MAX(freq)
  FROM (
    SELECT COUNT(*) as freq
    FROM objects
    WHERE type = 'circle'
    GROUP BY x, y
  ) as t
)
LIMIT 50;
