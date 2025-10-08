FROM python:3.12-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY app.py .
ENV SALUDO="Hola desde la imagen"
EXPOSE 5000
HEALTHCHECK CMD curl -f http://localhost:5000 || exit 1
CMD ["python", "app.py"]
