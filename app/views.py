from flask import render_template, flash
from app import app


@app.route('/', methods=['GET'])
def index():
    return render_template('index.html', title='Index')


def flash_errors(form):
    for field, errors in form.errors.items():
        for error in errors:
            flash(u"Error in the %s field - %s" % (
                getattr(form, field).label.text,
                error
            ))
