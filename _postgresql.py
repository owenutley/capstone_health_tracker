import psycopg2

hostname = 'localhost'
database = 'health'
username = 'postgres'
password = 'MyData'
port_id = 5432


conn = psycopg2.connect(dbname=database, user=username, password=password, host=hostname)

cur = conn.cursor()

cur.execute('''CREATE TABLE day_exercise
(day_id INT REFERENCES day(day_id),
exercise_id INT NOT NULL REFERENCES exercise(exercise_id));
''')

# cur.execute("INSERT INTO app_user (name, email, password)
# VALUES ('owen', 'owen@example.com', '123456789')")

# cur.execute("DELETE FROM app_user WHERE user_id = 2;")

# cur.execute("SELECT * FROM app_user;")

# print(cur.fetchall())

conn.commit()

cur.close()

conn.close()
