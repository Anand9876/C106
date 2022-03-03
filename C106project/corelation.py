import numpy as np
import plotly.express as px
import csv

def plotPoint(data_path):
    with open(data_path) as csv_file:
        df = csv.DictReader(csv_file)
        fig = px.scatter(df,x='Marks In Percentage',y='Days Present')
        fig.show()

def getDataSource(data_path):
    Marks_in_percentage=[]
    days_present=[]

    with open(data_path) as csv_file:
        csv_reader=csv.DictReader(csv_file)
        for row in csv_reader:
            Marks_in_percentage.append(float(row['Marks In Percentage']))
            days_present.append(float(row['Days Present']))
        return{'x':Marks_in_percentage,'y':days_present}

def findCorrelation(datasource):
    correlation=np.corrcoef(datasource['x'],datasource['y'])
    print('Correlation between number of days present and marks in percentage :-  \n--->',correlation[0,1])

def setup():
    data_path='C106data.csv'

    datasource=getDataSource(data_path)
    findCorrelation(datasource)
    plotPoint(data_path)

setup()

