import dash
from dash import dcc, html
import plotly.express as px
import pandas as pd
import os
import webbrowser

# ✅ Load Data
df = pd.read_excel('project/Mobiles_excel.xlsx', engine='openpyxl')

# ✅ Clean and Convert Price Columns
df['Launched Price (India)'] = df['Launched Price (India)'].str.replace('INR ', '').str.replace(',', '').astype(int)
df['Battery Capacity (mAh)'] = (
    df['Battery Capacity']
    .str.replace('mAh', '', regex=False)
    .str.replace(',', '', regex=False)
    .astype(int)
)

# ✅ Bar Chart: Average Price by Company
avg_price = df.groupby('Company Name')['Launched Price (India)'].mean().reset_index()
fig_bar = px.bar(avg_price, x='Company Name', y='Launched Price (India)', title='Average Price by Company (INR)', color='Company Name')

# ✅ Line Chart: Number of Phones Launched Over Time
phones_by_year = df.groupby('Launched Year')['Model Name'].count().reset_index()
phones_by_year.columns = ['Launched Year', 'Number of Models']
fig_line = px.line(phones_by_year, x='Launched Year', y='Number of Models', title='Number of Phones Launched Over Time', markers=True)

# ✅ Scatter Plot: Battery Capacity vs Price
scatter_plot = px.scatter(df, x='Battery Capacity (mAh)', y='Launched Price (India)', color='Company Name',
                          size='Battery Capacity (mAh)', hover_data=['Model Name'],
                          title='Battery Capacity vs Price')

# ✅ Pie Chart: Market Share by Company
market_share = df['Company Name'].value_counts().reset_index()
market_share.columns = ['Company Name', 'Number of Models']
pie_chart = px.pie(market_share, names='Company Name', values='Number of Models', title='Market Share by Company')

# ✅ Box Plot: Distribution of Prices by Company
box_plot = px.box(df, x='Company Name', y='Launched Price (India)', color='Company Name', title='Price Distribution by Company')

# ✅ Heatmap: Average Price by Company and Launch Year
heatmap_data = df.pivot_table(index='Company Name', columns='Launched Year', values='Launched Price (India)', aggfunc='mean', fill_value=0)
heatmap = px.imshow(heatmap_data, labels=dict(x="Launched Year", y="Company Name", color="Average Price (INR)"),
                    title="Heatmap of Average Phone Prices by Launch Year", aspect="auto")

# ✅ Initialize Dash App
app = dash.Dash(__name__)

# ✅ Layout
app.layout = html.Div([
    html.H1("📊 Mobile Data Dashboard", style={'text-align': 'center', 'margin-bottom': '20px'}),

    dcc.Graph(figure=fig_bar),
    dcc.Graph(figure=fig_line),
    dcc.Graph(figure=scatter_plot),
    dcc.Graph(figure=pie_chart),
    dcc.Graph(figure=box_plot),
    dcc.Graph(figure=heatmap),
])

# ✅ Run the App
if __name__ == '__main__':
    url = "http://127.0.0.1:8050/"
    print(f"🚀 Starting Dash app... Open: {url}")

    if os.environ.get("RENDER_ENV") != "production":
        webbrowser.open_new(url)

    app.run(host='0.0.0.0', port=int(os.environ.get("PORT", 8050)))
