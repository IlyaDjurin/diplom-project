import sqlite3
import internet_magaz

def add_column(database_name, table_name, column_name, data_type):


  connection = sqlite3.connect(database_name)
  cursor = connection.cursor()


  if data_type == "Integer":
    data_type_formatted = "INTEGER"

  elif data_type == "String":
    data_type_formatted = "VARCHAR(100)"


  format_str = ("ALTER TABLE '{table_name}' ADD column '{column_name}' '{data_type}'")
  sql_command = format_str.format(table_name=table_name, column_name=column_name, data_type=data_type_formatted)

  cursor.execute(sql_command)
  connection.commit()
  connection.close()

 add_column(internet_magaz, tovarphoto ,tovarphoto_test, VARCHAR)  
