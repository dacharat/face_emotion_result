import psycopg2
from psycopg2.extras import Json, DictCursor
import json

class Database:
  def __init__(self):
    self.conn = psycopg2.connect(
        host='my_postgres',
        port=5432,
        dbname='my_face_data',
        user='postgres',
    )
    self.cur = self.conn.cursor()
    self.TABLENAME = "test_person"
    self.SUB_TABLENAME = 'record'

  # create table
  def create_table(self):
    self.cur.execute(
        "CREATE TABLE IF NOT EXISTS {} (id serial PRIMARY KEY, face varchar, face_image text[], face_encoding text[]);".format(self.TABLENAME))
    self.cur.execute('CREATE TABLE IF NOT EXISTS {} (id SERIAL PRIMARY KEY, person_id INTEGER REFERENCES {}(id), record_name varchar, emotion_detail text[]);'.format(
        self.SUB_TABLENAME, self.TABLENAME))
    self.conn.commit()

  # insert new row to database
  def insert(self, face="Jack", image=[], face_encoding=[]):
    self.cur.execute("INSERT INTO {} (face, face_image, face_encoding) VALUES (%s, %s, %s);".format(
        self.TABLENAME), [face, image, face_encoding,])
    self.conn.commit()

  # show all rows in database
  def show_data(self):
    self.cur.execute("SELECT * FROM {};".format(self.TABLENAME))
    result = self.cur.fetchall()
    print(result)

  # get all rows in face column
  def get_all_face(self):
    self.cur.execute("SELECT face FROM {};".format(self.TABLENAME))
    return [row[0] for row in self.cur.fetchall()]

  # delete row from face
  def delete_row_from_name(self, face):
    self.cur.execute(
        "DELETE FROM {} WHERE face=%s;".format(self.TABLENAME), [face])
    self.conn.commit()

  # delete table
  def drop_database(self):
    self.cur.execute("DROP TABLE {};".format(self.TABLENAME))
    self.conn.commit()

  # check if table is exists or not
  def check_table_exists(self):
    self.cur.execute(
        "SELECT * FROM information_schema.tables WHERE table_name=%s;", [self.TABLENAME])
    return bool(self.cur.rowcount)

  # check database is exists or not
  def check_database_exists(self):
    self.cur.execute("SELECT 1 FROM pg_database WHERE datname='my_face_data';")
    return bool(self.cur.rowcount)

  # get number of rows in database
  def get_number_of_rows(self):
    self.cur.execute("SELECT COUNT(*) FROM {};".format(self.TABLENAME))
    return self.cur.fetchone()[0]

  def get_face_encoding(self):
    self.cur.execute(
        "SELECT face, face_encoding FROM {};".format(self.TABLENAME))
    return self.cur.fetchall()

  def change_face_name(self, face, newFaceName):
    self.cur.execute("UPDATE {} SET face=%s WHERE face=%s".format(
        self.TABLENAME), [newFaceName,face])
    self.conn.commit()

  def insert_new_record(self, person_id, emotion_detail, record_name = None):
    self.cur.execute(
        "SELECT * FROM {} WHERE person_id=%s;".format(self.SUB_TABLENAME), [person_id])
    number_of_record = len(self.cur.fetchall())
    record_name = "record-" + str(number_of_record + 1) if record_name is None else record_name
    self.cur.execute("INSERT INTO {} (person_id, record_name, emotion_detail) VALUES (%s, %s, %s);".format(
        self.SUB_TABLENAME), [person_id, record_name, [Json(i) for i in emotion_detail]])
    self.conn.commit()

  def get_primary_key_from_face(self, face):
    self.cur.execute('SELECT id FROM {} WHERE face=%s'.format(self.TABLENAME), [face])
    person_id = self.cur.fetchone()
    return person_id[0]

  # close cur and conn
  def close(self):
    self.cur.close()
    self.conn.close()
