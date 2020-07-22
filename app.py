from flask import Flask, request
from modules.image_processor import img_pipeline

app = Flask(__name__)


@app.route('/', methods=['POST', 'GET'])
def index():
    
    if request.method == 'POST':
        # img_pipeline()
        data = request.get_json()
        return data['hello']
    else:
        return "Hello World"


if __name__ == "__main__":
    app.run(debug=True, port=5000)
