FROM python:3.5

# Install uWSGI & flask
RUN pip install uwsgi && \
    pip install flask

# Standard set up Nginx
ENV NGINX_VERSION 1.9.11-1~jessie

# RUN wget -q http://nginx.org/keys/nginx_signing.key -O- | apt-key add - \
RUN apt-key adv --keyserver hkp://pgp.mit.edu:80 --recv-keys 573BFD6B3D8FBC641079A6ABABF5BD827BD9BF62 \
	&& echo "deb http://nginx.org/packages/mainline/debian/ jessie nginx" >> /etc/apt/sources.list \
	&& apt-get update \
	&& apt-get install -y ca-certificates nginx=${NGINX_VERSION} gettext-base \
	&& rm -rf /var/lib/apt/lists/*

# forward request and error logs to docker log collector
RUN ln -sf /dev/stdout /var/log/nginx/access.log \
	&& ln -sf /dev/stderr /var/log/nginx/error.log

# Make NGINX run on the foreground
RUN echo "daemon off;" >> /etc/nginx/nginx.conf

# Remove default configuration from Nginx
RUN rm /etc/nginx/conf.d/default.conf && rm /etc/nginx/nginx.conf

# nginx, uwsgi, and supervisord are all in separate folders
#   enabling their configs to be mounted as volumes
#   so they can be modified without rebuilding the container each time
COPY nginx/conf.d /etc/nginx/conf.d
COPY nginx/nginx-global.conf /etc/nginx/nginx.conf

# Copy uwsgi config (emporer and vassals)
COPY ./uwsgi /etc/uwsgi
# /etc/uwsgi/vassals will be monitored by uwsgi emperor

# Install Supervisord
RUN apt-get update && apt-get install -y supervisor \
&& rm -rf /var/lib/apt/lists/*

# Custom Supervisord config
COPY supervisord/conf.d /etc/supervisor/conf.d

COPY ./app /app

RUN pip install requests appdynamics==4.3.16.0
RUN mkdir /etc/appd
COPY ./ignore/appd.ini /etc/appd

RUN mkdir -p /tmp/appd/logs && chown -R nginx:nginx /tmp/appd && chmod -R g+ws /tmp/appd && setfacl -dRm g::rwX /tmp/appd

#RUN mkdir /app/log && chmod -R 777 /app/log
#RUN chown -R nginx /app  && chmod 777 /app/log
#RUN mkdir -p /tmp/appd/logs && chown -R nginx:nginx /tmp/appd && chmod -R g+ws /tmp/appd
#setfacl depends on underlying docker storage driver
#RUN setfacl -d -m u::rwX,g::rwX,o::rwX /tmp/appd/logs

WORKDIR /app

CMD ["/usr/bin/supervisord", "-c", "/etc/supervisor/conf.d/supervisord.conf"]
