#################################################
# Dependencies
#################################################

import os
import psycopg2
import pandas as pd
import plotly
import plotly.express as px
import plotly.io as pio
import plotly.graph_objects as go
import json
import matplotlib.pyplot as plt
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure
from django.shortcuts import render
from flask import Flask, render_template, jsonify, request, send_file
from wordcloud import WordCloud, STOPWORDS
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

@app.route("/")
def welcome():
    return render_template('index.html')

## LOCATION COUNT BAR PLOTS ##

### APP ROUTE FOR CONSTRUCTION LOCATION COUNT ###

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
    fig = px.bar(df, x="Locations ", y="Count ",  title= 'Construction Jobs - By Location', template="ggplot2", height=800)
    graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
    header="Construction Job Locations"
    description = """
    """
    return render_template('location.html', graphJSON=graphJSON, header=header,description=description)

### APP ROUTE FOR ENGINEERING LOCATION COUNT ###

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
    fig = px.bar(df, x="Locations ", y="Count ", title= 'Engineering Jobs - By Location', template="ggplot2", height=800)
    graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
    header="Engineering Job Locations"
    description = """
    """
    return render_template('location.html', graphJSON=graphJSON, header=header,description=description)

### APP ROUTE FOR HEALTHCARE LOCATION COUNT ###

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
    fig = px.bar(df, x="locations", y="count", title= 'Healthcare Jobs - By Location', template="ggplot2", height=800)
    graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
    header="Healthcare Job Locations"
    description = """
    """
    return render_template('location.html', graphJSON=graphJSON, header=header,description=description)

### APP ROUTE FOR SALES LOCATION COUNT ###

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
    fig = px.bar(df, x="Locations ", y="Count ", title= 'Sales Jobs - By Location', template="ggplot2", height=800)
    graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
    header="Sales Job Locations"
    description = """
    """
    return render_template('location.html', graphJSON=graphJSON, header=header,description=description)


## WORD COUNT PIE PLOTS ##

### APP ROUTE FOR CONSTRUCTION WORD COUNT ###

@app.route('/construction_word_count')
def construction_word_scrapes():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('SELECT count FROM construction_word_count LIMIT 20;')
    data = cur.fetchall()
    column_values = []
    for row in data: column_values.append(row[0])
    cur.execute('SELECT word FROM construction_word_count LIMIT 20;')
    data2 = cur.fetchall()
    column_values2 = []
    for row in data2: column_values2.append(row[0])
    cur.close()
    conn.close()
    df = pd.DataFrame({
        "Word ": column_values2,
        "Count ": column_values
    })
    fig = px.pie(df, values="Count ", names="Word ", hole=0.3, height=800, title= 'Construction Jobs - BuzzWords')
    fig.update_layout(margin=dict(t=0, b=0, l=0, r=0))
    fig.update_traces(textposition='inside')
    fig.update_layout(uniformtext_minsize=12, uniformtext_mode='hide')
    graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
    header="Construction Industry Key Words"
    description = """
    """
    return render_template('resume_helper_pie.html', graphJSON=graphJSON, header=header,description=description)
    fig.show()

### APP ROUTE FOR ENGINEERING WORD COUNT ###

@app.route('/engineering_word_count')
def engineering_word_scrapes():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('SELECT count FROM engineering_word_count LIMIT 20;')
    data = cur.fetchall()
    column_values = []
    for row in data: column_values.append(row[0])
    cur.execute('SELECT word FROM engineering_word_count LIMIT 20;')
    data2 = cur.fetchall()
    column_values2 = []
    for row in data2: column_values2.append(row[0])
    cur.close()
    conn.close()
    df = pd.DataFrame({
        "Word ": column_values2,
        "Count ": column_values
    })
    fig = px.pie(df, values="Count ", names="Word ", hole=0.3, height=800)
    fig.update_layout(margin=dict(t=0, b=0, l=0, r=0))
    fig.update_traces(textposition='inside')
    fig.update_layout(uniformtext_minsize=12, uniformtext_mode='hide') # , color="City", barmode="stack"
    graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
    header="Engineering Industry Key Words"
    description = """
    """
    return render_template('resume_helper_pie.html', graphJSON=graphJSON, header=header,description=description)

### APP ROUTE FOR HEALTHCARE WORD COUNT ###

@app.route('/healthcare_word_count')
def healthcare_word_scrapes():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('SELECT count FROM healthcare_word_count LIMIT 20;')
    data = cur.fetchall()
    column_values = []
    for row in data: column_values.append(row[0])
    cur.execute('SELECT word FROM healthcare_word_count LIMIT 20;')
    data2 = cur.fetchall()
    column_values2 = []
    for row in data2: column_values2.append(row[0])
    cur.close()
    conn.close()
    df = pd.DataFrame({
        "Word ": column_values2,
        "Count ": column_values
    })
    fig = px.pie(df, values="Count ", names="Word ", hole=0.3, height=800)
    fig.update_layout(margin=dict(t=0, b=0, l=0, r=0))
    fig.update_traces(textposition='inside')
    fig.update_layout(uniformtext_minsize=12, uniformtext_mode='hide') # , color="City", barmode="stack"
    graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
    header="Healthcare Industry Key Words"
    description = """
    """
    return render_template('resume_helper_pie.html', graphJSON=graphJSON, header=header,description=description)

### APP ROUTE FOR SALES WORD COUNT ###

@app.route('/sales_word_count')
def sales_word_scrapes():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('SELECT count FROM sales_word_count LIMIT 20;')
    data = cur.fetchall()
    column_values = []
    for row in data: column_values.append(row[0])
    cur.execute('SELECT word FROM sales_word_count LIMIT 20;')
    data2 = cur.fetchall()
    column_values2 = []
    for row in data2: column_values2.append(row[0])
    cur.close()
    conn.close()
    df = pd.DataFrame({
        "Word ": column_values2,
        "Count ": column_values
    })
    fig = px.pie(df, values="Count ", names="Word ", hole=0.3, height=800)
    fig.update_layout(margin=dict(t=0, b=0, l=0, r=0))
    fig.update_traces(textposition='inside')
    fig.update_layout(uniformtext_minsize=12, uniformtext_mode='hide')# # , color="City", barmode="stack"
    graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
    header="Sales Industry Key Words"
    description = """
    """
    return render_template('resume_helper_pie.html', graphJSON=graphJSON, header=header,description=description)

## WORD COUNT WORDCLOUD PLOTS ##

### APP ROUTE FOR CONSTRUCTION WORD CLOUD ###

@app.route('/construction_word_cloud')
def construction_word_cloud():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('SELECT count FROM construction_word_count;')
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
    text = df["Word "].str.cat(sep=" ")
    wordcloud = WordCloud(width = 800, height = 800,
                    background_color ='white',
                    min_font_size = 10).generate(text)  
    # plot the WordCloud
    fig = plt.figure(figsize=(8, 8), facecolor=None)
    ax = fig.add_subplot(111)
    ax.imshow(wordcloud, interpolation="bilinear")
    ax.axis("off")
    # Convert the figure to a PNG image
    filename = "wordcloud.png"
    file_path = os.path.join("static", filename)
    plt.savefig(file_path, format="png")
    # Return the image as a response
    return render_template("resume_helper_wordcloud.html", image_path=filename)

### APP ROUTE FOR ENGINEERING WORD CLOUD ###

@app.route('/engineering_word_cloud')
def engineering_word_cloud():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('SELECT count FROM engineering_word_count;')
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
    text = df["Word "].str.cat(sep=" ")
    wordcloud = WordCloud(width = 800, height = 800,
                    background_color ='white',
                    min_font_size = 10, 
                    ).generate(text)  
    # plot the WordCloud
    fig = plt.figure(figsize=(8, 8), facecolor=None)
    ax = fig.add_subplot(111)
    ax.imshow(wordcloud, interpolation="bilinear")
    ax.axis("off")
    # Convert the figure to a PNG image
    filename = "wordcloud.png"
    file_path = os.path.join("static", filename)
    plt.savefig(file_path, format="png")
    # Return the image as a response
    return render_template("resume_helper_wordcloud.html", image_path=filename)

### APP ROUTE FOR HEALTHCARE WORD CLOUD ###

@app.route('/healthcare_word_cloud')
def healthcare_word_cloud():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('SELECT count FROM healthcare_word_count;')
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
    text = df["Word "].str.cat(sep=" ")
    wordcloud = WordCloud(width = 800, height = 800,
                    background_color ='white',
                    min_font_size = 10).generate(text)  
    # plot the WordCloud
    fig = plt.figure(figsize=(8, 8), facecolor=None)
    ax = fig.add_subplot(111)
    ax.imshow(wordcloud, interpolation="bilinear")
    ax.axis("off")
    # Convert the figure to a PNG image
    filename = "wordcloud.png"
    file_path = os.path.join("static", filename)
    plt.savefig(file_path, format="png")
    # Return the image as a response
    return render_template("resume_helper_wordcloud.html", image_path=filename)

### APP ROUTE FOR SALES WORD CLOUD ###

@app.route('/sales_word_cloud')
def sales_word_cloud():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('SELECT count FROM sales_word_count;')
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
    text = df["Word "].str.cat(sep=" ")
    wordcloud = WordCloud(width = 800, height = 800,
                    background_color ='white',
                    min_font_size = 10).generate(text)
    # plot the WordCloud
    fig = plt.figure(figsize=(8, 8), facecolor=None)
    ax = fig.add_subplot(111)
    ax.imshow(wordcloud, interpolation="bilinear")
    ax.axis("off")
    # Convert the figure to a PNG image
    filename = "wordcloud.png"
    file_path = os.path.join("static", filename)
    plt.savefig(file_path, format="png")
    # Return the image as a response
    return render_template("resume_helper_wordcloud.html", image_path=filename)




