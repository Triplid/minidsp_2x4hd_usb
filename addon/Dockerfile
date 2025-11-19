ARG BUILD_FROM=ghcr.io/hassio-addons/base-python:latest
FROM $BUILD_FROM

WORKDIR /usr/src/app

COPY rootfs/ / 
RUN pip install flask pyusb hidapi

CMD [ "/run.sh" ]
