from flask import render_template, jsonify, redirect, url_for, request

from app import app
import random
from app.forms import user as user_forms
from werkzeug import secure_filename

@app.route('/', methods=["GET", "POST"])
@app.route('/index', methods=["GET", "POST"])
@app.route('/create', methods=["GET", "POST"])
def index():
    form = user_forms.Create()
    if form.validate_on_submit():
        text = request.form['text']
        filename = secure_filename(form.file.data.filename)
        # form.file.data.save('uploads/' + filename)
        print(filename)
        print(text)
        return redirect(url_for('index'))
    return render_template('index.html', title='Home', form=form)


@app.route('/map')
def map():
    return render_template('map.html', title='Map')

@app.route('/map/refresh', methods=['POST'])
def map_refresh():
    points = [(random.uniform(48.8434100, 48.8634100),
               random.uniform(2.3388000, 2.3588000))
              for _ in range(random.randint(2, 9))]
    return jsonify({'points': points})


@app.route('/contact')
def contact():
    return render_template('contact.html', title='Contact')
