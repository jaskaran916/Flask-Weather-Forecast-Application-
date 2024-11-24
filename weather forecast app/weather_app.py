from flask import Flask, render_template, request
import requests

app = Flask(__name__)

API_KEY = '214f1a3a1f54537701634f1b1a6bb4e1'

def get_weather_data(city):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return None

@app.route('/', methods=['GET', 'POST'])
def index():
    city = None
    weather_data = None
    error_message = None

    if request.method == 'POST':
        city = request.form['city']
        weather_data = get_weather_data(city)
        if weather_data is None:
            error_message = "City not found or API error. Please try again."

    return render_template('index.html', city=city, weather_data=weather_data, error_message=error_message)

if __name__ == '__main__':
    app.run(debug=True)