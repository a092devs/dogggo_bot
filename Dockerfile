FROM ubuntu:18.04

COPY requirements.txt
RUN pip3 install --no-cache-dir -r requirements.txt
CMD python3 main.py
