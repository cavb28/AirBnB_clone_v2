#!/usr/bin/env bash
# Web servers preparation script
apt-get -y update
apt-get -y install nginx
mkdir -p /data/web_static/releases/test/
mkdir -p /data/web_static/shared/

touch /data/web_static/releases/test/index.html
echo "<html>
  <head>
  </head>
  <body>
    Hello Holberton School!
  </body>
</html>" > /data/web_static/releases/test/index.html
ln -sf /data/web_static/releases/test /data/web_static/current
chown -R ubuntu:ubuntu /data/
sed -i "/^\tlocation \/ {$/ i\\\tlocation /hbnb_static {\n\t\talias /data/web_static/current/;\n\t\tautoindex off;\n}" /etc/nginx/sites-available/default
service nginx restart
