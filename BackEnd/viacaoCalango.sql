-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Tempo de geração: 26/11/2024 às 10:29
-- Versão do servidor: 10.4.32-MariaDB
-- Versão do PHP: 8.0.30

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Banco de dados: `viacaocalango`
--

CREATE DATABASE IF NOT EXISTS viacaocalango;
USE viacaocalango;

-- --------------------------------------------------------

--
-- Estrutura para tabela `usuario`
--

CREATE TABLE `usuario` (
  `id_usuario` int(11) NOT NULL,
  `nome` varchar(50) NOT NULL,
  `senha` varchar(20) NOT NULL,
  `email` varchar(50) NOT NULL,
  `tipo` tinyint(1) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Despejando dados para a tabela `usuario`
--

INSERT INTO `usuario` (`id_usuario`, `nome`, `senha`, `email`, `tipo`) VALUES
(1, 'Jorge da Silva', '123123', 'jorge@hotmail.com', 0),
(2, 'Claudio Costa', '123', 'adm@gmail.com', 1),
(5, 'Gekyume Serna', '666', 'gekyume@gmail.com', 0);

-- --------------------------------------------------------

--
-- Estrutura para tabela `usuario_viagem`
--

CREATE TABLE `usuario_viagem` (
  `usuario_viagem_id` int(11) NOT NULL,
  `usuario_id` int(11) NOT NULL,
  `viagem_id` int(11) NOT NULL,
  `assentos` longtext CHARACTER SET utf8mb4 COLLATE utf8mb4_bin NOT NULL CHECK (json_valid(`assentos`))
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Despejando dados para a tabela `usuario_viagem`
--

INSERT INTO `usuario_viagem` (`usuario_viagem_id`, `usuario_id`, `viagem_id`, `assentos`) VALUES
(3, 5, 21, '[\"A2\"]'),
(4, 5, 21, '[\"A3\",\"A4\",\"B2\"]'),
(5, 5, 26, '[\"B11\",\"A11\",\"A1\",\"B1\"]'),
(6, 5, 21, '[\"B5\",\"A5\"]'),
(7, 1, 28, '[\"B1\",\"A1\"]'),
(9, 1, 27, '[\"A3\",\"B3\"]'),
(10, 1, 31, '[\"B1\",\"B2\"]'),
(11, 1, 22, '[\"B5\"]'),
(12, 1, 31, '[\"B3\"]'),
(13, 5, 25, '[\"A1\",\"A2\"]');

-- --------------------------------------------------------

--
-- Estrutura para tabela `viagem`
--

CREATE TABLE `viagem` (
  `id_viagem` int(11) NOT NULL,
  `imgUrl` varchar(200) NOT NULL,
  `origem` varchar(50) NOT NULL,
  `destino` varchar(50) NOT NULL,
  `horario_de_partida` varchar(20) NOT NULL,
  `data_de_partida` varchar(20) NOT NULL,
  `assentos` longtext CHARACTER SET utf8mb4 COLLATE utf8mb4_bin NOT NULL CHECK (json_valid(`assentos`)),
  `preco` float NOT NULL,
  `status` tinyint(1) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Despejando dados para a tabela `viagem`
--

INSERT INTO `viagem` (`id_viagem`, `imgUrl`, `origem`, `destino`, `horario_de_partida`, `data_de_partida`, `assentos`, `preco`, `status`) VALUES
(21, 'https://content.r9cdn.net/rimg/dimg/f3/ac/2ca2def3-city-26168-164fc0204f5.jpg', 'Rio de Janeiro - RJ', 'Salvador - BA', '04:50', '2024-12-31', '[{\"nro_assento\":\"A1\",\"disponivel\":false},{\"nro_assento\":\"A2\",\"disponivel\":false},{\"nro_assento\":\"A3\",\"disponivel\":false},{\"nro_assento\":\"A4\",\"disponivel\":false},{\"nro_assento\":\"A5\",\"disponivel\":false},{\"nro_assento\":\"B1\",\"disponivel\":false},{\"nro_assento\":\"B2\",\"disponivel\":false},{\"nro_assento\":\"B3\",\"disponivel\":true},{\"nro_assento\":\"B4\",\"disponivel\":true},{\"nro_assento\":\"B5\",\"disponivel\":false}]', 120.5, 1),
(22, 'https://www.pjf.mg.gov.br/noticias/arquivo/0609_sedic_ranking_112728.jpg', 'São Paulo - SP', 'Juiz de Fora - MG', '04:50', '2025-06-11', '[{\"nro_assento\":\"A1\",\"disponivel\":true},{\"nro_assento\":\"A2\",\"disponivel\":true},{\"nro_assento\":\"A3\",\"disponivel\":true},{\"nro_assento\":\"A4\",\"disponivel\":true},{\"nro_assento\":\"A5\",\"disponivel\":true},{\"nro_assento\":\"B1\",\"disponivel\":true},{\"nro_assento\":\"B2\",\"disponivel\":true},{\"nro_assento\":\"B3\",\"disponivel\":true},{\"nro_assento\":\"B4\",\"disponivel\":true},{\"nro_assento\":\"B5\",\"disponivel\":false}]', 120.5, 1),
(24, 'https://upload.wikimedia.org/wikipedia/commons/thumb/1/19/Jardim_Bot%C3%A2nico_Centro_Curitiba.jpg/1200px-Jardim_Bot%C3%A2nico_Centro_Curitiba.jpg', 'São Paulo - SP', 'Curitiba - PR', '08:30', '2024-11-29', '[{\"nro_assento\":\"A1\",\"disponivel\":true},{\"nro_assento\":\"A2\",\"disponivel\":true},{\"nro_assento\":\"A3\",\"disponivel\":true},{\"nro_assento\":\"A4\",\"disponivel\":true},{\"nro_assento\":\"A5\",\"disponivel\":true},{\"nro_assento\":\"A6\",\"disponivel\":true},{\"nro_assento\":\"A7\",\"disponivel\":true},{\"nro_assento\":\"A8\",\"disponivel\":true},{\"nro_assento\":\"A9\",\"disponivel\":true},{\"nro_assento\":\"A10\",\"disponivel\":true},{\"nro_assento\":\"A11\",\"disponivel\":true},{\"nro_assento\":\"A12\",\"disponivel\":true},{\"nro_assento\":\"A13\",\"disponivel\":true},{\"nro_assento\":\"A14\",\"disponivel\":true},{\"nro_assento\":\"A15\",\"disponivel\":true},{\"nro_assento\":\"B1\",\"disponivel\":true},{\"nro_assento\":\"B2\",\"disponivel\":true},{\"nro_assento\":\"B3\",\"disponivel\":true},{\"nro_assento\":\"B4\",\"disponivel\":true},{\"nro_assento\":\"B5\",\"disponivel\":true},{\"nro_assento\":\"B6\",\"disponivel\":true},{\"nro_assento\":\"B7\",\"disponivel\":true},{\"nro_assento\":\"B8\",\"disponivel\":true},{\"nro_assento\":\"B9\",\"disponivel\":true},{\"nro_assento\":\"B10\",\"disponivel\":true},{\"nro_assento\":\"B11\",\"disponivel\":true},{\"nro_assento\":\"B12\",\"disponivel\":true},{\"nro_assento\":\"B13\",\"disponivel\":true},{\"nro_assento\":\"B14\",\"disponivel\":true},{\"nro_assento\":\"B15\",\"disponivel\":true}]', 250.5, 1),
(25, 'https://www.melhoresdestinos.com.br/wp-content/uploads/2017/11/o-que-fazer-em-porto-alegre-gasometro2-1-820x443.jpg', 'Florianópolis - SC', 'Porto Alegre - RS', '06:45', '2025-03-14', '[{\"nro_assento\":\"A1\",\"disponivel\":false},{\"nro_assento\":\"A2\",\"disponivel\":false},{\"nro_assento\":\"A3\",\"disponivel\":true},{\"nro_assento\":\"A4\",\"disponivel\":true},{\"nro_assento\":\"A5\",\"disponivel\":true},{\"nro_assento\":\"A6\",\"disponivel\":true},{\"nro_assento\":\"A7\",\"disponivel\":true},{\"nro_assento\":\"A8\",\"disponivel\":true},{\"nro_assento\":\"A9\",\"disponivel\":true},{\"nro_assento\":\"A10\",\"disponivel\":true},{\"nro_assento\":\"B1\",\"disponivel\":true},{\"nro_assento\":\"B2\",\"disponivel\":true},{\"nro_assento\":\"B3\",\"disponivel\":true},{\"nro_assento\":\"B4\",\"disponivel\":true},{\"nro_assento\":\"B5\",\"disponivel\":true},{\"nro_assento\":\"B6\",\"disponivel\":true},{\"nro_assento\":\"B7\",\"disponivel\":true},{\"nro_assento\":\"B8\",\"disponivel\":true},{\"nro_assento\":\"B9\",\"disponivel\":true},{\"nro_assento\":\"B10\",\"disponivel\":true}]', 280, 1),
(26, 'https://cdn.blablacar.com/wp-content/uploads/br/2023/11/05100004/campo-grande-ms-5.webp', 'Foz do Iguaçu - PR', 'Campo Grande - MS', '09:30', '2025-10-02', '[{\"nro_assento\":\"A1\",\"disponivel\":false},{\"nro_assento\":\"A2\",\"disponivel\":true},{\"nro_assento\":\"A3\",\"disponivel\":true},{\"nro_assento\":\"A4\",\"disponivel\":true},{\"nro_assento\":\"A5\",\"disponivel\":true},{\"nro_assento\":\"A6\",\"disponivel\":true},{\"nro_assento\":\"A7\",\"disponivel\":true},{\"nro_assento\":\"A8\",\"disponivel\":true},{\"nro_assento\":\"A9\",\"disponivel\":true},{\"nro_assento\":\"A10\",\"disponivel\":true},{\"nro_assento\":\"A11\",\"disponivel\":false},{\"nro_assento\":\"B1\",\"disponivel\":false},{\"nro_assento\":\"B2\",\"disponivel\":true},{\"nro_assento\":\"B3\",\"disponivel\":true},{\"nro_assento\":\"B4\",\"disponivel\":true},{\"nro_assento\":\"B5\",\"disponivel\":true},{\"nro_assento\":\"B6\",\"disponivel\":true},{\"nro_assento\":\"B7\",\"disponivel\":true},{\"nro_assento\":\"B8\",\"disponivel\":true},{\"nro_assento\":\"B9\",\"disponivel\":true},{\"nro_assento\":\"B10\",\"disponivel\":true},{\"nro_assento\":\"B11\",\"disponivel\":false}]', 230.99, 1),
(27, 'https://marazulreceptivo.com.br/wp-content/uploads/2023/03/Praia-do-forte-caninde-soares.jpg', 'Fortaleza - CE', 'Natal - RN', '07:00', '2025-04-17', '[{\"nro_assento\":\"A1\",\"disponivel\":false},{\"nro_assento\":\"A2\",\"disponivel\":false},{\"nro_assento\":\"A3\",\"disponivel\":false},{\"nro_assento\":\"A4\",\"disponivel\":true},{\"nro_assento\":\"A5\",\"disponivel\":true},{\"nro_assento\":\"A6\",\"disponivel\":true},{\"nro_assento\":\"A7\",\"disponivel\":true},{\"nro_assento\":\"A8\",\"disponivel\":true},{\"nro_assento\":\"A9\",\"disponivel\":true},{\"nro_assento\":\"B1\",\"disponivel\":false},{\"nro_assento\":\"B2\",\"disponivel\":false},{\"nro_assento\":\"B3\",\"disponivel\":false},{\"nro_assento\":\"B4\",\"disponivel\":true},{\"nro_assento\":\"B5\",\"disponivel\":true},{\"nro_assento\":\"B6\",\"disponivel\":true},{\"nro_assento\":\"B7\",\"disponivel\":true},{\"nro_assento\":\"B8\",\"disponivel\":true},{\"nro_assento\":\"B9\",\"disponivel\":true}]', 150.25, 1),
(28, 'https://staging5.appai.org.br/wp-content/uploads/2022/08/01-appai-passeio-cultural-niteroi-noticias.jpg', 'Aracaju - SE', 'Niterói - Rj', '15:30', '2024-12-02', '[{\"nro_assento\":\"A1\",\"disponivel\":false},{\"nro_assento\":\"A2\",\"disponivel\":true},{\"nro_assento\":\"A3\",\"disponivel\":true},{\"nro_assento\":\"A4\",\"disponivel\":true},{\"nro_assento\":\"A5\",\"disponivel\":true},{\"nro_assento\":\"A6\",\"disponivel\":true},{\"nro_assento\":\"A7\",\"disponivel\":true},{\"nro_assento\":\"B1\",\"disponivel\":false},{\"nro_assento\":\"B2\",\"disponivel\":true},{\"nro_assento\":\"B3\",\"disponivel\":true},{\"nro_assento\":\"B4\",\"disponivel\":true},{\"nro_assento\":\"B5\",\"disponivel\":true},{\"nro_assento\":\"B6\",\"disponivel\":true},{\"nro_assento\":\"B7\",\"disponivel\":true}]', 259.99, 1),
(30, 'https://th.bing.com/th/id/OIP.tx720jyhJT3wF1va2-lVwwHaE8?rs=1&pid=ImgDetMain', 'Rio de Janeiro - RJ', 'Paraty - RJ', '10:30', '2024-12-04', '[{\"nro_assento\":\"A1\",\"disponivel\":true},{\"nro_assento\":\"A2\",\"disponivel\":true},{\"nro_assento\":\"A3\",\"disponivel\":true},{\"nro_assento\":\"A4\",\"disponivel\":true},{\"nro_assento\":\"A5\",\"disponivel\":true},{\"nro_assento\":\"A6\",\"disponivel\":true},{\"nro_assento\":\"A7\",\"disponivel\":true},{\"nro_assento\":\"A8\",\"disponivel\":true},{\"nro_assento\":\"B1\",\"disponivel\":true},{\"nro_assento\":\"B2\",\"disponivel\":true},{\"nro_assento\":\"B3\",\"disponivel\":true},{\"nro_assento\":\"B4\",\"disponivel\":true},{\"nro_assento\":\"B5\",\"disponivel\":true},{\"nro_assento\":\"B6\",\"disponivel\":true},{\"nro_assento\":\"B7\",\"disponivel\":true},{\"nro_assento\":\"B8\",\"disponivel\":true}]', 100, 1),
(31, 'https://content.r9cdn.net/rimg/dimg/f3/ac/2ca2def3-city-26168-164fc0204f5.jpg', 'Rio de Janeiro - RJ', 'Salvador - BA', '21:58', '2024-12-21', '[{\"nro_assento\":\"A1\",\"disponivel\":true},{\"nro_assento\":\"A2\",\"disponivel\":true},{\"nro_assento\":\"A3\",\"disponivel\":true},{\"nro_assento\":\"A4\",\"disponivel\":true},{\"nro_assento\":\"A5\",\"disponivel\":true},{\"nro_assento\":\"A6\",\"disponivel\":true},{\"nro_assento\":\"A7\",\"disponivel\":true},{\"nro_assento\":\"A8\",\"disponivel\":true},{\"nro_assento\":\"B1\",\"disponivel\":false},{\"nro_assento\":\"B2\",\"disponivel\":false},{\"nro_assento\":\"B3\",\"disponivel\":false},{\"nro_assento\":\"B4\",\"disponivel\":true},{\"nro_assento\":\"B5\",\"disponivel\":true},{\"nro_assento\":\"B6\",\"disponivel\":true},{\"nro_assento\":\"B7\",\"disponivel\":true},{\"nro_assento\":\"B8\",\"disponivel\":true}]', 120, 1);

--
-- Índices para tabelas despejadas
--

--
-- Índices de tabela `usuario`
--
ALTER TABLE `usuario`
  ADD PRIMARY KEY (`id_usuario`);

--
-- Índices de tabela `usuario_viagem`
--
ALTER TABLE `usuario_viagem`
  ADD PRIMARY KEY (`usuario_viagem_id`),
  ADD KEY `usuario_id` (`usuario_id`),
  ADD KEY `viagem_id` (`viagem_id`);

--
-- Índices de tabela `viagem`
--
ALTER TABLE `viagem`
  ADD PRIMARY KEY (`id_viagem`);

--
-- AUTO_INCREMENT para tabelas despejadas
--

--
-- AUTO_INCREMENT de tabela `usuario`
--
ALTER TABLE `usuario`
  MODIFY `id_usuario` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT de tabela `usuario_viagem`
--
ALTER TABLE `usuario_viagem`
  MODIFY `usuario_viagem_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=14;

--
-- AUTO_INCREMENT de tabela `viagem`
--
ALTER TABLE `viagem`
  MODIFY `id_viagem` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=32;

--
-- Restrições para tabelas despejadas
--

--
-- Restrições para tabelas `usuario_viagem`
--
ALTER TABLE `usuario_viagem`
  ADD CONSTRAINT `usuario_viagem_ibfk_1` FOREIGN KEY (`usuario_id`) REFERENCES `usuario` (`id_usuario`) ON DELETE CASCADE,
  ADD CONSTRAINT `usuario_viagem_ibfk_2` FOREIGN KEY (`viagem_id`) REFERENCES `viagem` (`id_viagem`) ON DELETE CASCADE;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
