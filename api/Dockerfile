FROM python:3.6
RUN mkdir /api
COPY . /api/
WORKDIR /api
RUN pip install -r requirements.txt
CMD python -u main.py
