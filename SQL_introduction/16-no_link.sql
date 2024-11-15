-- List all records in second_table where the name is not null
-- Displaying score and name in descending order by score

SELECT score, name
FROM second_table
WHERE name IS NOT NULL
ORDER BY score DESC;

