FROM python:3.12-slim
WORKDIR /app
COPY requerimientos.txt .
RUN pip install -r requerimientos.txt
COPY . .
RUN cd /app
EXPOSE 8000
CMD [ "python","manage.py","runserver", "0.0.0.0:8000" ]    