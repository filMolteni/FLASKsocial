-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Creato il: Mag 31, 2024 alle 10:03
-- Versione del server: 10.4.32-MariaDB
-- Versione PHP: 8.0.30

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `db_social`
--

-- --------------------------------------------------------

--
-- Struttura della tabella `foto`
--

CREATE TABLE `foto` (
  `ID` int(11) NOT NULL,
  `idUtente` int(11) NOT NULL,
  `path` varchar(32) NOT NULL,
  `descrizione` varchar(255) NOT NULL,
  `isProfileImg` tinyint(1) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dump dei dati per la tabella `foto`
--

INSERT INTO `foto` (`ID`, `idUtente`, `path`, `descrizione`, `isProfileImg`) VALUES
(1, 1, 'img1.jpg', 'immagine di una montagna ', 0),
(2, 1, 'img2.jpg', 'immagine persona', 1),
(3, 2, 'img3.jpg', 'basket', 0),
(4, 1, 'img4.jpg', 'moto', 0),
(5, 1, 'img5.jpg', 'motoCross', 0),
(10, 2, 'anonymous.jpg', 'prova', 1),
(12, 5, 'tastiera.jpg', 'immagine ', 0),
(13, 5, 'panda.jpg', 'holidays', 1),
(14, 6, 'fiore.jpg', 'fiore', 0),
(15, 6, 'tiger.jpg', 'tigre', 1),
(16, 2, 'panda.jpg', 'prova', 0),
(17, 2, 'test.jpg', 'fewfe', 0),
(18, 2, 'Image.jpg', 'prova', 0),
(19, 2, 'fotocamera.jpg', 'immagine ', 0),
(20, 5, 'download.jfif', 'immagine ', 0),
(21, 5, 'papa.webp', 'holidays', 0),
(22, 5, 'immagini-gratis-big.jpg', 'fewfe', 0),
(23, 6, 'colosseo.jpg', 'fewfe', 0),
(25, 6, 'test.jpg', '', 0),
(26, 7, 'fiore.jpg', 'fiore', 0),
(27, 7, 'tiger.jpg', 'tigre', 0),
(28, 7, 'anonymous.jpg', 'fewfe', 0),
(29, 7, 'immagini-da-scaricare.jpg', 'immagine ', 1),
(31, 2, 'immagini-gratis-big.jpg', 'fewfe', 0),
(32, 2, 'fotocamera.jpg', 'fewfe', 0),
(33, 2, 'tastiera.jpg', 'holidays', 0),
(34, 2, 'immagini-da-scaricare.jpg', 'fewfe', 0),
(35, 2, 'fotocamera.jpg', 'fewfe', 0);

-- --------------------------------------------------------

--
-- Struttura della tabella `utenti`
--

CREATE TABLE `utenti` (
  `ID` int(11) NOT NULL,
  `username` varchar(32) NOT NULL,
  `email` varchar(255) NOT NULL,
  `password` varchar(32) NOT NULL,
  `descrizione` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dump dei dati per la tabella `utenti`
--

INSERT INTO `utenti` (`ID`, `username`, `email`, `password`, `descrizione`) VALUES
(1, 'filippo', 'filippo.molteni2005@gmail.com', 'password', 'ciao sono uno studente'),
(2, 'user2', 'user2@gmail.com', 'password', 'ciao sono user2'),
(5, 'manu', 'SSSSSS@gmail', 'password', 'SSSSSSSSSSSSSSSSSSS'),
(6, 'user3', 'filippo.molteni690@gmail.com', 'password', ''),
(7, 'molteni_filippo', 'filippo.molteni97@gmail.com', 'password', '');

--
-- Indici per le tabelle scaricate
--

--
-- Indici per le tabelle `foto`
--
ALTER TABLE `foto`
  ADD PRIMARY KEY (`ID`),
  ADD KEY `chiaveImg` (`idUtente`);

--
-- Indici per le tabelle `utenti`
--
ALTER TABLE `utenti`
  ADD PRIMARY KEY (`ID`);

--
-- AUTO_INCREMENT per le tabelle scaricate
--

--
-- AUTO_INCREMENT per la tabella `foto`
--
ALTER TABLE `foto`
  MODIFY `ID` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=36;

--
-- AUTO_INCREMENT per la tabella `utenti`
--
ALTER TABLE `utenti`
  MODIFY `ID` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=8;

--
-- Limiti per le tabelle scaricate
--

--
-- Limiti per la tabella `foto`
--
ALTER TABLE `foto`
  ADD CONSTRAINT `chiaveImg` FOREIGN KEY (`idUtente`) REFERENCES `utenti` (`ID`) ON DELETE CASCADE ON UPDATE CASCADE;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
