# -*- coding: utf-8 -*-

import dash
import dash_core_components as dcc
import dash_html_components as html

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_sytlesheets=external_stylesheets)

colors = {
        'background': '#999999',
        'text': '#123123'
}

app.layout = html.Div(style ={'backgroundColor': colors['background']}, children=[
    html.H1(children='Hello Dash !',
            style = {
                'textAlign': 'center',
                'color': colors['text']
            }),
    html.Div(children='''
        Dash: A web application framework for Python.
    ''',
             style={
                 'textAlign': 'center',
                 'color': colors['text']
                 }),
    dcc.Graph(
        id='example-graph',
        figure={

            'data':[
                 {'x': [1, 2, 3], 'y': [4, 1, 2], 'type': 'bar', 'name': 'SF'},
                 {'x': [1, 2, 3], 'y': [2, 4, 5], 'type': 'bar', 'name': u'Montréal'},
             ],
            'layout':{
                'plot_bgcolor': colors['background'],
                'paper_bgcolor': colors['background'],
                'font':{'color':colors['text']},
                'title':'Dash Data Visualization'
                }

            }
        )
    ])

if __name__ == '__main__':
    app.run_server(debug=True)
