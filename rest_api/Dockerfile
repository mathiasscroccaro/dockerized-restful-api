FROM python:3

COPY ./requirements.txt /requirements.txt
RUN pip install -r /requirements.txt

RUN mkdir /rest_api
COPY ./rest_api /rest_api
COPY ./run.py /rest_api

WORKDIR /rest_api

ENTRYPOINT [ "python3" ]
CMD [ "run.py" ]
