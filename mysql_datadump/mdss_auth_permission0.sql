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
-- Table structure for table `auth_permission`
--

DROP TABLE IF EXISTS `auth_permission`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_permission` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `content_type_id` int NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`),
  CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=97 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_permission`
--

LOCK TABLES `auth_permission` WRITE;
/*!40000 ALTER TABLE `auth_permission` DISABLE KEYS */;
INSERT INTO `auth_permission` VALUES (1,'Can add log entry',1,'add_logentry'),(2,'Can change log entry',1,'change_logentry'),(3,'Can delete log entry',1,'delete_logentry'),(4,'Can view log entry',1,'view_logentry'),(5,'Can add permission',2,'add_permission'),(6,'Can change permission',2,'change_permission'),(7,'Can delete permission',2,'delete_permission'),(8,'Can view permission',2,'view_permission'),(9,'Can add group',3,'add_group'),(10,'Can change group',3,'change_group'),(11,'Can delete group',3,'delete_group'),(12,'Can view group',3,'view_group'),(13,'Can add user',4,'add_user'),(14,'Can change user',4,'change_user'),(15,'Can delete user',4,'delete_user'),(16,'Can view user',4,'view_user'),(17,'Can add content type',5,'add_contenttype'),(18,'Can change content type',5,'change_contenttype'),(19,'Can delete content type',5,'delete_contenttype'),(20,'Can view content type',5,'view_contenttype'),(21,'Can add session',6,'add_session'),(22,'Can change session',6,'change_session'),(23,'Can delete session',6,'delete_session'),(24,'Can view session',6,'view_session'),(25,'Can add document',7,'add_document'),(26,'Can change document',7,'change_document'),(27,'Can delete document',7,'delete_document'),(28,'Can view document',7,'view_document'),(29,'Can add filename',8,'add_filename'),(30,'Can change filename',8,'change_filename'),(31,'Can delete filename',8,'delete_filename'),(32,'Can view filename',8,'view_filename'),(33,'Can add h r3100_ process',9,'add_hr3100_process'),(34,'Can change h r3100_ process',9,'change_hr3100_process'),(35,'Can delete h r3100_ process',9,'delete_hr3100_process'),(36,'Can view h r3100_ process',9,'view_hr3100_process'),(37,'Can add magnicon_cc c_ process',10,'add_magnicon_ccc_process'),(38,'Can change magnicon_cc c_ process',10,'change_magnicon_ccc_process'),(39,'Can delete magnicon_cc c_ process',10,'delete_magnicon_ccc_process'),(40,'Can view magnicon_cc c_ process',10,'view_magnicon_ccc_process'),(41,'Can add m i_6000 b_ process',11,'add_mi_6000b_process'),(42,'Can change m i_6000 b_ process',11,'change_mi_6000b_process'),(43,'Can delete m i_6000 b_ process',11,'delete_mi_6000b_process'),(44,'Can view m i_6000 b_ process',11,'view_mi_6000b_process'),(45,'Can add m i_6010 b_ process',12,'add_mi_6010b_process'),(46,'Can change m i_6010 b_ process',12,'change_mi_6010b_process'),(47,'Can delete m i_6010 b_ process',12,'delete_mi_6010b_process'),(48,'Can view m i_6010 b_ process',12,'view_mi_6010b_process'),(49,'Can add m i_6010 c_ process',13,'add_mi_6010c_process'),(50,'Can change m i_6010 c_ process',13,'change_mi_6010c_process'),(51,'Can delete m i_6010 c_ process',13,'delete_mi_6010c_process'),(52,'Can view m i_6010 c_ process',13,'view_mi_6010c_process'),(53,'Can add m i_6010 q_ process',14,'add_mi_6010q_process'),(54,'Can change m i_6010 q_ process',14,'change_mi_6010q_process'),(55,'Can delete m i_6010 q_ process',14,'delete_mi_6010q_process'),(56,'Can view m i_6010 q_ process',14,'view_mi_6010q_process'),(57,'Can add m i_6010s w_ process',15,'add_mi_6010sw_process'),(58,'Can change m i_6010s w_ process',15,'change_mi_6010sw_process'),(59,'Can delete m i_6010s w_ process',15,'delete_mi_6010sw_process'),(60,'Can view m i_6010s w_ process',15,'view_mi_6010sw_process'),(61,'Can add m i_6020 q_ process',16,'add_mi_6020q_process'),(62,'Can change m i_6020 q_ process',16,'change_mi_6020q_process'),(63,'Can delete m i_6020 q_ process',16,'delete_mi_6020q_process'),(64,'Can view m i_6020 q_ process',16,'view_mi_6020q_process'),(65,'Can add nis t_aa b_ process',17,'add_nist_aab_process'),(66,'Can change nis t_aa b_ process',17,'change_nist_aab_process'),(67,'Can delete nis t_aa b_ process',17,'delete_nist_aab_process'),(68,'Can view nis t_aa b_ process',17,'view_nist_aab_process'),(69,'Can add scaling_cc c_ process',18,'add_scaling_ccc_process'),(70,'Can change scaling_cc c_ process',18,'change_scaling_ccc_process'),(71,'Can delete scaling_cc c_ process',18,'delete_scaling_ccc_process'),(72,'Can view scaling_cc c_ process',18,'view_scaling_ccc_process'),(73,'Can add search_standard_resistor',19,'add_search_standard_resistor'),(74,'Can change search_standard_resistor',19,'change_search_standard_resistor'),(75,'Can delete search_standard_resistor',19,'delete_search_standard_resistor'),(76,'Can view search_standard_resistor',19,'view_search_standard_resistor'),(77,'Can add thomas_ process',20,'add_thomas_process'),(78,'Can change thomas_ process',20,'change_thomas_process'),(79,'Can delete thomas_ process',20,'delete_thomas_process'),(80,'Can view thomas_ process',20,'view_thomas_process'),(81,'Can add warshawsky_ process',21,'add_warshawsky_process'),(82,'Can change warshawsky_ process',21,'change_warshawsky_process'),(83,'Can delete warshawsky_ process',21,'delete_warshawsky_process'),(84,'Can view warshawsky_ process',21,'view_warshawsky_process'),(85,'Can add task result',22,'add_taskresult'),(86,'Can change task result',22,'change_taskresult'),(87,'Can delete task result',22,'delete_taskresult'),(88,'Can view task result',22,'view_taskresult'),(89,'Can add chord counter',23,'add_chordcounter'),(90,'Can change chord counter',23,'change_chordcounter'),(91,'Can delete chord counter',23,'delete_chordcounter'),(92,'Can view chord counter',23,'view_chordcounter'),(93,'Can add group result',24,'add_groupresult'),(94,'Can change group result',24,'change_groupresult'),(95,'Can delete group result',24,'delete_groupresult'),(96,'Can view group result',24,'view_groupresult');
/*!40000 ALTER TABLE `auth_permission` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2025-02-11 23:42:11
