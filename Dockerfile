FROM python:3.10-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY api/ api/
COPY data/ data/
COPY model/ model/
EXPOSE 5000
CMD ["python","api/app.py"]
