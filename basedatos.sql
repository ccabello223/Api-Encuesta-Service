CREATE DATABASE IF NOT EXISTS ptecnica;
use ptecnica;

CREATE TABLE ptecnica_cacs(
  `id` int NOT NULL AUTO_INCREMENT,
  `email` varchar(50) NOT NULL,
  `edades` varchar(10) NOT NULL,
  `sexo` varchar(10) NOT NULL,
  `social_fav` varchar(50) NOT NULL COMMENT 'Red Social Favorita',
  `time_on_fc` int(25) NOT NULL COMMENT 'Tiempo en Facebook',
  `time_on_ws` int(25) NOT NULL COMMENT 'Tiempo en WhatsApp',
  `time_on_tw` int(25) NOT NULL COMMENT 'Tiempo en Twitter',
  `time_on_ig` int(25) NOT NULL COMMENT 'Tiempo en Instagram',
  `time_on_tk` int(25) NOT NULL COMMENT 'Tiempo en Tiktok',
  PRIMARY KEY (`id`)
) ENGINE = InnoDB;