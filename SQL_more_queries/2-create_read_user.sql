-- creates a dabatase if it doesnt exist
CREATE DATABASE IF NOT EXISTS hbtn_0d_2;

-- creates a user
CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost' IDENTIFIED BY 'user_0d_2_pwd';

-- grants select privilages 
GRANT SELECT ON hbtn_0d_2.* TO 'user_0d_2'@'localhost';

