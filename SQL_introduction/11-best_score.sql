-- This script lists all records with score >= 10 from the table second_table in the specified database.

SELECT score, name
FROM second_table
WHERE score >= 10
ORDER BY score DESC;

