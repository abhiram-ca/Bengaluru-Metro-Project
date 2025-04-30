from flask import Flask, request, render_template
from source_code import bngroute
import json
from flask import url_for

app = Flask(__name__)

# List of stations
stations = [
    {"id": 1, "name": "Madavara"},
    {"id": 2, "name": "Chikkabidarakallu"},
    {"id": 3, "name": "Manjunathanagara"},
    {"id": 4, "name": "Nagasandra"},
    {"id": 5, "name": "Dasarahalli"},
    {"id": 6, "name": "Jalahalli"},
    {"id": 7, "name": "Peenya Industry"},
    {"id": 8, "name": "Peenya"},
    {"id": 9, "name": "Goraguntepalya"},
    {"id": 10, "name": "Yeshwanthpur"},
    {"id": 11, "name": "Sandal Soap Factory"},
    {"id": 12, "name": "Mahalakshmi"},
    {"id": 13, "name": "Rajajinagara"},
    {"id": 14, "name": "Mahakavi Kuvempu Road"},
    {"id": 15, "name": "Srirampura"},
    {"id": 16, "name": "Mantri Square Sampige Road"},
    {"id": 17, "name": "Nadaprabhu Kempegowda Station, Majestic"},
    {"id": 18, "name": "Chikkapete"},
    {"id": 19, "name": "Krishna Rajendra Market"},
    {"id": 20, "name": "National College"},
    {"id": 21, "name": "Lalbagh"},
    {"id": 22, "name": "South End Circle"},
    {"id": 23, "name": "Jayanagara"},
    {"id": 24, "name": "Rashtreeya Vidyalaya Road"},
    {"id": 25, "name": "Banashankari"},
    {"id": 26, "name": "Jayaprakash Nagara"},
    {"id": 27, "name": "Yelachenahalli"},
    {"id": 28, "name": "Konanakunte Cross"},
    {"id": 29, "name": "Doddakallasandra"},
    {"id": 30, "name": "Vajarahalli"},
    {"id": 31, "name": "Thalaghattapura"},
    {"id": 32, "name": "Silk Institute"},
    {"id": 33, "name": "Whitefield"},
    {"id": 34, "name": "Hopefarm Channasandra"},
    {"id": 35, "name": "Kadugodi Tree Park"},
    {"id": 36, "name": "Pattanduru Agrahara"},
    {"id": 37, "name": "Sri Sathya Sai Hospital"},
    {"id": 38, "name": "Nallurhalli"},
    {"id": 39, "name": "Kundalahalli"},
    {"id": 40, "name": "Seetharamapalya"},
    {"id": 41, "name": "Hoodi"},
    {"id": 42, "name": "Garudacharapalya"},
    {"id": 43, "name": "Singayyanapalya"},
    {"id": 44, "name": "Krishnarajapura (K.R.Pura)"},
    {"id": 45, "name": "Benniganahalli"},
    {"id": 46, "name": "Baiyappanahalli"},
    {"id": 47, "name": "Swami Vivekananda Road"},
    {"id": 48, "name": "Indiranagar"},
    {"id": 49, "name": "Halasuru"},
    {"id": 50, "name": "Trinity"},
    {"id": 51, "name": "Mahatma Gandhi Road"},
    {"id": 52, "name": "Cubbon Park"},
    {"id": 53, "name": "Dr. BR. Ambedkar Station, Vidhana Soudha"},
    {"id": 54, "name": "Sir M. Visveshwaraya Station, Central College"},
    {"id": 55, "name": "Krantivira Sangolli Rayanna Railway Station"},
    {"id": 56, "name": "Magadi Road"},
    {"id": 57, "name": "Sri Balagangadharanatha Swamiji Station, Hosahalli"},
    {"id": 58, "name": "Vijayanagara"},
    {"id": 59, "name": "Attiguppe"},
    {"id": 60, "name": "Deepanjali Nagara"},
    {"id": 61, "name": "Mysuru Road"},
    {"id": 62, "name": "Pantharapalya - Nayandahalli"},
    {"id": 63, "name": "Rajarajeshwari Nagara"},
    {"id": 64, "name": "Jnana Bharathi"},
    {"id": 65, "name": "Pattanagere"},
    {"id": 66, "name": "Kengeri Bus Terminal"},
    {"id": 67, "name": "Kengeri"},
    {"id": 68, "name": "Challaghatta"}
]

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        source_station_id = int(request.form['source_station'])
        destination_station_id = int(request.form['destination_station'])
        output = bngroute(source_station_id, destination_station_id)
        return render_template('index.html', stations=stations, output=output)
    return render_template('index.html', stations=stations)


if __name__ == '__main__':
    app.run(debug=True)