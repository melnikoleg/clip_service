FROM tiangolo/uvicorn-gunicorn-fastapi:python3.7

RUN apt-get update -y

# install dependencies
RUN pip install torch==1.6.0+cpu torchvision==0.7.0+cpu -f https://download.pytorch.org/whl/torch_stable.html --no-cache-dir
RUN pip install -r /app/requirements.txt --no-cache-dir

COPY ./app /app
