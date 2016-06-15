test:
<<<<<<< HEAD
	python todo/manage.py test functional_tests lists
=======
	python todo/manage.py test functional_tests 
>>>>>>> 29992ec37751d20f4777f5b92af303c2e2963830

migrate:
	python todo/manage.py makemigrations todo lists
	python todo/manage.py migrate

clean:
	find . -name "*.pyc" -exec rm -rf {} \;
	find . -name "*.swp" -exec rm -rf {} \;
	find . -name ".DS_Store" -exec rm -rf {} \;
