CREATE DATABASE sistema_academico;

-- USE sistema_academico;

CREATE TABLE Alunos (
    id_aluno INT PRIMARY KEY NOT NULL AUTO_INCREMENT,
    nome VARCHAR(100) NOT NULL,
    data_nascimento DATE NOT NULL,
    matricula VARCHAR(11) NOT NULL UNIQUE,
    data_matricula TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    id_curso_fk INT NOT NULL,
    FOREIGN KEY (id_curso_fk) REFERENCES Cursos (id_curso)
);

CREATE TABLE Cursos (
    id_curso INT PRIMARY KEY NOT NULL AUTO_INCREMENT,
    codigo VARCHAR(10) NOT NULL UNIQUE,
    nome VARCHAR(100) NOT NULL,
    carga_horaria FLOAT NOT NULL
 );
 