test:
	python todo/manage.py test functional_tests 

migrate:
	python todo/manage.py makemigrations todo lists
	python todo/manage.py migrate

clean:
	find . -name "*.pyc" -exec rm -rf {} \;
	find . -name "*.swp" -exec rm -rf {} \;
	find . -name ".DS_Store" -exec rm -rf {} \;
