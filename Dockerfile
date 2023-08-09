FROM python:3.10

WORKDIR /pyimgs

ENV PORT=32251
ENV SECRET_KEY=default
COPY . .
RUN pip install -r /pyimgs/requirements.txt

CMD ["python", "server/main.py"]
