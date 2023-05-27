
FROM python:3.9
RUN mkdir /sirelab
WORKDIR /sirelab
COPY requirements.txt .
RUN pip install psycopg2
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
EXPOSE 8000
