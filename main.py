from fastapi import FastAPI, Query, HTTPException
from starlette.middleware.cors import CORSMiddleware
from starlette.responses import JSONResponse
import requests

app = FastAPI()

# Enable CORS for all origins
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

def is_prime(n: int) -> bool:
    """Check if a number is prime."""
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_perfect(n: int) -> bool:
    """Check if a number is a perfect number."""
    return sum(i for i in range(1, n) if n % i == 0) == n

def is_armstrong(n: int) -> bool:
    """Check if a number is an Armstrong number."""
    digits = [int(d) for d in str(abs(n))]  # Ensure it works with negative numbers
    return sum(d ** len(digits) for d in digits) == abs(n)

@app.get("/")
def read_root():
    """Handles requests to the root endpoint with a 400 Bad Request error."""
    raise HTTPException(status_code=400, detail="Invalid endpoint. Use '/api/classify-number'")

@app.get("/api/classify-number")
def classify_number(number: float = Query(..., description="Number to classify")):
    """API Endpoint to classify a number."""
    
    # Ensure the number is valid
    try:
        number = float(number)  # Convert to float to handle decimals
        if number.is_integer():
            number = int(number)  # Convert back to int if it's a whole number
    except ValueError:
        return JSONResponse(
            status_code=400,
            content={"number": str(number), "error": True, "message": "Invalid number format"},
        )

    properties = []

    # Check if the number is Armstrong, odd/even
    if is_armstrong(number):
        properties.append("armstrong")
    if number % 2 == 0:
        properties.append("even")
    else:
        properties.append("odd")

    # Create the fun fact for Armstrong numbers
    if is_armstrong(number):
        digits = [int(d) for d in str(abs(number))]
        powers = " + ".join([f"{d}^{len(digits)}" for d in digits])
        fun_fact = f"{number} is an Armstrong number because {powers} = {number}"
    else:
        fun_fact = f"{number} is not an Armstrong number."

    response = {
        "number": number,
        "is_prime": is_prime(number),
        "is_perfect": is_perfect(number),
        "properties": properties,
        "digit_sum": sum(map(int, str(abs(number)))),
        "fun_fact": fun_fact
    }

    return JSONResponse(status_code=200, content=response)

@app.exception_handler(422)
async def validation_exception_handler(request, exc):
    """Handles invalid inputs (e.g., text input instead of numbers)."""
    return JSONResponse(
        status_code=400,
        content={"error": True, "message": "Invalid input. Please provide a valid number."},
    )
