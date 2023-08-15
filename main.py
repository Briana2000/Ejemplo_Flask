#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import Flask, render_template, request, redirect, url_for, flash
#from flask_sqlalchemy import SQLAlchemy
from fashiondoll import FashionDoll



app = Flask(__name__)


# region Dommies
dolls : list[FashionDoll] = []
barbie : FashionDoll  = FashionDoll(Name="Barbie", Type="Fashion Doll", Price=1000, Details="Pink Dress")
dolls.append(barbie)
dolls.append(FashionDoll(Name="Ken", Type="Fashion Doll", Price=1000, Details="Blue Dress"))
dolls.append(FashionDoll(Name="Cindy", Type="Fashion Doll", Price=1000, Details="Yellow Dress"))
dolls.append(FashionDoll(Name="Cindy", Type="Fashion Doll", Price=1000, Details="Beach Dress"))
dolls.append(FashionDoll(Name="Linda", Type="Fashion Doll", Price=1000, Details="Green Dress"))
# endregion


@app.route('/', methods=['GET', 'POST'])
def index() -> str:
	return render_template('index.html', doll=barbie)

@app.route('/about', methods=['GET'])
def about() -> str:
	about_content : str = "Prueba de envío de strings XD."
	return render_template('about.html', message=about_content)

# creemos un método para visualizar todas las dolls que existen
@app.route('/dolls', methods=['GET'])
def dolls_list() -> str:
	return ''.join(str(doll)+'\n' for doll in dolls)

# creemos un método para visualizar una doll en específico by id
@app.route('/dolls/<int:doll_id>', methods=['GET'])
def doll_by_id(doll_id : int) -> str:
	return str(d) if (d := next((doll for doll in dolls if doll.id == doll_id), None)) else f"Doll with id {doll_id} not found"

if __name__ == '__main__':
	app.run(debug=True)