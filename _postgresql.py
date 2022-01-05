import psycopg2

hostname = 'ec2-3-212-172-25.compute-1.amazonaws.com'
database = 'dbipg177vham9q'
username = 'ayfhllgylxnjov'
password = 'ec4c8c03775f2c5635ee6ae71b6ab5ce077f0c49f5cb625acf946fb1fd468eb7'
port_id = 5432


conn = psycopg2.connect(dbname=database, user=username, password=password, host=hostname)

cur = conn.cursor()

# cur.execute('''CREATE TABLE day(
# day_id SERIAL PRIMARY KEY,
# day int NOT NULL,
# month int NOT NULL,
# year int NOT NULL,
# feeling_level INT NOT NULL,
# exercise_level INT NOT NULL,
# sleep_quality INT NOT NULL
# );
# ''')

# cur.execute("DELETE FROM app_user WHERE user_id = 2;")

# cur.execute("SELECT * FROM app_user;")

# print(cur.fetchall())

conn.commit()

cur.close()

conn.close()
