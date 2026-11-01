FROM python:3.14-slim
RUN apt update && \
  apt install -y build-essential cmake wget pkg-config patchelf rustc cargo
WORKDIR /mdpo
COPY entrypoint.sh .
ENTRYPOINT ["./entrypoint.sh"]
