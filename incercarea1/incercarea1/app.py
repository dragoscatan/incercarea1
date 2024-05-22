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
@app.route('/cauta/id', methods=['GET'])
def api_id():
    #verificam daca a fost introdus un id valid
        if 'id' in request.args:
            #daca a fost, variabilei id ii va fi atribuit id ul introdus
            id = request.args['id']
        else:
            #daca nu a fost, afisam o eroare
            return "Error: No id field provided. Please specify an id."
        results = list(filter(lambda a: id in str(a['Id']), dataJ))
        return jsonify(results)
@app.route('/descriptions', methods=['GET'])
#functia descrieri va parcurge cu ajutorul map lista dataJ, urmand sa afiseze descrierile fiecarui element
def descrieri():
    desc=list(map(lambda a: a['Description'], dataJ))
    return jsonify(desc)
app.run()