----Script Creación DATA BASE tfg
CREATE DATABASE models_tfg;
\c models_tfg
DROP TABLE IF EXISTS Instances;

CREATE TABLE Instances (
	Cod_Instance serial PRIMARY KEY,
	Content json  NOT NULL
);
DROP TABLE IF EXISTS Logs;
CREATE TABLE Logs (
	Cod_Log serial PRIMARY KEY,
	Content text,	
	CONSTRAINT fk_cod_instance
      FOREIGN KEY(Cod_Instance) 
	  REFERENCES Viveros(Cod_Instance) ON DELETE CASCADE
);

