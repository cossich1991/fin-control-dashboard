from dash import html, dcc
import dash
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc
import pandas as pd
import plotly.express as px

from app import *
from components import sidebar, dashboards, extracts


content = html.Div(id='page-content')

app.layout = dbc.Container(children=[
    dbc.Row([
        dbc.Col(
            [
                dcc.Location(id='url'),
                sidebar.layout],
            md=2,
            style={'background-color': 'red', 'height': '1080px'}),
        dbc.Col(
            [content],
            md=10,
            style={'background-color': 'blue', 'height': '1080px'})
        ])
    ], fluid=True)

@app.callback(Output('page-content', 'children'),
              [Input('url', 'pathname')])
def render_page(pathname: str):
    if pathname in ['/', 'dashboards']:
        return dashboards.layout

    if pathname == '/extracts':
        return extracts.layout


if __name__ == '__main__':
    app.run_server(port=8051, debug=True)
