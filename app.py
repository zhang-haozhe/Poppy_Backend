from flask import Flask, request
from modules.image_processor import img_pipeline
import base64

app = Flask(__name__)


@app.route('/', methods=['POST', 'GET'])
def index():
    
    if request.method == 'POST':
        img_data = request.form['img_string']

        with open("imageToSave.png", "wb") as fh:
            fh.write(base64.b64decode(img_data))
        return "file received"
    else:
        return "Hello World"


if __name__ == "__main__":
    app.run(debug=True, port=5000)
