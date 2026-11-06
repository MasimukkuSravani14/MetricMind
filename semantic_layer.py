
import sqlite3
import pandas as pd

# Database location
DB_PATH = "database/metricmind.db"

# Governed business metric definitions
METRICS = {
    "revenue": "SUM(revenue)",
    "profit": "SUM(profit)",
    "profit_margin": "(SUM(profit) * 100.0 / SUM(revenue))"
}

# Allowed dimensions
DIMENSIONS = [
    "region",
    "country",
    "product"
]


# Function to retrieve business metrics
def get_metric(metric, group_by=None):

    # Validate metric
    if metric not in METRICS:
        raise ValueError("Invalid metric: " + metric)

    # Validate dimension
    if group_by is not None and group_by not in DIMENSIONS:
        raise ValueError("Invalid dimension: " + group_by)

    metric_sql = METRICS[metric]

    # Build SQL query
    if group_by:

        query = f"""
            SELECT
                {group_by},
                ROUND({metric_sql}, 2) AS {metric}
            FROM sales
            GROUP BY {group_by}
            ORDER BY {metric} DESC
        """

    else:

        query = f"""
            SELECT
                ROUND({metric_sql}, 2) AS {metric}
            FROM sales
        """

    # Connect to database
    conn = sqlite3.connect(DB_PATH)

    # Execute query
    result = pd.read_sql_query(query, conn)

    # Close connection
    conn.close()

    return result


# Main program
if __name__ == "__main__":

    print("=" * 50)
    print("       METRICMIND SEMANTIC LAYER")
    print("=" * 50)

    # Display available metrics
    print("\n1. AVAILABLE METRICS")

    for metric in METRICS:
        print("-", metric)

    # Display available dimensions
    print("\n2. AVAILABLE DIMENSIONS")

    for dimension in DIMENSIONS:
        print("-", dimension)

    # Total revenue
    print("\n3. TOTAL REVENUE")
    print(get_metric("revenue"))

    # Total profit
    print("\n4. TOTAL PROFIT")
    print(get_metric("profit"))

    # Overall profit margin
    print("\n5. OVERALL PROFIT MARGIN")
    print(get_metric("profit_margin"))

    # Revenue by region
    print("\n6. REVENUE BY REGION")
    print(get_metric("revenue", "region"))

    # Profit by region
    print("\n7. PROFIT BY REGION")
    print(get_metric("profit", "region"))

    # Profit margin by region
    print("\n8. PROFIT MARGIN BY REGION")
    print(get_metric("profit_margin", "region"))

    # Revenue by country
    print("\n9. REVENUE BY COUNTRY")
    print(get_metric("revenue", "country"))

    # Revenue by product
    print("\n10. REVENUE BY PRODUCT")
    print(get_metric("revenue", "product"))

    print("\n" + "=" * 50)
    print("SEMANTIC LAYER EXECUTION COMPLETED!")
    print("=" * 50)

