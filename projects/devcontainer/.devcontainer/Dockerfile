FROM ubuntu:21.10 
ENV HOME /home
ENV SPACE /workspaces/vscode_dev_env
RUN export DEBIAN_FRONTEND=noninteractive \
    && apt-get update \
    && apt-get -y install tree \
    git \
    unixodbc-dev \
    postgresql \
    libmagic-dev \
    libpq-dev \
    freetds-dev \
    dnsutils \
    wget \
    curl \
    zip \
    unzip \
    vim \
    gcc \
    g++ \
    && curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip" \
    && unzip awscliv2.zip \
    && ./aws/install \
    && rm /awscliv2.zip \
    # miniconda installation
    && mkdir -p ~/miniconda3 \
    && wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh -O ~/miniconda3/miniconda.sh \
    && bash ~/miniconda3/miniconda.sh -b -u -p ~/miniconda3 \
    && rm -rf ~/miniconda3/miniconda.sh \
WORKDIR $SPACE
COPY . $SPACE
# install fish
RUN apt-get install -y fish \
    && ~/miniconda3/bin/conda init \
    && ~/miniconda3/bin/conda init fish \
    && chsh -s usr/bin/fish
