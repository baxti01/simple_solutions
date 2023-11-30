FROM python:3.11.0

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY requirements.txt app/

WORKDIR app/

RUN pip3 install --upgrade pip && pip3 install -r requirements.txt

COPY . .

RUN chmod +x server_run.sh && chmod +x wait-for-it.sh