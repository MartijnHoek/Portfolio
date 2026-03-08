CREATE TABLE regions (
    uuid CHAR(36) PRIMARY KEY,
    name VARCHAR(100) NOT NULL
);

CREATE TABLE countries (
   uuid CHAR(36) PRIMARY KEY,
   name VARCHAR(100) NOT NULL,
   region_uuid CHAR(36) NOT NULL,
   FOREIGN KEY (region_uuid) REFERENCES regions(uuid)
);
