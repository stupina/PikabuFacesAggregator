FROM python:3.6
RUN mkdir /parser
COPY . /parser/
WORKDIR /parser
RUN pip install -r requirements.txt
CMD python -u main.py
