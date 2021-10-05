FROM python:3.9

WORKDIR /app

COPY . /app

RUN python3 -m pip install -r requirements.txt

EXPOSE 80

CMD ["streamlit", "run", "app.py", "--server.port", "80"]