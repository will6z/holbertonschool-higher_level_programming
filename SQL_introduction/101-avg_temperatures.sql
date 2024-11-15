-- Select the city and calculate the average temperature rounded to four decimal places
SELECT
    city,
    ROUND(AVG(temperature), 4) AS avg_temp
-- Specify the table from which data is retrieved
FROM
    temperatures
-- Group the results by city to calculate the average temperature per city
GROUP BY
    city
-- Order the results by average temperature in descending order
ORDER BY
    avg_temp DESC;

