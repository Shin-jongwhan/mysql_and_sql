### 241122
## trigger
### 특정 foreign key에 따라서 자동으로 값이 설정되도록 함
### ex)
```
DELIMITER $$

CREATE TRIGGER set_pipeline_name_version_i
BEFORE INSERT ON pipeline_version
FOR EACH ROW
BEGIN
    -- pipeline 테이블에서 name 값을 가져와 NEW.pipeline에 설정
    SET NEW.pipeline = (SELECT name FROM pipeline WHERE idx = NEW.pipeline_idx_fk);
END$$

DELIMITER ;
```
