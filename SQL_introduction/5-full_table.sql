-- This script creates the table first_table with specified columns and properties.

CREATE TABLE IF NOT EXISTS `first_table` (
    `id` int NOT NULL AUTO_INCREMENT,
    `name` varchar(128) DEFAULT NULL,
    `c` char(1) DEFAULT NULL,
    `created_at` date DEFAULT NULL,
    PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

