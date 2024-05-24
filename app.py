from flask import Flask, render_template, jsonify
import requests

app = Flask(__name__)


AUTH_TOKEN = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzE2NjY1ODc3LCJpYXQiOjE3MTY1Nzk0NzcsImp0aSI6ImRhNTM0OTM3OGUxYzRjYWE5YzJiZWMwMDE5NjMwMjVmIiwidXNlcl9pZCI6MX0.UPQ8qkurGWJ7Xa3G2Iq6JycUpMLIZu2VT9HBO7xeH3Q"


# Função para obter dados dos atores da API
def fetch_actors():
    url = "https://sergiohscl.pythonanywhere.com/api/v1/actors/"
    headers = {
        'Authorization': f'Token {AUTH_TOKEN}'
    }
    response = requests.get(url, headers=headers, verify=False)

    if response.status_code == 200:
        print(response.content)
        return response.json()
    else:
        return []

@app.route('/')
def index():
    actors = fetch_actors()
    return render_template('index.html', actors=actors)


if __name__ == '__main__':
    app.run(debug=True)
