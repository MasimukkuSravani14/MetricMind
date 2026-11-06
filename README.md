## MetricMind – Semantic BI Engine

## Project Overview
MetricMind is a Business Intelligence project that converts raw sales data into meaningful business metrics using Python, Pandas, SQLite, FastAPI, and Next.js.

## Problem Statement
Businesses need an efficient way to analyze revenue, profit, and profit margins across different regions and products. Manual analysis takes time and makes business decisions difficult.

## Objectives
- Process sales data using Python.
- Calculate revenue, profit, and profit margin.
- Store processed data in SQLite.
- Build a semantic metrics layer.
- Provide REST APIs using FastAPI.
- Display business metrics through a web dashboard.

## Technologies Used
- Python
- Pandas
- SQLite
- FastAPI
- Next.js
- React
- TypeScript

## Key Features
- Total Revenue
- Total Profit
- Overall Profit Margin
- Revenue by Region
- Revenue by Product
- Revenue by Country
- Live dashboard connected to FastAPI

## Project Structure

```text
MetricMind/
├── data/
├── database/
├── frontend/
├── api.py
├── create_data.py
├── load_database.py
├── semantic_layer.py
├── requirements.txt
└── README.md
```

## How to Run

### 1. Clone the repository

```bash
git clone https://github.com/MasimukkuSravani14/MetricMind.git
cd MetricMind
```

### 2. Create virtual environment

```bash
python -m venv .venv
.venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Load database

```bash
python load_database.py
```

### 5. Start backend

```bash
python -m uvicorn api:app --reload
```

API documentation: http://127.0.0.1:8000/docs

### 6. Start frontend

Open another terminal:

```bash
cd frontend
npm install
npm run dev
```

Dashboard: http://localhost:3000

Live Dashboard: http://localhost:3000/live

## Future Enhancements
- Natural language queries using AI.
- AI-powered business insights.
- Automated anomaly detection.
- Advanced interactive visualizations.

## Conclusion
MetricMind demonstrates how raw sales data can be transformed into useful business insights through data processing, semantic metrics, APIs, and a web dashboard.

## Author
Masimukku Sravani

## GitHub Repository
https://github.com/MasimukkuSravani14/MetricMind
