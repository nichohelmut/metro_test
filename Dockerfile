# Dockerfile with multiple stages

# trains ml model
FROM python:3.9-slim as model_image
WORKDIR /model
COPY ./model/* .
RUN pip3 install --quiet --no-cache-dir -r requirements.txt

RUN python3 main.py

FROM python:3.9-slim as app_runner
WORKDIR /app
COPY app/requirements.txt .
RUN pip3 install --quiet --no-cache-dir -r requirements.txt
COPY app .

RUN mkdir -p artifacts
# copies artifacts from previous stage
COPY --from=model_image /model/* ./artifacts
# runs tests
RUN pytest

CMD ["uvicorn", "api:app", "--host", "0.0.0.0", "--port", "80"]
