FROM python:3.9

WORKDIR /app

COPY requirements.txt requirements.txt

RUN apt-get update && apt-get install -y

RUN /usr/local/bin/python -m pip install --upgrade pip

RUN pip3 install -r requirements.txt --user

COPY . .

CMD ["python3", "-u", "lob_consumer.py"]


