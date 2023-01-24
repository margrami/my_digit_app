My Digit App, performs handwriting digit recognition. 
In the first version of this app, the TF model was loaded at the beginning of the main.py using the function load_model (see the code). This version uses Tensorflow serving to load the model and perform the prediction.

TensorFlow Serving with Docker

- This is the easiest way. it just needs to pull the image as:

docker pull tensorflow/serving 
(to use with CPU only)

- Start TensorFlow Serving container and open the REST API port

This is the command to start TF Serving if as me your are using a windows version of docker:

docker run -p 8501:8501 --name tfserv_two --mount type=bind,source=$(PWD)/static/handwriting_model_convnet/,target=/models/img_classifier -e TF_CPP_VMODULE=http_server=1 -e  MODEL_NAME=img_classifier -t tensorflow/serving

the command :
TF_CPP_VMODULE=http_server=1 is to activate the logs.

Once the container TFserv_two is up  my_digit_app can make REST requests. 
to run the app 

python main.py