import pandas as pd
from dash import Dash, html, dcc, Input, Output
import plotly.express as px

# Loading the data
df = pd.read_csv("data/clean_data.csv")

app = Dash(__name__)

app.layout = html.Div(
    children=[

        html.H1(
            "Soul Foods Pink Morsel Sales Dashboard",
            className="header"
        ),

        html.P(
            "Analyse sales before and after the Pink Morsel price increase on 15 January 2021.",
            className="description"
        ),

        html.Div([
            html.Label("Select Region:", className="radio-label"),

            dcc.RadioItems(
                id="region-filter",
                options=[
                    {"label": "All", "value": "all"},
                    {"label": "North", "value": "north"},
                    {"label": "East", "value": "east"},
                    {"label": "South", "value": "south"},
                    {"label": "West", "value": "west"},
                ],
                value="all",
                inline=True
            ),
        ],
        className="radio-container"),

        dcc.Graph(id="sales-chart")

    ],
    className="main-container"
)


@app.callback(
    Output("sales-chart", "figure"),
    Input("region-filter", "value")
)
def update_chart(selected_region):

    if selected_region == "all":
        filtered_df = df
    else:
        filtered_df = df[df["Region"].str.lower() == selected_region]

    daily_sales = (
        filtered_df.groupby("Date")["Sales"]
        .sum()
        .reset_index()
        .sort_values("Date")
    )

    fig = px.line(
        daily_sales,
        x="Date",
        y="Sales",
        title=f"Sales Trend - {selected_region.title()}"
    )

    fig.update_layout(
        template="plotly_white",
        title_x=0.5,
        xaxis_title="Date",
        yaxis_title="Sales ($)"
    )

    fig.add_vline(
        x="2021-01-15",
        line_dash="dash",
        annotation_text="Price Increase",
        annotation_position="top"
    )

    return fig


if __name__ == "__main__":
    app.run(debug=True)