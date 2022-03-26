FROM python:3.7-alpine
WORKDIR /app
RUN mkdir /app/static \ && mkdir /app/templates
ADD static ./static
ADD templates ./templates
COPY MainScore.py .
WORKDIR /
COPY Score.txt /
RUN pip install flask
CMD ["python", "/app/MainScore.py"]