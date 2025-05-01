import dash
from dash import dcc, html
import pandas as pd
import plotly.express as px
from sqlalchemy import create_engine

app = dash.Dash(__name__)

engine = create_engine('postgresql://nisha:yourpassword@localhost:5432/customer_db')

df = pd.read_sql("SELECT * FROM customer_summary;", engine)

df['is_churned'] = df['is_churned'].astype(int)
churn_counts = df['is_churned'].value_counts()

churn_fig = px.pie(
    names=['Active', 'Churned'],
    values=churn_counts,
    title='Customer Churn Distribution',
    hole=0.4
)

app.layout = html.Div([
    html.H1("Customer Analytics Dashboard", style={'textAlign': 'center'}),
    dcc.Graph(figure=churn_fig)
])

if __name__ == "__main__":
    app.run_server(debug=True)