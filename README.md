# How to get Django and React to work together

This repo follows the blog post on [how to setup django and react with minimal configuration](http://michaelgainyo.com/articles/how-to-get-django-and-reactjs-to-work-together/)

### How to use

I have broken the steps by branches so you can follow along.

In your working directory:

```
git clone https://github.com/marqetintl/django-react-boilerplate.git
```

Next, create a virtual environment called `env` and activate it with:

```
cd  django-react-boilerplate
python3 -m venv env
source env/bin/activate
```

Install dependencies:

```
pip3 install -r requirements.txt
cd client/
npm install
```

Build the project

```
npm run build
cd ..
./manage.py collectstatic
./manage.py collectbase
./manage.py runserver
```

Finally, open your browser and navigate to `http://127.0.0.1:8000/`.
