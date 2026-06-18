from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return """
    <h1>🍕 Pizza Menu Chaos</h1>
    <h2>Team 1: Margherita</h2>
    <h2>Team 2: Farmhouse</h2>
    <h2>Team 3: Mexican</h2>
    """

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)