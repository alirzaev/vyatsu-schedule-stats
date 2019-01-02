FROM python:3.6-alpine
EXPOSE 80

WORKDIR /usr/src/project

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["python", "server.py"]
