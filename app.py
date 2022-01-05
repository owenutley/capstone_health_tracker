from flask import Flask, render_template, request, redirect, url_for
# from flask import Flask, flash, redirect, render_template, request, session, abort
from _postgresql import hostname, database, username, password, port_id
import psycopg2

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("home.html")


# def show_info():
#     print(month + 'month')
#     print(day + 'day')
#     print(year + 'year')
#     print(feel)
#     print(exercise)
#     print(sleep)

@app.route("/_entry", methods=["GET", "POST"])
def edit_entry():
    if request.method == "POST":
        global month, day, year, feel, exercise, sleep
        date = request.form['date']
        date = date.split('-')
        year = date[0]
        month = date[1]
        day = date[2]
        feel = request.form['feel']
        exercise = request.form['elevel']
        sleep = request.form['slevel']

        # show_info()

        conn = psycopg2.connect(dbname=database, user=username, password=password, host=hostname)

        cur = conn.cursor()

        cur.execute(f'''INSERT INTO day (day, month, year, feeling_level, exercise_level, sleep_quality)
        VALUES ({day}, {month}, {year}, {feel}, {exercise}, {sleep});
        ''')
        conn.commit()

        cur.close()

        conn.close()

        return render_template('_entry.html')
    else:
        return render_template('_entry.html')

@app.route("/entry")
def entry():
    conn = psycopg2.connect(dbname=database, user=username, password=password, host=hostname)

    cur = conn.cursor()

    cur.execute("SELECT * FROM day;")

    this_month = cur.fetchall()

    conn.commit()

    cur.close()

    conn.close()

    global month
    if month == "01":
        month = "Jan"
    return render_template('entry.html', month=month, year=year, this_month=this_month)


# def show():
#     print("month", smonth, "year", syear)


@app.route("/summary", methods=["GET", "POST"])
def summary():
    month_measurement = ''
    if request.method == "POST":

        # global smonth, syear
        smonth = request.form['smonth']
        syear = request.form['syear']
        # show()

        conn = psycopg2.connect(dbname=database, user=username, password=password, host=hostname)

        cur = conn.cursor()

        cur.execute(
            f'''SELECT day, feeling_level, exercise_level, sleep_quality FROM day
            WHERE year = {syear} AND month = {smonth};''')

        month_measurement = cur.fetchall()

        conn.commit()

        cur.close()

        conn.close()
        return render_template("summary.html", month_measurement=month_measurement)
    else:
        month_measurement = ''
        return render_template("summary.html")

if __name__ == "__main__":
    app.run(debug=True)
