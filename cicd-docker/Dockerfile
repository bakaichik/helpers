FROM ubuntu:22.04

# Install prerequisites
RUN apt update && apt install -y \
    gnupg software-properties-common jq curl zip unzip ca-certificates build-essential wget libffi-dev libssl-dev zlib1g-dev libbz2-dev libreadline-dev libsqlite3-dev

# Download and build Python 3.12.4 from source
RUN cd /usr/src && \
    wget https://www.python.org/ftp/python/3.12.4/Python-3.12.4.tgz && \
    tar xzf Python-3.12.4.tgz && \
    cd Python-3.12.4 && \
    ./configure --enable-optimizations && \
    make -j$(nproc) && \
    make altinstall && \
    ln -s /usr/local/bin/python3.12 /usr/bin/python3 && \
    ln -s /usr/local/bin/pip3.12 /usr/bin/pip3

# Clean up build files
RUN rm -rf /usr/src/Python-3.12.4* && apt clean

# Verify installation
RUN python3 --version && pip3 --version
