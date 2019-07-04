DROP PROCEDURE IF EXISTS test;
CREATE PROCEDURE test()
BEGIN
  SET @name = 'registrobicis';

  SELECT COUNT(*) FROM @name;
END;

DROP PROCEDURE IF EXISTS execute_create_table_query;
CREATE PROCEDURE execute_create_table_query(query TEXT)
BEGIN
  PREPARE createtb FROM query;
  EXECUTE createtb;
  DEALLOCATE PREPARE createtb;
END;
  
DROP PROCEDURE IF EXISTS execute_drop_table_query;
CREATE PROCEDURE execute_drop_table_query(query TEXT)
BEGIN
  PREPARE deletetb FROM query;
  EXECUTE deletetb;
  DEALLOCATE PREPARE deletetb;
END;