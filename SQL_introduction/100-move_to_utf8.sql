-- Select the database first
USE hbtn_0c_0;

-- Convert database to UTF8 (utf8mb4) with utf8mb4_unicode_ci collation
ALTER DATABASE hbtn_0c_0 CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

-- Convert table first_table to UTF8 (utf8mb4) with utf8mb4_unicode_ci collation
ALTER TABLE first_table CONVERT TO CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

-- Convert field name in first_table to use utf8mb4_unicode_ci collation
ALTER TABLE first_table MODIFY name VARCHAR(256) COLLATE utf8mb4_unicode_ci;
