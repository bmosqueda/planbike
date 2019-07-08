DROP PROCEDURE IF EXISTS test;
CREATE PROCEDURE test()
BEGIN
  SET @name = 'registrobicis';

  SELECT 10 * 15;

  SELECT 'hola' AS mundo;
END;

DROP PROCEDURE IF EXISTS execute_create_table_query;
CREATE PROCEDURE execute_create_table_query(query TEXT)
BEGIN
  SET @query_tmp = query;

  PREPARE createtb FROM @query_tmp;
  EXECUTE createtb;
  DEALLOCATE PREPARE createtb;
END;
  
DROP PROCEDURE IF EXISTS execute_drop_table_query;
CREATE PROCEDURE execute_drop_table_query(query TEXT)
BEGIN
  SET @query_tmp = query;

  PREPARE deletetb FROM @query_tmp;
  EXECUTE deletetb;
  DEALLOCATE PREPARE deletetb;
END;