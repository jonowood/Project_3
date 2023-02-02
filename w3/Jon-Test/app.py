import os

import psycopg2

import pandas as pd

import plotly

import plotly.express as px

import json
from django.shortcuts import render
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure
from wordcloud import WordCloud
import io

from flask import Flask, render_template, jsonify, request

from flask_restful import Api, Resource

from api_keys import postgres_p



#################################################
# Database Setup
#################################################

def get_db_connection():
    conn = psycopg2.connect(host='localhost',
                            database='jon_seek',
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

@app.route("/")
def welcome():
    return render_template('new.html')


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
    df = pd.DataFrame({
        "Locations ": column_values2,
        "Count ": column_values
    })
    fig = px.bar(df, x="Locations ", y="Count ")
    fig.update_layout(margin=dict(t=0, b=0, l=0, r=0)) # , color="City", barmode="stack"
    graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
    header="Construction Job Locations"
    description = """
    """
    return render_template('location.html', graphJSON=graphJSON, header=header,description=description)

@app.route('/engineering_location_count')
def engineering_scrapes():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('SELECT count FROM engineering_location_count;')
    data = cur.fetchall()
    column_values = []
    for row in data: column_values.append(row[0])
    cur.execute('SELECT job_location FROM engineering_location_count;')
    data2 = cur.fetchall()
    column_values2 = []
    for row in data2: column_values2.append(row[0])
    cur.close()
    conn.close()
    df = pd.DataFrame({
        "Locations ": column_values2,
        "Count ": column_values
    })
    fig = px.bar(df, x="Locations ", y="Count ") # , color="City", barmode="stack"
    graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
    header="Engineering Job Locations"
    description = """
    """
    return render_template('location.html', graphJSON=graphJSON, header=header,description=description)

@app.route('/healthcare_location_count')
def healthcare_scrapes():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('SELECT count FROM healthcare_location_count;')
    data = cur.fetchall()
    column_values = []
    for row in data: column_values.append(row[0])
    cur.execute('SELECT job_location FROM healthcare_location_count;')
    data2 = cur.fetchall()
    column_values2 = []
    for row in data2: column_values2.append(row[0])
    cur.close()
    conn.close()
    df = pd.DataFrame({
        "locations": column_values2,
        "count": column_values
    })
    fig = px.bar(df, x="locations", y="count") # , color="City", barmode="stack"
    graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
    header="Healthcare Job Locations"
    description = """
    """
    return render_template('location.html', graphJSON=graphJSON, header=header,description=description)

@app.route('/sales_location_count')
def sales_scrapes():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('SELECT count FROM sales_location_count;')
    data = cur.fetchall()
    column_values = []
    for row in data: column_values.append(row[0])
    cur.execute('SELECT job_location FROM sales_location_count;')
    data2 = cur.fetchall()
    column_values2 = []
    for row in data2: column_values2.append(row[0])
    cur.close()
    conn.close()
    df = pd.DataFrame({
        "Locations ": column_values2,
        "Count ": column_values
    })

    fig = px.bar(df, x="Locations ", y="Count ") # , color="City", barmode="stack"
    graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
    header="Sales Job Locations"
    description = """
    """
    return render_template('location.html', graphJSON=graphJSON, header=header,description=description)




## WORD COUNT PIE GRAPHS



@app.route('/construction_word_count')
def construction_word_scrapes():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('SELECT frequency FROM construction_word_count;')
    data = cur.fetchall()
    column_values = []
    for row in data: column_values.append(row[0])
    cur.execute('SELECT word FROM construction_word_count;')
    data2 = cur.fetchall()
    column_values2 = []
    for row in data2: column_values2.append(row[0])
    cur.close()
    conn.close()
    df = pd.DataFrame({
        "Word ": column_values2,
        "Count ": column_values
    })
    fig = px.pie(df, values="Count ", names="Word ", hole=0.3)
    fig.update_layout(margin=dict(t=0, b=0, l=0, r=0))
    fig.update_traces(textposition='inside')
    fig.update_layout(uniformtext_minsize=12, uniformtext_mode='hide') # , color="City", barmode="stack"
    graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
    header="Construction Industry Key Words"
    description = """
    """
    return render_template('words.html', graphJSON=graphJSON, header=header,description=description)

@app.route('/engineering_word_count')
def engineering_word_scrapes():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('SELECT frequency FROM engineering_word_count;')
    data = cur.fetchall()
    column_values = []
    for row in data: column_values.append(row[0])
    cur.execute('SELECT word FROM engineering_word_count;')
    data2 = cur.fetchall()
    column_values2 = []
    for row in data2: column_values2.append(row[0])
    cur.close()
    conn.close()
    df = pd.DataFrame({
        "Word ": column_values2,
        "Count ": column_values
    })
    fig = px.pie(df, values="Count ", names="Word ", hole=0.3)
    fig.update_layout(margin=dict(t=0, b=0, l=0, r=0))
    fig.update_traces(textposition='inside')
    fig.update_layout(uniformtext_minsize=12, uniformtext_mode='hide') # , color="City", barmode="stack"
    graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
    header="Engineering Industry Key Words"
    description = """
    """
    return render_template('words.html', graphJSON=graphJSON, header=header,description=description)


@app.route('/healthcare_word_count')
def healthcare_word_scrapes():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('SELECT frequency FROM healthcare_word_count;')
    data = cur.fetchall()
    column_values = []
    for row in data: column_values.append(row[0])
    cur.execute('SELECT word FROM healthcare_word_count;')
    data2 = cur.fetchall()
    column_values2 = []
    for row in data2: column_values2.append(row[0])
    cur.close()
    conn.close()
    df = pd.DataFrame({
        "Word ": column_values2,
        "Count ": column_values
    })
    fig = px.pie(df, values="Count ", names="Word ", hole=0.3)
    fig.update_layout(margin=dict(t=0, b=0, l=0, r=0))
    fig.update_traces(textposition='inside')
    fig.update_layout(uniformtext_minsize=12, uniformtext_mode='hide') # , color="City", barmode="stack"
    graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
    header="Healthcare Industry Key Words"
    description = """
    """
    return render_template('words.html', graphJSON=graphJSON, header=header,description=description)


@app.route('/sales_word_count')
def sales_word_scrapes():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('SELECT frequency FROM sales_word_count;')
    data = cur.fetchall()
    column_values = []
    for row in data: column_values.append(row[0])
    cur.execute('SELECT word FROM sales_word_count;')
    data2 = cur.fetchall()
    column_values2 = []
    for row in data2: column_values2.append(row[0])
    cur.close()
    conn.close()
    df = pd.DataFrame({
        "Word ": column_values2,
        "Count ": column_values
    })
    fig = px.pie(df, values="Count ", names="Word ", hole=0.3)
    fig.update_layout(margin=dict(t=0, b=0, l=0, r=0))
    fig.update_traces(textposition='inside')
    fig.update_layout(uniformtext_minsize=12, uniformtext_mode='hide')# # , color="City", barmode="stack"
    graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
    header="Sales Industry Key Words"
    description = """
    """
    return render_template('words.html', graphJSON=graphJSON, header=header,description=description)










# @app.route('/construction_location_count2')
# def construction_scrapes2():
#     conn = get_db_connection()
#     cur = conn.cursor()
#     cur.execute('SELECT count FROM construction_location_count;')
#     data = cur.fetchall()
#     column_values = []
#     for row in data: column_values.append(row[0])
#     cur.execute('SELECT job_location FROM construction_location_count;')
#     data2 = cur.fetchall()
#     column_values2 = []
#     for row in data2: column_values2.append(row[0])
#     cur.close()
#     conn.close()
#     df = pd.DataFrame({
#         "locations": column_values2,
#         "count": column_values
#     })
#     return render_template('animated-chart.html')


# @app.route('/construction_word_count')
# def plot_wordcloud():
#     conn = get_db_connection()
#     cur = conn.cursor()
#     cur.execute('SELECT word FROM construction_words;')
#     data3 = cur.fetchall()
#     text = []
#     for row in data3: text.append(row[0])
#     wc = WordCloud().generate(text)
#     figure = Figure(figsize=(6, 6), dpi=100)
#     axis = figure.add_subplot(1, 1, 1)
#     axis.imshow(wc, interpolation='bilinear')
#     axis.axis('off')

#     output = io.BytesIO()
#     FigureCanvas(figure).print_png(output)
#     return output.getvalue()


# @app.route('/chart1')
# def index(request, format=None):
#     electricity_price_data = [
#       { "y": 8.58, "label": "Texas" },
#       { "y": 9.69, "label": "Pennsylvania" },
#       { "y": 10.35, "label": "Florida" },
#       { "y": 14.9, "label": "New York" },
#       { "y": 18.05, "label": "Massachusetts" },
#       { "y": 18.15, "label": "California" }
#     ]
#     return render(request, 'animated_chart.html', { "electricity_price_data" : electricity_price_data })                       





# if __name__ == '__main__':
#     app.run(debug=True)
