from fastapi import FastAPI, Query
from starlette.middleware.cors import CORSMiddleware
import requests

app = FastAPI()

# Enable CORS for all origins
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins, you can specify more strict rules
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods (GET, POST, etc.)
    allow_headers=["*"],  # Allows all headers
)

def is_prime(n):
    """Check if a number is prime."""
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_perfect(n):
    """Check if a number is a perfect number."""
    return sum(i for i in range(1, n) if n % i == 0) == n

def is_armstrong(n):
    """Check if a number is an Armstrong number."""
    digits = [int(d) for d in str(n)]
    return sum(d ** len(digits) for d in digits) == n

@app.get("/api/classify-number")
def classify_number(number: int = Query(..., description="Number to classify")):
    """API Endpoint to classify a number."""
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
        # Generate the Armstrong number fun fact with the correct formula
        digits = [int(d) for d in str(number)]
        powers = " + ".join([f"{d}^{len(digits)}" for d in digits])
        fun_fact = f"{number} is an Armstrong number because {powers} = {number}"
    else:
        # If it's not Armstrong, provide a fallback fun fact
        fun_fact = f"{number} is not an Armstrong number."

    # Construct the response
    response = {
        "number": number,
        "is_prime": is_prime(number),
        "is_perfect": is_perfect(number),
        "properties": properties,
        "digit_sum": sum(map(int, str(number))),
        "fun_fact": fun_fact
    }

    return response
