FROM python:3.11
WORKDIR /app
COPY . .
RUN pip install fastapi uvicorn numpy
CMD ["uvicorn", "core.api.rest.main:app", "--host", "0.0.0.0", "--port", "8000"]
