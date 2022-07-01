FROM public.ecr.aws/lambda/python:3.9 as stage

# Hack to install chromium dependencies
RUN yum install -y -q sudo unzip

# Find the version of latest stable build of chromium from below
# https://omahaproxy.appspot.com/
# Then follow the instructions here in below URL to download old builds of Chrome/Chromium that are stable
# Current stable version of Chromium
ENV CHROMIUM_VERSION=1002910 


# Install Chromium
COPY install-browser.sh /tmp/
RUN /usr/bin/bash /tmp/install-browser.sh

FROM public.ecr.aws/lambda/python:3.9 as base

COPY chrome-deps.txt /tmp/
RUN yum install -y $(cat /tmp/chrome-deps.txt)
RUN yum install -y xorg-x11-server-Xvfb.x86_64 xorg-x11-xauth.x86_64 procps xdpyinfo python3-tkinter.x86_64 python3-devel.x86_64 sudo
#RUN yum search xauth
# Install Python dependencies for function
COPY requirements.txt /tmp/
RUN python3 -m pip install --upgrade pip -q
RUN python3 -m pip install -r /tmp/requirements.txt -q 

COPY GoFullPage.crx /opt/

COPY --from=stage /opt/chrome /opt/chrome
COPY --from=stage /opt/chromedriver /opt/chromedriver
COPY app.py ${LAMBDA_TASK_ROOT}

COPY entrypoint.sh /

CMD [ "app.handler" ]
ENTRYPOINT ["/entrypoint.sh"]
