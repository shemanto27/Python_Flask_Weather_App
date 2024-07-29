from flask import Flask, render_template, request
import requests

app = Flask(__name__)

API_KEY = "d5757c464d1aed3a3d5cbafe849a267e"


@app.route("/", methods=["GET", "POST"])
@app.route("/home")
def home():
    if request.method == "POST":
        city_name = request.form.get("city_name")
        country_code = request.form.get("country_code")
        url = "http://api.openweathermap.org/geo/1.0/direct?q=city_name,{state code},country_code&limit={limit}&appid=API_KEY"
        weather_data = requests.get(url).json()
    else:
        city_name = "Dhaka"
        country_code = "BGD"
        url = "http://api.openweathermap.org/geo/1.0/direct?q=city_name,{state code},country_code&limit={limit}&appid=API_KEY"
        weather_data = requests.get(url).json()
    return render_template("base.html", weather_data = weather_data, city_name = city_name, country_code = country_code)






if __name__ == "__main__":
    app.run(debug=True)