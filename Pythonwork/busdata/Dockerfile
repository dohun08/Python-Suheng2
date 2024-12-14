FROM python:3.12.3
WORKDIR /app
COPY main.py /app/main.py
COPY requirements.txt /app/requirements.txt
COPY traffic_data_20231231.csv /app/
RUN pip install --no-cache-dir -r requirements.txt
CMD ["uvicorn","main:app","--host","0.0.0.0", "--port", "8000" ]