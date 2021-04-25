release: python backend/manage.py migrate
release: python backend/manage.py createadmin

web: sh -c 'cd ./backend/ && exec gunicorn --preload SABAR.wsgi --log-file -'
