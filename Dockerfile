FROM python:3.7-alpine
RUN mkdir /app
RUN mkdir /app/static
RUN mkdir /app/templates
RUN pip install flask
COPY MainScore.py /app
COPY Score.txt /
ADD static /app/static
ADD templates /app/templates
CMD ["python", "/app/MainScore.py"]
