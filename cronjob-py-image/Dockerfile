FROM python:3.8-slim
WORKDIR /app
COPY requirements.txt /app
COPY connect_db.py /app
RUN pip install -r requirements.txt
CMD python connect_db.py