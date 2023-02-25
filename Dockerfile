FROM python:3.9
RUN pip3 install -U pip setuptools wheel

EXPOSE 8080

WORKDIR /app

COPY ./requirements.txt /app/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt

COPY ./app/ /app

CMD python main.py --reload

