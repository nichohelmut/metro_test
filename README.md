<h3 align="center">Data Engineer - Coding Exercise Task</h3>


Steps to fulfil
* Deploy a trained model in a containerized application (e.g. using TF Server).
* Write a Python application that exposes one or several APIs, which consume and then serve
predictions from the served model.
* You can use the Python framework of your choice to build the API.
* Your application should be fully tested with unit and integration tests. You can use
the test framework of your choice.
* Your application should be containerized.
* To submit:
 Public git repository with deployment instructions

Bonus
* You provide Kubernetes manifests which would cover the deployment of the entire applications.
* You write system tests which demonstrate the performance of your application under load.


```
git clone https://github.com/nichohelmut/metro_test.git
```

```
docker build -t mpg-prediction-total -f Dockerfile . --progress=plain
```

```
docker run -p 80:80 mpg-prediction-total:latest
```

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
  "Europe": 1,
  "Japan": 0,                                
```