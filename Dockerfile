FROM python:alpine3.17
COPY requirements.txt .
RUN pip3 install --no-cache-dir -r requirements.txt
COPY key.json .
# COPY *.html .
COPY *.py .
CMD ["python", "app.py"]