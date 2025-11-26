import json
from urllib import request

json_path = "pid_prodejni_mista.json"

def download_data():
    url = "https://data.pid.cz/pointsOfSale/json/pointsOfSale.json"

    with request.urlopen(url) as response:
        data = json.load(response)

        with open(json_path, mode="w", encoding="utf-8") as file:
            json.dump(data, file)


def read_data():
    with open(json_path, mode="r", encoding="utf-8") as file:
        return json.load(file)


def generate_page(item):

    opening = item["openingHours"][0]

    html = f"""
    <body style="background-color: #C0C0C0">
    <h1 style="text-align: center">Prodejní místa</h1>
    <br>
    <h2 style="text-decoration: underline">{item["name"]}</h2>
    <p><span style="font-weight: bold">Typ:</span> {item["type"]}</p>
    <p><span style="font-weight: bold">Adresa:</span> {item["address"]}</p>
    <p><span style="font-weight: bold">Otevírací hodiny:</span> {opening["hours"]} (od: {opening["from"]} do: {opening["to"]})</p>
    <p><span style="font-weight: bold">Zeměpisná šířka:</span> {item["lat"]}</p>
    <p><span style="font-weight: bold">Zeměpisná délka:</span> {item["lon"]}</p>
    </body>
    """

    # přidat type, openingHours, lat, lon
    # volitelně přidat CSS
    # lat o lon použít při vykreslení mapy pomocí leaflet

    with open(f"html-pages/{item['id']}.html", mode="w", encoding="utf-8") as file:
        file.write(html)


def generate():
    data = read_data()

    for item in data:
        generate_page(item)


generate()

generate_page({
    "id": "dp2",
    "type": "ticketMachine",
    "name": "Grand Hotel International",
    "address": "Koulova 1501/15, Dejvice, Praha 6",
    "openingHours": [
      {
        "from": 0,
        "to": 6,
        "hours": "5:00-24:00"
      }
    ],
    "lat": 50.1093445,
    "lon": 14.3935671,
    "services": 196608,
    "payMethods": 1
  })