import requests
import os
from datetime import datetime

# 1. Setup Directories
output_dir = "../raw_images"
os.makedirs(output_dir, exist_ok=True)

# 2. NASA API Config (Use 'DEMO_KEY' for testing, it has a 30 req/hour limit)
API_KEY = "DEMO_KEY"
URL = "https://api.nasa.gov/planetary/apod"

def get_space_pic():
    print("> Contacting NASA API...")
    
    # Get the data
    params = {'api_key': API_KEY, 'hd': 'True'}
    response = requests.get(URL, params=params)
    
    if response.status_code != 200:
        print(f"Error: {response.status_code}")
        return

    data = response.json()
    
    # Extract details
    title = data.get('title', 'Space_Image').replace(" ", "_")
    image_url = data.get('hdurl', data.get('url'))
    explanation = data.get('explanation')
    date_str = datetime.now().strftime("%Y-%m-%d")
    
    print(f"> Found: {data.get('title')}")
    
    # Download the Image
    img_filename = f"{date_str}_{title}.jpg"
    img_path = os.path.join(output_dir, img_filename)
    
    img_data = requests.get(image_url).content
    with open(img_path, 'wb') as handler:
        handler.write(img_data)
        
    print(f"> [SUCCESS] Saved to: {img_path}")
    print(f"> Caption Info: {explanation[:200]}...")

if __name__ == "__main__":
    get_space_pic()
