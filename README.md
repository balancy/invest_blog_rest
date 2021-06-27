# Invest blog

![App image](https://i.ibb.co/Ch6mxJ0/111.png)

Приложение представляет pet-project для изучения принципов авторизации в Django Rest Framework по JWT токену.

В приложении есть 7 моделей: Преподаватель, Ученик, Категория, Курс,
Занятие, Расписание, Тэг. Каждый курс принадлежит к категории, и имеет 
определенное количество занятий. У курса есть ответственный за него 
преподаватель, у занятий есть их кураторы. Каждое занятие имеет определенные 
тэги. Модель расписание связывает учеников с определенными занятиями на 
определенное время.

Пользователь, который не является администратором ресурса, может просматривать список преподавателей, уроков, курсов и категорий курсов.
Пользователь с правами администратора может изменять данные посредством JWT токена с помощью удобного для него http клиента (например, postman).
Для получения или обновления токена нужно обращаться по адресу `/api/token` и `/api/token/refresh/` соответственно.
Для изменения данных с праваи администратора нужно делать запросы методом POST в соответствующие ветки с предоставлением актуального токена.

## Install

Python3 and Git should be already installed. 

1. Clone the repository by command:
```console
git clone https://github.com/balancy/invest-blog
```

2. Go inside cloned repository and create virtual environment by command:
```console
python -m venv env
```

3. Activate virtual environment. For linux-based OS:
```console
source env/bin/activate
```
&nbsp;&nbsp;&nbsp;
For Windows:
```console
env\scripts\activate
```

4. Install requirements by command:
```console
pip install -r requirements.txt
```

5. Rename `.env.example` to `.env` and define your propre values for environmental variables:

- `DEBUG` — debug mode
- `SECRET_KEY` — project django secret key
- `ALLOWED_HOSTS` — see [Django documentation](https://docs.djangoproject.com/en/3.1/ref/settings/#allowed-hosts)
- `EMAIL_HOST` = project email host (for sending emails)
- `EMAIL_PORT` = project email port
- `EMAIL_HOST_USER` = project admin email
- `EMAIL_HOST_PASSWORD` = project admin email password
- `EMAIL_USE_SSL` = does project use SSL?

## Launch

1. Make migrations
```console
python3 manage.py migrate
```

2. Run server
```console
python3 manage.py runserver
```

3. Launch redis server and queue workers (for sending emails)

They don't work in Windows, so if you have one, you need to launch them in 
   emulated unix-OS (wsl or emulated ubuntu)

Launch server in one terminal
```console
redis-server
```

Launch workers in another terminal
```console
celery -A invest_blog worker -l INFO
```