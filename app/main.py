import os
from PIL import Image, ImageOps
from flask import Flask, render_template, request, jsonify
import base64
import json
from io import BytesIO
import requests

# all ML stuff
import numpy as np
#import matplotlib.pyplot as plt
import tensorflow as tf
from tensorflow.keras.preprocessing.image import img_to_array, load_img

# initialize flask application
app = Flask(__name__)
HOST = '0.0.0.0'
PORT = 8080

''' 
to upload the model without Tensorflow Serving

model = tf.keras.models.load_model('static/handwriting_model_convnet')

'''

url = 'http://tensorflow-serving:8501/v1/models/img_classifier:predict'


def make_prediction(instances):
    '''
    Permits to interact with TensorFlow serving.
    '''
    
    data = json.dumps({"signature_name": "serving_default",
                      "instances": instances.tolist()})
    headers = {"content-type": "application/json"}
    json_response = requests.post(url, data=data, headers=headers)
    predictions = json.loads(json_response.text)['predictions']
    return predictions


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/predict', methods=['GET', 'POST'])
def predict():
    results = {"prediction": "Empty", "probability": {}}
    # Get data stream
    input = BytesIO(base64.urlsafe_b64decode(request.form['img']))
    # convert data to object PIL.Image.Image
    input_img = load_img(input, target_size=(28, 28), color_mode="grayscale")
    # invert black(originally 0) to whites (originally 255)
    invert_img = ImageOps.invert(input_img)
    y = img_to_array(invert_img)/255
    # the model requires input's dimensions = (1,28,28,1)
    y = np.expand_dims(y, axis=0)
    images = np.vstack([y])

    '''
    When the model is loading without tensorflow serving.

    classes = model.predict(images) 
    
    '''

    classes = make_prediction(images)
    results["prediction"] = str(np.argmax(classes))
    results["probability"] = float(np.max(classes)) * 100
    return json.dumps(results)


if __name__ == '__main__':
    app.run(host=HOST,
            debug=True,
            port=PORT)
