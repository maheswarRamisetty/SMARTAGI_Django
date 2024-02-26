
CREATE TABLE users (
    user_id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(50) NOT NULL UNIQUE,
    email VARCHAR(100) NOT NULL UNIQUE,
    password VARCHAR(100) NOT NULL
)ENGINE=InnoDB;


CREATE TABLE sessions (
    session_id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT NOT NULL,
    session_key VARCHAR(100) NOT NULL UNIQUE,
    FOREIGN KEY (user_id) REFERENCES users(user_id)
)ENGINE=InnoDB;
