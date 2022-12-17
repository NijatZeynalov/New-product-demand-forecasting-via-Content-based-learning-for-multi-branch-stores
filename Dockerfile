FROM --platform=linux/x86_64 python:3.9-buster

RUN mkdir /code

WORKDIR /code

COPY requirements.txt .

RUN pip install --no-cache-dir catboost

RUN pip install uvicorn
RUN pip install -r requirements.txt

COPY . .
EXPOSE 8000

ENTRYPOINT ["uvicorn"]
CMD ["main:app","--host", "0.0.0.0"]