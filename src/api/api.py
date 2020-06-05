from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin
from KMP import translate
from BM import translateBM
from regex import translateregex

app = Flask(__name__)

cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

sidict = {}
isdict = {}

teh = ['kamu','saya','aku','dia','mereka','kami','gue','kau']
with open("is.dict",'r') as f:
    lines = f.read()
    for line in lines.split('\n'):
        kata = line.split(' = ')
        # print(kata[0])
        isdict[kata[0]] = kata[1]
        if kata[0] in teh:
            isdict[kata[0]] += " teh"

with open("si.dict",'r') as f:
    lines = f.read()
    for line in lines.split('\n'):
        kata = line.split(' = ')
        sidict[kata[0]] = kata[1]


@app.route('/kmpis',methods=['POST'])
@cross_origin()
def pattern_matchingkmpis():
    datas = request.get_json()
    hasil = translate(datas['sentence'],isdict)
    return jsonify({'data' : hasil}),200

@app.route('/kmpsi',methods=['POST'])
@cross_origin()
def pattern_matchingkmpsi():
    datas = request.get_json()
    hasil = translate(datas['sentence'],sidict)
    return jsonify({'data' : hasil}),200

@app.route('/bmis',methods=['POST'])
@cross_origin()
def pattern_matchingbm():
    datas = request.get_json()
    hasil = translateBM(datas['sentence'],isdict)
    return jsonify({'data' : hasil}),200

@app.route('/bmsi',methods=['POST'])
@cross_origin()
def pattern_matchingbmsi():
    datas = request.get_json()
    hasil = translateBM(datas['sentence'],sidict)
    return jsonify({'data' : hasil}),200


@app.route('/regexis',methods=['POST'])
@cross_origin()
def pattern_matchingreis():
    datas = request.get_json()
    hasil = translateregex(datas['sentence'],isdict)
    return jsonify({'data' : hasil}),200

@app.route('/regexsi',methods=['POST'])
@cross_origin()
def pattern_matchingresi():
    datas = request.get_json()
    hasil = translateregex(datas['sentence'],sidict)
    return jsonify({'data' : hasil}),200