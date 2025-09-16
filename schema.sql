CREATE DATABASE quiz_db;
USE quiz_db;

CREATE TABLE IF NOT EXISTS admin (
    admin_id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(50) UNIQUE NOT NULL,
    password VARCHAR(50) NOT NULL
);

CREATE TABLE IF NOT EXISTS questions (
    q_id INT AUTO_INCREMENT PRIMARY KEY,
    technology VARCHAR(50),
    question_text TEXT,
    option1 VARCHAR(100),
    option2 VARCHAR(100),
    option3 VARCHAR(100),
    option4 VARCHAR(100),
    correct_answer INT
);

CREATE TABLE IF NOT EXISTS users (
    user_id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(50),
    mobile VARCHAR(15)
);

CREATE TABLE IF NOT EXISTS results (
    result_id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT,
    technology VARCHAR(50),
    score INT,
    quiz_time DATETIME,
    FOREIGN KEY (user_id) REFERENCES users(user_id)
);

INSERT INTO admin (username, password) VALUES ('hafeez', '123');


