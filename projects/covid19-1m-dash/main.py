import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
import plotly.graph_objs as go
from dash.dependencies import Input, Output

from load_data import request_data, extract_data_covidtracking_states
from get_articles import top_reddit_posts, top_youtube_vids

df_us, df_states, df_global = request_data()
data_reddit = top_reddit_posts(8)

state_list = ['AL','AK','AZ','AR','CA','CO','CT','DE','DC','FL','GA',
              'HI','ID','IL','IN','IA','KS','KY','LA','ME','MD','MA',
              'MI','MN','MS','MO','MT','NE','NV','NH','NJ','NM','NY',
              'NC','ND','OH','OK','OR','PA','PR','RI','SC','SD','TN','TX','UT',
              'VT','VA','VI','WA','WV','WI','WY']

app_colors = {
    'dark grey': '#0C0F0A',
    'white': '#FFFFFF',
    'red': '#FF6F6F',
    'grey': '#B4B4B4',
    'grey2': '#1A1A1A',
    'blue': '#6CAAFF',
    'orange': '#FFAF77'
}

tab_selected_style1 = {
    'backgroundColor': app_colors['grey'],
    'borderTop': '5px solid ' + app_colors['blue']
}

tab_selected_style2 = {
    'backgroundColor': app_colors['grey'],
    'borderTop': '3px solid ' + app_colors['red']
}

external_stylesheets = ["https://cdnjs.cloudflare.com/ajax/libs/materialize/0.100.2/css/materialize.min.css"]

app = dash.Dash(__name__,  external_stylesheets=[dbc.themes.BOOTSTRAP]+external_stylesheets)

server = app.server

app.layout = html.Div(children=[
    html.Div(id='title', children=[
        html.H1('1 Min Covid-19 Dashboard',
                style={'margin-top': '10px', 'backgroundColor': app_colors['dark grey'], 'color':app_colors['white']}),
    ]),
    html.Div(id='options', children=[
        html.Hr(style={'border-width': 5, 'background-color': 'white'}),
        dbc.Row([
            dbc.Col([
                html.Div(children=[
                    html.Label("State: ", style={'font-size': '24px'}),
                    dcc.Input(id='state-input',
                              value='VA',
                              type='text',
                              style={'font-size': '24px', 'text-align':'center', 'color': app_colors['white']},
                              placeholder='two letter state code')
                ])
            ], width=2),
            dbc.Col([
                dcc.Tabs(id='hcd-tab', value='hospitalizedCurrently', children=[
                    dcc.Tab(label='Daily Cases', value='positiveIncrease', selected_style=tab_selected_style1),
                    dcc.Tab(label='Current Hospitalizations', value='hospitalizedCurrently', selected_style=tab_selected_style1),
                    dcc.Tab(label='Daily Deaths', value='deathIncrease', selected_style=tab_selected_style1)
                ], colors={'border': app_colors['grey'], 'primary': app_colors['blue'], 'background': app_colors['dark grey']}),
                dcc.Tabs(id='locality-tab', value='United States', children=[
                    dcc.Tab(label='State', value='State', selected_style=tab_selected_style2),
                    dcc.Tab(label='United States', value='United States', selected_style=tab_selected_style2),
                    dcc.Tab(label='Global', value='Global', selected_style=tab_selected_style2)
                ], colors={'border': app_colors['grey'], 'primary': app_colors['red'], 'background': app_colors['dark grey']})
            ], width=10),
        ], align='center', style={'font-size': '24px'}),
    ]),
    html.Hr(style={'border-width': 5, 'background-color': 'white'}),
    html.Div(id='at-a-glance'),
    html.Div(children=[
        html.Hr(style={'border-width': 5, 'background-color': 'white'}),
        html.Div(id='outputs'),
        html.H6('Click and drag to zoom in graph. . . . . . . . Double click to return to default view.',
                style={'font-style': 'italic', 'color': app_colors['grey']}),
    ]),
    html.Hr(style={'border-width': 5, 'background-color': 'white'}),
    dbc.Row([dbc.Col(html.Div(className='flex-container', children=[html.H5("Showing "),
            dcc.Input(id='show-num-articles',
              value=8,
              type='number',
              style={'font-size': '20px', 'text-align': 'center', 'color': app_colors['white'], 'width':'15%'},
              placeholder='Show How Many Articles?'),
            html.H5(" Results"),
            ], style={'display': 'flex', 'justify-content': 'center'}))]),
    html.Div([
        html.Div(id='reddit-posts'),
        html.Div(id='youtube-vids')
    ]),
    html.Hr(style={'border-width': 5, 'background-color': 'white'}),
    html.Label('US and state data from "The COVID Tracking Project at The Atlantic"', style={'margin-right': '50px'}),
    html.Label('Global data from github.com/datasets/covid-19 under the Open Data Commons Public Domain and Dedication License'),
    dcc.Interval(
        id='interval-component',
        interval=1000 * 60 * 10,
        n_intervals=0
    ),
    ], style={'backgroundColor': app_colors['dark grey'],
              'color':
                  app_colors['white'],
              'margin-top': '30px',
              'text-align': 'center',
              'height': '2000px'})

@app.callback(
    Output(component_id='at-a-glance', component_property='children'),
    Output(component_id='outputs', component_property='children'),

    Input(component_id='hcd-tab', component_property='value'),
    Input(component_id='locality-tab', component_property='value'),
    Input(component_id='state-input', component_property='value'),
)
def update_figure(hcd, locality, state_input):
    graph_title_dict = {'hospitalizedCurrently': 'Current Hospitalizations', 'deathIncrease': 'Daily Deaths', 'positiveIncrease': 'Daily Cases'}
    if state_input in state_list:
        if locality == 'United States':
            df_cur = df_us
        elif locality == 'State':
            df_cur = extract_data_covidtracking_states(df_states, state_input)
        elif locality == 'Global':
            df_cur = df_global

        # returns nothing because there is no global hospitalization data
        if locality == 'Global' and hcd == 'hospitalizedCurrently':
            return dbc.Row([dbc.Col(html.H4('At a Glance', style={'margin-right': '100px'}), width=2, align='center')]), dcc.Graph(
                figure={
                    'layout': go.Layout(title='No Global Hospitalization Data',
                        font={'color': app_colors['white'], 'size': 24},
                        plot_bgcolor = app_colors['grey2'],
                        paper_bgcolor = app_colors['dark grey'],)
                })

        return dbc.Row([
            dbc.Col(html.H4('At a Glance', style={'margin-left': '100px', 'margin-right': '100px'}), width=3, align='center'),
            dbc.Col(html.Table(id='summary-table', children=[
                html.Tr(children=[
                    html.Th('Today'),
                    html.Th("Yesterday"),
                    html.Th("7 Days Ago"),
                    html.Th("7 Day Moving Average")
                ]),
                html.Tr(children=[
                    html.Td(f"{df_cur[hcd].iloc[0]:,}"),
                    html.Td(f"{df_cur[hcd].iloc[1]:,}"),
                    html.Td(f"{df_cur[hcd].iloc[6]:,}"),
                    html.Td(f'{df_cur[hcd+"MA"].iloc[6]:,}'),
                ])
            ], style={'font-size': '24px'}), align='center')
            ], justify='center'), \
                dcc.Graph(id='graph1',
                          figure={
                              'data': [{'x': df_cur['date'], 'y': df_cur[hcd], 'type': 'bar', 'name': 'daily'},
                                       {'x': df_cur['date'], 'y': df_cur[hcd + 'MA'], 'type': 'line', 'name': '7 day average'},],
                              'layout': go.Layout(
                                    title=locality + ' ' + graph_title_dict[hcd],
                                    font={'color': app_colors['white'], 'size': 20},
                                    plot_bgcolor=app_colors['grey2'],
                                    paper_bgcolor=app_colors['dark grey'],
                                ),
                          },
                          # animate is buggy if input field is change too rapidly, maybe try dropdown in future
                          animate=False
                )
    else:
        return dbc.Row(), dcc.Graph(figure={'layout': go.Layout(
                    title=locality + ' ' + graph_title_dict[hcd],
                    font={'color': app_colors['white']},
                    plot_bgcolor=app_colors['dark grey'],
                    paper_bgcolor=app_colors['dark grey'],
                )})

@app.callback(
    Output(component_id='reddit-posts', component_property='children'),
    #Output(component_id='youtube-vids', component_property='children'),
    Input(component_id='show-num-articles', component_property='value'),
    Input(component_id='interval-component', component_property='n_intervals')
)
def update_articles(num_articles, n):
    data_reddit = top_reddit_posts(num_articles)
    def format_reddit_data():
        temp_layout_list = []
        for key in data_reddit.keys():
            temp_layout_list.append(html.Div(dbc.Row([
                html.A('Reddit Post  ', href=data_reddit[key]['inurl'], target='_blank', style={'font-size': '16px', 'margin-right': '20px'}),
                html.P(data_reddit[key]['title'] + '  ', style={'font-size': '16px', 'margin-right': '16px'}),
                html.P(str(data_reddit[key]['upvote']) + 'k upvotes  ', style={'font-size': '16px', 'margin-right': '16px', 'color': app_colors['orange']}),
                html.P(str(data_reddit[key]['upvote_ratio']) + '% upvote ratio', style={'font-size': '16px', 'margin-right': '20px', 'color': app_colors['orange']}),
                html.A('External Link', href=data_reddit[key]['exurl'], target='_blank', style={'font-size': '16px', 'margin-right': '20px'}),
            ]), className='flex-container', style={'margin-left': '5%'}))
        return temp_layout_list
    return format_reddit_data()

#
# if __name__ == '__main__':
#     app.run_server(debug=True)