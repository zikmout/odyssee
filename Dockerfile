FROM debian:jessie

MAINTAINER ziKmouT <ssicard@student.42.fr>

ENV DEBIAN_FRONTEND noninteractive

RUN apt-get update && apt-get install -y \
    #dialog \
    git \
    #libxml2-dev \
    python \
    build-essential \
    #make \
    #gcc \
    python-dev \
    locales \
    python-pip \
    nginx \
    openssh-server \
    supervisor \
    curl \
    wget \
    zsh

RUN dpkg-reconfigure locales && \
    locale-gen C.UTF-8 && \
    /usr/sbin/update-locale LANG=C.UTF-8

ENV LC_ALL C.UTF-8

ENV NAME toto

ADD index.html /var/www/html/index.html

RUN mkdir -p /var/log/supervisor
COPY supervisord.conf /etc/supervisor/conf.d/supervisord.conf

#--------------------------------SSH ROOT WITHOUT PASSWD-----------------------

RUN mkdir /var/run/sshd
RUN echo 'root:root' | chpasswd
RUN sed -i 's/PermitRootLogin without-password/PermitRootLogin yes/' /etc/ssh/sshd_config

# SSH login fix. Otherwise user is kicked off after login
RUN sed 's@session\s*required\s*pam_loginuid.so@session optional pam_loginuid.so@g' -i /etc/pam.d/sshd

ENV NOTVISIBLE "in users profile"
RUN echo "export VISIBLE=now" >> /etc/profile

#RUN echo "export SHELL=/bin/zsh" >> /etc/profile

#EXPOSE 22
#CMD ["/usr/sbin/sshd", "-D"]

#-----------------------------------------------------------------------------

RUN curl -fsSL https://raw.githubusercontent.com/robbyrussell/oh-my-zsh/master/tools/install.sh | bash

EXPOSE 80 22

CMD ["/usr/bin/supervisord"]
