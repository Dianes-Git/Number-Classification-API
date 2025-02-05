# Number Classification API

This project implements a FastAPI-based API that classifies a number based on mathematical properties. The API handles requests to classify a number and provides a detailed response including fun facts, properties (e.g., Armstrong, prime, even/odd), and a digit sum. 

## Features
- Classifies numbers as prime, perfect, Armstrong, odd, or even.
- Provides a fun fact about the number.
- Returns responses in JSON format.
- Handles CORS to allow cross-origin requests.
- Handles invalid inputs and returns an appropriate error response (400 Bad Request).

## Technologies Used
- Python: Programming language for implementing the API.
- FastAPI: Web framework for building the API.
- Uvicorn: ASGI server for running the FastAPI app.
- Requests: Library for fetching fun facts from an external API.
- GitHub: Version control and repository hosting.
- Render: Platform for deploying the API.
- CORS Middleware: To handle cross-origin resource sharing (CORS).

## Example Response (200 OK)
<img width="1280" alt="Screenshot 2025-02-05 at 19 09 30" src="https://github.com/user-attachments/assets/cd12015a-d311-4b65-b2ed-0d4df18f2661" />

## Example Response (400 Bad Request)
<img width="1267" alt="Screenshot 2025-02-05 at 19 34 00" src="https://github.com/user-attachments/assets/5e5eb68e-a033-4d50-b18f-7d760e196854" />

## Setup
- 1. Install Dependencies
- Create a virtual environment and install the necessary dependencies:
 ```bash
python -m venv venv
source venv/bin/activate  # On Windows use venv\Scripts\activate
pip install fastapi uvicorn requests
```
- 2. Run the API Locally
To start the development server, use:
- `uvicorn main:app --reload
`

This will run the application locally on http://127.0.0.1:8000
