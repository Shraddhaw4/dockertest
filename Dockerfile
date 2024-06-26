FROM python:3-alpine3.15
RUN mkdir /app
WORKDIR /app
COPY . /app
RUN pip install -r requirements.txt
EXPOSE 3000
CMD ["python", "app.py"]
