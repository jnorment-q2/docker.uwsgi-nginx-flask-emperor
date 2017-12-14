
Run init-repo.sh to initialize repo.

     docker.uwsgi-nginx-flask-emperor]$ ./init-repo.sh

This mainly creates the appd.ini file that will be needed when building the container. The file it creates will need to be updated with live configuration. This file is configured to be ignored by git.


