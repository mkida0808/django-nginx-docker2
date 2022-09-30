FROM ubuntu:20.04

ENV TZ=Asia/Tokyo
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

# Install required packages and remove the apt packages cache when done.

RUN apt-get -y update && apt-get install -y \
    git \
    python3 \
    python3-dev \
    python3-setuptools \
    python3-pip \
    nginx \
    supervisor \
    sqlite3 \
    libpq-dev \
  && rm -rf /var/lib/apt/lists/*

RUN pip3 install --upgrade pip setuptools

# install uwsgi now because it takes a little while
RUN pip3 install uwsgi

# setup all the configfiles
# daemon off = daemonをoffにする事で、foregroundで実行するようになる。daemonだとコンテナが停止してしまうため。
RUN echo "daemon off;" >> /etc/nginx/nginx.conf

# nginx-app.confをコピーしてコンテナに配置する。
COPY nginx-app.conf /etc/nginx/sites-available/default

COPY nginx.conf /etc/nginx

# supervisor-app.conf をコピーしてコンテナに配置する。
COPY supervisor-app.conf /etc/supervisor/conf.d/

# COPY requirements.txt and RUN pip install BEFORE adding the rest of your code, this will cause Docker's caching mechanism
# to prevent re-installinig (all your) dependencies when you made a change a line or two in your app. 
# 先にrequirements.txtだけコピーして、pip installする。

COPY requirements.txt /home/docker/code/app/
RUN pip3 install -r /home/docker/code/app/requirements.txt

# add (the rest of) our code
COPY . /home/docker/code/

RUN chmod 755 /home/docker/code/docker-entrypoint.sh

# install django, normally you would remove this step because your project would already
# be installed in the code/app/ directory
# RUN django-admin.py startproject website /home/docker/code/app/

COPY uwsgi_params /home/docker/code/app/

# RUN python3 /home/docker/code/app/manage.py migrate
# RUN python3 /home/docker/code/app/manage.py collectstatic --noinput

WORKDIR /home/docker/code

# コンテナの80portを解放
EXPOSE 80

# supervisord -n のオプションは、foregroundで実行するオプションなので、すごく重要！
CMD ["supervisord", "-n"]