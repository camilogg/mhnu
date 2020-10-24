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
	docker-compose exec mhnu ./manage.py makemessages -l en

compilemessages:
	docker-compose exec mhnu ./manage.py compilemessages -f
