-- MySQL dump 10.13  Distrib 8.0.36, for Win64 (x86_64)
--
-- Host: localhost    Database: rp2024
-- ------------------------------------------------------
-- Server version	8.0.36

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `auth_group`
--
ALTER USER 'root'@'%' IDENTIFIED WITH mysql_native_password BY 'root';
FLUSH PRIVILEGES;

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
  `id` bigint NOT NULL AUTO_INCREMENT,
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
) ENGINE=InnoDB AUTO_INCREMENT=61 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_permission`
--

LOCK TABLES `auth_permission` WRITE;
/*!40000 ALTER TABLE `auth_permission` DISABLE KEYS */;
INSERT INTO `auth_permission` VALUES (1,'Can add log entry',1,'add_logentry'),(2,'Can change log entry',1,'change_logentry'),(3,'Can delete log entry',1,'delete_logentry'),(4,'Can view log entry',1,'view_logentry'),(5,'Can add permission',2,'add_permission'),(6,'Can change permission',2,'change_permission'),(7,'Can delete permission',2,'delete_permission'),(8,'Can view permission',2,'view_permission'),(9,'Can add group',3,'add_group'),(10,'Can change group',3,'change_group'),(11,'Can delete group',3,'delete_group'),(12,'Can view group',3,'view_group'),(13,'Can add user',4,'add_user'),(14,'Can change user',4,'change_user'),(15,'Can delete user',4,'delete_user'),(16,'Can view user',4,'view_user'),(17,'Can add content type',5,'add_contenttype'),(18,'Can change content type',5,'change_contenttype'),(19,'Can delete content type',5,'delete_contenttype'),(20,'Can view content type',5,'view_contenttype'),(21,'Can add session',6,'add_session'),(22,'Can change session',6,'change_session'),(23,'Can delete session',6,'delete_session'),(24,'Can view session',6,'view_session'),(25,'Can add novel',7,'add_novel'),(26,'Can change novel',7,'change_novel'),(27,'Can delete novel',7,'delete_novel'),(28,'Can view novel',7,'view_novel'),(29,'Can add author',8,'add_author'),(30,'Can change author',8,'change_author'),(31,'Can delete author',8,'delete_author'),(32,'Can view author',8,'view_author'),(33,'Can add novel_category',9,'add_novel_category'),(34,'Can change novel_category',9,'change_novel_category'),(35,'Can delete novel_category',9,'delete_novel_category'),(36,'Can view novel_category',9,'view_novel_category'),(37,'Can add novel_chapter',10,'add_novel_chapter'),(38,'Can change novel_chapter',10,'change_novel_chapter'),(39,'Can delete novel_chapter',10,'delete_novel_chapter'),(40,'Can view novel_chapter',10,'view_novel_chapter'),(41,'Can add comment',11,'add_comment'),(42,'Can change comment',11,'change_comment'),(43,'Can delete comment',11,'delete_comment'),(44,'Can view comment',11,'view_comment'),(45,'Can add novel_list',12,'add_novel_list'),(46,'Can change novel_list',12,'change_novel_list'),(47,'Can delete novel_list',12,'delete_novel_list'),(48,'Can view novel_list',12,'view_novel_list'),(49,'Can add recently_reading',13,'add_recently_reading'),(50,'Can change recently_reading',13,'change_recently_reading'),(51,'Can delete recently_reading',13,'delete_recently_reading'),(52,'Can view recently_reading',13,'view_recently_reading'),(53,'Can add bookmark',14,'add_bookmark'),(54,'Can change bookmark',14,'change_bookmark'),(55,'Can delete bookmark',14,'delete_bookmark'),(56,'Can view bookmark',14,'view_bookmark'),(57,'Can add user',15,'add_user'),(58,'Can change user',15,'change_user'),(59,'Can delete user',15,'delete_user'),(60,'Can view user',15,'view_user');
/*!40000 ALTER TABLE `auth_permission` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user`
--

DROP TABLE IF EXISTS `auth_user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_user` (
  `id` int NOT NULL AUTO_INCREMENT,
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
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user`
--

LOCK TABLES `auth_user` WRITE;
/*!40000 ALTER TABLE `auth_user` DISABLE KEYS */;
INSERT INTO `auth_user` VALUES (1,'pbkdf2_sha256$260000$aHtsjCl2qCijtMl9m7AW97$MSnBGsGidKH4cYBHyaHBOKEzNomWUkj1UblOWSe4TyQ=','2024-08-23 12:28:04.952862',1,'root','','','1@1.com',1,1,'2024-08-23 12:28:01.883535'),(2,'pbkdf2_sha256$260000$m35DjeeLwx6dm3JOug1AMR$ZUhjUJOvPKgGR6qV5P+26kWZ1eGHVWCPNm8fbfUZsNQ=',NULL,1,'1','','','1@1.com',1,1,'2024-08-23 13:24:04.445836');
/*!40000 ALTER TABLE `auth_user` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user_groups`
--

DROP TABLE IF EXISTS `auth_user_groups`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_user_groups` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `user_id` int NOT NULL,
  `group_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`),
  CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_groups`
--

LOCK TABLES `auth_user_groups` WRITE;
/*!40000 ALTER TABLE `auth_user_groups` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_groups` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user_user_permissions`
--

DROP TABLE IF EXISTS `auth_user_user_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_user_user_permissions` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `user_id` int NOT NULL,
  `permission_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  KEY `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_user_permissions`
--

LOCK TABLES `auth_user_user_permissions` WRITE;
/*!40000 ALTER TABLE `auth_user_user_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_user_permissions` ENABLE KEYS */;
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
  `user_id` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  KEY `django_admin_log_user_id_c564eba6_fk_auth_user_id` (`user_id`),
  CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`),
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
) ENGINE=InnoDB AUTO_INCREMENT=16 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_content_type`
--

LOCK TABLES `django_content_type` WRITE;
/*!40000 ALTER TABLE `django_content_type` DISABLE KEYS */;
INSERT INTO `django_content_type` VALUES (1,'admin','logentry'),(3,'auth','group'),(2,'auth','permission'),(4,'auth','user'),(5,'contenttypes','contenttype'),(8,'novels','author'),(14,'novels','bookmark'),(11,'novels','comment'),(7,'novels','novel'),(9,'novels','novel_category'),(10,'novels','novel_chapter'),(12,'novels','novel_list'),(13,'novels','recently_reading'),(6,'sessions','session'),(15,'users','user');
/*!40000 ALTER TABLE `django_content_type` ENABLE KEYS */;
UNLOCK TABLES;

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
) ENGINE=InnoDB AUTO_INCREMENT=22 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_migrations`
--

LOCK TABLES `django_migrations` WRITE;
/*!40000 ALTER TABLE `django_migrations` DISABLE KEYS */;
INSERT INTO `django_migrations` VALUES (1,'contenttypes','0001_initial','2024-08-23 12:26:57.051108'),(2,'auth','0001_initial','2024-08-23 12:26:58.531693'),(3,'admin','0001_initial','2024-08-23 12:26:58.879870'),(4,'admin','0002_logentry_remove_auto_add','2024-08-23 12:26:58.895514'),(5,'admin','0003_logentry_add_action_flag_choices','2024-08-23 12:26:58.911115'),(6,'contenttypes','0002_remove_content_type_name','2024-08-23 12:26:59.052861'),(7,'auth','0002_alter_permission_name_max_length','2024-08-23 12:26:59.179399'),(8,'auth','0003_alter_user_email_max_length','2024-08-23 12:26:59.195048'),(9,'auth','0004_alter_user_username_opts','2024-08-23 12:26:59.219186'),(10,'auth','0005_alter_user_last_login_null','2024-08-23 12:26:59.305527'),(11,'auth','0006_require_contenttypes_0002','2024-08-23 12:26:59.321998'),(12,'auth','0007_alter_validators_add_error_messages','2024-08-23 12:26:59.337688'),(13,'auth','0008_alter_user_username_max_length','2024-08-23 12:26:59.447687'),(14,'auth','0009_alter_user_last_name_max_length','2024-08-23 12:26:59.588799'),(15,'auth','0010_alter_group_name_max_length','2024-08-23 12:26:59.636160'),(16,'auth','0011_update_proxy_permissions','2024-08-23 12:26:59.651789'),(17,'auth','0012_alter_user_first_name_max_length','2024-08-23 12:26:59.761624'),(18,'sessions','0001_initial','2024-08-23 12:26:59.840220'),(19,'users','0001_initial','2024-08-23 13:22:16.246246'),(20,'novels','0001_initial','2024-08-23 13:22:16.728752'),(21,'novels','0002_initial','2024-08-23 13:22:18.129341');
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
INSERT INTO `django_session` VALUES ('oipzbn4mmxv7obz3iajmd452938y0329','.eJxVjMsOwiAQRf-FtSGFTmVw6b7fQAZmkKqBpI-V8d-1SRe6veec-1KBtrWEbZE5TKwuyqjT7xYpPaTugO9Ub02nVtd5inpX9EEXPTaW5_Vw_w4KLeVbkxdiA9yRcQlM5ugATZbeoWcfEQaIiNKDBcdDkiEz24gW5UzJdVm9P_gsOHY:1shTOe:7kuCKtGm0UW9XDP3Re4Rz--i0i7uWTaHGqLPqbmzAfs','2024-09-06 12:28:04.957188');
/*!40000 ALTER TABLE `django_session` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `novels_author`
--

DROP TABLE IF EXISTS `novels_author`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `novels_author` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `author_name` varchar(32) NOT NULL,
  `author_gender` int NOT NULL,
  `author_detail` longtext NOT NULL,
  `author_icon` varchar(100) NOT NULL,
  `author_user_id` bigint DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `author_user_id` (`author_user_id`),
  CONSTRAINT `novels_author_author_user_id_ea0ac1fc_fk_users_user_id` FOREIGN KEY (`author_user_id`) REFERENCES `users_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `novels_author`
--

LOCK TABLES `novels_author` WRITE;
/*!40000 ALTER TABLE `novels_author` DISABLE KEYS */;
/*!40000 ALTER TABLE `novels_author` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `novels_bookmark`
--

DROP TABLE IF EXISTS `novels_bookmark`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `novels_bookmark` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `cfi` varchar(255) NOT NULL,
  `note` longtext NOT NULL,
  `is_public` tinyint(1) NOT NULL,
  `type` varchar(255) DEFAULT NULL,
  `novel_id` bigint NOT NULL,
  `novel_chapter_id` bigint NOT NULL,
  `user_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `novels_bookmark_novel_id_07421da2_fk_novels_novel_id` (`novel_id`),
  KEY `novels_bookmark_novel_chapter_id_c23db043_fk_novels_no` (`novel_chapter_id`),
  KEY `novels_bookmark_user_id_da61b0d5_fk_users_user_id` (`user_id`),
  CONSTRAINT `novels_bookmark_novel_chapter_id_c23db043_fk_novels_no` FOREIGN KEY (`novel_chapter_id`) REFERENCES `novels_novel_chapter` (`id`),
  CONSTRAINT `novels_bookmark_novel_id_07421da2_fk_novels_novel_id` FOREIGN KEY (`novel_id`) REFERENCES `novels_novel` (`id`),
  CONSTRAINT `novels_bookmark_user_id_da61b0d5_fk_users_user_id` FOREIGN KEY (`user_id`) REFERENCES `users_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `novels_bookmark`
--

LOCK TABLES `novels_bookmark` WRITE;
/*!40000 ALTER TABLE `novels_bookmark` DISABLE KEYS */;
/*!40000 ALTER TABLE `novels_bookmark` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `novels_comment`
--

DROP TABLE IF EXISTS `novels_comment`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `novels_comment` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `comment_time` datetime(6) NOT NULL,
  `comment_content` longtext NOT NULL,
  `up_number` int NOT NULL,
  `chapter_id` bigint DEFAULT NULL,
  `novel_id` bigint NOT NULL,
  `user_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `novels_comment_chapter_id_76bc8bff` (`chapter_id`),
  KEY `novels_comment_novel_id_b4abf5f5` (`novel_id`),
  KEY `novels_comment_user_id_e52c0e6e` (`user_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `novels_comment`
--

LOCK TABLES `novels_comment` WRITE;
/*!40000 ALTER TABLE `novels_comment` DISABLE KEYS */;
/*!40000 ALTER TABLE `novels_comment` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `novels_novel`
--

DROP TABLE IF EXISTS `novels_novel`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `novels_novel` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `novel_img` varchar(100) NOT NULL,
  `novel_status` int NOT NULL,
  `novel_name` varchar(64) NOT NULL,
  `detail` longtext NOT NULL,
  `tuijian` int NOT NULL,
  `dianji` int NOT NULL,
  `total_words` int NOT NULL,
  `chapter_start` int NOT NULL,
  `chapter_end` int NOT NULL,
  `author_id` bigint NOT NULL,
  `category_id` bigint DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `novels_novel_author_id_9ee48fb6` (`author_id`),
  KEY `novels_novel_category_id_6b5a8fd2` (`category_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `novels_novel`
--

LOCK TABLES `novels_novel` WRITE;
/*!40000 ALTER TABLE `novels_novel` DISABLE KEYS */;
/*!40000 ALTER TABLE `novels_novel` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `novels_novel_category`
--

DROP TABLE IF EXISTS `novels_novel_category`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `novels_novel_category` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `category_name` varchar(64) NOT NULL,
  `category_file` varchar(100) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `novels_novel_category`
--

LOCK TABLES `novels_novel_category` WRITE;
/*!40000 ALTER TABLE `novels_novel_category` DISABLE KEYS */;
/*!40000 ALTER TABLE `novels_novel_category` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `novels_novel_chapter`
--

DROP TABLE IF EXISTS `novels_novel_chapter`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `novels_novel_chapter` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `chapter_id` int NOT NULL,
  `title` varchar(64) NOT NULL,
  `content` varchar(100) NOT NULL,
  `words` int NOT NULL,
  `novel_id` bigint DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `novels_novel_chapter_novel_id_chapter_id_b8cd779c_uniq` (`novel_id`,`chapter_id`),
  CONSTRAINT `novels_novel_chapter_novel_id_1070b454_fk_novels_novel_id` FOREIGN KEY (`novel_id`) REFERENCES `novels_novel` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `novels_novel_chapter`
--

LOCK TABLES `novels_novel_chapter` WRITE;
/*!40000 ALTER TABLE `novels_novel_chapter` DISABLE KEYS */;
/*!40000 ALTER TABLE `novels_novel_chapter` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `novels_novel_list`
--

DROP TABLE IF EXISTS `novels_novel_list`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `novels_novel_list` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `update_time` datetime(6) NOT NULL,
  `Novel_id` bigint DEFAULT NULL,
  `user_id` bigint DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `novels_novel_list_Novel_id_ab87dc45_fk_novels_novel_id` (`Novel_id`),
  KEY `novels_novel_list_user_id_595a7c47` (`user_id`),
  CONSTRAINT `novels_novel_list_Novel_id_ab87dc45_fk_novels_novel_id` FOREIGN KEY (`Novel_id`) REFERENCES `novels_novel` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `novels_novel_list`
--

LOCK TABLES `novels_novel_list` WRITE;
/*!40000 ALTER TABLE `novels_novel_list` DISABLE KEYS */;
/*!40000 ALTER TABLE `novels_novel_list` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `novels_recently_reading`
--

DROP TABLE IF EXISTS `novels_recently_reading`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `novels_recently_reading` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `update_time` datetime(6) NOT NULL,
  `Novel_id` bigint DEFAULT NULL,
  `chapter_id` bigint DEFAULT NULL,
  `user_id` bigint DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `novels_recently_reading_Novel_id_c28982ad_fk_novels_novel_id` (`Novel_id`),
  KEY `novels_recently_reading_chapter_id_139af84e` (`chapter_id`),
  KEY `novels_recently_reading_user_id_e457c7d9` (`user_id`),
  CONSTRAINT `novels_recently_reading_Novel_id_c28982ad_fk_novels_novel_id` FOREIGN KEY (`Novel_id`) REFERENCES `novels_novel` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `novels_recently_reading`
--

LOCK TABLES `novels_recently_reading` WRITE;
/*!40000 ALTER TABLE `novels_recently_reading` DISABLE KEYS */;
/*!40000 ALTER TABLE `novels_recently_reading` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `users_user`
--

DROP TABLE IF EXISTS `users_user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `users_user` (
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
  `mobile` varchar(11) NOT NULL,
  `user_icon` varchar(100) NOT NULL,
  `gender` int NOT NULL,
  `is_delete` tinyint(1) NOT NULL,
  `create_time` datetime(6) NOT NULL,
  `is_author` tinyint(1) NOT NULL,
  `birth_date` date DEFAULT NULL,
  `signature` varchar(255) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`),
  UNIQUE KEY `mobile` (`mobile`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `users_user`
--

LOCK TABLES `users_user` WRITE;
/*!40000 ALTER TABLE `users_user` DISABLE KEYS */;
/*!40000 ALTER TABLE `users_user` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `users_user_groups`
--

DROP TABLE IF EXISTS `users_user_groups`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `users_user_groups` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `user_id` bigint NOT NULL,
  `group_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `users_user_groups_user_id_group_id_b88eab82_uniq` (`user_id`,`group_id`),
  KEY `users_user_groups_group_id_9afc8d0e_fk_auth_group_id` (`group_id`),
  CONSTRAINT `users_user_groups_group_id_9afc8d0e_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `users_user_groups_user_id_5f6f5a90_fk_users_user_id` FOREIGN KEY (`user_id`) REFERENCES `users_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `users_user_groups`
--

LOCK TABLES `users_user_groups` WRITE;
/*!40000 ALTER TABLE `users_user_groups` DISABLE KEYS */;
/*!40000 ALTER TABLE `users_user_groups` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `users_user_user_permissions`
--

DROP TABLE IF EXISTS `users_user_user_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `users_user_user_permissions` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `user_id` bigint NOT NULL,
  `permission_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `users_user_user_permissions_user_id_permission_id_43338c45_uniq` (`user_id`,`permission_id`),
  KEY `users_user_user_perm_permission_id_0b93982e_fk_auth_perm` (`permission_id`),
  CONSTRAINT `users_user_user_perm_permission_id_0b93982e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `users_user_user_permissions_user_id_20aca447_fk_users_user_id` FOREIGN KEY (`user_id`) REFERENCES `users_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `users_user_user_permissions`
--

LOCK TABLES `users_user_user_permissions` WRITE;
/*!40000 ALTER TABLE `users_user_user_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `users_user_user_permissions` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-08-23 22:47:10
