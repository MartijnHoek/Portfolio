CREATE TABLE game_versions (
    uuid CHAR(36) PRIMARY KEY,
    name VARCHAR(50) NOT NULL
);

CREATE TABLE clubs (
    uuid CHAR(36) PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    country_uuid CHAR(36),
    FOREIGN KEY (country_uuid) REFERENCES countries(uuid)
);

CREATE TABLE career_modes (
    uuid CHAR(36) PRIMARY KEY,
    game_version_uuid CHAR(36),
    year INTEGER,
    club_uuid CHAR(36),
    FOREIGN KEY (game_version_uuid) REFERENCES game_versions(uuid),
    FOREIGN KEY (club_uuid) REFERENCES clubs(uuid)
);