
CREATE SCHEMA IF NOT EXISTS `stackoverflow` DEFAULT CHARACTER SET utf8 ;
USE `stackoverflow` ;

CREATE TABLE IF NOT EXISTS `stackoverflow`.`user` (
  `userId` BINARY(16) NOT NULL,
  `username` VARCHAR(32),
  PRIMARY KEY (`userId`))
ENGINE = InnoDB;
