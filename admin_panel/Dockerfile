FROM python:3.7.3

RUN echo "alias ll='ls -al --color=auto'" >> /root/.bashrc

WORKDIR /code
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

CMD [ "./start_service.sh" ]

