#/bin/bash
uwsgi --ini uwsgi.ini & >> $PWD"/log/uwsgi.log"
