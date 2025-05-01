def transform_data():
    engine = create_engine('postgresql://nisha:yourpassword@localhost:5432/customer_db')
    df = pd.read_sql('SELECT * FROM customers', engine)
    df['signup_date'] = pd.to_datetime(df['signup_date'])
    df['last_purchase_date'] = pd.to_datetime(df['last_purchase_date'])
    df['days_since_last_purchase'] = (pd.Timestamp('now') - df['last_purchase_date']).dt.days
    df.to_sql('customer_summary', engine, if_exists='replace', index=False)