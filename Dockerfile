FROM python:3.7-alpine
RUN mkdir /app
RUN pip install flask
COPY MainScore.py /app
COPY Score.txt /Score.txt
CMD ["python", "/app/MainScore.py"]