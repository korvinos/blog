sudo rm /etc/nginx/sites-enabled/default
sudo rm /etc/nginx/sites-avilable/default
sudo ln -sf /home/korvinos/Documents/blog/etc/nginx.conf  /etc/nginx/sites-enabled/test.conf
sudo /etc/init.d/nginx restart
sudo ln -sf /home/korvinos/Documents/blog/etc/gunicorn_blog.conf  /etc/gunicorn.d/blog
sudo /etc/init.d/gunicorn restart

