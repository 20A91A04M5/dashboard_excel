import dash
from dash import dcc, html
import plotly.express as px
import pandas as pd

# Read the Excel file from 'project' folder
excel_file_path = 'project/sampledata.xlsx'
df = pd.read_excel(excel_file_path)

# Create figures

# 1. Bar Chart: total sales by category
sales_by_category = df.groupby('Category', as_index=False, observed=False)['Sales'].sum()
fig_bar = px.bar(
    sales_by_category,
    x='Category',
    y='Sales',
    title='Total Sales by Category',
    color='Category'
)

# 2. Line Graph: monthly sales trend
#    We need to ensure months are in correct order, so let's define a mapping:
month_order = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
               'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
df['Month'] = pd.Categorical(df['Month'], categories=month_order, ordered=True)
sales_by_month = df.groupby('Month', as_index=False)['Sales'].sum()
fig_line = px.line(
    sales_by_month,
    x='Month',
    y='Sales',
    title='Monthly Sales Trend',
    markers=True
)

# 3. Scatter Plot: relationship between sales and profit
fig_scatter = px.scatter(
    df,
    x='Sales',
    y='Profit',
    color='Category',
    title='Relationship between Sales and Profit',
    hover_data=['Month']
)

# 4. Pie Chart: distribution of sales by month
fig_pie = px.pie(
    sales_by_month,
    names='Month',
    values='Sales',
    title='Distribution of Sales by Month'
)

# Create the Dash app
app = dash.Dash(__name__)

app.layout = html.Div(children=[
    html.H1('Excel Data Visualization Dashboard', style={'textAlign': 'center'}),

    # Bar Chart
    html.Div([
        dcc.Graph(
            id='bar-chart',
            figure=fig_bar
        )
    ], style={'width': '48%', 'display': 'inline-block', 'verticalAlign': 'top'}),

    # Line Graph
    html.Div([
        dcc.Graph(
            id='line-chart',
            figure=fig_line
        )
    ], style={'width': '48%', 'display': 'inline-block', 'verticalAlign': 'top'}),

    # Scatter Plot
    html.Div([
        dcc.Graph(
            id='scatter-plot',
            figure=fig_scatter
        )
    ], style={'width': '48%', 'display': 'inline-block', 'verticalAlign': 'top'}),

    # Pie Chart
    html.Div([
        dcc.Graph(
            id='pie-chart',
            figure=fig_pie
        )
    ], style={'width': '48%', 'display': 'inline-block', 'verticalAlign': 'top'})
])

if __name__ == '__main__':
    app.run(debug=True)

