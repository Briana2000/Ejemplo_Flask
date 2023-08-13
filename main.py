#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import Flask, render_template, request, redirect, url_for, flash
#from flask_sqlalchemy import SQLAlchemy
from fashiondoll import FashionDoll


app = Flask(__name__)


barbie = FashionDoll("Barbie", "Fashion Doll", 1000, "Pink Dress")

@app.route('/', methods=['GET', 'POST'])
def index():
    # return barbie.__str__()
	return render_template('index.html', doll=barbie)

@app.route('/about', methods=['GET'])
def about() -> 'html':
	about_content = "Prueba de envío de strings XD."
	return render_template('about.html', message=about_content)

if __name__ == '__main__':
	app.run(debug=True)