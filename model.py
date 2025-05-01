import pandas as pd
from sqlalchemy import create_engine
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report


def run_model():
    engine = create_engine('postgresql://nisha:yourpassword@localhost:5432/customer_db')
    df = pd.read_sql('SELECT * FROM customer_summary', engine)

    df['is_churned'] = df['days_since_last_purchase'] > 30

    X = df[['days_since_last_purchase']]
    y = df['is_churned'].astype(int)

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    model = LogisticRegression()
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)

    print(classification_report(y_test, y_pred))
    df['predicted_churn'] = model.predict(X)
    df.to_sql('customer_summary', engine, if_exists='replace', index=False)