run this:

# git clone https://github.com/nichohelmut/metro_test.git

# docker build -t mpg-prediction-app -f app/Dockerfile app/
# docker run -p 80:80 mpg-prediction-app:latest

# curl -X 'POST' \
#   'http://0.0.0.0/predict/' \
#   -H 'accept: application/json' \
#   -H 'Content-Type: application/json' \
#   -d '{
#   "Cylinders": 5,
#   "Displacement": 100,
#   "Horsepower": 100,
#   "Weight": 2500,
#   "Acceleration": 15,
#   "Model_Year": 77,
#   "Europe": 1,
#   "Japan": 0,
#   "USA": 0
# }'
