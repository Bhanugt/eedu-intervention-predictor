# -*- coding: utf-8 -*-
"""RequestHandler.py

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1KFbeQLgpJaTTUQJGJoTOlu7Yr6O5UuEL
"""

import requests

def send_prediction_request(input_features):
    """
    Sends a POST request to the prediction API with input features.
    """
    API_URL = "https://your-render-api-url.com/predict"  # Replace with actual API URL

    try:
        response = requests.post(API_URL, json={"features": input_features}, timeout=10)
        response.raise_for_status()  # Raises an HTTPError for bad responses (4xx and 5xx)
        return response.json()  # Return the JSON response
    except requests.ConnectionError:
        return {"error": "Connection error. Unable to reach the prediction server."}
    except requests.Timeout:
        return {"error": "Request timed out. The server is taking too long to respond."}
    except requests.RequestException as e:
        return {"error": f"An error occurred: {str(e)}"}