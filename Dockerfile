FROM python:3.7.3

RUN echo "alias ll='ls -al --color=auto'" >> /root/.bashrc

RUN mkdir /code
WORKDIR /code
ADD . /code/

RUN pip3 install -r requirements.txt

#CMD [ "admin_panel/start_service.sh" ]

