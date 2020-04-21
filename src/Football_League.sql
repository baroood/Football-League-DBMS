CREATE DATABASE IF NOT EXISTS Football_League;
use Football_League;

drop table if exists Players;
drop table if exists Managers;
drop table if exists Coaches;
drop table if exists Tournaments_Played;
drop table if exists Fans;
drop table if exists Tournaments;
drop table if exists Employee;
drop table if exists Clubs;
drop table if exists Stadiums;



create table Stadiums(
	Stadium_ID INT NOT NULL, 
	Stadium_Name VARCHAR(30) NOT NULL, 
    Stadium_Location VARCHAR(30) NOT NULL, 
	Capacity BIGINT NOT NULL,  
	PRIMARY KEY (Stadium_ID)
);
create table Clubs(
	Club_ID INT NOT NULL, 
	Club_Name VARCHAR(30) NOT NULL, 
	Stadium_ID INT NOT NULL, 
	Games_Won INT NOT NULL, 
	Games_Lost INT NOT NULL, 
	PRIMARY KEY (Club_ID),
    FOREIGN KEY (Stadium_ID) REFERENCES Stadiums(Stadium_ID)
);
create table Employee(
	Employee_ID INT NOT NULL, 
	First_Name VARCHAR(30) NOT NULL, 
	Last_Name VARCHAR(30) NOT NULL, 
	Salary BIGINT, 
	Club_ID INT NOT NULL, 
	PRIMARY KEY (Employee_ID),
    FOREIGN KEY (Club_ID) REFERENCES Clubs(Club_ID)
);
create table Tournaments_Played( 
	Club_ID INT NOT NULL, 
	Tournaments_Played VARCHAR(30) NOT NULL,  
	PRIMARY KEY(Club_ID, Tournaments_Played)
);
create table Fans(
	Club_Name VARCHAR(30) NOT NULL, 
	No_Of_Fans BIGINT, 
	No_Of_Fan_Clubs BIGINT
);
create table Tournaments(
	Tournament_Name VARCHAR(30), 
	No_Of_Clubs INT NOT NULL, 
	Prize_Pool BIGINT, 
	Duration INT NOT NULL
);
create table Players(
	Employee_ID INT, 
	Goals INT,
    Assists INT,
    Tackles INT,
    Posotion VARCHAR(30) NOT NULL,
	FOREIGN KEY (Employee_ID) REFERENCES Employee(Employee_ID)
);
create table Managers(
	Employee_ID INT,
	FOREIGN KEY (Employee_ID) REFERENCES Employee(Employee_ID)
);
create table Coaches(
	Employee_ID INT,
	FOREIGN KEY (Employee_ID) REFERENCES Employee(Employee_ID)
);

INSERT INTO Stadiums VALUES (1,'Trafford','Manchester',19000);
INSERT INTO Stadiums VALUES (2,'Emirates','Arsenal',20000);
INSERT INTO Stadiums VALUES (3,'CampNou','Barcelona',21000);


INSERT INTO Clubs VALUES (1,'ManU',1,2,3);
INSERT INTO Clubs VALUES (2,'Arsenal',2,0,0);
INSERT INTO Clubs VALUES (3,'Barca',3,1,2);

INSERT INTO Employee VALUES (1,'Romelu','Lukaku',102383,1);
INSERT INTO Employee VALUES (2,'Jorjo','Mason',102343,2);
INSERT INTO Employee VALUES (3,'Lionel','Messi',1023383,3);
INSERT INTO Employee VALUES (4,'Kiya','Titan',102213,2);
INSERT INTO Employee VALUES (5,'Rand','Kreed',10383,3);

INSERT INTO Tournaments VALUES ('WorldCup',2,1023833,10);
INSERT INTO Tournaments VALUES ('League',2,2021833,15);

INSERT INTO Tournaments_Played VALUES (1,'League');
INSERT INTO Tournaments_Played VALUES (3,'League');
INSERT INTO Tournaments_Played VALUES (2,'WorldCup');
INSERT INTO Tournaments_Played VALUES (3,'WorldCup');

INSERT INTO Players VALUES (1,5,2,0,'CF');
INSERT INTO Players VALUES (3,10,9,4,'LW');
INSERT INTO Managers VALUES (2);
INSERT INTO Managers VALUES (5);
INSERT INTO Coaches VALUES (4);

INSERT INTO Fans VALUES ('ManU', 123, 12);
INSERT INTO Fans VALUES ('Arsenal', 78, 7);
INSERT INTO Fans VALUES ('Barca', 431, 123);














