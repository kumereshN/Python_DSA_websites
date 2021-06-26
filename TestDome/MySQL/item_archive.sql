CREATE TABLE item (
  id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
  name VARCHAR(50) NOT NULL,
  quantity INT NOT NULL
);

CREATE TABLE item_archive (
  archive_id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
  name VARCHAR(50) NOT NULL
);

DELIMITER $$
CREATE
TRIGGER
 item_delete
AFTER DELETE
 ON item
FOR EACH ROW
BEGIN
  INSERT INTO item_archive(name) VALUES (
old.name
);
END;
$$
DELIMITER ;
