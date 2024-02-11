FROM python:3.11.2

ADD main.py .

COPY requirements.txt .

RUN pip install -r requirements.txt

CMD [ "python", "main.py" ]