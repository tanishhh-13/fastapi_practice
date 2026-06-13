#base image
FROM python:3.14.5-slim
#workdir
WORKDIR /app
#copy reqirements and run
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
#copy other files
COPY . .
#port
EXPOSE 8000
#command
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]