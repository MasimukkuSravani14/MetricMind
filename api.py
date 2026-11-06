
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware

from semantic_layer import get_metric, METRICS, DIMENSIONS

app = FastAPI(
    title="MetricMind BI API",
    description="Governed Business Metrics API",
    version="1.0.0"
)

# Allow the Next.js frontend to connect
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def home():
    return {
        "message": "Welcome to MetricMind BI API",
        "status": "running"
    }


@app.get("/metrics")
def available_metrics():
    return {
        "metrics": list(METRICS.keys()),
        "dimensions": DIMENSIONS
    }


@app.get("/metrics/{metric}")
def read_metric(metric: str, group_by: str = None):

    try:
        result = get_metric(metric, group_by)

        return {
            "metric": metric,
            "group_by": group_by,
            "data": result.to_dict(orient="records")
        }

    except ValueError as error:
        raise HTTPException(
            status_code=400,
            detail=str(error)
        )

    except Exception as error:
        raise HTTPException(
            status_code=500,
            detail="Unable to retrieve metric: " + str(error)
        )
