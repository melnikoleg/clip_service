FROM tiangolo/uvicorn-gunicorn-fastapi:python3.7

RUN apt-get update -y

# install dependencies
RUN pip install -r /app/requirements.txt --no-cache-dir

COPY ./app /app
