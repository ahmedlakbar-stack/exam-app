FROM python

WORKDIR /app

COPY . /app

RUN pip install flask

EXPOSE 8080

CMD ["python3", "exam_app.py"]
