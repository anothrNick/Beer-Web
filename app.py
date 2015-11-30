import os
from flask import Flask, redirect, request, render_template, url_for, jsonify, g
from model import *
from forms import *
from werkzeug.utils import secure_filename
#from flask_peewee.rest import RestAPI
import json
#from bson import json_util
from playhouse.shortcuts import *

app = Flask(__name__)
app.secret_key = 'asdopiasdijnnrnkjasdkjlkbababooey'
app.config['IMAGES'] = 'static/upload/images/'

ALLOWED_IMAGES = set(['png', 'jpg', 'jpeg'])

#api = RestAPI(app)

#api.register(BeerStyle)

#api.setup()


def allowed_image(filename):
    return '.' in filename and filename.rsplit('.', 1)[1] in ALLOWED_IMAGES


@app.route('/api/beer', methods=['GET'])
def _api_beers():
    beers = Beer.select()
    json_beers = [model_to_dict(beer) for beer in beers]
   
    return json.dumps(json_beers, sort_keys=True, indent=4, separators=(',',': '))


@app.route('/api/brewery', methods=['GET'])
def _api_brewery():
    brews = Brewery.select()
    json_brews = [model_to_dict(brew) for brew in brews]
    
    return json.dumps(json_brews, sort_keys=True, indent=4, separators=(',',': '))


@app.route('/api/beer/styles', methods=['GET'])
def _api_styles():
    styles = BeerStyle.select()
    json_styles = [model_to_dict(style) for style in styles]

    return json.dumps(json_styles, sort_keys=True, indent=4, separators=(',',': '))


@app.route('/', methods=['GET', 'POST'])
def index():
    return redirect(url_for('list_beer'))


@app.route('/beer/list', methods=['GET', 'POST'])
def list_beer():
    beer = Beer.select()
    form = BeerForm()

    form.brewery.choices = [(typ.id, typ.name) for typ in Brewery.select().order_by('name')]
    form.style.choices = [(typ.id, typ.label) for typ in BeerStyle.select().order_by('label')]

    if form.validate_on_submit():
        print(form.name.data)
        print(form.description.data)
        print(form.style.data)
        print(form.brewery.data)
        print(form.alcohol.data)

        file = request.files['file']
        if file and allowed_image(file.filename):
            filename = secure_filename(file.filename)
            directory = app.config['IMAGES']
            if not os.path.exists(directory):
                os.makedirs(directory)
            file.save(os.path.join(directory, filename))

            beer = Beer.create(
                name=form.name.data,
                description=form.description.data,
                style=form.style.data,
                brewer=form.brewery.data,
                alcohol=form.alcohol.data,
                image=directory+filename
            )

            return redirect(url_for("list_beer"))

    return render_template('list.html', beer=beer, form=form)


@app.route('/brewery/list', methods=['GET', 'POST'])
def list_brewery():
    brews = Brewery.select()
    form = BreweryForm()

    form.size.choices = [(typ.id, typ.label) for typ in BrewerySize.select().order_by('label')]

    if form.validate_on_submit():
        file = request.files['file']
        if file and allowed_image(file.filename):
            filename = secure_filename(file.filename)
            directory = app.config['IMAGES']
            if not os.path.exists(directory):
                os.makedirs(directory)
            file.save(os.path.join(directory, filename))

            brewery = Brewery.create(
                name=form.name.data,
                description=form.description.data,
                location=form.location.data,
                size=form.size.data,
                image=directory+filename
            )

            return redirect(url_for("list_brewery"))

    return render_template('brewery_list.html', form=form, brews=brews)


@app.route('/brewery/sizes', methods=['GET', 'POST'])
def list_brewery_size():
    sizes = BrewerySize.select()
    form = BrewerySizeForm()

    if form.validate_on_submit():
        size = BrewerySize.create(
            label=form.label.data,
            description=form.description.data
        )

        return redirect(url_for("list_brewery_size"))

    return render_template('brewery_size_list.html', form=form, sizes=sizes)


@app.route('/style/list', methods=['GET', 'POST'])
def list_style():
    styles = BeerStyle.select()
    form = BeerStyleForm()

    if form.validate_on_submit():
        style = BeerStyle.create(
            label=form.label.data,
            description=form.description.data
        )

        return redirect(url_for("list_style"))

    return render_template('style_list.html', form=form, styles=styles)



@app.before_request
def before_request():
    g.db = db
    g.db.connect()


@app.after_request
def after_request(response):
    g.db.close()
    return response


# START
if __name__ == '__main__':
    app.run(debug=True, host="127.0.0.1")
