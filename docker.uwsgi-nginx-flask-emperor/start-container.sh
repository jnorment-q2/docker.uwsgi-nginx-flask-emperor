# logs are now accessible outside of docker container in ./logs
# and inside docker container at /tmp/appd/logs
rm logs/*
# sudo docker run -it -v `pwd`/logs:/tmp/appd/logs:z -p 80:80 testjae-appd:3
# can also curl port 80 outside of container
# sudo docker run -it -v `pwd`/logs:/tmp/appd/logs:z -v `pwd`/supervisord:/etc/supervisor:z -v `pwd`/nginx/conf.d:/etc/nginx/conf.d:z -v `pwd`/uwsgi:/etc/uwsgi:z -p 80:80 testjae-appd:3 bash
echo run this: /usr/bin/supervisord -c /etc/supervisor/conf.d/supervisord.conf
sudo docker run -it -v `pwd`/logs:/tmp/appd/logs:z -v `pwd`/supervisord/conf.d:/etc/supervisor/conf.d:z -v `pwd`/nginx/conf.d:/etc/nginx/conf.d:z -v `pwd`/uwsgi:/etc/uwsgi:z -v `pwd`/app:/app:z -p 80:80 testjae-appd:3 bash


