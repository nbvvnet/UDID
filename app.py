from flask import Flask, request, json, make_response
import time, jwt

app = Flask(__name__)

@app.route('/getToken', methods=['post'])
def getToken():
    privatekey = request.json.get('p8')
    kid = request.json.get('kid')
    iss = request.json.get('iss')
    # 1. Create the JWT header
    header = {
        "alg": "ES256",
        "kid": kid,  # your own key ID
        "typ": "JWT"
    }
    # 2.1 Create the JWT payload
    payload = {
        "iss": iss,
        # 在Store Connect上可以点击复制 iss ID
        "exp": int(time.time()) + 60 * 10,
        # token最长有效时间20min，这里设置为10min
        "aud": "appstoreconnect-v1"
    }
    token = str(jwt.encode(payload=payload, key=privatekey, algorithm='ES256', headers=header), 'utf-8')
    return token


if __name__ == '__main__':
    # app.config.from_object(Config)
    app.run(port=8080, debug=True, host='0.0.0.0')
