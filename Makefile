migrate:
	docker-compose exec mhnu ./manage.py makemigrations
	docker-compose exec mhnu ./manage.py migrate

requirements:
	docker-compose exec mhnu pip install -r requirements.txt

statics:
	docker-compose exec mhnu ./manage.py collectstatic --no-input

superuser:
	docker-compose exec mhnu ./manage.py createsuperuser

app:
	docker-compose exec mhnu ./manage.py startapp $(APP_NAME)

logs:
	docker-compose logs -f -t --tail=$(lines) $(service)

mergemigrations:
	docker-compose exec mhnu ./manage.py makemigrations --merge

test:
	docker-compose exec mhnu ./manage.py test

makemessages:
	docker-compose exec mhnu ./manage.py makemessages -l es
	# docker-compose exec mhnu ./manage.py makemessages -l en

compilemessages:
	docker-compose exec mhnu ./manage.py compilemessages -f

flake:
	docker-compose exec mhnu flake8

reset:
	docker-compose down -v

clean:
	rm -rf src/*/migrations/00**.py
	find . -name "*.pyc" -exec rm -- {} +
	rm -rf src/*/migrations/__pycache__/*

FILENAME=mhnu
USER=mhnu-user
DATABASE=mhnu-db
backup:
	docker-compose exec db sh -c "pg_dump -U $(USER) -Fc -x -O $(DATABASE) > /docker-entrypoint-initdb.d/dumps/$(FILENAME).dump"