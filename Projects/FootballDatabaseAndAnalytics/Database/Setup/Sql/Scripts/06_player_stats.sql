CREATE TABLE physical_stats (
    uuid CHAR(36) PRIMARY KEY,
    acceleration SMALLINT UNSIGNED,
    agility SMALLINT UNSIGNED,
    balance SMALLINT UNSIGNED,
    jumping SMALLINT UNSIGNED,
    reactions SMALLINT UNSIGNED,
    sprint_speed SMALLINT UNSIGNED,
    stamina SMALLINT UNSIGNED,
    strength SMALLINT UNSIGNED,
    FOREIGN KEY (uuid) REFERENCES person_info(uuid)
);

CREATE TABLE mental_stats (
    uuid CHAR(36) PRIMARY KEY,
    aggression SMALLINT UNSIGNED,
    att_positioning SMALLINT UNSIGNED,
    composure SMALLINT UNSIGNED,
    interceptions SMALLINT UNSIGNED,
    vision SMALLINT UNSIGNED,
    FOREIGN KEY (uuid) REFERENCES person_info(uuid)
);

CREATE TABLE technical_stats (
    uuid CHAR(36) PRIMARY KEY,
    ball_control SMALLINT UNSIGNED,
    crossing SMALLINT UNSIGNED,
    curve SMALLINT UNSIGNED,
    def_awareness SMALLINT UNSIGNED,
    dribbling SMALLINT UNSIGNED,
    fk_accuracy SMALLINT UNSIGNED,
    finishing SMALLINT UNSIGNED,
    heading_accuracy SMALLINT UNSIGNED,
    long_pass SMALLINT UNSIGNED,
    long_shots SMALLINT UNSIGNED,
    penalties SMALLINT UNSIGNED,
    short_pass SMALLINT UNSIGNED,
    shot_power SMALLINT UNSIGNED,
    slide_tackle SMALLINT UNSIGNED,
    stand_tackle SMALLINT UNSIGNED,
    volleys SMALLINT UNSIGNED,
    FOREIGN KEY (uuid) REFERENCES person_info(uuid)
);

CREATE TABLE goalkeeping_stats (
    uuid CHAR(36) PRIMARY KEY,
    gk_diving SMALLINT UNSIGNED,
    gk_handling SMALLINT UNSIGNED,
    gk_kicking SMALLINT UNSIGNED,
    gk_positioning SMALLINT UNSIGNED,
    gk_reflexes SMALLINT UNSIGNED,
    FOREIGN KEY (uuid) REFERENCES person_info(uuid)
);