start: set_FLASK_APP set_FLASK_DEBUG
	@flask run --host=0.0.0.0 --port=9090

set_FLASK_APP:
	export FLASK_APP=/srv/app/webapp.py

set_FLASK_DEBUG:
	export FLASK_DEBUG=1

copy_nginx:
	@sudo cp nginx.conf /etc/nginx/sites-available/webapp && sudo ln -s /etc/nginx/sites-available/webapp /etc/nginx/sites-enabled/ && sudo systemctl restart nginx


# 192.168.43.159