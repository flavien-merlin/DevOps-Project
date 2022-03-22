FROM python:3.7-alpine
RUN bash -c "mkdir -p /app/{static,templates}" \
    pip install flask
COPY MainScore.py /app \
     Score.txt /
ADD static /app/static \
    templates /app/templates
CMD ["python", "/app/MainScore.py"]
