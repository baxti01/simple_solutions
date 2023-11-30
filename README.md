# Описание проекта
Проект имеет 3 вида реализации которые разделены по соответствующим веткам:
1. ветка - `session`. Demo - http://141.147.13.81:8090/admin/:
   - Реализация с помощью `stripe.checkout.Session`.
2. ветка - `main`. Demo http://141.147.13.81:8080/admin/:
   - Реализация с помощью `stripe.PaymentIntent`. 

## Выполненные задания 
### Из основных
- API с двумя методами - GET /buy/{id} и GET /item/{id} с использованием `stripe.checkout.Session`
- Залить решение на Github, описать запуск в Readme.md
### Из бонусных
- Запуск используя Docker
- Использование environment variables
- Просмотр Django Моделей в Django Admin панели
- Запуск приложения на удаленном сервере, доступном для тестирования
- Добавить поле Item.currency, создать 2 Stripe Keypair на две разные валюты и в зависимости от валюты выбранного товара предлагать оплату в соответствующей валюте

## Запуск проекта

Можно example.env переименовать в .env и использовать
настройки оттуда или делать как показано ниже.

---
#### Создаём .env файл и добавляем следующие настройки

- Настройки Django super user 
  - `DJANGO_SUPERUSER_USERNAME=`... (обязательное поле)
  - `DJANGO_SUPERUSER_EMAIL=`... (обязательное поле)
  - `DJANGO_SUPERUSER_PASSWORD=`... (обязательное поле)
- Настройки базы данных 
  - `POSTGRES_HOST=`... (поумолчанию 0.0.0.0)
  - `POSTGRES_PORT=`... (поумолчанию 5432)
  - `POSTGRES_DB=`... (обязательное поле)
  - `POSTGRES_USER=`... (обязательное поле)
  - `POSTGRES_PASSWORD=`... (обязательное поле)
- Настройки Stripe API Keys 
  - `STRIPE_SECRET_KEY=`... (обязательное поле)
  - `STRIPE_PUBLIC_KEY=`... (обязательное поле)

#### Запускаем проект на компьютере
Устанавливаем зависимости.
```
pip install -r requirements.txt
```
Создаём супер пользователя. (Это пользовательская команда)
```
python manage.py initsuperuser
```
И запускаем проект
```
python manage.py runserver
```

### Запускаем проект в docker.

```
docker-compose up
```

И пользуемся!

---