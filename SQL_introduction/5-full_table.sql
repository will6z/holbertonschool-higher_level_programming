-- This script prints the description of the table first_table from the specified database.

SELECT COLUMN_NAME, DATA_TYPE, CHARACTER_MAXIMUM_LENGTH
FROM INFORMATION_SCHEMA.COLUMNS
WHERE TABLE_SCHEMA = 'hbtn_0c_0'  -- Replace 'hbtn_0c_0' with the actual database name
  AND TABLE_NAME = 'first_table';

