test:
	python todo/manage.py test todo

migrate:
	python todo/manage.py makemigrations todo 
	python todo/manage.py migrate

clean:
	find . -name "*.pyc" -exec rm -rf {} \;
	find . -name "*.swp" -exec rm -rf {} \;
	find . -name ".DS_Store" -exec rm -rf {} \;
