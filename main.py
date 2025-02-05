from fastapi import FastAPI, Query
import requests

app = FastAPI()

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
    properties = ["odd" if number % 2 else "even"]
    if is_armstrong(number):
        properties.insert(0, "armstrong")

    # Fetch fun fact from Numbers API
    try:
        fun_fact = requests.get(f"http://numbersapi.com/{number}/math").text
    except:
        fun_fact = "No fun fact available."

    response = {
        "number": number,
        "is_prime": is_prime(number),
        "is_perfect": is_perfect(number),
        "properties": properties,
        "digit_sum": sum(map(int, str(number))),
        "fun_fact": fun_fact
    }
    
    return response
