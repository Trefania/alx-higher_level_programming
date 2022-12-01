--creates the table force_name on your MySQL server.
--force_name description:
--id NT
--me VARCHAR(256) can’t be null
--The datbase name wil be passed as an argument of the mysql command
--if e tble force_name already exists, your script should not fail

CREATE TABLE IF NOT EXISTS force_name (id INT, name VARCHAR(256) NOT NULL);
