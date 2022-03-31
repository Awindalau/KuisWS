from flask import Flask, jsonify, request
app = Flask(__name__)

#curl -i -X POST http://127.0.0.1:4023/api/bmi -H 'Content-Type: application/json' -d '{"tinggi":170, "berat":70}'
@app.route('/api/bmi', methods=['POST'])
def bmi():
    tinggi = float(request.json.get('tinggi'))
    berat = float(request.json.get('berat'))
    bmi = berat / (tinggi/100)**2
    msg = "BMI anda " + str(bmi)
    if bmi <= 18.5 :
        ket = " kurus "
    elif bmi <= 25 :
        ket = " normal"
    elif bmi <= 40 :
        ket = "berlebih"
    else :
        ket = "bahaya"
    data = {'result': 'true', 'msg': msg, 'ket':ket}
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug = True, port= 4023)