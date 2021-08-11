-- MySQL dump 10.13  Distrib 8.0.25, for Linux (x86_64)
--
-- Host: localhost    Database: student_management_system2
-- ------------------------------------------------------
-- Server version	8.0.25-0ubuntu0.20.04.1

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
-- Table structure for table `auth_group`
--

DROP TABLE IF EXISTS `auth_group`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_group` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(150) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group`
--

LOCK TABLES `auth_group` WRITE;
/*!40000 ALTER TABLE `auth_group` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_group_permissions`
--

DROP TABLE IF EXISTS `auth_group_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_group_permissions` (
  `id` int NOT NULL AUTO_INCREMENT,
  `group_id` int NOT NULL,
  `permission_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group_permissions`
--

LOCK TABLES `auth_group_permissions` WRITE;
/*!40000 ALTER TABLE `auth_group_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group_permissions` ENABLE KEYS */;
UNLOCK TABLES;

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
) ENGINE=InnoDB AUTO_INCREMENT=45 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_permission`
--

LOCK TABLES `auth_permission` WRITE;
/*!40000 ALTER TABLE `auth_permission` DISABLE KEYS */;
INSERT INTO `auth_permission` VALUES (1,'Can add log entry',1,'add_logentry'),(2,'Can change log entry',1,'change_logentry'),(3,'Can delete log entry',1,'delete_logentry'),(4,'Can view log entry',1,'view_logentry'),(5,'Can add permission',2,'add_permission'),(6,'Can change permission',2,'change_permission'),(7,'Can delete permission',2,'delete_permission'),(8,'Can view permission',2,'view_permission'),(9,'Can add group',3,'add_group'),(10,'Can change group',3,'change_group'),(11,'Can delete group',3,'delete_group'),(12,'Can view group',3,'view_group'),(13,'Can add content type',4,'add_contenttype'),(14,'Can change content type',4,'change_contenttype'),(15,'Can delete content type',4,'delete_contenttype'),(16,'Can view content type',4,'view_contenttype'),(17,'Can add session',5,'add_session'),(18,'Can change session',5,'change_session'),(19,'Can delete session',5,'delete_session'),(20,'Can view session',5,'view_session'),(21,'Can add user',6,'add_customuser'),(22,'Can change user',6,'change_customuser'),(23,'Can delete user',6,'delete_customuser'),(24,'Can view user',6,'view_customuser'),(25,'Can add courses',7,'add_courses'),(26,'Can change courses',7,'change_courses'),(27,'Can delete courses',7,'delete_courses'),(28,'Can view courses',7,'view_courses'),(29,'Can add staffs',8,'add_staffs'),(30,'Can change staffs',8,'change_staffs'),(31,'Can delete staffs',8,'delete_staffs'),(32,'Can view staffs',8,'view_staffs'),(33,'Can add subjects',9,'add_subjects'),(34,'Can change subjects',9,'change_subjects'),(35,'Can delete subjects',9,'delete_subjects'),(36,'Can view subjects',9,'view_subjects'),(37,'Can add students',10,'add_students'),(38,'Can change students',10,'change_students'),(39,'Can delete students',10,'delete_students'),(40,'Can view students',10,'view_students'),(41,'Can add admin hod',11,'add_adminhod'),(42,'Can change admin hod',11,'change_adminhod'),(43,'Can delete admin hod',11,'delete_adminhod'),(44,'Can view admin hod',11,'view_adminhod');
/*!40000 ALTER TABLE `auth_permission` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_admin_log`
--

DROP TABLE IF EXISTS `django_admin_log`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_admin_log` (
  `id` int NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint unsigned NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int DEFAULT NULL,
  `user_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  KEY `django_admin_log_user_id_c564eba6_fk_student_m` (`user_id`),
  CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `django_admin_log_user_id_c564eba6_fk_student_m` FOREIGN KEY (`user_id`) REFERENCES `student_management_app_customuser` (`id`),
  CONSTRAINT `django_admin_log_chk_1` CHECK ((`action_flag` >= 0))
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_admin_log`
--

LOCK TABLES `django_admin_log` WRITE;
/*!40000 ALTER TABLE `django_admin_log` DISABLE KEYS */;
/*!40000 ALTER TABLE `django_admin_log` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_content_type`
--

DROP TABLE IF EXISTS `django_content_type`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_content_type` (
  `id` int NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=InnoDB AUTO_INCREMENT=12 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_content_type`
--

LOCK TABLES `django_content_type` WRITE;
/*!40000 ALTER TABLE `django_content_type` DISABLE KEYS */;
INSERT INTO `django_content_type` VALUES (1,'admin','logentry'),(3,'auth','group'),(2,'auth','permission'),(4,'contenttypes','contenttype'),(5,'sessions','session'),(11,'student_management_app','adminhod'),(7,'student_management_app','courses'),(6,'student_management_app','customuser'),(8,'student_management_app','staffs'),(10,'student_management_app','students'),(9,'student_management_app','subjects');
/*!40000 ALTER TABLE `django_content_type` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_migrations`
--

DROP TABLE IF EXISTS `django_migrations`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_migrations` (
  `id` int NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=20 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_migrations`
--

LOCK TABLES `django_migrations` WRITE;
/*!40000 ALTER TABLE `django_migrations` DISABLE KEYS */;
INSERT INTO `django_migrations` VALUES (1,'contenttypes','0001_initial','2021-08-04 19:22:17.547800'),(2,'contenttypes','0002_remove_content_type_name','2021-08-04 19:22:24.884295'),(3,'auth','0001_initial','2021-08-04 19:22:51.407758'),(4,'auth','0002_alter_permission_name_max_length','2021-08-04 19:22:58.003747'),(5,'auth','0003_alter_user_email_max_length','2021-08-04 19:22:58.845987'),(6,'auth','0004_alter_user_username_opts','2021-08-04 19:22:59.215651'),(7,'auth','0005_alter_user_last_login_null','2021-08-04 19:22:59.536352'),(8,'auth','0006_require_contenttypes_0002','2021-08-04 19:23:00.018157'),(9,'auth','0007_alter_validators_add_error_messages','2021-08-04 19:23:00.429432'),(10,'auth','0008_alter_user_username_max_length','2021-08-04 19:23:00.933186'),(11,'auth','0009_alter_user_last_name_max_length','2021-08-04 19:23:01.332001'),(12,'auth','0010_alter_group_name_max_length','2021-08-04 19:23:02.495260'),(13,'auth','0011_update_proxy_permissions','2021-08-04 19:23:02.748025'),(14,'auth','0012_alter_user_first_name_max_length','2021-08-04 19:23:03.078417'),(15,'student_management_app','0001_initial','2021-08-04 19:24:08.859330'),(16,'admin','0001_initial','2021-08-04 19:24:20.579875'),(17,'admin','0002_logentry_remove_auto_add','2021-08-04 19:24:20.811133'),(18,'admin','0003_logentry_add_action_flag_choices','2021-08-04 19:24:20.954575'),(19,'sessions','0001_initial','2021-08-04 19:24:25.983660');
/*!40000 ALTER TABLE `django_migrations` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_session`
--

DROP TABLE IF EXISTS `django_session`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_expire_date_a5c62663` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_session`
--

LOCK TABLES `django_session` WRITE;
/*!40000 ALTER TABLE `django_session` DISABLE KEYS */;
INSERT INTO `django_session` VALUES ('9areui1tulwn35iubaiki9z8luljwal3','.eJxVjM0OgjAQhN-lZ2PoUin1aMJzNLPdrRClIfycjO8u3OQ2M9_k-5iIbe3jtugcBzF3Y83lf2Okl5YDLOsmWtY4ouCp4xExTdduxPB-7K-uyKmcPT2Wfpc4q1JTJtcwsXhqBeobClWFmwZuPIGCp9rC-ToFJy0kZw6WU8oMZ74_u1g7Fw:1mCjOG:HDhf8pC2kpFmb-1I4SLwz7gMpEg9WUreX6fyxrwfCK8','2021-08-22 14:03:00.931324'),('isyev57e4j3lteti4ewy4cy9ellupr1x','.eJxVjMsOwiAURP-FtTE85FGXJv0OcuFepFFIU2Bl_Hfbnd3NzJmcD_Mwevaj0eYXZHc2scv_FiC-qB6g9YFUuy9Q4UnliLCu17nA8n7sr7niqZw9GVreJeB0TBR0JGHIJmeCCNyGm5QqRYtKOj0FbQQCOaeTUAkTcS65ATRKCPb9AeNcOvA:1mDdjh:Gj7aMRl3fBVxPEh5mBdsPraM5-Dl7s89978tVQjTo8Y','2021-08-25 02:12:53.076271'),('lne6twgb3et46hs4oko90cmc2x6anoaa','.eJxVjM0OgjAQhN-lZ2PoUin1aMJzNLPdrRClIfycjO8u3OQ2M9_k-5iIbe3jtugcBzF3Y83lf2Okl5YDLOsmWtY4ouCp4xExTdduxPB-7K-uyKmcPT2Wfpc4q1JTJtcwsXhqBeobClWFmwZuPIGCp9rC-ToFJy0kZw6WU8oMZ74_u1g7Fw:1mBOz2:XZurNeFhCW9szIyG4w06cz7PMSFybeNN2RMHoW2mtlw','2021-08-18 22:03:28.732141'),('nglq9m9zza0qetug502p61bkpr2jdauq','.eJxVjM0OgjAQhN-lZ2PoUin1aMJzNLPdrRClIfycjO8u3OQ2M9_k-5iIbe3jtugcBzF3Y83lf2Okl5YDLOsmWtY4ouCp4xExTdduxPB-7K-uyKmcPT2Wfpc4q1JTJtcwsXhqBeobClWFmwZuPIGCp9rC-ToFJy0kZw6WU8oMZ74_u1g7Fw:1mBxco:5kJA-yAWMh-xCrURLRyP01oH8b6HJDsZ1JdmhpY21K4','2021-08-20 11:02:50.027915');
/*!40000 ALTER TABLE `django_session` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `student_management_app_adminhod`
--

DROP TABLE IF EXISTS `student_management_app_adminhod`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `student_management_app_adminhod` (
  `id` int NOT NULL AUTO_INCREMENT,
  `created_at` datetime(6) NOT NULL,
  `updated_at` datetime(6) NOT NULL,
  `admin_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `admin_id` (`admin_id`),
  CONSTRAINT `student_management_a_admin_id_2d75304f_fk_student_m` FOREIGN KEY (`admin_id`) REFERENCES `student_management_app_customuser` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `student_management_app_adminhod`
--

LOCK TABLES `student_management_app_adminhod` WRITE;
/*!40000 ALTER TABLE `student_management_app_adminhod` DISABLE KEYS */;
INSERT INTO `student_management_app_adminhod` VALUES (1,'2021-08-04 19:25:34.161692','2021-08-04 19:25:34.161844',1),(2,'2021-08-10 03:53:21.094289','2021-08-10 03:53:21.094392',8),(3,'2021-08-10 04:11:15.695749','2021-08-10 04:11:15.695866',9),(4,'2021-08-10 04:19:09.385850','2021-08-10 04:19:09.385967',10);
/*!40000 ALTER TABLE `student_management_app_adminhod` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `student_management_app_courses`
--

DROP TABLE IF EXISTS `student_management_app_courses`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `student_management_app_courses` (
  `id` int NOT NULL AUTO_INCREMENT,
  `course_name` varchar(255) NOT NULL,
  `created_at` datetime(6) NOT NULL,
  `updated_at` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `student_management_app_courses`
--

LOCK TABLES `student_management_app_courses` WRITE;
/*!40000 ALTER TABLE `student_management_app_courses` DISABLE KEYS */;
INSERT INTO `student_management_app_courses` VALUES (1,'B.TECH','2021-08-04 19:27:19.666706','2021-08-04 19:27:19.666822'),(2,'B.E','2021-08-04 19:27:34.724635','2021-08-04 19:27:34.724773'),(3,'MBBS','2021-08-04 19:27:42.963680','2021-08-04 19:27:42.963814'),(4,'BSC','2021-08-04 19:27:50.515621','2021-08-04 19:27:50.515751');
/*!40000 ALTER TABLE `student_management_app_courses` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `student_management_app_customuser`
--

DROP TABLE IF EXISTS `student_management_app_customuser`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `student_management_app_customuser` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(150) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  `user_type` varchar(10) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB AUTO_INCREMENT=13 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `student_management_app_customuser`
--

LOCK TABLES `student_management_app_customuser` WRITE;
/*!40000 ALTER TABLE `student_management_app_customuser` DISABLE KEYS */;
INSERT INTO `student_management_app_customuser` VALUES (1,'pbkdf2_sha256$260000$USUdHb9I7zzWQcO8JaWRvo$Ue9wBU6Wlvlt7i9eaUXyHOBZDNjGPy2M0C7Kjlj+2LU=','2021-08-10 01:46:54.191128',1,'chandu@gmail.com','','','chandu@gmail.com',1,1,'2021-08-04 19:25:33.419902','1'),(2,'pbkdf2_sha256$260000$CWge1pHRnEVv9yL5HJEUkO$GYAO7/vOf2uVM7RZ9UDIq7LbQozDhUy6bFDas3nSALo=','2021-08-04 19:34:47.462979',0,'aatif','Aatif ','Siddiqui ','aatif@gmail.com',0,1,'2021-08-04 19:28:29.583317','3'),(3,'pbkdf2_sha256$260000$glhG6Q6EvbhFpRzANSgNcR$IpSfehW48VFrTJmFCQoQFhZ9XNVQhsG8tvp+i05Hyno=',NULL,0,'ajay','ajay','ajay','ajay@gmail.com',0,1,'2021-08-05 00:28:45.382613','2'),(4,'pbkdf2_sha256$260000$LIjfVeMyuY8rZC06S59FNF$AQA+Mrazl/FJ/p4yNzQI4KtioWVBqJMUrmN4sVtsY6g=',NULL,0,'anjalirahane123','anjali','rahane','anjali@gmail.com',0,1,'2021-08-05 00:30:03.769931','3'),(5,'pbkdf2_sha256$260000$RP3P3U37XkgPCdRwixXcy1$zTHSQ3YnTlPPOwQm5sTw1YUz8jM5zuJhRahOrGJJrnw=',NULL,0,'chandrakar1234','Chandrakar','Bhagat','chandrakarbhagat222@gmail.com',0,1,'2021-08-08 14:24:10.005752','2'),(6,'pbkdf2_sha256$260000$OdNMcE07y9S25uEoHH2PRk$6t3XqClKnYAzq3g4tyHIsWDonG2hFGz3CJxpDjsDnts=','2021-08-09 06:27:27.177188',0,'chandu12345','Chandrakar','Bhagat','chandrakarbhagat2222@gmail.com',0,1,'2021-08-08 14:28:45.174650','3'),(7,'pbkdf2_sha256$260000$2bwZGjr4wjrJT33OXpaP0D$dqcGo76eIOLGiJG6h4obS6JSlxKexEGfLHmMWfewxPM=',NULL,0,'pooja123','pooja','pooja','pooja@gmail.com',0,1,'2021-08-08 14:51:00.984473','3'),(8,'pbkdf2_sha256$260000$2ChtxgDAJ8NfAvxdfqrkbL$3XIPJVzFKK+4jg+3q6noqLnIR+ZZfg0Mn4e/+EJ/RDk=','2021-08-10 03:53:58.758360',0,'chandu1','','','chandu1@gmail.com',0,1,'2021-08-10 03:53:19.316811','1'),(9,'pbkdf2_sha256$260000$L86BQ6cVBgfp1O3IJ5vBNZ$+f/QqXRZteCFPyXjshUfVXbDvn309ZippwraUNLLi34=','2021-08-11 02:12:52.986630',0,'chandu2','','','chandu2@gmail.com',0,1,'2021-08-10 04:11:14.859706','1'),(10,'pbkdf2_sha256$260000$uSJWYriWQYcWMzbGfVLTyD$Gjv0T9wa+zuJ2ptebtejxr6NAMm/ew/oIeCPc0iqj6Y=',NULL,0,'chandu3','','','chandu3@gmail.com',0,1,'2021-08-10 04:19:08.698354','1'),(11,'pbkdf2_sha256$260000$KY5TrbN8HIjNxEZ13yc6Vg$+Iug2+wWw1qn+cZaOFFfdQN9Syb9ZVoN6ovw2uW4WFg=','2021-08-11 02:12:05.351944',0,'student1','student','mii','student1@gmail.com',0,1,'2021-08-10 05:53:38.471755','3'),(12,'pbkdf2_sha256$260000$PX5EZfzaQuuEsJMEflpJ6a$868jxvypgIy3nWn0ZkXcIe1hqragI+WIi/AyVP/2xW8=',NULL,0,'ruthawik123','Ruthawik','raja','ru@gmail.com',0,1,'2021-08-10 15:35:49.690637','3');
/*!40000 ALTER TABLE `student_management_app_customuser` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `student_management_app_customuser_groups`
--

DROP TABLE IF EXISTS `student_management_app_customuser_groups`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `student_management_app_customuser_groups` (
  `id` int NOT NULL AUTO_INCREMENT,
  `customuser_id` bigint NOT NULL,
  `group_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `student_management_app_c_customuser_id_group_id_d872a780_uniq` (`customuser_id`,`group_id`),
  KEY `student_management_a_group_id_61accfd6_fk_auth_grou` (`group_id`),
  CONSTRAINT `student_management_a_customuser_id_1e347552_fk_student_m` FOREIGN KEY (`customuser_id`) REFERENCES `student_management_app_customuser` (`id`),
  CONSTRAINT `student_management_a_group_id_61accfd6_fk_auth_grou` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `student_management_app_customuser_groups`
--

LOCK TABLES `student_management_app_customuser_groups` WRITE;
/*!40000 ALTER TABLE `student_management_app_customuser_groups` DISABLE KEYS */;
/*!40000 ALTER TABLE `student_management_app_customuser_groups` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `student_management_app_customuser_user_permissions`
--

DROP TABLE IF EXISTS `student_management_app_customuser_user_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `student_management_app_customuser_user_permissions` (
  `id` int NOT NULL AUTO_INCREMENT,
  `customuser_id` bigint NOT NULL,
  `permission_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `student_management_app_c_customuser_id_permission_af9a6989_uniq` (`customuser_id`,`permission_id`),
  KEY `student_management_a_permission_id_cd344297_fk_auth_perm` (`permission_id`),
  CONSTRAINT `student_management_a_customuser_id_41a474d7_fk_student_m` FOREIGN KEY (`customuser_id`) REFERENCES `student_management_app_customuser` (`id`),
  CONSTRAINT `student_management_a_permission_id_cd344297_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `student_management_app_customuser_user_permissions`
--

LOCK TABLES `student_management_app_customuser_user_permissions` WRITE;
/*!40000 ALTER TABLE `student_management_app_customuser_user_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `student_management_app_customuser_user_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `student_management_app_staffs`
--

DROP TABLE IF EXISTS `student_management_app_staffs`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `student_management_app_staffs` (
  `id` int NOT NULL AUTO_INCREMENT,
  `address` longtext NOT NULL,
  `created_at` datetime(6) NOT NULL,
  `updated_at` datetime(6) NOT NULL,
  `admin_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `admin_id` (`admin_id`),
  CONSTRAINT `student_management_a_admin_id_5bfdd57d_fk_student_m` FOREIGN KEY (`admin_id`) REFERENCES `student_management_app_customuser` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `student_management_app_staffs`
--

LOCK TABLES `student_management_app_staffs` WRITE;
/*!40000 ALTER TABLE `student_management_app_staffs` DISABLE KEYS */;
INSERT INTO `student_management_app_staffs` VALUES (1,'bhilai','2021-08-05 00:28:47.678148','2021-08-05 00:28:47.678241',3),(2,'bhilai','2021-08-08 14:24:11.101583','2021-08-08 14:24:11.101738',5);
/*!40000 ALTER TABLE `student_management_app_staffs` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `student_management_app_students`
--

DROP TABLE IF EXISTS `student_management_app_students`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `student_management_app_students` (
  `id` int NOT NULL AUTO_INCREMENT,
  `gender` varchar(255) NOT NULL,
  `profile_pic` varchar(100) NOT NULL,
  `address` longtext NOT NULL,
  `session_start_year` date NOT NULL,
  `session_end_year` date NOT NULL,
  `created_at` datetime(6) NOT NULL,
  `updated_at` datetime(6) NOT NULL,
  `admin_id` bigint NOT NULL,
  `course_id_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `admin_id` (`admin_id`),
  KEY `student_management_a_course_id_id_fcd09bed_fk_student_m` (`course_id_id`),
  CONSTRAINT `student_management_a_admin_id_1a8517ae_fk_student_m` FOREIGN KEY (`admin_id`) REFERENCES `student_management_app_customuser` (`id`),
  CONSTRAINT `student_management_a_course_id_id_fcd09bed_fk_student_m` FOREIGN KEY (`course_id_id`) REFERENCES `student_management_app_courses` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `student_management_app_students`
--

LOCK TABLES `student_management_app_students` WRITE;
/*!40000 ALTER TABLE `student_management_app_students` DISABLE KEYS */;
INSERT INTO `student_management_app_students` VALUES (1,'Male','/media/pic4_QNB9wPl.jpeg','pune','2021-08-10','2021-08-14','2021-08-04 19:28:30.424888','2021-08-04 19:28:30.424980',2,2),(2,'Female','/media/pic1_FazncmS.jpeg','pune','2021-08-13','2021-08-21','2021-08-05 00:30:04.520608','2021-08-05 00:30:04.520710',4,1),(3,'Male','/media/pic3.jpeg','pune','2021-08-13','2021-08-12','2021-08-08 14:28:46.033817','2021-08-08 14:28:46.033906',6,1),(5,'Male','/media/pic7.jpeg','bhilai','2020-01-01','2020-01-01','2021-08-10 05:53:41.730967','2021-08-10 05:53:41.731068',11,1),(6,'Male','/media/pic5.jpeg','pune','2020-01-01','2020-01-01','2021-08-10 15:35:50.617637','2021-08-10 15:35:50.617714',12,4);
/*!40000 ALTER TABLE `student_management_app_students` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `student_management_app_subjects`
--

DROP TABLE IF EXISTS `student_management_app_subjects`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `student_management_app_subjects` (
  `id` int NOT NULL AUTO_INCREMENT,
  `subject_name` varchar(255) NOT NULL,
  `created_at` datetime(6) NOT NULL,
  `updated_at` datetime(6) NOT NULL,
  `course_id_id` int NOT NULL,
  `staff_id_id` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `student_management_a_course_id_id_342668dd_fk_student_m` (`course_id_id`),
  KEY `student_management_a_staff_id_id_5f47119a_fk_student_m` (`staff_id_id`),
  CONSTRAINT `student_management_a_course_id_id_342668dd_fk_student_m` FOREIGN KEY (`course_id_id`) REFERENCES `student_management_app_courses` (`id`),
  CONSTRAINT `student_management_a_staff_id_id_5f47119a_fk_student_m` FOREIGN KEY (`staff_id_id`) REFERENCES `student_management_app_staffs` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `student_management_app_subjects`
--

LOCK TABLES `student_management_app_subjects` WRITE;
/*!40000 ALTER TABLE `student_management_app_subjects` DISABLE KEYS */;
/*!40000 ALTER TABLE `student_management_app_subjects` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2021-08-11 10:00:09
