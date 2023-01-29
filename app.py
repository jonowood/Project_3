import os

import psycopg2

from flask import Flask, render_template

from flask import Flask, jsonify

from api_keys import postgres_p


#################################################
# Database Setup
#################################################

def get_db_connection():
    conn = psycopg2.connect(host='localhost',
                            database='Project_3',
                            user='postgres',
                            password=postgres_p)
    return conn


#################################################
# Flask Setup
#################################################

app = Flask(__name__)


#################################################
# Flask Routes
#################################################


## CURRENTLY JOB ID @ INDEX
@app.route("/")
def index():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('SELECT * FROM job_id;')
    jobs = cur.fetchall()
    cur.close()
    conn.close()
    # return render_template('index.html', jobs=jobs)
    return jsonify(jobs)

@app.route("/construction_scrapes")
def construction_scrapes():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('SELECT * FROM construction_scrapes;')
    jobs = cur.fetchall()
    cur.close()
    conn.close()
    # return render_template('index.html', jobs=jobs)
    return jsonify(jobs)

if __name__ == '__main__':
    app.run(debug=True)
