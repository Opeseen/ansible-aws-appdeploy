from flask import Blueprint, render_template, flash;
from .models import Record;

views = Blueprint('views',__name__)

@views.route('/')
def home():
    return render_template('home.html')


@views.route('/dashboard')
def dashboard():
    try:
        record = Record.query.all()
        return render_template('dashboard.html', data=record)
    except:
        flash('There was an error while loading your note...',category='error')

    return render_template('dashboard.html')

@views.route('/enter-note-id')
def noteid():
    return render_template('note_id.html')

