CREATE DATABASE job51;
USE job51;

CREATE TABLE train_posts_data(
id INT UNSIGNED NOT NULL AUTO_INCREMENT,
post_url VARCHAR(500) NOT NULL,
post_name VARCHAR(100) NOT NULL,
post_salary FLOAT NOT NULL,
post_city VARCHAR(50) NOT NULL,
post_experience VARCHAR(50) NOT NULL,
post_education VARCHAR(50) NOT NULL,
post_number INT NOT NULL,
post_release_time VARCHAR(50) NOT NULL,
post_information VARCHAR(3000) NOT NULL,
post_category VARCHAR(100) NOT NULL,
post_keywords VARCHAR(100) NOT NULL,

company_url VARCHAR(500) NOT NULL,
company_name VARCHAR(100) NOT NULL,
company_nature VARCHAR(50) NOT NULL,
company_scale VARCHAR(50) NOT NULL,
company_category VARCHAR(100) NOT NULL,

crawl_date VARCHAR(50) NOT NULL,

PRIMARY KEY(id)
)ENGINE=InnoDB DEFAULT CHARSET=utf8
;