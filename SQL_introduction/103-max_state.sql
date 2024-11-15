SELECT
    state,
    MAX(temperature) AS max_temp
FROM
    temperatures
GROUP BY
    state
ORDER BY
    state ASC;  -- Order results by state name

