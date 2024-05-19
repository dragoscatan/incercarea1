from flask import Flask
from flask import request, jsonify
import json
app = Flask(__name__)
app.config["DEBUG"] = True
with open('products.json', 'r') as inf:
    dataJ = list(json.load(inf))
@app.route('/', methods=['GET'])
def home():
    try:
        import csv
        with open('produse.csv', 'w', newline='') as outf:
            csvw = csv.writer(outf)
            csvw.writerows(dataJ)
    except BaseException:
        return '''<h1> "Eroare: Nu am putut scrie informația în numele_fisierului.csv"</h1>'''
    else:
        return '''<h1>informația a fost scrisă în produse.csv</h1>'''
@app.route('/api/cauta', methods=['GET'])
def api_id():
        # Check if an ID was provided as part of the URL.
        # If ID is provided, assign it to a variable.
        # If no ID is provided, display an error in the browser.
        if 'id' in request.args:
            id = int(request.args['id'])
        else:
            return "Error: No id field provided. Please specify an id."

        # Create an empty list for our results
        results = []

        # Loop through the data and match results that fit the requested ID.
        # IDs are unique, but other fields might return many results
        for a in dataJ:
            if a['Id'] == id:
                results.append(a)

        # Use the jsonify function from Flask to convert our list of
        # Python dictionaries to the JSON format.
        return jsonify(results)
app.run()