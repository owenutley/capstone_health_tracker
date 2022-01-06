from _postgresql import database, username, password, hostname
from matplotlib import pyplot as plt
import psycopg2

conn = psycopg2.connect(dbname=database, user=username, password=password, host=hostname)

cur = conn.cursor()

cur.execute(f'''SELECT day, feeling_level, exercise_level, sleep_quality FROM day
            WHERE year = {2022} AND month = {3};''')

this_month = cur.fetchall()

conn.commit()

cur.close()

conn.close()

print(this_month)

feel = []
exercise = []
sleep = []
days = []

for day in this_month:
    days.append(day[0])
    if day[1] == 3:
        feel.append(5)
    elif day[1] == 2:
        feel.append(3)
    else:
        feel.append(1)
    exercise.append(day[2])
    sleep.append(day[3])



plt.plot(days, feel, color="navy")
plt.plot(days, exercise, color="green")
plt.plot(days, sleep, color="red")
plt.show()