DROP DATABASE IF EXISTS NHL_Top_100;
CREATE DATABASE NHL_Top_100; 
USE NHL_Top_100;

CREATE TABLE Teams(
Team_ID INT NOT NULL,
Team ENUM('Anaheim Ducks',
        'Arizona Coyotes',
        'Boston Bruins',
        'Buffalo Sabres',
        'Calgary Flames',
        'Carolina Hurricanes',
        'Chicago Blackhawks',
        'Colorado Avalanche',
        'Columbus Blue Jackets',
        'Dallas Stars',
        'Detroit Red Wings',
        'Edmonton Oilers',
        'Florida Panthers',
        'Los Angeles Kings',
        'Minnesota Wild',
        'Montreal Canadiens',
        'Nashville Predators',
        'New Jersey Devils',
        'New York Islanders',
        'New York Rangers',
        'Ottawa Senators',
        'Philadelphia Flyers',
        'Pittsburgh Penguins',
        'San Jose Sharks',
        'Seattle Kraken',
        'St. Louis Blues',
        'Tampa Bay Lightning',
        'Toronto Maple Leafs',
        'Vancouver Canucks',
        'Vegas Golden Knights',
        'Washington Capitals',
        'Winnipeg Jets'), 
        Division ENUM('Atlantic', 'Metropolitan', 'Central', 'Pacific'), 
        PRIMARY KEY(Team_ID)
);

INSERT INTO Teams (Team_ID, Team, Division) VALUES
(1, 'Anaheim Ducks', 'Pacific'),
(2, 'Arizona Coyotes', 'Central'),
(3, 'Boston Bruins', 'Atlantic'),
(4, 'Buffalo Sabres', 'Atlantic'),
(5, 'Calgary Flames', 'Pacific'),
(6, 'Carolina Hurricanes', 'Metropolitan'),
(7, 'Chicago Blackhawks', 'Central'),
(8, 'Colorado Avalanche', 'Central'),
(9, 'Columbus Blue Jackets', 'Metropolitan'),
(10, 'Dallas Stars', 'Central'),
(11, 'Detroit Red Wings', 'Atlantic'),
(12, 'Edmonton Oilers', 'Pacific'),
(13, 'Florida Panthers', 'Atlantic'),
(14, 'Los Angeles Kings', 'Pacific'),
(15, 'Minnesota Wild', 'Central'),
(16, 'Montreal Canadiens', 'Atlantic'),
(17, 'Nashville Predators', 'Central'),
(18, 'New Jersey Devils', 'Metropolitan'),
(19, 'New York Islanders', 'Metropolitan'),
(20, 'New York Rangers', 'Metropolitan'),
(21, 'Ottawa Senators', 'Atlantic'),
(22, 'Philadelphia Flyers', 'Metropolitan'),
(23, 'Pittsburgh Penguins', 'Metropolitan'),
(24, 'San Jose Sharks', 'Pacific'),
(25, 'Seattle Kraken', 'Pacific'),
(26, 'St. Louis Blues', 'Central'),
(27, 'Tampa Bay Lightning', 'Atlantic'),
(28, 'Toronto Maple Leafs', 'Atlantic'),
(29, 'Vancouver Canucks', 'Pacific'),
(30, 'Vegas Golden Knights', 'Pacific'),
(31, 'Washington Capitals', 'Metropolitan'),
(32, 'Winnipeg Jets', 'Central');


CREATE TABLE Olympic_Team(
Country_ID INT NOT NULL, 
Country VARCHAR(50), 
PRIMARY KEY(Country_ID)
);

INSERT INTO Olympic_Team (Country_ID, Country) 
VALUES
(1, 'USA'),
(2, 'Canada'),
(3, 'Finland'),
(4, 'Switzerland'),
(5, 'Czech Republic'),
(6, 'Sweden'),
(7, 'Russia'),
(8, 'Germany'),
(9, 'Denmark'),
(10, 'Norway');

CREATE TABLE Players(
player_ID INT NOT NULL AUTO_INCREMENT, 
tID INT NOT NULL, 
pName VARCHAR(50), 
Country INT NOT NULL,
position ENUM('C', 'LW', 'RW', 'D', 'G'),
Stanley_Cup TINYINT DEFAULT 0,
PRIMARY KEY (player_ID, pName, position),
FOREIGN KEY(tID) REFERENCES Teams(Team_ID) ON DELETE CASCADE ON UPDATE CASCADE,
FOREIGN KEY(Country) REFERENCES Olympic_Team(Country_ID) ON DELETE CASCADE ON UPDATE CASCADE
);

-- Centers (C)
INSERT INTO Players (player_ID, tID, pName, Country, position, Stanley_Cup)
VALUES
(1, 12, 'Connor McDavid', 2, 'C', 0),
(2, 28, 'Auston Matthews', 1, 'C', 0),
(3, 8, 'Nathan MacKinnon', 2, 'C', 1),
(4, 23, 'Sidney Crosby', 2, 'C', 1),
(5, 30, 'Jack Eichel', 1, 'C', 1),
(6, 29, 'Elias Pettersson', 6, 'C', 0),
(7, 6, 'Sebastian Aho', 3, 'C', 0),
(8, 11, 'Dylan Larkin', 1, 'C', 0),
(9, 19, 'Mathew Barzal', 2, 'C', 0),
(10, 16, 'Nick Suzuki', 2, 'C', 0);

-- Left Wings (LW)
INSERT INTO Players VALUES
(11, 7, 'Artemi Panarin', 7, 'LW', 0),
(12, 13, 'Brad Marchand', 2,'LW', 1),
(13, 32, 'Kyle Connor', 1,'LW', 0),
(14, 31, 'Alex Ovechkin', 7,'LW', 1),
(15, 5, 'Jonathan Huberdeau', 2, 'LW', 0),
(16, 27, 'Jake Guentzel', 1, 'LW', 1),
(17, 8, 'Gabriel Landeskog', 2, 'LW', 1),
(18, 18, 'Timo Meier', 4, 'LW', 0),
(19, 5, 'Brady Tkachuk', 1, 'LW', 0),
(20, 20, 'Alexis Lafrenière', 2, 'LW', 0);

-- Right Wings (RW)
INSERT INTO Players VALUES
(21, 10, 'Mikko Rantanen', 3, 'RW', 1),
(22, 3, 'David Pastrnak', 5, 'RW', 0),
(23, 11, 'Patrick Kane', 1, 'RW', 1),
(24, 28, 'William Nylander', 6, 'RW', 0),
(25, 30, 'Mark Stone', 2, 'RW', 1),
(26, 15, 'Vladimir Tarasenko', 7, 'RW', 1),
(27, 26, 'Jordan Kyrou', 2,'RW', 0),
(28, 29, 'Brock Boeser', 1, 'RW', 0),
(29, 21, 'Claude Giroux', 2, 'RW', 0),
(30, 22, 'Travis Konecny', 2, 'RW', 0);

-- Defensemen (D)
INSERT INTO Players VALUES
(31, 8, 'Cale Makar', 2,'D', 1),
(32, 27, 'Victor Hedman', 6,'D', 1),
(33, 17, 'Roman Josi', 4, 'D', 0),
(34, 20, 'Adam Fox', 2, 'D', 0),
(35, 18, 'Dougie Hamilton', 2, 'D', 0),
(36, 3, 'Charlie McAvoy', 1, 'D', 0),
(37, 29, 'Quinn Hughes', 1, 'D', 0),
(38, 4, 'Rasmus Dahlin', 6, 'D', 0),
(39, 28, 'Morgan Rielly', 2, 'D', 0),
(40, 6, 'Brent Burns', 2, 'D', 0);

-- Goalies (G)
INSERT INTO Players VALUES
(41, 20, 'Igor Shesterkin', 7, 'G', 0),
(42, 17, 'Juuse Saros', 3, 'G', 0),
(43, 32, 'Connor Hellebuyck', 1, 'G', 0),
(44, 19, 'Ilya Sorokin', 7, 'G', 0),
(45, 10, 'Jake Oettinger', 1, 'G', 0),
(46, 29, 'Thatcher Demko', 1, 'G', 0),
(47, 21, 'Linus Ullmark', 6, 'G', 0),
(48, 28, 'Frederik Andersen', 9, 'G', 0),
(49, 1, 'John Gibson', 1, 'G', 0),
(50, 3, 'Jeremy Swayman', 1, 'G', 0);

CREATE TABLE Stats(
stat_ID INT NOT NULL AUTO_INCREMENT,
pID INT NOT NULL, 
GP INT DEFAULT 0,
Goals INT DEFAULT 0,
Assists INT DEFAULT 0,
Points INT DEFAULT 0,
Saves INT DEFAULT 0,
SVP DECIMAL(5,3) DEFAULT 0.0,
GAA DECIMAL(5,3) DEFAULT 0.0,
Wins INT DEFAULT 0,
PRIMARY KEY(stat_ID), 
FOREIGN KEY(pID) REFERENCES Players(player_ID) ON DELETE CASCADE ON UPDATE CASCADE
); 

-- Centers
INSERT INTO Stats (pID, GP, Goals, Assists, Points) VALUES
(1, 67, 26, 74, 100),       -- Connor McDavid
(2, 67, 33, 45, 78),        -- Auston Matthews
(3, 79, 32, 84, 116),       -- Nathan MacKinnon
(4, 80, 33, 58, 91),        -- Sidney Crosby
(5, 77, 28, 66, 94),        -- Jack Eichel
(7, 79, 29, 45, 74),        -- Sebastian Aho
(8, 82, 30, 40, 70),        -- Dylan Larkin
(10, 82, 30, 59, 89);       -- Nick Suzuki

-- Left Wings
INSERT INTO Stats (pID, GP, Goals, Assists, Points) VALUES
(11, 80, 37, 52, 89),       -- Artemi Panarin
(12, 71, 23, 28, 51),       -- Brad Marchand
(13, 82, 41, 56, 97),       -- Kyle Connor
(14, 65, 44, 29, 73),       -- Alex Ovechkin
(15, 81, 28, 34, 62),       -- Jonathan Huberdeau
(16, 80, 41, 39, 80),       -- Jake Guentzel
(19, 72, 29, 26, 55),       -- Brady Tkachuk
(20, 82, 17, 28, 45);       -- Alexis Lafrenière

-- Right Wings
INSERT INTO Stats (pID, GP, Goals, Assists, Points) VALUES
(21, 82, 32, 56, 88),       -- Mikko Rantanen
(22, 82, 43, 63, 106),      -- David Pastrnak
(23, 72, 21, 38, 59),       -- Patrick Kane
(24, 82, 45, 39, 84),       -- William Nylander
(25, 66, 19, 48, 67),       -- Mark Stone
(27, 82, 36, 34, 70),       -- Jordan Kyrou
(28, 75, 25, 25, 50),       -- Brock Boeser
(29, 81, 15, 35, 50),       -- Claude Giroux
(30, 82, 24, 52, 76);       -- Travis Konecny

-- Defensemen
INSERT INTO Stats (pID, GP, Goals, Assists, Points) VALUES
(31, 80, 30, 62, 92),       -- Cale Makar
(32, 79, 15, 51, 66),       -- Victor Hedman
(33, 53, 9, 29, 38),        -- Roman Josi
(34, 74, 10, 51, 61),       -- Adam Fox
(35, 64, 9, 31, 40),        -- Dougie Hamilton
(37, 68, 16, 60, 76),       -- Quinn Hughes
(38, 73, 17, 51, 68),       -- Rasmus Dahlin
(39, 82, 7, 34, 41),        -- Morgan Rielly
(40, 78, 4, 28, 32);        -- Brent Burns

-- Goalies
INSERT INTO Stats (pID, GP, Saves, SVP, GAA, Wins) VALUES
(41, 61, 1584, 0.905, 2.86, 27),   -- Igor Shesterkin
(42, 58, 1426, 0.896, 2.98, 20),  -- Juuse Saros
(43, 63, 1539, 0.925, 2.000, 47), -- Connor Hellebuyck
(44, 61, 1538, 0.907, 2.71, 30),  -- Ilya Sorokin
(45, 58, 1464, 0.909, 2.59, 36),  -- Jake Oettinger
(46, 29, 740, 0.912, 2.77, 11),   -- Thatcher Demko
(47, 44, 1118, 0.910, 2.72, 25),  -- Linus Ullmark
(48, 22, 491, 0.899, 2.50, 13),   -- Frederik Andersen
(49, 29, 740, 0.912, 2.77, 11),   -- John Gibson
(50, 58, 1456, 0.892, 3.11, 22);  -- Jeremy Swayman
CREATE TABLE Contracts(
contract_ID INT NOT NULL AUTO_INCREMENT,
pID INT NOT NULL, 
AAV DECIMAL(5,2) NOT NULL, -- This is calculated in millions for easier numbers
Length INT NOT NULL, 
Date_Signed DATE NOT NULL,
PRIMARY KEY(contract_ID), 
FOREIGN KEY(pID) REFERENCES Players(player_ID) ON DELETE CASCADE ON UPDATE CASCADE

);

INSERT INTO Contracts (pID, AAV, length, date_signed) VALUES
(1, 12.50, 8, '2022-07-01'),
(2, 11.64, 5, '2023-07-13'),
(3, 12.60, 8, '2022-08-01'),
(4, 8.70, 3, '2021-06-30'),
(5, 10.00, 8, '2023-07-01'),
(6, 9.25, 7, '2024-01-10'),
(7, 8.46, 8, '2022-07-26'),
(8, 6.10, 5, '2023-08-15'),
(9, 9.15, 8, '2022-11-01'),
(10, 7.88, 8, '2023-10-12'),
(11, 11.64, 7, '2021-07-01'),
(12, 6.13, 4, '2020-09-14'),
(13, 7.14, 7, '2022-09-01'),
(14, 9.50, 5, '2021-07-01'),
(15, 10.50, 8, '2022-07-13'),
(16, 6.00, 5, '2021-07-01'),
(17, 7.00, 8, '2021-07-01'),
(18, 8.80, 8, '2023-06-30'),
(19, 8.21, 7, '2021-09-07'),
(20, 2.50, 3, '2022-07-01'),
(21, 9.25, 6, '2021-07-01'),
(22, 11.25, 8, '2023-01-01'),
(23, 2.50, 1, '2023-07-15'),
(24, 6.96, 4, '2022-08-01'),
(25, 9.50, 8, '2021-10-01'),
(26, 5.50, 1, '2023-07-01'),
(27, 8.13, 8, '2022-09-13'),
(28, 6.65, 6, '2021-07-01'),
(29, 6.50, 3, '2022-07-13'),
(30, 5.50, 6, '2020-09-14'),
(31, 9.00, 6, '2022-07-13'),
(32, 7.87, 8, '2020-12-01'),
(33, 9.06, 8, '2021-07-01'),
(34, 9.50, 7, '2023-07-01'),
(35, 9.00, 7, '2021-07-01'),
(36, 9.50, 8, '2021-07-01'),
(37, 7.85, 6, '2022-09-09'),
(38, 11.00, 8, '2023-10-01'),
(39, 7.50, 8, '2020-08-01'),
(40, 5.28, 2, '2022-07-13'),
(41, 5.67, 4, '2021-08-03'),
(42, 5.00, 4, '2022-08-16'),
(43, 6.17, 7, '2023-07-01'),
(44, 8.25, 8, '2023-07-01'),
(45, 4.00, 3, '2022-09-01'),
(46, 5.00, 5, '2021-12-01'),
(47, 5.00, 4, '2022-07-01'),
(48, 3.40, 2, '2023-07-01'),
(49, 6.40, 7, '2019-08-01'),
(50, 3.10, 3, '2024-07-01');

SET SQL_SAFE_UPDATES = 0;

/* VIEWS */

CREATE VIEW Player_Profile AS 
SELECT 
concat(Players.pName, ' ', '(', Teams.Team, ')') AS Profile, 
concat('G', ':', Stats.Goals, ' ', 'A', ':', Stats.Assists, ' ', 'P', ':', Stats.Points) AS Stats,
concat(
  Contracts.Length, ' Year', ',', ' ', Contracts.AAV * Length, 'M', ' ', 'Contract, with an AAV of ',
  Contracts.AAV, 'M Signed on ',
  DATE_FORMAT(Contracts.Date_Signed, '%M %D, %Y')
) AS Financials
FROM 
Contracts 
JOIN 
Players ON Players.Player_ID = Contracts.pID 
JOIN 
Teams ON Teams.Team_ID = Players.tID
JOIN 
Stats ON Stats.pID = Players.Player_ID
WHERE Players.Position IN ('C', 'LW', 'RW', 'D')
ORDER BY AAV DESC;

CREATE VIEW Goalie_Profile AS 
SELECT 
concat(Players.pName, ' ', '(', Teams.Team, ')') AS Profile, 
concat('S', ':', Stats.Saves, ' ', 'Sv%', ':', ' ', Stats.SVP, ' ', 'W', ':', Stats.Wins) AS Stats,
concat(
  Contracts.Length, ' Year', ',', ' ', Contracts.AAV * Length, 'M', ' ', 'Contract, with an AAV of ',
  Contracts.AAV, 'M Signed on ',
  DATE_FORMAT(Contracts.Date_Signed, '%M %D, %Y')
) AS Financials
FROM 
Contracts 
JOIN 
Players ON Players.Player_ID = Contracts.pID 
JOIN 
Teams ON Teams.Team_ID = Players.tID
JOIN 
Stats ON Stats.pID = Players.Player_ID
WHERE Players.Position IN ('G')
ORDER BY AAV DESC;



CREATE VIEW Team_USA AS 
SELECT 
Players.pName, Olympic_Team.Country 
FROM 
Players 
JOIN 
Olympic_Team 
ON
Players.Country = Olympic_Team.Country_ID 
WHERE 
Players.Country = '1';


CREATE VIEW Top_GoalScorers AS 
SELECT Players.pName, Players.position, Teams.team, Stats.Goals 
FROM Players 
JOIN Stats 
ON Players.player_ID = Stats.pID 
JOIN Teams 
ON Teams.Team_ID = Players.tID
WHERE Stats.Goals >= 30; 

/*FUNCTIONS*/ 
DELIMITER $$
 
CREATE FUNCTION getPlayerID(playerName VARCHAR(50))
RETURNS INT DETERMINISTIC
BEGIN
	DECLARE pID_Found INT; 
    SELECT player_ID INTO pID_Found 
    FROM Players 
    WHERE pName = playerName;
    
    IF pID_Found is NULL
    THEN SET pID_Found = -1; 
    END IF;
    
    
    RETURN pID_Found;
 
END $$  

CREATE FUNCTION getTeamID(teamName VARCHAR(50)) 
RETURNS INT DETERMINISTIC 
BEGIN
	DECLARE foundTeam INT; 
    SELECT Team_ID INTO foundTeam 
    FROM Teams 
    WHERE Team = teamName; 
    
    IF foundTeam is NULL
    THEN SET foundTeam = -1; 
    END IF;
    
    RETURN foundTeam;
END $$

CREATE FUNCTION getCountryID(nation VARCHAR(50)) 
RETURNS INT DETERMINISTIC 
BEGIN 
	DECLARE foundCountry INT; 
    SELECT Country_ID INTO foundCountry 
    FROM Olympic_Team
    WHERE Country = nation; 
    
    IF foundCountry IS NULL 
    THEN SET foundCountry = -1;
    END IF ; 
    
    RETURN foundCountry;

END $$

CREATE FUNCTION getContractID(playerName VARCHAR(50))
RETURNS INT DETERMINISTIC 
BEGIN
	DECLARE foundcID INT; 
    DECLARE playerID INT;
    SELECT getPlayerID(playerName) INTO playerID;
    SELECT contract_ID INTO foundcID
    FROM Contracts 
    WHERE pID = playerID; 
    
    IF foundcID IS NULL 
    THEN SET foundcID = -1; 
    END IF; 
    
    RETURN foundcID;
	
END $$

/*STORED PROCEDURES*/ 

CREATE PROCEDURE getTeamRoster(IN teamName VARCHAR(50)) 
BEGIN 
	SELECT Players.pName, Players.position, Teams.Team 
    FROM 
    Players 
    JOIN 
    Teams 
    ON 
    Players.tID = Teams.Team_ID
    WHERE Teams.Team = teamName;
    
END $$

CREATE PROCEDURE addPlayer(
    playerName VARCHAR(50),
    playerPosition VARCHAR(25),
    playerTeam VARCHAR(25),
    nation VARCHAR(50)
)
BEGIN
    DECLARE findPlayer INT;
    DECLARE findTeam INT;
    DECLARE findNation INT;
    DECLARE duplicate INT;

    SELECT getPlayerID(playerName) INTO findPlayer;
    SELECT getTeamID(playerTeam) INTO findTeam;
    SELECT getCountryID(nation) INTO findNation;

    
    IF findPlayer != -1 THEN
		SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'DUPLICATE ENTRY';
    ELSEIF findPlayer = -1 AND findTeam = -1 AND findNation = -1 THEN
        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'IMCOMPLETE DATA';
    ELSEIF findTeam = -1 THEN
        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'The team you entered does not match our records';
    ELSEIF findNation = -1 THEN
        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'Country does not match our database';
    ELSE
        INSERT INTO Players(tID, pName, Country, position, Stanley_Cup)
        VALUES(findTeam, playerName, findNation, playerPosition, 0);
    END IF;
END $$

CREATE PROCEDURE addContract(playerName VARCHAR(50), newAAV DECIMAL(5,3), newLength INT, newSign DATE)
 BEGIN 
	DECLARE new_pID INT; 
    SELECT getPlayerID(playerName) INTO new_pID; 
    
    IF new_pID = -1
    THEN SELECT 'No Such Player Exists in our Database' AS PlayerError;
    ELSE 
    INSERT INTO Contracts (pID, AAV, length, date_signed) 
    VALUES 
    (new_pID, newAAV, newLength, newSign);
    END IF;
 END $$
 
 CREATE PROCEDURE addStats(playerName VARCHAR(50), playerGP INT, playerGoals INT, playerAssists INT, playerPoints INT)
 BEGIN 
	DECLARE new_pID INT; 
    SELECT getPlayerID(playerName) INTO new_pID; 
    
    IF new_pID = -1
    THEN SELECT 'No Such Player Exists in our Database' AS PlayerError;
    ELSE 
    INSERT INTO Stats (pID, GP, Goals, Assists, Points) 
    VALUES 
    (new_pID, playerGP, playerGoals, playerAssists, playerPoints);
    END IF;
 END $$
 
 
 CREATE PROCEDURE addStatsGoalie(playerName VARCHAR(50), playerGP INT, playerSaves INT, playerSVP DECIMAL(5,3), playerWins INT)
 BEGIN 
	DECLARE new_pID INT; 
    SELECT getPlayerID(playerName) INTO new_pID; 
    
    IF new_pID = -1
    THEN SELECT 'No Such Player Exists in our Database' AS PlayerError;
    ELSE 
    INSERT INTO Stats (pID, GP, Goals, Assists, Points) 
    VALUES 
    (new_pID, playerGP, playerSaves, playerSVP, playerWins);
    END IF;
 END $$
 
 
 CREATE PROCEDURE rosterMove(playerName VARCHAR(50), newTeam VARCHAR(50))
 BEGIN
	DECLARE new_pID INT; 
    SELECT getPlayerID(playerName) INTO new_pID; 
    
    IF new_pID = -1
    THEN SELECT 'No Such Player Exists in our Database' AS PlayerError;
    ELSE 
    UPDATE Players
    SET tID = getTeamID(newTeam)
    WHERE pName = playerName;
    END IF;
 END $$
 
 CREATE PROCEDURE deletePlayer(playerName VARCHAR(50))
 BEGIN
 DECLARE new_pID INT; 
    SELECT getPlayerID(playerName) INTO new_pID; 
    
    IF new_pID = -1
    THEN SELECT 'No Such Player Exists in our Database' AS PlayerError;
    ELSE 
    DELETE FROM Players 
    WHERE pName = playerName;
    END IF;
 END $$
 
CREATE PROCEDURE playerGuesser()
BEGIN
  SELECT P.pName, P.position, T.Team, O.Country
  FROM (
    SELECT player_ID
    FROM Players
    ORDER BY RAND()
    LIMIT 1
  ) AS RandomPlayer
  JOIN Players P ON P.player_ID = RandomPlayer.player_ID
  JOIN Teams T ON T.Team_ID = P.tID
  JOIN Olympic_Team O ON O.Country_ID = P.Country;
END $$
 
 DELIMITER ; 
 
 
 /* Views Called */
SELECT * FROM Player_Profile;
SELECT * FROM Goalie_Profile;

/* One call for each stored procedure */
/*Player Demonstration*/
CALL getTeamRoster('Vegas Golden Knights');
CALL getTeamRoster('Toronto Maple Leafs');
CALL addPlayer('Ace Dunn', 'RW', 'Vegas Golden Knights', 'USA'); 
CALL addStats('Ace Dunn', 62, 51, 22, 73);
CALL addContract('Ace Dunn', 11.25, 8, '2025-08-23');

/*Goalie Demonstration*/
CALL addPlayer('Merrimack Warrior', 'G', 'Toronto Maple Leafs', 'Canada');
CALL addStatsGoalie('Merrimack Warrior', 62, 791, 0.907, 44);
CALL addContract('Merrimack Warrior', 6.2, 5, '2025-07-01');

/*Updated Views with procedures to see clear player adds */
CALL getTeamRoster('Vegas Golden Knights');
CALL getTeamRoster('Toronto Maple Leafs');
SELECT * FROM Player_Profile; 
SELECT * FROM Goalie_Profile;
