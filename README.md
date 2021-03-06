![Logo](https://soshace.com/wp-content/uploads/2021/01/1200-jpg.jpg)
# Django Project MRBIT Exchange
Django Project MRBIT Exchange is a challenge project with Django and Django Rest Framework. This project include:

- API Documentation (Swagger and Redoc)
- Custom Admin panel with Volt Template
- Manage Crypto
- Initial Crypto (BTC, ETH and LTC)
- Authentication System
- Trading System

## Requirements
This project supports on Windows and Linux, but not tested in MAC OS.

- [Python 3.8+](https://www.python.org/downloads/)
- [Django 3.1+](https://www.djangoproject.com/)
- [Django Rest Framework 3.13+](https://www.django-rest-framework.org/)
- [Django Rest Auth](https://django-rest-auth.readthedocs.io/en/latest/installation.html)
- [DRF Yasg](https://drf-yasg.readthedocs.io/en/stable/)
- [Django Admin Volt](https://pypi.org/project/django-admin-volt/)
- [Python Decouple](https://github.com/henriquebastos/python-decouple/)

## Quickstart
Using linux:

```bash
$ git clone https://github.com/ismaelbenjamim/desafio-exchange-criptomoedas
$ cd desafio-exchange-criptomoedas # open directory of project
$ python -m venv .venv # create your venv
$ source .venv/bin/activate # open your venv
$ pip install -r requirements.txt # install all requirements
$ cp config/.env .env # copy file of globals variables to root directory
$ python manage.py migrate
$ python manage.py runserver
```

Using Windows:

```bash
$ git clone https://github.com/ismaelbenjamim/desafio-exchange-criptomoedas
$ cd desafio-exchange-criptomoedas # open directory of project
$ python -m venv .venv # create your venv
$ \.venv\Scripts\activate # open your venv
$ pip install -r requirements.txt # install all requirements
$ copy config\.env .env # copy file of globals variables to root directory
$ python manage.py migrate
$ python manage.py runserver
```

## Documentation

This project is using Swagger and Redoc for API Documentation.

### APIs include:
```
http://127.0.0.1:8000/apis/crypto/currency # Get Cryptocurrency Rate in real time
http://127.0.0.1:8000/apis/trades/sell/ # User create trade
http://127.0.0.1:8000/apis/trades/buy/ # Buy crypto of user and confirm trade
http://127.0.0.1:8000/apis/wallet/user-wallet # Get actually balance crypto of user
http://127.0.0.1:8000/apis/wallet/user-balance # Get actually balance of user in USD
```

### Swagger url
```
http://127.0.0.1:8000/swagger/
```
![Swagger](https://i.imgur.com/AYyBEt3.png)

### Redoc url
```
http://127.0.0.1:8000/redoc/
```
![Redoc](https://i.imgur.com/ubxZneX.png)

## Admin Panel

- Manage the users: `http://127.0.0.1:8000/admin/users/user/`
- Insert money to user balance: `http://127.0.0.1:8000/admin/users/userwallet/`
- View the crypto wallet user: `http://127.0.0.1:8000/admin/cryptocurrencies/cryptowallet/`
- Manage the crypto available: `http://127.0.0.1:8000/admin/cryptocurrencies/crypto/`

## Thanks
I hope you liked it, thank you!
Best regards, 
Ismael Benjamim.