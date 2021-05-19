# Invest blog

Web-app representing an investment blog.

App consists of 5 models: Author, Article, Category, Comment, Tag. Users of
the app can be authors of articles, and they can also write comments. Every article 
belongs to a certain category. Every article could have several tags. The main page 
show the list of all posts divided by categories in its main section. In the side section
there is a list of all tags with the count of articles that have them linked.

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

## Launch

1. Make migrations
```console
python3 manage.py migrate
```

2. Run server
```console
python3 manage.py runserver
```