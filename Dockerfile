# We're using Alpine Edge
FROM ubuntu

#
# We have to uncomment Community repo for some packages
#


#
# Installing Packages
#
RUN apt install --no-cache=true --update \
    coreutils \
    bash \
    build-base \
    bzip2-dev \
    curl \
    figlet \
    gcc \
    g++ \
    git \
    aria2 \
    util-linux \
    libevent \
    jpeg-dev \
    libffi-dev \
    libpq \
    libwebp-dev \
    libxml2 \
    libxml2-dev \
    libxslt-dev \
    linux-headers \
    musl \
    neofetch \
    openssl-dev \
    postgresql \
    postgresql-client \
    postgresql-dev \
    openssl \
    pv \
    jq \
    wget \
    python3 \
    python3-dev \
    readline-dev \
    sqlite \
    ffmpeg \
    sqlite-dev \
    sudo \
    chromium \
    chromium-chromedriver \
    zlib-dev \
    jpeg \
    zip \
    php \
    freetype-dev

RUN python3 -m ensurepip \
    && pip3 install --upgrade pip setuptools \
    && pip3 install wheel \
    && rm -r /usr/lib/python*/ensurepip && \
    if [ ! -e /usr/bin/pip ]; then ln -s pip3 /usr/bin/pip ; fi && \
    if [[ ! -e /usr/bin/python ]]; then ln -sf /usr/bin/python3 /usr/bin/python; fi && \
    rm -r /root/.cache

#
# Clone repo and prepare working directory
#
RUN git clone -b master https://github.com/rizpedia/ProjectBish /home/projectbish/
RUN mkdir /home/projectbish/bin/
WORKDIR /home/projectbish/
#
# Install requirements
#
RUN pip install -r requirements.txt
#Init system
RUN rm /bin/sh && ln -s /bin/bash /bin/sh
CMD ["python","-m","userbot"]
