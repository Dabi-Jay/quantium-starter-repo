import pandas as pd 
from dash import Dash, html, dcc
import plotly.express as px

df = pd.read_csv("data/clean_data.csv")

# df["Date"] = pd.to_datetime(df["Date"])

# Aggregate total sales by date
daily_sales = (
    df.groupby("Date")["Sales"]
    .sum()
    .reset_index()
    .sort_values("Date")
)

# Create line chart
fig = px.line(
    daily_sales,
    x="Date",
    y="Sales",
    title="Pink Morsel Sales Over Time"
)

fig.update_layout(
    xaxis_title="Date",
    yaxis_title="Sales"
)

# Mark the price increase date
fig.add_vline(
    x="2021-01-15",
    line_dash="dash",
    annotation_text="Price Increase",
    annotation_position="top"
)

# Create Dash app
app = Dash(__name__)

app.layout = html.Div([
    html.H1(
        "Soul Foods Pink Morsel Sales Visualiser",
        style={"textAlign": "center"}
    ),

    dcc.Graph(
        id="sales-line-chart",
        figure=fig
    )
])

if __name__ == "__main__":
    app.run(debug=True)


print(df.head())