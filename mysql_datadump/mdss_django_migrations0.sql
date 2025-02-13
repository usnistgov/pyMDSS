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
-- Table structure for table `django_migrations`
--

DROP TABLE IF EXISTS `django_migrations`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_migrations` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=84 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_migrations`
--

LOCK TABLES `django_migrations` WRITE;
/*!40000 ALTER TABLE `django_migrations` DISABLE KEYS */;
INSERT INTO `django_migrations` VALUES (1,'contenttypes','0001_initial','2024-10-05 05:56:11.234022'),(2,'auth','0001_initial','2024-10-05 05:56:11.892586'),(3,'admin','0001_initial','2024-10-05 05:56:12.031506'),(4,'admin','0002_logentry_remove_auto_add','2024-10-05 05:56:12.038540'),(5,'admin','0003_logentry_add_action_flag_choices','2024-10-05 05:56:12.046823'),(6,'contenttypes','0002_remove_content_type_name','2024-10-05 05:56:12.125550'),(7,'auth','0002_alter_permission_name_max_length','2024-10-05 05:56:12.195081'),(8,'auth','0003_alter_user_email_max_length','2024-10-05 05:56:12.269760'),(9,'auth','0004_alter_user_username_opts','2024-10-05 05:56:12.287758'),(10,'auth','0005_alter_user_last_login_null','2024-10-05 05:56:12.350384'),(11,'auth','0006_require_contenttypes_0002','2024-10-05 05:56:12.353384'),(12,'auth','0007_alter_validators_add_error_messages','2024-10-05 05:56:12.365020'),(13,'auth','0008_alter_user_username_max_length','2024-10-05 05:56:12.431584'),(14,'auth','0009_alter_user_last_name_max_length','2024-10-05 05:56:12.495586'),(15,'auth','0010_alter_group_name_max_length','2024-10-05 05:56:12.550169'),(16,'auth','0011_update_proxy_permissions','2024-10-05 05:56:12.557729'),(17,'auth','0012_alter_user_first_name_max_length','2024-10-05 05:56:12.660340'),(18,'django_celery_results','0001_initial','2024-10-05 05:56:12.700340'),(19,'django_celery_results','0002_add_task_name_args_kwargs','2024-10-05 05:56:12.747119'),(20,'django_celery_results','0003_auto_20181106_1101','2024-10-05 05:56:12.752119'),(21,'django_celery_results','0004_auto_20190516_0412','2024-10-05 05:56:12.832742'),(22,'django_celery_results','0005_taskresult_worker','2024-10-05 05:56:12.869990'),(23,'django_celery_results','0006_taskresult_date_created','2024-10-05 05:56:12.930599'),(24,'django_celery_results','0007_remove_taskresult_hidden','2024-10-05 05:56:12.991245'),(25,'django_celery_results','0008_chordcounter','2024-10-05 05:56:13.017245'),(26,'django_celery_results','0009_groupresult','2024-10-05 05:56:13.277297'),(27,'django_celery_results','0010_remove_duplicate_indices','2024-10-05 05:56:13.287266'),(28,'django_celery_results','0011_taskresult_periodic_task_name','2024-10-05 05:56:13.312297'),(29,'resistors','0001_initial','2024-10-05 05:56:13.824422'),(30,'sessions','0001_initial','2024-10-05 05:56:13.870229'),(31,'resistors','0002_alter_search_standard_resistor_nominal','2024-10-05 06:06:08.750755'),(32,'resistors','0003_alter_search_standard_resistor_nominal','2024-10-05 06:06:08.818040'),(33,'resistors','0004_alter_search_standard_resistor_nominal','2024-10-05 06:09:56.485951'),(34,'resistors','0005_alter_search_standard_resistor_nominal','2024-10-05 15:46:43.467089'),(35,'resistors','0006_alter_search_standard_resistor_nominal','2024-10-05 15:50:07.464245'),(36,'resistors','0007_alter_search_standard_resistor_nominal','2024-10-05 16:51:07.688302'),(37,'resistors','0008_alter_warshawsky_process_meas_voltage','2024-10-07 01:15:48.485352'),(38,'resistors','0009_alter_hr3100_process_ccc_components_and_more','2024-10-07 01:37:45.434025'),(39,'resistors','0010_alter_hr3100_process_ccc_i_fb1_and_more','2024-10-07 01:43:36.803758'),(40,'resistors','0011_alter_hr3100_process_system_id','2024-10-07 01:45:09.914880'),(41,'resistors','0012_alter_hr3100_process_ccc_nom_ratio','2024-10-07 01:47:35.502676'),(42,'resistors','0013_alter_hr3100_process_ccc_i_fb1_and_more','2024-10-07 01:49:33.250684'),(43,'resistors','0014_alter_hr3100_process_ccc_r','2024-10-07 01:50:55.783985'),(44,'resistors','0015_alter_hr3100_process_sd_c_field','2024-10-07 01:53:21.046502'),(45,'resistors','0016_alter_hr3100_process_meassets','2024-10-07 01:55:32.845254'),(46,'resistors','0017_alter_hr3100_process_pred_c_field','2024-10-07 01:57:25.946307'),(47,'resistors','0018_alter_search_standard_resistor_format','2024-10-07 16:24:54.971107'),(48,'resistors','0019_alter_mi_6000b_process_mi_range_and_more','2024-10-07 17:03:42.981524'),(49,'resistors','0020_alter_nist_aab_process_pred_c_field','2024-10-07 19:59:00.553627'),(50,'resistors','0021_alter_nist_aab_process_room_temp','2024-10-07 20:06:26.780341'),(51,'resistors','0022_alter_nist_aab_process_room_rh','2024-10-07 20:07:58.108562'),(52,'resistors','0023_alter_nist_aab_process_left_rh_and_more','2024-10-07 20:11:19.378414'),(53,'resistors','0024_alter_nist_aab_process_aab_scanner','2024-10-07 20:25:55.427813'),(54,'resistors','0025_alter_nist_aab_process_date_decimal','2024-10-07 20:40:40.639544'),(55,'resistors','0026_alter_scaling_ccc_process_meas_delay','2024-10-08 02:38:32.218156'),(56,'resistors','0027_alter_scaling_ccc_process_pred_c_field','2024-10-08 02:39:58.318623'),(57,'resistors','0028_alter_scaling_ccc_process_ccc_r','2024-10-08 02:44:47.810224'),(58,'resistors','0029_alter_hr3100_process_nominal_and_more','2024-10-08 02:53:17.178410'),(59,'resistors','0030_alter_scaling_ccc_process_dvm_nplc_and_more','2024-10-08 02:57:15.211891'),(60,'resistors','0031_alter_scaling_ccc_process_pressure','2024-10-08 02:59:07.417010'),(61,'resistors','0032_alter_scaling_ccc_process_sd_c_field','2024-10-08 03:01:56.144848'),(62,'resistors','0033_alter_scaling_ccc_process_system_id','2024-10-08 03:03:53.472510'),(63,'resistors','0034_alter_scaling_ccc_process_sd_c_field','2024-10-08 03:25:14.683768'),(64,'resistors','0035_alter_scaling_ccc_process_ccc_nom_ratio_and_more','2024-10-08 03:25:15.963589'),(65,'resistors','0036_alter_scaling_ccc_process_area','2024-10-08 03:25:16.047558'),(66,'resistors','0037_alter_scaling_ccc_process_sd_c_field','2024-10-08 03:25:16.052556'),(67,'resistors','0038_alter_scaling_ccc_process_sd_c_field','2024-10-08 03:31:58.277046'),(68,'resistors','0039_remove_scaling_ccc_process_sd_c_field','2024-10-08 03:38:42.796902'),(69,'resistors','0040_scaling_ccc_process_sd_c_field','2024-10-08 03:43:07.125089'),(70,'resistors','0041_alter_scaling_ccc_process_sd_c_field','2024-10-08 03:45:30.239834'),(71,'resistors','0042_alter_hr3100_process_nominal_and_more','2024-10-08 18:43:40.375641'),(72,'resistors','0043_alter_mi_6000b_process_dvm_nplc_and_more','2024-10-10 15:37:50.188823'),(73,'resistors','0044_alter_magnicon_ccc_process_date','2024-10-10 16:03:45.744848'),(74,'resistors','0045_alter_mi_6000b_process_date','2024-10-10 19:42:21.897000'),(75,'resistors','0046_alter_scaling_ccc_process_date','2024-10-10 21:04:00.619725'),(76,'resistors','0047_alter_hr3100_process_date','2024-10-10 21:13:53.628245'),(77,'resistors','0048_alter_magnicon_ccc_process_end_time_and_more','2024-10-11 03:37:40.027055'),(78,'resistors','0049_alter_mi_6000b_process_end_time_and_more','2024-10-11 05:18:53.630396'),(79,'resistors','0050_alter_mi_6010c_process_serial','2024-10-11 06:20:46.242803'),(80,'resistors','0051_alter_mi_6010c_process_mi_stats','2024-10-11 15:53:49.816481'),(81,'resistors','0052_alter_nist_aab_process_date_decimal','2024-10-29 15:54:12.415077'),(82,'resistors','0053_alter_nist_aab_process_date_decimal','2024-10-29 15:54:14.315903'),(83,'resistors','0054_alter_nist_aab_process_date_decimal','2024-10-29 15:54:14.315903');
/*!40000 ALTER TABLE `django_migrations` ENABLE KEYS */;
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
