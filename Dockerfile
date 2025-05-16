FROM python:3.12-slim

# Instalar dependencias del sistema
RUN apt-get update && \
    apt-get install -y \
        pkg-config \
        default-libmysqlclient-dev \
        gcc && \
    rm -rf /var/lib/apt/lists/*

WORKDIR /app

# Instalar dependencias
COPY requerimientos.txt .
RUN pip install --upgrade pip && \
    pip install -r requerimientos.txt gunicorn

# Copiar el proyecto
COPY . .

# Variables de entorno
ENV PYTHONUNBUFFERED=1
ENV DJANGO_SETTINGS_MODULE=APIREGPROV.config.settings

# Puerto
EXPOSE 8000

# Comando para producción (¡AQUÍ ESTÁ EL CAMBIO CLAVE!)
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "--workers", "3", "APIREGPROV.config.wsgi:application"]