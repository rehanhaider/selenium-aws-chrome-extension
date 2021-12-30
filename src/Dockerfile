# Define function directory
ARG FUNCTION_DIR="/function"
ARG RUNTIME_VERSION="3.9"


FROM ubuntu:latest as base-image

RUN apt-get update && DEBIAN_FRONTEND=noninteractive TZ=Etc/UTC
RUN apt-get install -y g++ make cmake unzip libcurl4-openssl-dev
RUN apt-get install -y python3 python3-pip 
RUN apt-get install xvfb python3-tk python3-dev -y
RUN apt-get install curl wget -y

ARG FUNCTION_DIR
# Create function directory
RUN mkdir -p ${FUNCTION_DIR}
# Copy function code


RUN pip install \
    --target ${FUNCTION_DIR} \
    awslambdaric

# Include global arg in this stage of the build
ARG FUNCTION_DIR
# Set working directory to function root directory
WORKDIR ${FUNCTION_DIR}

# Copy setup & other temporary files
COPY requirements.txt /tmp/
#COPY GoFullPage.crx /opt/
RUN pip install --upgrade pip -q
RUN pip install -r /tmp/requirements.txt -q
COPY install_chrome.sh /tmp/
RUN /bin/bash /tmp/install_chrome.sh
COPY install_driver.sh /tmp/
RUN /bin/bash /tmp/install_driver.sh
COPY install_chromium.sh /tmp/
RUN /bin/bash /tmp/install_chromium.sh
COPY app.py ${FUNCTION_DIR}
RUN ls -al /opt/chrome/stable/

ENTRYPOINT [ "python3", "-m", "awslambdaric" ]
CMD [ "app.handler" ]

