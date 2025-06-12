# Usamos Python 3.11
FROM python:3.11-slim

WORKDIR /app

# Copiamos dependencias y las instalamos
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt


# Copiamos los archivos de la app refactorizada
COPY app.py .
COPY routes.py .


# Exponemos el puerto que usarás en Azure Container Apps
EXPOSE 8000

# Comando de arranque (usando la nueva estructura)
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]
