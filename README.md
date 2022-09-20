<h2 align="center">Data Engineer - Coding Exercise Task</h3>

### Steps to fulfil

* Deploy a trained model in a containerized application (e.g. using TF Server).
* Write a Python application that exposes one or several APIs, which consume and then serve
  predictions from the served model.
* You can use the Python framework of your choice to build the API.
* Your application should be fully tested with unit and integration tests. You can use
  the test framework of your choice.
* Your application should be containerized.
* To submit:
  Public git repository with deployment instructions

### Bonus

* You provide Kubernetes manifests which would cover the deployment of the entire applications.
    * Was not fulfilled, will continue working on this
* You write system tests which demonstrate the performance of your application under load.
    * Was not fulfilled, will look into this

### Model Folder

A Regression model is trained with a deep neural network (DNN), which accepts multiple inputs. The model is saved within
model
directory in artifacts folder. Training the DNN model was not the focus of this exercise.

### App Folder

The FastAPI framework was chosen for building the Web API. In order to validate the input fields, pydentic and pytest 
are used.

The predict entry point provides two http requests which are get and post. The first (get) provides a text output with
a 200 as an OK http code to confirm the communication with the model. The second (post) is used to send the input to
the model and provide the prediction as an output.

### Dockerfile

The Dockerfile was build with two stage: model_iamge and app_runner.
With multi-stage builds, you use multiple FROM statements in your Dockerfile. Each FROM instruction can use a
different base, and each of them begins a new stage of the build.

In the model_image stage the DNN model is trained and saved within the model folder.
In the app_runner stage, the artifacts folder from the model_image stage was copied into the app folder. By only
copying the needed artifacts, we do not include unneeded files in the app folder.

1. Clone the repository

```
git clone https://github.com/nichohelmut/metro_test.git
```

2. Build the container

```
docker build -t mpg-prediction-total -f Dockerfile . --progress=plain
```

3. Run the container

```
docker run -p 80:80 mpg-prediction-total:latest
```

4. Enter the curl command in your CLI

```
curl -X 'POST' \
  'http://0.0.0.0:8080/predict/' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "Cylinders": 5,
  "Displacement": 100,
  "Horsepower": 100,
  "Weight": 2500,
  "Acceleration": 15,
  "Model_Year": 77,
  "Europe": 0,
  "Japan":0,
  "USA": 1
}'                           
```

Within the next weeks I will look into the Bonus tasks and implement them.