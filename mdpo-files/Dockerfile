FROM python:3.12.4-slim
RUN apt update && \
  apt install -y git build-essential cmake wget autoconf pkg-config
WORKDIR /mdpo
COPY entrypoint.sh .
ENTRYPOINT ["./entrypoint.sh"]
