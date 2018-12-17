start:
	@flask run --host=0.0.0.0 --port=9090

copy_nginx:
	@sudo cp nginx.conf /etc/nginx/sites-available/webapp && sudo ln -s /etc/nginx/sites-available/webapp /etc/nginx/sites-enabled/ && sudo systemctl restart nginx