FROM ubuntu

ARG pass

RUN apt-get update
RUN apt-get upgrade -y
RUN apt-get install -y python python-pip python-dev && pip install --upgrade pip

RUN apt-get update -y && apt-get install git -y

RUN pip install pytest
RUN pip install requests

RUN git clone https://github.com/MaslovU/ApiTestsForMyrestAplic.git /ApiTestsForMyrestAplic

WORKDIR ./ApiTestsForMyrestAplic

CMD ["/bin/bash"]
