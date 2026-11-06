
"use client";

import { useEffect, useState } from "react";

type MetricResponse = {
  metric: string;
  group_by: string | null;
  data: Record<string, string | number>[];
};

const API = "http://127.0.0.1:8000";

export default function LiveDashboard() {
  const [revenue, setRevenue] = useState(0);
  const [profit, setProfit] = useState(0);
  const [margin, setMargin] = useState(0);

  const [regions, setRegions] = useState<Record<string, string | number>[]>([]);
  const [products, setProducts] = useState<Record<string, string | number>[]>([]);

  const [loading, setLoading] = useState(true);
  const [error, setError] = useState("");

  useEffect(() => {
    async function loadDashboard() {
      try {
        setLoading(true);
        setError("");

        const responses = await Promise.all([
          fetch(`${API}/metrics/revenue`),
          fetch(`${API}/metrics/profit`),
          fetch(`${API}/metrics/profit_margin`),
          fetch(`${API}/metrics/revenue?group_by=region`),
          fetch(`${API}/metrics/revenue?group_by=product`),
        ]);

        if (responses.some((response) => !response.ok)) {
          throw new Error("API request failed. Check the backend server.");
        }

        const [
          revenueData,
          profitData,
          marginData,
          regionData,
          productData,
        ]: MetricResponse[] = await Promise.all(
          responses.map((response) => response.json())
        );

        setRevenue(Number(revenueData.data[0]?.revenue ?? 0));
        setProfit(Number(profitData.data[0]?.profit ?? 0));
        setMargin(Number(marginData.data[0]?.profit_margin ?? 0));

        setRegions(regionData.data);
        setProducts(productData.data);
      } catch (err) {
        setError(
          err instanceof Error ? err.message : "Something went wrong."
        );
      } finally {
        setLoading(false);
      }
    }

    loadDashboard();
  }, []);

  const money = (value: number) =>
    new Intl.NumberFormat("en-IN", {
      style: "currency",
      currency: "INR",
      maximumFractionDigits: 2,
    }).format(value);

  return (
    <main style={{
      minHeight: "100vh",
      background: "#f4f7fb",
      padding: "35px",
      fontFamily: "Arial, sans-serif",
      color: "#17233c"
    }}>
      <h1>MetricMind – Live BI Dashboard</h1>
      <p>Real-time connection to governed business metrics API</p>

      {loading && <p>Loading actual sales data...</p>}

      {error && (
        <p style={{ color: "red" }}>Error: {error}</p>
      )}

      {!loading && !error && (
        <>
          <section style={{
            display: "grid",
            gridTemplateColumns: "repeat(auto-fit, minmax(200px, 1fr))",
            gap: "18px",
            marginTop: "28px"
          }}>
            <MetricCard title="Total Revenue" value={money(revenue)} />
            <MetricCard title="Total Profit" value={money(profit)} />
            <MetricCard title="Profit Margin" value={`${margin.toFixed(2)}%`} />
          </section>

          <section style={{
            display: "grid",
            gridTemplateColumns: "repeat(auto-fit, minmax(280px, 1fr))",
            gap: "20px",
            marginTop: "28px"
          }}>
            <div style={panelStyle}>
              <h2>Revenue by Region</h2>
              {regions.map((item, index) => (
                <div key={index} style={rowStyle}>
                  <span>{String(item.region)}</span>
                  <strong>{money(Number(item.revenue))}</strong>
                </div>
              ))}
            </div>

            <div style={panelStyle}>
              <h2>Revenue by Product</h2>
              {products.map((item, index) => (
                <div key={index} style={rowStyle}>
                  <span>{String(item.product)}</span>
                  <strong>{money(Number(item.revenue))}</strong>
                </div>
              ))}
            </div>
          </section>

          <p style={{ marginTop: "25px", color: "#16834a" }}>
            ✓ Connected successfully to MetricMind FastAPI backend.
          </p>
        </>
      )}
    </main>
  );
}

function MetricCard({ title, value }: { title: string; value: string }) {
  return (
    <div style={{
      background: "white",
      padding: "24px",
      borderRadius: "12px",
      boxShadow: "0 2px 10px #0000000d"
    }}>
      <p style={{ color: "#65718a", margin: 0 }}>{title}</p>
      <h2 style={{ fontSize: "27px", marginBottom: 0 }}>{value}</h2>
    </div>
  );
}

const panelStyle = {
  background: "white",
  padding: "24px",
  borderRadius: "12px",
  boxShadow: "0 2px 10px #0000000d"
};

const rowStyle = {
  display: "flex",
  justifyContent: "space-between",
  gap: "12px",
  padding: "14px 0",
  borderBottom: "1px solid #edf0f5"
};
