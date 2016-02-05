DROP DATABASE xo_db;
CREATE DATABASE xo_db;
CREATE TABLE IF NOT EXISTS `xo_db`.`players` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `nickname` VARCHAR(50) NOT NULL COMMENT 'Nickname of player',
  `xp` INT NOT NULL COMMENT 'experience points',
  `email` VARCHAR(200) NOT NULL COMMENT 'Email of player, used for authentication',
  `password_hash` VARCHAR(200) NOT NULL COMMENT 'password salted hash',
  `created` DATETIME NOT NULL COMMENT 'player created timestamp(utc)',
  `updated` DATETIME NOT NULL COMMENT 'player updated timestamp(utc)',
  PRIMARY KEY (`id`),
  UNIQUE INDEX `nickname_unique_idx` (`nickname` ASC),
  UNIQUE INDEX `email_unique_idx` (`email` ASC))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8
COLLATE = utf8_general_ci
COMMENT = 'Main table for storing information about game players.';


CREATE TABLE IF NOT EXISTS `xo_db`.`player_sessions` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `player_id` INT NOT NULL COMMENT 'See players by id.',
  `sid` VARCHAR(40) NOT NULL COMMENT 'Unique session id',
  `ip_addr` VARCHAR(25) NULL COMMENT 'Ip address of user(text)',
  `created` DATETIME NOT NULL COMMENT 'session created timestamp(utc)',
  `updated` DATETIME NOT NULL COMMENT 'session updated timestamp(utc)',
  PRIMARY KEY (`id`),
  UNIQUE INDEX `sid_unique_idx` (`sid` ASC),
  INDEX `player_id_idx` (`player_id` ASC),
  CONSTRAINT `fk_session_player_id`
    FOREIGN KEY (`player_id`)
    REFERENCES `xo_db`.`players` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8
COLLATE = utf8_general_ci
COMMENT = 'Table for storing game sessions info.';


CREATE TABLE IF NOT EXISTS `xo_db`.`player_achievements` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `player_id` INT NOT NULL COMMENT 'Player unique id, see players.id.',
  `achievement_id` TINYINT NOT NULL,
  `created` DATETIME NOT NULL COMMENT 'utc timestamp',
  PRIMARY KEY (`id`),
  UNIQUE INDEX `player_achievement_unique_idx` (`player_id` ASC, `achievement_id` ASC),
  CONSTRAINT `fk_achievemnt_player_id`
    FOREIGN KEY (`player_id`)
    REFERENCES `xo_db`.`players` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB
COMMENT = 'List of player achievements';


CREATE TABLE IF NOT EXISTS `xo_db`.`log_game_events` (
  `id` BIGINT NOT NULL AUTO_INCREMENT,
  `player_id` INT NOT NULL COMMENT 'See players by id.',
  `event_type` INT NOT NULL COMMENT 'see balance for event codes describing',
  `event_data` TEXT NOT NULL COMMENT 'Event data(serialized in json)',
  `created` DATETIME NOT NULL COMMENT 'event date(utc timestamp)',
  PRIMARY KEY (`id`),
  INDEX `fk_player_id_idx` (`player_id` ASC),
  CONSTRAINT `fk_game_event_player_id`
    FOREIGN KEY (`player_id`)
    REFERENCES `xo_db`.`players` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


CREATE TABLE IF NOT EXISTS `xo_db`.`player_stats` (
  `id` INT NOT NULL,
  `player_id` INT NOT NULL,
  `stat_id` TINYINT NOT NULL,
  `value` INT NOT NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_player_id_idx` (`player_id` ASC),
  CONSTRAINT `fk_stats_player_id`
    FOREIGN KEY (`player_id`)
    REFERENCES `xo_db`.`players` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;
