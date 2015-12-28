#Makefile

clean:
	rm -rf *~* && find . -name '*.pyc' -exec rm {} \;
	
heroku:
	pip install django-toolbelt
	heroku login
	heroku create
	git add .
	git commit -m "despliegue en heroku"
	git push heroku master
	heroku ps:scale web=1
	heroku open
