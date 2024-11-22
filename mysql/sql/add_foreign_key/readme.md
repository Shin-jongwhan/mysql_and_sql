### 241122
## foreign key 추가 sql
### ex)
```
-- 1. 새로운 컬럼 생성
ALTER TABLE pipeline_version
ADD COLUMN pipeline_idx_fk INT;

-- 2. 외래 키 제약 조건 등록
ALTER TABLE pipeline_version
ADD CONSTRAINT FK_pipeline_version_pipeline
FOREIGN KEY (pipeline_idx_fk)
REFERENCES pipeline (idx)
ON UPDATE NO ACTION
ON DELETE NO ACTION;
```
