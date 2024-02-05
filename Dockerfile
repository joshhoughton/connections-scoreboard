# syntax=docker/dockerfile:1

FROM python:3.11
COPY requirements.txt /app/
WORKDIR /app
RUN pip install -r requirements.txt
COPY . .

RUN chmod a+x run.sh
CMD ["./run.sh"]