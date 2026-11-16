from fastapi import FastAPI
from pydantic import BaseModel, Field

app = FastAPI(
    title="HRMS Leave Management API"
)


class LeaveRequest(BaseModel):
    total_leaves: int = Field(ge=0)
    leaves_taken: int = Field(ge=0)


@app.get("/health")
def health_check():
    return {"status": "healthy"}


@app.post("/leave-balance")
def calculate_leave_balance(
    request: LeaveRequest
):
    if request.leaves_taken > request.total_leaves:
        return {
            "error": "Leaves taken exceeds total leaves"
        }

    balance = (
        request.total_leaves
        - request.leaves_taken
    )

    return {
        "total_leaves": request.total_leaves,
        "leaves_taken": request.leaves_taken,
        "leave_balance": balance
    }
