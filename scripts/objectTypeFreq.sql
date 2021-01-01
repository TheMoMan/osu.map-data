-- Gets frequency of each object type

SELECT type, count(*) as freq
FROM objects
GROUP BY type
