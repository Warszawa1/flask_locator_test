from flask import Flask, render_template, jsonify
import requests
import json
from twilio.rest import Client
import ssl

app = Flask(__name__)

app.run(host='0.0.0.0', port=5000, debug=True)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/run_function', methods=['POST'])
def run_function():
    # # Your Python function code here
    # result = "Python function executed!"
    # return jsonify({'result': result})

    # url = 'http://ipinfo.io/json'
    # response = urlopen(url)
    # data = json.load(response)
    #
    # print(data)

    # account_sid = 'AC489ed68069cbf0d82f44e9c035201b8f'
    # auth_token = '43f246fa138fb72fbf801c698be2002e'
    # client = Client(account_sid, auth_token)

    ip = requests.get('https://api.ipify.org?format=json')
    ip_data = json.loads(ip.text)
    res = requests.get('http://ip-api.com/json/' + ip_data["ip"])
    location_data_one = res.text
    location_data = json.loads(location_data_one)
    lat = location_data['lat']
    lon = location_data['lon']
    result = location_data['city']

    message_body_template = f'You are here: lat:{lat}, lon:{lon}, city:{result} 📍'
    message_body = message_body_template.format(lat=lat, lon=lon, city=result)
    #
    # message = client.messages \
    #     .create(
    #         body=message_body,
    #         from_='+12052362290',
    #         to='+34633409911'
    # )
    #
    # print(message.sid)

    return jsonify({'result': result})
#
# def prueba():
#     print("Yes, it works!")
#
# prueba()
