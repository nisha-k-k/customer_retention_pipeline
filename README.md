# PROJECT IN PROGRESS

# 🧩 Customer Analytics Pipeline Project

This project is a full **end-to-end data pipeline** that demonstrates the key skills of an Analytics Engineer: **data ingestion, transformation, modeling, scheduling, and dashboarding** — all built using **Python**, **PostgreSQL**, **Airflow**, and **Dash**.

---

## 🚀 Project Overview

**Customer Analytics Pipeline** processes customer data from a CSV source file into a PostgreSQL database, applies data transformations, trains a churn prediction model, and displays key insights on an interactive dashboard.

The pipeline is modular, scalable, and production-ready — ideal for real-world business analytics needs.

---


---

## 📊 Dashboard Preview

Key dashboard features include:
- Gender distribution (pie chart)
- Customer counts by tier (bar chart)
- Age distribution (histogram)
- Churn rate by customer tier (bar chart)

Built using **Plotly Dash** for interactive, responsive visuals.

---

## ⚙️ Tech Stack

| Tool | Purpose |
|:----|:-------|
| Python | Programming language |
| PostgreSQL | Relational database |
| SQLAlchemy | Database connection |
| Pandas | Data manipulation |
| scikit-learn | Machine learning |
| Airflow | Workflow scheduling and orchestration |
| Dash + Plotly | Dashboarding and visualization |
| dotenv | Secure credential handling |

---

## 🧩 How to Run This Project

1. **Clone the repository:**
   ```bash
   git clone https://github.com/nisha-k-k/customer_retention_pipeline.git
   cd customer-analytics-pipeline
2. **Set up virtual environment:**
   ```bash
   python -m venv venv
    source venv/bin/activate  # Mac/Linux
    venv\Scripts\activate     # Windows
3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt

4. **Configure database credentials:**
    ```bash
      DATABASE_URL=postgresql://username:password@localhost:5432/your_database_name
5. **Set up PostgreSQL Database:**
   - Create new database locally
   - Ensure PostgreSQL service is running
6. **Run ingestion script:**
     ```bash
     python ingest.py
7. **Transformations:**
     ```bash
     python transform.py
8. **Run the churn model:**
   ```bash
   python model.py
9. **Start dashboard locally:**
    ```bash
    python dashboard/app.py
## 🌟 Key Learnings
- Secure database management using .env

- Modular pipeline design for ingestion, transformation, and modeling

- End-to-end pipeline orchestration with Airflow

- Real-time dashboards with professional visualizations

- Best practices for production-quality analytics engineering

## 📚 Future Enhancements
- Add customer segmentation (K-Means clustering)

- Connect dashboard live to the database

- Add authentication layer to the dashboard

- Deploy dashboard online (Render, Railway, AWS, etc.)

## 📝 License
This project is open-sourced under the MIT License. 

## 🙋‍♂️ Questions?
Feel free to open an issue or reach out if you have any questions, ideas, or feedback!





