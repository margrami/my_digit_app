# My Digit App

This web app performs handwriting digit recognition using a ConvNET model. 

In the first version of this app, the TF model was loaded at the beginning of the main.py file, using the function load_model (see the code). 

This version uses Tensorflow serving to load the model and perform the prediction. This offers several advantages as mode efficient model inference.

Used in bootcamp #2.

# TensorFlow Serving with Docker

The easiest way is running TF Serving in a docker container. Once the docker desktop is running, pull this image:

```bash
docker pull tensorflow/serving
```

(to use with CPU only)

# Start TensorFlow Serving container and open the REST API port

This is the command to start TF Serving if as me, your are using a windows version of docker:

```bash
docker run -p 8501:8501 --name tfserv_two --mount type=bind,source=$(PWD)/static/handwriting_model_convnet/,target=/models/img_classifier -e TF_CPP_VMODULE=http_server=1 -e  MODEL_NAME=img_classifier -t tensorflow/serving

```

Some info about the command's options:
- TF_CPP_VMODULE=http_server=1             , is to activate the logs.

- target=/models/img_classifier            ,is the model's directory in docker. 

- --name tfserv_two                        ,it's better to include a name in order to identifier the container. 

Once the container TFserv_two is up, my_digit_app can make REST requests. 

# To run the app 

```bash
python main.py

```
and then follow the link to open the web app. 

# other useful info:
https://github.com/tensorflow/serving/blob/master/tensorflow_serving/g3doc/building_with_docker.md
