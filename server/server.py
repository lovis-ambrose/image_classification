from flask import Flask, render_template, request, jsonify
import util

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('app.html')

@app.route('/classify_image', methods=['POST'])
def classify_image():
    image_data = request.form['image_data']
    response = jsonify(util.classify_image(image_data))
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

if __name__ == '__main__':
    # Run the Flask app on localhost and port 4000
    print("Starting Python Flask Server For Tech Celebrity Image Classification")
    util.load_saved_artifacts()
    app.run(host='localhost', port=4000)
