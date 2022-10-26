FROM python:3.10.0-alpine

WORKDIR /usr/src/app

ADD requirements.txt .

RUN pip install --trusted-host pypi.python.org -r requirements.txt

CMD [ "uvicorn", "main:app", "--reload", "--host", "0.0.0.0", "--port", "8000"]