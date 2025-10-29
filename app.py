from flask import Flask, render_template, request
import requests

app = Flask(__name__)

@app.route("/", methods=["POST", "GET"])
def home():
    if request.method == "POST":
        city = request.form["city"]
        api_key = "YOUR_API_KEY"  # 🔹 Replace with your actual OpenWeather key
        url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
        
        response = requests.get(url)
        data = response.json()

        # 👇 Print the response to check
        print("API Response:", data)

        # ✅ Check if the response has 'main' key
        if response.status_code == 200 and "main" in data:
            temperature = data["main"]["temp"]
            description = data["weather"][0]["description"]
            return render_template("index.html", temperature=temperature, description=description, city=city)
        else:
            # 🟡 If no 'main', show an error message instead of crashing
            message = data.get("message", "City not found or invalid API key.")
            return render_template("index.html", error=message)

    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)