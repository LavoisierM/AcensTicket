run:
	@python manage.py runserver

setup:
	@python manage.py makemigrations
	@python manage.py migrate 	
