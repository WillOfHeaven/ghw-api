from flask import Flask, request

app = Flask(__name__)

hackathons = {
    "GHW: API Week": {
        "start_date": "2023-04-03 12:00:00",
        "end_date": "2023-04-10 12:00:00",
        "location": "Everywhere, Online",
        "type": "Digital Only"
    },
    "Bitcamp": {
        "start_date": "2023-04-07 12:00:00",
        "end_date": "2023-04-09 12:00:00",
        "location": "College Park, Maryland",
        "type": "In-Person Only"
    }
}


@app.route("/")
def hello_world():
    return "<p>Hello, World! Will of Heaven here !</p>"


@app.route('/gethackathon', methods=['GET'])
@app.route('/hackathons', methods=['GET', 'POST'])
def getHackathons():
    if request.method == 'POST':
        hackathons["New Hackathon"] = request.json
        return hackathons
    else:
        return hackathons


if __name__ == "__main__":
    app.run(debug=True)
