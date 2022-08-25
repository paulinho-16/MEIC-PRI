CREATE DATABASE IF NOT EXISTS netflix_database;

USE netflix_database;

-- Drop previous tables

SET FOREIGN_KEY_CHECKS=0;

DROP TABLE IF EXISTS Year;
DROP TABLE IF EXISTS Genre;
DROP TABLE IF EXISTS Type;
DROP TABLE IF EXISTS Actor;
DROP TABLE IF EXISTS Language;
DROP TABLE IF EXISTS Country;
DROP TABLE IF EXISTS Certificate;
DROP TABLE IF EXISTS Classification;
DROP TABLE IF EXISTS ImdbEntry;
DROP TABLE IF EXISTS ImdbEntry_Genre;
DROP TABLE IF EXISTS ImdbEntry_Actor;
DROP TABLE IF EXISTS ImdbEntry_Certificate;

SET FOREIGN_KEY_CHECKS=1;

-- Create and Load Year Table

CREATE TABLE Year(
    id SERIAL,
    year VARCHAR(30),
    CONSTRAINT YearPK PRIMARY KEY (id)
);

-- Create and Load Genre Table

CREATE TABLE Genre(
    id SERIAL,
    genre VARCHAR(300),
    CONSTRAINT GenrePK PRIMARY KEY (id) 
);

-- Create and Load Type Table

CREATE TABLE Type(
    id SERIAL,
    typeName VARCHAR(300),
    CONSTRAINT TypePK PRIMARY KEY (id)
);

-- Create and Load Actor Table

CREATE TABLE Actor(
    id SERIAL,
    actorName VARCHAR(300),
    CONSTRAINT ActorPK PRIMARY KEY (id)
);

-- Create and Load Language Table

CREATE TABLE Language(
    id SERIAL,
    language VARCHAR(300),
    CONSTRAINT LanguagePK PRIMARY KEY (id)
);

-- Create and Load Country Table

CREATE TABLE Country(
    id SERIAL,
    countryName VARCHAR(300),
    CONSTRAINT CountryPK PRIMARY KEY (id)
);

-- Create and Load Classification Table

CREATE TABLE Classification(
    id SERIAL,
    classification VARCHAR(30),
    CONSTRAINT ClassificationPK PRIMARY KEY (id)
);

-- Create and Load Certificate Table
CREATE TABLE Certificate(
    id SERIAL,
    countryID BIGINT UNSIGNED,
    classificationID BIGINT UNSIGNED,
    CONSTRAINT CertificatePK PRIMARY KEY (id),
    CONSTRAINT CountryFK FOREIGN KEY (countryID) REFERENCES Country(id),
    CONSTRAINT ClassificationFK FOREIGN KEY (classificationID) REFERENCES Classification(id)
);

-- Create and Load ImdbEntry Table

CREATE TABLE ImdbEntry(
    imdbID VARCHAR(30) NOT NULL,
    title VARCHAR(30) NOT NULL,
    popularRank VARCHAR(50),
    episodes VARCHAR(50),
    runtime VARCHAR(50),
    summary VARCHAR(3000),
    rating VARCHAR(50),
    numVotes VARCHAR(50),
    image VARCHAR(300),
    startYearID BIGINT UNSIGNED,
    endYearID BIGINT UNSIGNED,
    typeID BIGINT UNSIGNED,
    languageID BIGINT UNSIGNED,
    countryID BIGINT UNSIGNED,
    CONSTRAINT StartYearFK FOREIGN KEY (startYearID) REFERENCES Year(id),
    CONSTRAINT EndYearFK FOREIGN KEY (endYearID) REFERENCES Year(id),
    CONSTRAINT TypeFK FOREIGN KEY (TypeID) REFERENCES Type(id),
    CONSTRAINT LanguageFK FOREIGN KEY (languageID) REFERENCES Language(id),
    CONSTRAINT OriginCountryFK FOREIGN KEY (countryID) REFERENCES Country(id),
    CONSTRAINT ImdbEntryPK PRIMARY KEY (imdbID)
);

-- Relation between ImdbEntry and Genre

CREATE TABLE ImdbEntry_Genre(
    ImdbEntryID VARCHAR(30) NOT NULL,
    GenreID BIGINT UNSIGNED NOT NULL,
    CONSTRAINT ImdbEntry_GenrePK PRIMARY KEY (ImdbEntryID, GenreID),
    CONSTRAINT ImdbEntryFK1 FOREIGN KEY (ImdbEntryID) REFERENCES ImdbEntry(imdbID),
    CONSTRAINT GenreFK FOREIGN KEY (GenreID) REFERENCES Genre(id)
);

-- Relation between ImdbEntry and Actor

CREATE TABLE ImdbEntry_Actor(
    ImdbEntryID VARCHAR(30) NOT NULL,
    ActorID BIGINT UNSIGNED NOT NULL,
    CONSTRAINT ImdbEntry_Actor PRIMARY KEY (ImdbEntryID, ActorID),
    CONSTRAINT ImdbEntryFK2 FOREIGN KEY (ImdbEntryID) REFERENCES ImdbEntry(imdbID),
    CONSTRAINT ActorIDFK FOREIGN KEY (ActorID) REFERENCES Actor(id)
);

-- Relation between ImdbEntry and Certificate

CREATE TABLE ImdbEntry_Certificate(
    ImdbEntryID VARCHAR(30) NOT NULL,
    CertificateID BIGINT UNSIGNED NOT NULL,
    CONSTRAINT ImdbEntry_Certificate PRIMARY KEY (ImdbEntryID, CertificateID),
    CONSTRAINT ImdbEntryFK3 FOREIGN KEY (ImdbEntryID) REFERENCES ImdbEntry(imdbID),
    CONSTRAINT CertificateIDFK FOREIGN KEY (CertificateID) REFERENCES Certificate(id)
);