#Setup

* `mkvirtualenv flask`
* Run all the pip install commands in requirements.txt
* Define you db in config.py
* Setup your models
* `python manage.py db init`
* `python manage.py db migrate`
* `python manage.py db upgrade`
* `python run.py`
* Setup your views




#Layout

    --project_name
        |--lib/
        |--migrations/
        |--tmp/
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
        |--config.py
        |--manage.py
        |--run.py
        |--requirements.txt
        |--README.md