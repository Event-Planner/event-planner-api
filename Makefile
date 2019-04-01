setup:
	- virtualenv -p python3.7 venv; \
	. venv/bin/activate; \
	pip install -r requirements.txt

update:
	- . venv/bin/activate; \
	pip install -r requirements.txt

test:
	- . local.env; \
	. venv/bin/activate; \
	./manage.py test --noinput
