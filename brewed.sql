CREATE TABLE `Employee` (
    `id`    INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    `name`  TEXT NOT NULL,
    `email` TEXT NOT NULL,
    `hourly_rate` INTEGER NOT NULL
);

CREATE TABLE `Product` (
    `id`    INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    `name`  TEXT NOT NULL,
    `price` REAL NOT NULL
);

CREATE TABLE `Order` (
    `id`    INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    `product_id`    INTEGER NOT NULL,
    `employee_id`   INTEGER NOT NULL,
    `timestamp`     INTEGER NOT NULL,
    FOREIGN KEY(`product_id`) REFERENCES `Product`(`id`),
    FOREIGN KEY(`employee_id`) REFERENCES `Employee`(`id`)
);

INSERT INTO `Employee` VALUES (null, "Bob", "null@null.com", 20);
INSERT INTO `Employee` VALUES (null, "Steve", "steve@null.com", 20);
INSERT INTO `Employee` VALUES (null, "Derek", "derek@null.com", 21);

INSERT INTO `Product` VALUES (null, "Snuggie", 29.99);
INSERT INTO `Product` VALUES (null, "Coffee", 29.98);
INSERT INTO `Product` VALUES (null, "Beer", 30);

INSERT INTO `Order` VALUES (null, 1, 3, 19991222);
INSERT INTO `Order` VALUES (null, 3, 2, 20010202);
INSERT INTO `Order` VALUES (null, 2, 1, 20040120);

SELECT 
o.id, 
o.timestamp,
p.name
FROM `Order` o
Join `Product` p
ON p.id = o.product_id

SELECT 
o.id, 
o.timestamp,
e.name
FROM `Order` o
Join `Employee` e
ON e.id = o.employee_id

SELECT * FROM `Product`;

SELECT * 
FROM `Product`
WHERE id = 1


DELETE FROM `Product`
WHERE id = 3
