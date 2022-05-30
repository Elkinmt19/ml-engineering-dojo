-- SIMPLE DATABASE CONFIGURATION FOR APPLICATION
SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET @@global.time_zone = "+00:00";
--
-- Database: `mlflow_entities_db`
--
DROP DATABASE IF EXISTS mlflow_entities_db;
CREATE DATABASE mlflow_entities_db;
