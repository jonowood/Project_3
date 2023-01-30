import os

import psycopg2

import plotly

import plotly.express as px

import json

from flask import Flask, render_template, jsonify, request

from flask_restful import Api, Resource

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

api =   Api(app)

#################################################
# Flask Routes
#################################################

# @api.route('/')

## CURRENTLY JOB ID @ INDEX
@app.route("/job_id")
def job_id():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('SELECT * FROM job_id;')
    jobs = cur.fetchall()
    cur.close()
    conn.close()
    # return render_template('index.html', jobs=jobs)
    return jsonify(jobs)




@app.route('/construction_location_count')
def construction_scrapes():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('SELECT count FROM construction_location_count;')
    data = cur.fetchall()
    column_values = []
    for row in data: column_values.append(row[0])
    cur.execute('SELECT job_location FROM construction_location_count;')
    data2 = cur.fetchall()
    column_values2 = []
    for row in data2: column_values2.append(row[0])
    cur.close()
    conn.close()
    # return render_template('index.html', jobs=jobs)
    return jsonify(column_values, column_values2)


# api.add_resource(returnjsons,'/returnjson')

#     conn = get_db_connection()
#     cur = conn.cursor()
#     cur.execute('SELECT job_location FROM construction_location_count;')
#     locations = cur.fetchall()
#     locations = locations
#     cur.execute('SELECT count FROM construction_location_count;')
#     count = cur.fetchall()
#     count = count
#     cur.close()
#     conn.close()
#     # # return render_template('index.html', jobs=jobs)
#     # df = count
#     fig = px.bar(x=locations, y=count, color="City", barmode="group")
    
#     graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
#     header="Fruit in North America"
#     description = """    """
#     return render_template('notdash2.html', graphJSON=graphJSON, header=header,description=description)
#     # return jsonify(count)

if __name__ == '__main__':
    app.run(debug=True)
