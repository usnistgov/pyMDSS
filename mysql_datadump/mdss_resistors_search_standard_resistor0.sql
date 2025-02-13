-- MySQL dump 10.13  Distrib 8.0.38, for Win64 (x86_64)
--
-- Host: 127.0.0.1    Database: mdss
-- ------------------------------------------------------
-- Server version	9.0.1

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `resistors_search_standard_resistor`
--

DROP TABLE IF EXISTS `resistors_search_standard_resistor`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `resistors_search_standard_resistor` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `Serial` varchar(20) NOT NULL,
  `Nominal` varchar(20) DEFAULT NULL,
  `Service Id` varchar(20) NOT NULL,
  `Process name` varchar(30) NOT NULL,
  `Format` varchar(10) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=217 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `resistors_search_standard_resistor`
--

LOCK TABLES `resistors_search_standard_resistor` WRITE;
/*!40000 ALTER TABLE `resistors_search_standard_resistor` DISABLE KEYS */;
INSERT INTO `resistors_search_standard_resistor` VALUES (5,'',NULL,'','',''),(6,'',NULL,'','',''),(7,'',NULL,'','',''),(8,'334041',NULL,'','',''),(9,'',NULL,'','',''),(10,'1216',NULL,'','',''),(11,'1216',NULL,'','',''),(12,'1216',NULL,'','',''),(13,'1216',NULL,'','',''),(14,'',NULL,'','',''),(15,'1215',NULL,'','',''),(16,'',NULL,'','',''),(17,'1215',NULL,'','',''),(18,'',NULL,'','',''),(19,'1215',NULL,'','',''),(20,'334041',NULL,'','',''),(21,'334041',NULL,'','',''),(22,'334041',NULL,'','',''),(23,'1214',NULL,'','',''),(24,'',NULL,'','',''),(25,'1215',NULL,'','',''),(26,'1215',NULL,'','',''),(27,'1215',NULL,'','',''),(28,'',NULL,'','',''),(29,'1215',NULL,'','',''),(30,'1215',NULL,'','',''),(31,'',NULL,'','',''),(32,'',NULL,'','',''),(33,'1215',NULL,'','',''),(34,'',NULL,'','',''),(35,'1215',NULL,'','',''),(36,'',NULL,'','',''),(37,'1215',NULL,'','',''),(38,'',NULL,'','',''),(39,'1215',NULL,'','',''),(40,'1215',NULL,'','',''),(41,'',NULL,'','',''),(42,'1215',NULL,'','',''),(43,'1215',NULL,'','',''),(44,'',NULL,'','',''),(45,'1215',NULL,'','',''),(46,'',NULL,'','',''),(47,'1215',NULL,'','',''),(48,'',NULL,'','',''),(49,'1215',NULL,'','',''),(50,'',NULL,'','',''),(51,'1215',NULL,'','',''),(52,'',NULL,'','',''),(53,'1215',NULL,'','',''),(54,'',NULL,'','',''),(55,'1215',NULL,'','',''),(56,'',NULL,'','',''),(57,'1214',NULL,'','',''),(58,'',NULL,'','',''),(59,'334041',NULL,'','',''),(60,'1214',NULL,'','',''),(61,'',NULL,'','',''),(62,'',NULL,'','',''),(63,'',NULL,'','',''),(64,'1215',NULL,'','',''),(65,'',NULL,'','',''),(66,'1215',NULL,'','',''),(67,'',NULL,'','',''),(68,'1214',NULL,'','',''),(69,'',NULL,'','',''),(70,'',NULL,'','',''),(71,'',NULL,'','',''),(72,'1215',NULL,'','',''),(73,'',NULL,'','',''),(74,'1214',NULL,'','',''),(75,'1215',NULL,'','',''),(76,'1216',NULL,'','',''),(77,'',NULL,'','',''),(78,'334041',NULL,'','',''),(79,'1216',NULL,'','',''),(80,'',NULL,'','',''),(81,'1214',NULL,'','',''),(82,'1215',NULL,'','',''),(83,'1216',NULL,'','',''),(84,'1214',NULL,'','',''),(85,'1218',NULL,'','',''),(86,'1215',NULL,'','',''),(87,'1218',NULL,'','',''),(88,'1216',NULL,'','',''),(89,'',NULL,'','',''),(90,'1216',NULL,'','',''),(91,'',NULL,'','',''),(92,'1446',NULL,'','',''),(93,'1216',NULL,'','',''),(94,'1216',NULL,'','Magnicon CCC Process',''),(95,'',NULL,'','',''),(96,'1216',NULL,'','',''),(97,'',NULL,'','',''),(98,'1215',NULL,'','Magnicon CCC Process',''),(99,'',NULL,'','',''),(100,'',NULL,'','',''),(101,'F005A',NULL,'','',''),(102,'F05A',NULL,'','',''),(103,'F054A',NULL,'','',''),(104,'F005A',NULL,'','',''),(105,'',NULL,'','',''),(106,'60906',NULL,'','',''),(107,'60659',NULL,'','',''),(108,'',NULL,'','',''),(109,'1019',NULL,'','',''),(110,'1016',NULL,'','',''),(111,'1027',NULL,'','',''),(112,'1100557',NULL,'','',''),(113,'1206',NULL,'','',''),(114,'',NULL,'','',''),(115,'1100577',NULL,'','',''),(116,'',NULL,'','',''),(117,'',NULL,'','',''),(118,'',NULL,'','',''),(119,'1100955',NULL,'','',''),(120,'',NULL,'','',''),(121,'','1E14','','',''),(122,'','1E12','','',''),(123,'','1^12','','',''),(124,'','1000000000000','','',''),(125,'','1000','','',''),(126,'1101151',NULL,'','',''),(127,'',NULL,'','',''),(128,'246691',NULL,'','',''),(129,'',NULL,'','',''),(130,'1101151',NULL,'','',''),(131,'',NULL,'','',''),(132,'1101151',NULL,'','',''),(133,'J/895',NULL,'','',''),(134,'',NULL,'','',''),(135,'66',NULL,'','',''),(136,'',NULL,'','',''),(137,'1D2',NULL,'','',''),(138,'01A',NULL,'','',''),(139,'',NULL,'','',''),(140,'F005A',NULL,'','',''),(141,'F005A',NULL,'','',''),(142,'',NULL,'','',''),(143,'1215',NULL,'','',''),(144,'1215',NULL,'','',''),(145,'1216',NULL,'','',''),(146,'',NULL,'','',''),(147,'1893938',NULL,'','',''),(148,'1893938',NULL,'','',''),(149,'1893938',NULL,'','',''),(150,'',NULL,'','',''),(151,'1893938',NULL,'','',''),(152,'',NULL,'','',''),(153,'1215',NULL,'','',''),(154,'F005A',NULL,'','',''),(155,'',NULL,'','',''),(156,'M1-2345133',NULL,'','',''),(157,'M1-2345133',NULL,'','',''),(158,'1658855',NULL,'','',''),(159,'',NULL,'','',''),(160,'1701679',NULL,'','',''),(161,'',NULL,'','',''),(162,'1020721',NULL,'','',''),(163,'',NULL,'','',''),(164,'',NULL,'','',''),(165,'',NULL,'','',''),(166,'',NULL,'','',''),(167,'',NULL,'','',''),(168,'',NULL,'','',''),(169,'',NULL,'','',''),(170,'1100356',NULL,'','',''),(171,'1102351',NULL,'','',''),(172,'1100820',NULL,'','',''),(173,'1100587',NULL,'','',''),(174,'',NULL,'','',''),(175,'246691',NULL,'','',''),(176,'234435',NULL,'','',''),(177,'19631-01',NULL,'','',''),(178,'',NULL,'','',''),(179,'J/8',NULL,'','',''),(180,'',NULL,'','',''),(181,'1100356',NULL,'','',''),(182,'',NULL,'','',''),(183,'246691',NULL,'','',''),(184,'',NULL,'','',''),(185,'',NULL,'','',''),(186,'F094A',NULL,'','',''),(187,'',NULL,'','',''),(188,'1100356',NULL,'','',''),(189,'J/8',NULL,'','',''),(190,'1100587',NULL,'','',''),(191,'1100820',NULL,'','',''),(192,'11002351',NULL,'','',''),(193,'1102351',NULL,'','',''),(194,'',NULL,'','',''),(195,'246691',NULL,'','',''),(196,'234435',NULL,'','',''),(197,'19631-01',NULL,'','',''),(198,'',NULL,'','',''),(199,'1105582',NULL,'','',''),(200,'268693',NULL,'','',''),(201,'',NULL,'','',''),(202,'246691',NULL,'','',''),(203,'234435',NULL,'','',''),(204,'19631-01',NULL,'','',''),(205,'',NULL,'','',''),(206,'1100356',NULL,'','',''),(207,'J/8',NULL,'','',''),(208,'1100587',NULL,'','',''),(209,'1100820',NULL,'','',''),(210,'1102351',NULL,'','',''),(211,'',NULL,'','',''),(212,'236066',NULL,'','',''),(213,'',NULL,'','',''),(214,'18669-02',NULL,'','',''),(215,'1103669',NULL,'','',''),(216,'268693',NULL,'','','');
/*!40000 ALTER TABLE `resistors_search_standard_resistor` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2025-02-11 23:42:21
