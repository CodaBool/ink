FROM python:alpine3.18
COPY docker_requirements.txt requirements.txt
RUN pip3 install --no-cache-dir -r requirements.txt
COPY key.json .
COPY *.py .
CMD ["python", "app.py"]
# ENTRYPOINT ["tail", "-f", "/dev/null"]
