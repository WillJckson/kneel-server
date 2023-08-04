CREATE TABLE `Metals`
(
    `id` INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    `metal` NVARCHAR(160) NOT NULL,
    `price` NUMERIC(5,2) NOT NULL
);

CREATE TABLE `Size`
(
    `id` INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    `carats` NUMERIC(5, 2) NOT NULL,
    `price` NUMERIC(10, 2) NOT NULL
);

CREATE TABLE `Styles`
(
    `id` INTEGER NOT NULL PRIMARY KEY,
    `style` NVARCHAR(100) NOT NULL,
    `price` NUMERIC(10, 2) NOT NULL
);

CREATE TABLE `Orders`
(
    `id` INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    `metal_id` INTEGER NOT NULL,
    `size_id` INTEGER NOT NULL,
    `style_id` INTEGER NOT NULL,
    -- Add other columns related to orders here
    FOREIGN KEY (`metal_id`) REFERENCES `Metals` (`id`),
    FOREIGN KEY (`size_id`) REFERENCES `Sizes` (`id`),
    FOREIGN KEY (`style_id`) REFERENCES `Styles` (`id`)
);

INSERT INTO `Metals` (`metal`, `price`)
VALUES
    ('Gold', 1500.00),
    ('Silver', 30.00),
    ('Platinum', 2000.00);

INSERT INTO `Size` (`carats`, `price`)
VALUES
    (1.00, 100.00),
    (0.50, 50.00),
    (2.00, 200.00);

INSERT INTO `Styles` (`style`, `price`)
VALUES
    ('Classic', 500.00),
    ('Modern', 700.00),
    ('Elegant', 800.00);

INSERT INTO `Orders` (`metal_id`, `size_id`, `style_id`)
VALUES
    (2, 2, 2),
    (3, 3, 3);

SELECT
    o.size_id,
    o.style_id,
    o.metal_id,
    m.metal,
    m.price
FROM `Orders` o
JOIN Metals m ON m.id = o.metal_id

SELECT
    o.id,
    o.metal_id,
    o.style_id,
    o.size_id,
    m.metal metal_metal,
    m.price metal_price,
    st.style style_style,
    st.price style_price,
    si.carats size_carats,
    si.price size_price
FROM `Orders` o
JOIN Metals m ON m.id = o.metal_id 
JOIN Styles st ON st.id = o.style_id 
JOIN Size si ON si.id = o.size_id

DROP TABLE Metals