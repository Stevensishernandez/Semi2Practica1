CREATE DATABASE Semi2P1;
USE Semi2P1;


CREATE TABLE temp (
    Year varchar(50),
    Mo varchar(50),
    Dy varchar(50),
    Hr varchar(50),
    Mn varchar(50),
    Sec varchar(50),
    Tsunami_Event_Validity varchar(50),
    Tsunami_Cause_Code varchar(50),
    Earthquake_Magnitude varchar(50),
    Deposits varchar(50),
    Country varchar(50),
    Location_Name varchar(50),
    Latitude varchar(50),
    Longitude varchar(50),
    Maximum_Water_Height varchar(50),
    Number_of_Runups varchar(50),
    Tsunami_Magnitude varchar(50),
    Tsunami_Intensity varchar(50),
    Total_Deaths varchar(50),
    Total_Missing varchar(50),
    Total_Missing_Description varchar(50),
    Total_Injuries varchar(50),
    Total_Damage  varchar(50),
    Total_Damage_Description varchar(50),
    Total_Houses_Destroyed varchar(50),
    Total_Houses_Damaged  varchar(50)
    )
    


CREATE TABLE TsunamiCauseCode (
    idTsunamiCauseCode int PRIMARY KEY,
    name varchar(50)
    )
    


CREATE TABLE TsunamiEventValidity (
    idTsunamiEventValidity int PRIMARY KEY,
    name varchar(50)
    )
    


CREATE TABLE Date (
    idDate INT IDENTITY(1,1) PRIMARY KEY,
    Mo INT NULL,
    Dy INT NULL,
    Year INT NULL
    )
    


CREATE TABLE Location (
    idLocation INT IDENTITY(1,1) PRIMARY KEY,
    Country varchar(50) NULL,
    LocationName varchar(50) NULL
    )
    


CREATE TABLE Position (
    idPosition INT IDENTITY(1,1) PRIMARY KEY,
    Latitude float NULL,
    Longitude float NULL
    )
    


CREATE TABLE Event (
    idEvent INT IDENTITY(1,1) PRIMARY KEY,
    MaximumWaterHeight float NULL,
    NumberofRunups INT NULL,
    TsunamiMagnitude float NULL,
    TsunamiIntensity float NULL,
    TotalDeaths float NULL,
    TotalMissing float NULL,
    TotalMissingDescription float NULL,
    TotalInjuries float NULL,
    TotalDamage float NULL,
    TotalDamageDescription float NULL,
    TotalHousesDestroyed float NULL,
    TotalHousesDamaged float NULL,
    Hr float NULL,
    Mn float NULL,
    Sec float NULL,
    idPosition INT NULL,
    idTsunamiCauseCode INT NULL,
    idTsunamiEventValidity INT NULL,
    idDate INT NULL,
    idLocation INT NULL,
    FOREIGN KEY (idPosition) REFERENCES Position(idPosition),
    FOREIGN KEY (idTsunamiCauseCode) REFERENCES TsunamiCauseCode(idTsunamiCauseCode),
    FOREIGN KEY (idTsunamiEventValidity) REFERENCES TsunamiEventValidity(idTsunamiEventValidity),
    FOREIGN KEY (idDate) REFERENCES Date(idDate),
    FOREIGN KEY (idLocation) REFERENCES Location(idLocation)
    
    )
    
