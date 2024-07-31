from flask import Flask, request, jsonify, render_template_string
import requests

app = Flask(__name__)

# HTML template with embedded JavaScript
HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Location-Aware Website</title>
</head>
<body>
    <h1>Welcome to our Location-Aware Website</h1>
    <p id="location-info">Detecting your location...</p>

    <script>
    function getLocation() {
        if (navigator.geolocation) {
            navigator.geolocation.getCurrentPosition(showPosition, showError);
        } else {
            document.getElementById("location-info").innerHTML = "Geolocation is not supported by this browser.";
        }
    }

    function showPosition(position) {
        var lat = position.coords.latitude;
        var lon = position.coords.longitude;
        
        fetch('/set_location', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({latitude: lat, longitude: lon}),
        })
        .then(response => response.json())
        .then(data => {
            document.getElementById("location-info").innerHTML = `Your location: ${data.city}, ${data.country}`;
        })
        .catch((error) => {
            console.error('Error:', error);
            document.getElementById("location-info").innerHTML = "Unable to retrieve location information.";
        });
    }

    function showError(error) {
        switch(error.code) {
            case error.PERMISSION_DENIED:
                document.getElementById("location-info").innerHTML = "User denied the request for Geolocation.";
                break;
            case error.POSITION_UNAVAILABLE:
                document.getElementById("location-info").innerHTML = "Location information is unavailable.";
                break;
            case error.TIMEOUT:
                document.getElementById("location-info").innerHTML = "The request to get user location timed out.";
                break;
            case error.UNKNOWN_ERROR:
                document.getElementById("location-info").innerHTML = "An unknown error occurred.";
                break;
        }
    }

    window.onload = getLocation;
    </script>
</body>
</html>
"""


@app.route("/")
def index():
    return render_template_string(HTML_TEMPLATE)


@app.route("/set_location", methods=["POST"])
def set_location():
    data = request.json
    lat = data["latitude"]
    lon = data["longitude"]

    location_info = get_location_info(lat, lon)

    if location_info:
        city = location_info.get("address", {}).get("city", "Unknown City")
        country = location_info.get("address", {}).get("country", "Unknown Country")
        return jsonify({"status": "success", "city": city, "country": country})
    else:
        return jsonify(
            {"status": "error", "message": "Unable to retrieve location information"}
        )


def get_location_info(lat, lon):
    url = f"https://nominatim.openstreetmap.org/reverse?format=json&lat={lat}&lon={lon}"
    headers = {
        "User-Agent": "YourAppName/1.0"
    }  # It's good practice to identify your application
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.json()
    else:
        return None


if __name__ == "__main__":
    app.run(debug=True)
