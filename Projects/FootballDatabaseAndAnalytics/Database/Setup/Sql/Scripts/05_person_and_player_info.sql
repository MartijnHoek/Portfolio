CREATE TABLE person_info (
    uuid CHAR(36) PRIMARY KEY,
    first_name VARCHAR(100) NOT NULL,
    last_name VARCHAR(100) NOT NULL,
    country_uuid VARCHAR(36) NOT NULL,
    career_mode_uuid VARCHAR(36) NOT NULL,
    height_cm SMALLINT,
    weight_kg SMALLINT,
    birthyear INT,
    FOREIGN KEY (country_uuid) REFERENCES countries(uuid),
    FOREIGN KEY (career_mode_uuid) REFERENCES career_modes(uuid)
);

CREATE TABLE player_traits (
    person_uuid CHAR(36),
    trait_uuid CHAR(36),
    PRIMARY KEY (person_uuid, trait_uuid),
    FOREIGN KEY (person_uuid) REFERENCES person_info(uuid),
    FOREIGN KEY (trait_uuid) REFERENCES traits(uuid)
);

CREATE TABLE player_info (
    uuid CHAR(36) PRIMARY KEY,
    weak_foot TINYINT UNSIGNED,
    skill_moves TINYINT UNSIGNED,
    att_work_rate ENUM('LOW', 'MEDIUM', 'HIGH', 'NOT AVAILABLE') NOT NULL,
    def_work_rate ENUM('LOW', 'MEDIUM', 'HIGH', 'NOT AVAILABLE') NOT NULL,
    kit_number SMALLINT UNSIGNED,
    FOREIGN KEY (uuid) REFERENCES person_info(uuid)
);