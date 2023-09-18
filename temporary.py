# Voice Short program For understanding concepts of library.
'''
import pyttsx3

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')

for voice in voices:
    print("Voice:")
    print(" - Name:", voice.name)
    print(" - Languages:", voice.languages)
    engine.setProperty('voice', voice.id)
    engine.say("The rain is raining all around, It falls on field and tree, It rains on the umbrellas here, And on the ships at sea.")
    engine.runAndWait()

selected_voice_id = input("Enter the ID of the voice you want to select: ")
engine.setProperty('voice', selected_voice_id)

text = "This is the voice you selected."
engine.say(text)
engine.runAndWait()
'''
'''
import requests
import pyttsx3  # Import a text-to-speech library

def chat_with_gpt(query):
    # Replace with the actual URL or endpoint where your ChatGPT service is hosted
    chatgpt_url = "https://chat.openai.com/c/c4e32186-a7e9-49f2-90fd-d53b17c0d173"

    # Define the request payload with your query
    payload = {"query": query}

    try:
        # Send a POST request to the ChatGPT service
        response = requests.post(chatgpt_url, json=payload)
        response.raise_for_status()

        # Get the response text from ChatGPT
        response_text = response.json().get("response")

        # Print the response
        print(response_text)

        # Use pyttsx3 or another text-to-speech library to speak the response
        engine = pyttsx3.init()
        engine.say(response_text)
        engine.runAndWait()

    except Exception as e:
        print("An error occurred:", str(e))

# Example usage
if __name__ == "__main__":
    query = "What is the capital of France?"
    chat_with_gpt(query)
'''
from config import weather
import requests

# Replace with your OpenWeatherMap API key
api_key = weather

# Define the parameters for your request (e.g., city name and units)
params = {
    "q": "Uttarakhand, India",         # Replace with the desired location (city, country)
    "units": "metric",      # Use "imperial" for Fahrenheit
    "appid": api_key
}

# Define the base API URL for the "weather" endpoint
base_url = "https://api.openweathermap.org/data/2.5/weather"

# Construct the complete URL by combining the base URL and parameters
api_url = f"{base_url}?q={params['q']}&units={params['units']}&appid={params['appid']}"
print(api_url)
# Send the GET request
response = requests.get(api_url)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    data = response.json()
    # Print the weather data
    print("City:", data["name"])
    print("Temperature:", data["main"]["temp"], "°C")
    print("Description:", data["weather"][0]["description"])
else:
    print("Error:", response.status_code)
