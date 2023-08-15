#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from fashiondoll import FashionDoll
from dotenv import load_dotenv
import os
# pongamos la configuración en el aplicativo
app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY')
app.config['Base_DIR'] = os.environ.get('Base_DIR')
app.config['DEBUG'] = os.environ.get('DEBUG')
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('SQLAlchemy_DATABASE_URI')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = os.environ.get('SQLALCHEMY_TRACK_MODIFICATIONS')


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

#region Delete

@app.route('/dolls/<int:doll_id>', methods=['DELETE'])
def delete_doll_by_id(doll_id : int) -> str:
	"""Elimina una doll por su id
	Args:
		doll_id (int): id de la doll a eliminar
		Returns:
		str: Mensaje de confirmación de eliminación o de que no se encontró la doll
	"""
	if (d := next((doll for doll in dolls if doll.id == doll_id), None)):
		dolls.remove(d)
		return f"Doll with id {doll_id} deleted"
	else:
		return f"Doll with id {doll_id} not found"
#endregion

#region Update


@app.route('/dolls/<int:doll_id>/update_name/<string:doll_name>', methods=['PUT'])
def update_doll_by_id(doll_id : int, doll_name : str) -> str:
	"""Actualiza el nombre de una doll por su id
	Args:
		doll_id (int): id de la doll a actualizar
		doll_name (str): nuevo nombre de la doll
	Returns:
		str: Mensaje de confirmación de actualización o de que no se encontró la doll
	"""
	if (d := next((doll for doll in dolls if doll.id == doll_id), None)):
		d.name = doll_name
		return f"Doll with id {doll_id} updated"
	else:
		return f"Doll with id {doll_id} not found"

@app.route('/dolls/<int:doll_id>/update_price/<int:doll_price>', methods=['PUT'])
def update_doll_price_by_id(doll_id : int, doll_price : int) -> str:
	"""Actualiza el precio de una doll por su id
	Args:
		doll_id (int): id de la doll a actualizar
		doll_price (int): nuevo precio de la doll
	Returns:
		str: Mensaje de confirmación de actualización o de que no se encontró la doll
	"""
	if (d := next((doll for doll in dolls if doll.id == doll_id), None)):
		d.price = doll_price
		return f"Doll with id {doll_id} updated"
	else:
		return f"Doll with id {doll_id} not found"

@app.route('/dolls/<int:doll_id>/update_details/<string:doll_details>', methods=['PUT'])
def update_doll_details_by_id(doll_id : int, doll_details : str) -> str:
	"""Actualiza los detalles de una doll por su id
	Args:
		doll_id (int): id de la doll a actualizar
		doll_details (str): nuevos detalles de la doll
	Returns:
		str: Mensaje de confirmación de actualización o de que no se encontró la doll
	"""
	if (d := next((doll for doll in dolls if doll.id == doll_id), None)):
		d.details = doll_details
		return f"Doll with id {doll_id} updated"
	else:
		return f"Doll with id {doll_id} not found"

@app.route('/dolls/<int:doll_id>/update_type/<string:doll_type>', methods=['PUT'])
def update_doll_type_by_id(doll_id : int, doll_type : str) -> str:
	"""Actualiza el tipo de una doll por su id
	Args:
		doll_id (int): id de la doll a actualizar
		doll_type (str): nuevo tipo de la doll
	Returns:
		str: Mensaje de confirmación de actualización o de que no se encontró la doll
	"""
	if (d := next((doll for doll in dolls if doll.id == doll_id), None)):
		d.type = doll_type
		return f"Doll with id {doll_id} updated"
	else:
		return f"Doll with id {doll_id} not found"
#endregion

#region Create

@app.route('/', methods=['POST'])
def create_doll() -> str:
	"""Crea una nueva doll
	Returns:
		str: Mensaje de confirmación de creación
	"""
	doll = FashionDoll(Name=request.form['name'], Type=request.form['type'], Price=request.form['price'], Details=request.form['details'])
	dolls.append(doll)
	return f"Doll with id {doll.id} created"
#endregion

if __name__ == '__main__':
	app.run()