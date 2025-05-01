FROM python:3.12-slim
WORKDIR /app
COPY ApiRegProv /app/
COPY requerimientos.txt /app/
RUN pip install -r /app/requerimientos.txt
RUN cd /app/ApiRegProv
EXPOSE 8000
CMD [ "python","manage.py","runserver", "0.0.0.0:8000" ]