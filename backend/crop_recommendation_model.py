import requests
import json
from typing import Dict, Optional

# Hugging Face API endpoint for crop recommendation
API_URL = "https://api-inference.huggingface.co/models/your-username/crop-recommendation"
HEADERS = {
    "Authorization": "Bearer hf_xxx"  # Replace with your Hugging Face API token
}

def predict_crop(temperature: float, humidity: float, rainfall: float, soil_ph: float = 6.5) -> Optional[Dict]:
    """Get crop recommendation from Hugging Face model"""
    try:
        # Prepare the input data
        payload = {
            "inputs": {
                "temperature": temperature,
                "humidity": humidity,
                "rainfall": rainfall,
                "soil_ph": soil_ph
            }
        }

        # Make the API request
        response = requests.post(API_URL, headers=HEADERS, json=payload)
        
        if response.status_code == 200:
            result = response.json()
            return {
                "crop": result["crop"],
                "confidence": result["confidence"],
                "all_probabilities": result["probabilities"],
                "message": f"🌱 Based on the weather conditions, {result['crop']} would be a great choice!"
            }
        else:
            print(f"Error from API: {response.status_code}")
            return None

    except Exception as e:
        print(f"Error in prediction: {str(e)}")
        return None

if __name__ == "__main__":
    # Test the model
    test_prediction = predict_crop(temperature=25, humidity=70, rainfall=800)
    print("Test prediction:", test_prediction) 