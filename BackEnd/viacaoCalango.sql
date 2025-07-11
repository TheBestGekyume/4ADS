-- MySQL dump 10.13  Distrib 8.0.42, for Win64 (x86_64)
--
-- Host: localhost    Database: viacaocalango
-- ------------------------------------------------------
-- Server version	8.0.42

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
-- Table structure for table `usuario`
--

DROP TABLE IF EXISTS `usuario`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `usuario` (
  `id_usuario` int NOT NULL AUTO_INCREMENT,
  `nome` varchar(50) COLLATE utf8mb4_general_ci NOT NULL,
  `senha` varchar(255) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `email` varchar(50) COLLATE utf8mb4_general_ci NOT NULL,
  `tipo` tinyint(1) NOT NULL,
  PRIMARY KEY (`id_usuario`)
) ENGINE=InnoDB AUTO_INCREMENT=12 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `usuario`
--

LOCK TABLES `usuario` WRITE;
/*!40000 ALTER TABLE `usuario` DISABLE KEYS */;
INSERT INTO `usuario` VALUES (1,'Jorge da Silva','$2b$12$gdSBgQh0Z90LSJ0AYF/SYuN5/NlTCb.FKprFQTeSKPZiu2C81DAtC','jorge@hotmail.com',0),(2,'Claudio Costa','$2b$12$HpLxwZOEAeEY2vwPxDu2re.fojhq/IfNlFrRvUl36dGbP4QJWxDie','adm@gmail.com',1),(5,'Gekyume Serna','$2b$12$kWArg26qNeNg9.wWzz618eUypUmBL9hSN3OMGLGbkyGp/SOV9IHz6','gekyume@gmail.com',0),(6,'Tallyson Silva','$2b$12$B0JIOAWZafltirg2dH4Bfe59z5AgPqkfEmPz9E6ooA/QwUy8UK9su','tallyson@gmail.com',0),(11,'Luana Tavares','$2b$12$Rz6GijLTdRuixNwjmEGK2uTgQFyRm0JB1EduyqL4/3ZFEfom3z/LO','luana@gmail.com',0);
/*!40000 ALTER TABLE `usuario` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `usuario_viagem`
--

DROP TABLE IF EXISTS `usuario_viagem`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `usuario_viagem` (
  `usuario_viagem_id` int NOT NULL AUTO_INCREMENT,
  `usuario_id` int NOT NULL,
  `viagem_id` int NOT NULL,
  `assentos` longtext CHARACTER SET utf8mb4 COLLATE utf8mb4_bin NOT NULL,
  PRIMARY KEY (`usuario_viagem_id`),
  KEY `usuario_id` (`usuario_id`),
  KEY `viagem_id` (`viagem_id`),
  CONSTRAINT `usuario_viagem_ibfk_1` FOREIGN KEY (`usuario_id`) REFERENCES `usuario` (`id_usuario`) ON DELETE CASCADE,
  CONSTRAINT `usuario_viagem_ibfk_2` FOREIGN KEY (`viagem_id`) REFERENCES `viagem` (`id_viagem`) ON DELETE CASCADE,
  CONSTRAINT `usuario_viagem_chk_1` CHECK (json_valid(`assentos`))
) ENGINE=InnoDB AUTO_INCREMENT=17 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `usuario_viagem`
--

LOCK TABLES `usuario_viagem` WRITE;
/*!40000 ALTER TABLE `usuario_viagem` DISABLE KEYS */;
INSERT INTO `usuario_viagem` VALUES (3,5,21,'[\"A2\"]'),(4,5,21,'[\"A3\",\"A4\",\"B2\"]'),(5,5,26,'[\"B11\",\"A11\",\"A1\",\"B1\"]'),(6,5,21,'[\"B5\",\"A5\"]'),(7,1,28,'[\"B1\",\"A1\"]'),(9,1,27,'[\"A3\",\"B3\"]'),(10,1,31,'[\"B1\",\"B2\"]'),(11,1,22,'[\"B5\"]'),(12,1,31,'[\"B3\"]'),(13,5,25,'[\"A1\",\"A2\"]'),(14,6,24,'[\"A1\", \"B1\"]'),(15,6,31,'[\"A8\"]'),(16,6,25,'[\"B9\"]');
/*!40000 ALTER TABLE `usuario_viagem` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `viagem`
--

DROP TABLE IF EXISTS `viagem`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `viagem` (
  `id_viagem` int NOT NULL AUTO_INCREMENT,
  `imgUrl` varchar(200) COLLATE utf8mb4_general_ci NOT NULL,
  `origem` varchar(50) COLLATE utf8mb4_general_ci NOT NULL,
  `destino` varchar(50) COLLATE utf8mb4_general_ci NOT NULL,
  `horario_de_partida` varchar(20) COLLATE utf8mb4_general_ci NOT NULL,
  `data_de_partida` varchar(20) COLLATE utf8mb4_general_ci NOT NULL,
  `assentos` longtext CHARACTER SET utf8mb4 COLLATE utf8mb4_bin NOT NULL,
  `preco` float NOT NULL,
  `status` tinyint(1) NOT NULL,
  PRIMARY KEY (`id_viagem`),
  CONSTRAINT `viagem_chk_1` CHECK (json_valid(`assentos`))
) ENGINE=InnoDB AUTO_INCREMENT=35 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `viagem`
--

LOCK TABLES `viagem` WRITE;
/*!40000 ALTER TABLE `viagem` DISABLE KEYS */;
INSERT INTO `viagem` VALUES (21,'https://content.r9cdn.net/rimg/dimg/f3/ac/2ca2def3-city-26168-164fc0204f5.jpg','Rio de Janeiro - RJ','Salvador - BA','04:50','2025-12-02','[{\"nro_assento\":\"A1\",\"disponivel\":false},{\"nro_assento\":\"A2\",\"disponivel\":false},{\"nro_assento\":\"A3\",\"disponivel\":false},{\"nro_assento\":\"A4\",\"disponivel\":false},{\"nro_assento\":\"A5\",\"disponivel\":false},{\"nro_assento\":\"B1\",\"disponivel\":false},{\"nro_assento\":\"B2\",\"disponivel\":false},{\"nro_assento\":\"B3\",\"disponivel\":true},{\"nro_assento\":\"B4\",\"disponivel\":true},{\"nro_assento\":\"B5\",\"disponivel\":false}]',120.5,1),(22,'https://www.pjf.mg.gov.br/noticias/arquivo/0609_sedic_ranking_112728.jpg','São Paulo - SP','Juiz de Fora - MG','04:50','2025-09-11','[{\"nro_assento\":\"A1\",\"disponivel\":true},{\"nro_assento\":\"A2\",\"disponivel\":true},{\"nro_assento\":\"A3\",\"disponivel\":true},{\"nro_assento\":\"A4\",\"disponivel\":true},{\"nro_assento\":\"A5\",\"disponivel\":true},{\"nro_assento\":\"B1\",\"disponivel\":true},{\"nro_assento\":\"B2\",\"disponivel\":true},{\"nro_assento\":\"B3\",\"disponivel\":true},{\"nro_assento\":\"B4\",\"disponivel\":true},{\"nro_assento\":\"B5\",\"disponivel\":false}]',120.5,1),(24,'https://upload.wikimedia.org/wikipedia/commons/thumb/1/19/Jardim_Bot%C3%A2nico_Centro_Curitiba.jpg/1200px-Jardim_Bot%C3%A2nico_Centro_Curitiba.jpg','São Paulo - SP','Curitiba - PR','08:30','2025-11-29','[{\"nro_assento\": \"A1\", \"disponivel\": false}, {\"nro_assento\": \"A2\", \"disponivel\": true}, {\"nro_assento\": \"A3\", \"disponivel\": true}, {\"nro_assento\": \"A4\", \"disponivel\": true}, {\"nro_assento\": \"A5\", \"disponivel\": true}, {\"nro_assento\": \"A6\", \"disponivel\": true}, {\"nro_assento\": \"A7\", \"disponivel\": true}, {\"nro_assento\": \"A8\", \"disponivel\": true}, {\"nro_assento\": \"A9\", \"disponivel\": true}, {\"nro_assento\": \"A10\", \"disponivel\": true}, {\"nro_assento\": \"A11\", \"disponivel\": true}, {\"nro_assento\": \"A12\", \"disponivel\": true}, {\"nro_assento\": \"A13\", \"disponivel\": true}, {\"nro_assento\": \"A14\", \"disponivel\": true}, {\"nro_assento\": \"A15\", \"disponivel\": true}, {\"nro_assento\": \"B1\", \"disponivel\": false}, {\"nro_assento\": \"B2\", \"disponivel\": true}, {\"nro_assento\": \"B3\", \"disponivel\": true}, {\"nro_assento\": \"B4\", \"disponivel\": true}, {\"nro_assento\": \"B5\", \"disponivel\": true}, {\"nro_assento\": \"B6\", \"disponivel\": true}, {\"nro_assento\": \"B7\", \"disponivel\": true}, {\"nro_assento\": \"B8\", \"disponivel\": true}, {\"nro_assento\": \"B9\", \"disponivel\": true}, {\"nro_assento\": \"B10\", \"disponivel\": true}, {\"nro_assento\": \"B11\", \"disponivel\": true}, {\"nro_assento\": \"B12\", \"disponivel\": true}, {\"nro_assento\": \"B13\", \"disponivel\": true}, {\"nro_assento\": \"B14\", \"disponivel\": true}, {\"nro_assento\": \"B15\", \"disponivel\": true}]',250.5,1),(25,'https://www.melhoresdestinos.com.br/wp-content/uploads/2017/11/o-que-fazer-em-porto-alegre-gasometro2-1-820x443.jpg','Florianópolis - SC','Porto Alegre - RS','06:45','2025-09-14','[{\"nro_assento\": \"A1\", \"disponivel\": false}, {\"nro_assento\": \"A2\", \"disponivel\": false}, {\"nro_assento\": \"A3\", \"disponivel\": true}, {\"nro_assento\": \"A4\", \"disponivel\": true}, {\"nro_assento\": \"A5\", \"disponivel\": true}, {\"nro_assento\": \"A6\", \"disponivel\": true}, {\"nro_assento\": \"A7\", \"disponivel\": true}, {\"nro_assento\": \"A8\", \"disponivel\": true}, {\"nro_assento\": \"A9\", \"disponivel\": true}, {\"nro_assento\": \"A10\", \"disponivel\": true}, {\"nro_assento\": \"B1\", \"disponivel\": true}, {\"nro_assento\": \"B2\", \"disponivel\": true}, {\"nro_assento\": \"B3\", \"disponivel\": true}, {\"nro_assento\": \"B4\", \"disponivel\": true}, {\"nro_assento\": \"B5\", \"disponivel\": true}, {\"nro_assento\": \"B6\", \"disponivel\": true}, {\"nro_assento\": \"B7\", \"disponivel\": true}, {\"nro_assento\": \"B8\", \"disponivel\": true}, {\"nro_assento\": \"B9\", \"disponivel\": false}, {\"nro_assento\": \"B10\", \"disponivel\": true}]',280,1),(26,'https://cdn.blablacar.com/wp-content/uploads/br/2023/11/05100004/campo-grande-ms-5.webp','Foz do Iguaçu - PR','Campo Grande - MS','09:30','2025-10-02','[{\"nro_assento\":\"A1\",\"disponivel\":false},{\"nro_assento\":\"A2\",\"disponivel\":true},{\"nro_assento\":\"A3\",\"disponivel\":true},{\"nro_assento\":\"A4\",\"disponivel\":true},{\"nro_assento\":\"A5\",\"disponivel\":true},{\"nro_assento\":\"A6\",\"disponivel\":true},{\"nro_assento\":\"A7\",\"disponivel\":true},{\"nro_assento\":\"A8\",\"disponivel\":true},{\"nro_assento\":\"A9\",\"disponivel\":true},{\"nro_assento\":\"A10\",\"disponivel\":true},{\"nro_assento\":\"A11\",\"disponivel\":false},{\"nro_assento\":\"B1\",\"disponivel\":false},{\"nro_assento\":\"B2\",\"disponivel\":true},{\"nro_assento\":\"B3\",\"disponivel\":true},{\"nro_assento\":\"B4\",\"disponivel\":true},{\"nro_assento\":\"B5\",\"disponivel\":true},{\"nro_assento\":\"B6\",\"disponivel\":true},{\"nro_assento\":\"B7\",\"disponivel\":true},{\"nro_assento\":\"B8\",\"disponivel\":true},{\"nro_assento\":\"B9\",\"disponivel\":true},{\"nro_assento\":\"B10\",\"disponivel\":true},{\"nro_assento\":\"B11\",\"disponivel\":false}]',229.99,1),(27,'https://marazulreceptivo.com.br/wp-content/uploads/2023/03/Praia-do-forte-caninde-soares.jpg','Fortaleza - CE','Natal - RN','07:00','2026-02-17','[{\"nro_assento\":\"A1\",\"disponivel\":false},{\"nro_assento\":\"A2\",\"disponivel\":false},{\"nro_assento\":\"A3\",\"disponivel\":false},{\"nro_assento\":\"A4\",\"disponivel\":true},{\"nro_assento\":\"A5\",\"disponivel\":true},{\"nro_assento\":\"A6\",\"disponivel\":true},{\"nro_assento\":\"A7\",\"disponivel\":true},{\"nro_assento\":\"A8\",\"disponivel\":true},{\"nro_assento\":\"A9\",\"disponivel\":true},{\"nro_assento\":\"B1\",\"disponivel\":false},{\"nro_assento\":\"B2\",\"disponivel\":false},{\"nro_assento\":\"B3\",\"disponivel\":false},{\"nro_assento\":\"B4\",\"disponivel\":true},{\"nro_assento\":\"B5\",\"disponivel\":true},{\"nro_assento\":\"B6\",\"disponivel\":true},{\"nro_assento\":\"B7\",\"disponivel\":true},{\"nro_assento\":\"B8\",\"disponivel\":true},{\"nro_assento\":\"B9\",\"disponivel\":true}]',139.99,1),(28,'https://staging5.appai.org.br/wp-content/uploads/2022/08/01-appai-passeio-cultural-niteroi-noticias.jpg','Aracaju - SE','Niterói - Rj','15:30','2025-01-06','[{\"nro_assento\":\"A1\",\"disponivel\":false},{\"nro_assento\":\"A2\",\"disponivel\":true},{\"nro_assento\":\"A3\",\"disponivel\":true},{\"nro_assento\":\"A4\",\"disponivel\":true},{\"nro_assento\":\"A5\",\"disponivel\":true},{\"nro_assento\":\"A6\",\"disponivel\":true},{\"nro_assento\":\"A7\",\"disponivel\":true},{\"nro_assento\":\"B1\",\"disponivel\":false},{\"nro_assento\":\"B2\",\"disponivel\":true},{\"nro_assento\":\"B3\",\"disponivel\":true},{\"nro_assento\":\"B4\",\"disponivel\":true},{\"nro_assento\":\"B5\",\"disponivel\":true},{\"nro_assento\":\"B6\",\"disponivel\":true},{\"nro_assento\":\"B7\",\"disponivel\":true}]',199.99,1),(30,'https://th.bing.com/th/id/OIP.tx720jyhJT3wF1va2-lVwwHaE8?rs=1&pid=ImgDetMain','Rio de Janeiro - RJ','Paraty - RJ','10:30','2024-12-04','[{\"nro_assento\":\"A1\",\"disponivel\":true},{\"nro_assento\":\"A2\",\"disponivel\":true},{\"nro_assento\":\"A3\",\"disponivel\":true},{\"nro_assento\":\"A4\",\"disponivel\":true},{\"nro_assento\":\"A5\",\"disponivel\":true},{\"nro_assento\":\"A6\",\"disponivel\":true},{\"nro_assento\":\"A7\",\"disponivel\":true},{\"nro_assento\":\"A8\",\"disponivel\":true},{\"nro_assento\":\"B1\",\"disponivel\":true},{\"nro_assento\":\"B2\",\"disponivel\":true},{\"nro_assento\":\"B3\",\"disponivel\":true},{\"nro_assento\":\"B4\",\"disponivel\":true},{\"nro_assento\":\"B5\",\"disponivel\":true},{\"nro_assento\":\"B6\",\"disponivel\":true},{\"nro_assento\":\"B7\",\"disponivel\":true},{\"nro_assento\":\"B8\",\"disponivel\":true}]',59.99,1),(31,'https://content.r9cdn.net/rimg/dimg/f3/ac/2ca2def3-city-26168-164fc0204f5.jpg','Rio de Janeiro - RJ','Salvador - BA','21:58','2024-12-21','[{\"nro_assento\": \"A1\", \"disponivel\": true}, {\"nro_assento\": \"A2\", \"disponivel\": true}, {\"nro_assento\": \"A3\", \"disponivel\": true}, {\"nro_assento\": \"A4\", \"disponivel\": true}, {\"nro_assento\": \"A5\", \"disponivel\": true}, {\"nro_assento\": \"A6\", \"disponivel\": true}, {\"nro_assento\": \"A7\", \"disponivel\": true}, {\"nro_assento\": \"A8\", \"disponivel\": false}, {\"nro_assento\": \"B1\", \"disponivel\": false}, {\"nro_assento\": \"B2\", \"disponivel\": false}, {\"nro_assento\": \"B3\", \"disponivel\": false}, {\"nro_assento\": \"B4\", \"disponivel\": true}, {\"nro_assento\": \"B5\", \"disponivel\": true}, {\"nro_assento\": \"B6\", \"disponivel\": true}, {\"nro_assento\": \"B7\", \"disponivel\": true}, {\"nro_assento\": \"B8\", \"disponivel\": true}]',120,1),(32,'https://blog.blablacar.com.br/wp-content/uploads/2023/11/palmas-to.webp','Natal - RN','Palmas - TO','22:15','2025-08-20','[{\"nro_assento\": \"A1\", \"disponivel\": true}, {\"nro_assento\": \"A2\", \"disponivel\": true}, {\"nro_assento\": \"A3\", \"disponivel\": true}, {\"nro_assento\": \"A4\", \"disponivel\": true}, {\"nro_assento\": \"A5\", \"disponivel\": true}, {\"nro_assento\": \"A6\", \"disponivel\": true}, {\"nro_assento\": \"B1\", \"disponivel\": true}, {\"nro_assento\": \"B2\", \"disponivel\": true}, {\"nro_assento\": \"B3\", \"disponivel\": true}, {\"nro_assento\": \"B4\", \"disponivel\": true}, {\"nro_assento\": \"B5\", \"disponivel\": true}, {\"nro_assento\": \"B6\", \"disponivel\": true}]',99.99,1);
/*!40000 ALTER TABLE `viagem` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2025-07-11 18:34:58
