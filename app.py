from flask import Flask, render_template, request
import json
from fintools import FA_dataset
from dotenv import load_dotenv
import os
import plotly

load_dotenv()

api_key = os.getenv('FIN_API')
app = Flask(__name__)

@app.route('/')
def main():
    return render_template('base.html')

@app.route('/display_metrics',methods=['POST'])
def plotter():
    if request.method == 'POST':
        ticker = request.form['ticker']
        ticker = ticker.upper()


        #create FAA object and convert to plot
        FAA_figure = FA_dataset(api_key,ticker).plot_metrics()
        plotly.offline.plot(FAA_figure,filename=f'templates/View_{ticker}_plot.html',auto_open=False)
    return render_template(f'View_{ticker}_plot.html')
if __name__ == '__main__':
    app.run()
