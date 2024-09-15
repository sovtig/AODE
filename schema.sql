CREATE TABLE detections (
    id INT PRIMARY KEY,
    name VARCHAR(255),
    confidence FLOAT,
    x INT,
    y INT
);

CREATE TABLE images (
    id INT PRIMARY KEY,
    image_data BLOB
);