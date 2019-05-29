
from flask import Flask, render_template, request
from elasticsearch import Elasticsearch

app = Flask(__name__)
es = Elasticsearch([{'host': 'localhost', 'port': 9200}])

doc1 = {"food": "Japanese", "spice_level": "moderate"}
doc2 = {"food": "Italian", "spice_level": "mild"}
doc3 = {"food": "Indian", "spice_level": "spicy"}
es.index(index="food", doc_type="spice_level", id=1, body=doc2)
#resp = es.get(index="food", doc_type="spice_level", id=1)
#print(resp)


@app.route('/')
def home():
    return render_template('index.html')

app.route('/dashboard', methods=['GET', 'POST'])


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)