import dash
from dash import dcc, html
import plotly.express as px
import pandas as pd


excel_file_path = 'project/sampledata.xlsx'
df = pd.read_excel(excel_file_path)




sales_by_category = df.groupby('Category', as_index=False, observed=True)['Sales'].sum()
fig_bar = px.bar(
    sales_by_category,
    x='Category',
    y='Sales',
    title='Total Sales by Category',
    color='Category'
)


month_order = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
               'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
df['Month'] = pd.Categorical(df['Month'], categories=month_order, ordered=True)
sales_by_month = df.groupby('Month', as_index=False, observed=True)['Sales'].sum()
fig_line = px.line( 
    sales_by_month,
    x='Month',
    y='Sales',
    title='Monthly Sales Trend',
    markers=True
)

fig_scatter = px.scatter(
    df,
    x='Sales',
    y='Profit',
    color='Category',
    title='Relationship between Sales and Profit',
    hover_data=['Month']
)


fig_pie = px.pie(
    sales_by_month,
    names='Month',
    values='Sales',
    title='Distribution of Sales by Month'
)


app = dash.Dash(__name__)

app.layout = html.Div(children=[
    html.H1('Excel Data Visualization Dashboard', style={'textAlign': 'center'}),

   
    html.Div([
        dcc.Graph(
            id='bar-chart',
            figure=fig_bar
        )
    ], style={'width': '48%', 'display': 'inline-block', 'verticalAlign': 'top'}),

    
    html.Div([
        dcc.Graph(
            id='line-chart',
            figure=fig_line
        )
    ], style={'width': '48%', 'display': 'inline-block', 'verticalAlign': 'top'}),

    
    html.Div([
        dcc.Graph(
            id='scatter-plot',
            figure=fig_scatter
        )
    ], style={'width': '48%', 'display': 'inline-block', 'verticalAlign': 'top'}),

   
    html.Div([
        dcc.Graph(
            id='pie-chart',
            figure=fig_pie
        )
    ], style={'width': '48%', 'display': 'inline-block', 'verticalAlign': 'top'})
])

if __name__ == '__main__':
    import os
    port = int(os.getenv("PORT", 8050))
    app.run(debug=False, host='0.0.0.0', port=port)
