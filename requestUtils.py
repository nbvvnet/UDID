import requests, json

# post请求
def post(token, url, data):
    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer %s' %token,
    }
    return requests.post(url, headers=headers, data=json.dumps(data))