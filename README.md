#Setup

* `mkvirtualenv flask`
* Run all the pip install commands in requirements.txt
* Define your db in db.txt
* Setup your models
* `python manage.py db init`
* `python manage.py db migrate`
* `python manage.py db upgrade`
* `python run.py`
* Setup your views
* change the AP_ENV in __init__.py and in app.wsgi
* adjust app.wsgi
* Add MONITOR_ID in default.py from flaskmonitor
* Adjust error_emailer.py for error emails (2 spots), then uncomment the section in __init__.py


#Layout

    --project_name
        |--lib/
        |--migrations/
        |--app/
            |--models.py
            |--forms.py
            |--views.py
            |--templates
               |--base.html
               |--index.html
            |--static
                |--style.css
                |--main.js
                |--images/
        |--configs
            |--db.txt
            |--prod.py
            |--default.py
        |--manage.py
        |--run.py
        |--requirements.txt
        |--README.md
        |--app.wsgi