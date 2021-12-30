# Define function directory
ARG FUNCTION_DIR="/function"

FROM python:buster as build-image

# Install aws-lambda-cpp build dependencies
RUN apt-get update && export DEBIAN_FRONTEND=noninteractive

RUN apt-get install -y g++ make cmake unzip libcurl4-openssl-dev

# Include global arg in this stage of the build
ARG FUNCTION_DIR
# Create function directory
RUN mkdir -p ${FUNCTION_DIR}
# Copy function code
COPY app.py ${FUNCTION_DIR}

# Install the runtime interface client
RUN pip install \
    --target ${FUNCTION_DIR} \
    awslambdaric

# Multi-stage build: grab a fresh copy of the base image
FROM python:buster

# Include global arg in this stage of the build
ARG FUNCTION_DIR
# Set working directory to function root directory
WORKDIR ${FUNCTION_DIR}

# Copy setup & other temporary files
COPY *.sh requirements.txt /tmp/
COPY GoFullPage.crx /opt/
RUN pip install --upgrade pip -q
RUN pip install -r /tmp/requirements.txt -q
RUN /bin/bash /tmp/install_chrome.sh
RUN /bin/bash /tmp/install_driver.sh
RUN apt-get install xvfb python3-tk python3-dev -y

# Copy in the build image dependencies
COPY --from=build-image ${FUNCTION_DIR} ${FUNCTION_DIR}
RUN ls -al /opt
ENTRYPOINT [ "/usr/local/bin/python", "-m", "awslambdaric" ]
CMD [ "app.handler" ]
