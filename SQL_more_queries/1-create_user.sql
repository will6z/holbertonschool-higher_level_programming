-- Create user user_0d_1 with the specified password if not exists
CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost' IDENTIFIED BY 'user_0d_1_pwd';

-- Grant all privileges to user_0d_1
GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1'@'localhost' WITH GRANT OPTION;

-- Show grants for user_0d_1
SHOW GRANTS FOR 'user_0d_1'@'localhost';

