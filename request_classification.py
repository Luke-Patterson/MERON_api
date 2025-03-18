#!/usr/bin/env python
import requests
from pathlib import Path


def main():
    """
    Send a request to the MERON API to get classification and score for a face image.
    """
    # API endpoint (local development server)
    api_url = "http://127.0.0.1:8000/"
    
    # Path to the image file
    image_path = Path("data/face.jpg")
    
    if not image_path.exists():
        print(f"Error: Image file not found at {image_path}")
        return
    
    # Sample data for a child (modify as needed)
    # age: age in months
    # gender: 'm' for male, 'f' for female
    data = {
        "age": 30,  # 2.5 years old
        "gender": "m",
        "score": True,
        "classification": True
    }
    
    # Open the image file in binary mode
    files = {
        "image": open(image_path, "rb")
    }
    
    print(f"Sending request to {api_url} with image: {image_path}")
    print(f"Parameters: age={data['age']} months, gender={data['gender']}")
    
    try:
        # Send the POST request
        response = requests.post(api_url, files=files, data=data)
        
        # Check if request was successful
        if response.status_code == 200:
            result = response.json()
            print("\nResults:")
            print("-" * 40)
            
            if "score" in result:
                print(f"Weight-for-height z-score: {result['score']}")
            
            if "classification" in result:
                print(f"Malnutrition classification: {result['classification']}")
            
            # If there are any additional fields in the response
            for key, value in result.items():
                if key not in ["score", "classification"]:
                    print(f"{key}: {value}")
        else:
            print(f"Error: Received status code {response.status_code}")
            print(f"Response: {response.text}")
    
    except Exception as e:
        print(f"Error occurred: {e}")
    
    finally:
        # Close the image file
        files["image"].close()


if __name__ == "__main__":
    main() 