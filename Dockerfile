FROM python:3.11

WORKDIR /code

COPY ./requiriments.txt /code/requiriments.txt

RUN pip install --no-cache-dir --upgrade -r /code/requiriments.txt

COPY . /code

CMD ["python3 main.py"]