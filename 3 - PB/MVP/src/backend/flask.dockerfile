FROM python:3.12-slim

WORKDIR /app

COPY requirements.txt ./

ENV PYTHONDONTWRITEBYTECODE=1

RUN apt-get update --fix-missing && apt-get install -y --fix-missing build-essential

RUN pip install -r requirements.txt

COPY . .

EXPOSE 4000

CMD [ "flask", "run", "--host=0.0.0.0", "--port=4000"]