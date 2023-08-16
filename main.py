#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import Flask, abort, render_template, request
from fashiondoll import FashionDoll
from dotenv import load_dotenv
import sqlite3
import os

load_dotenv()
app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY')
app.config['Base_DIR'] = os.environ.get('Base_DIR')
app.config['DATABASE'] = os.environ.get('DATABASE')
app.config['DEBUG'] = os.environ.get('DEBUG', False)


# region Dommies
def dummy_dolls() -> list[FashionDoll]:
	dolls : list[FashionDoll] = []
	barbie : FashionDoll  = FashionDoll(Name="Barbie", Type="Fashion Doll", Price=1000, Details="Pink Dress")
	dolls.append(barbie)
	dolls.append(FashionDoll(Name="Ken", Type="Fashion Doll", Price=1000, Details="Blue Dress"))
	dolls.append(FashionDoll(Name="Cindy", Type="Fashion Doll", Price=1000, Details="Yellow Dress"))
	dolls.append(FashionDoll(Name="Cindy", Type="Fashion Doll", Price=1000, Details="Beach Dress"))
	dolls.append(FashionDoll(Name="Linda", Type="Fashion Doll", Price=1000, Details="Green Dress"))
	return dolls
#endregion

#region DB_Context

def Get_DB_Connection() -> sqlite3.Connection:
	"""Obtiene una conexión a la base de datos
	Returns:
		sqlite3.Connection: Conexión a la base de datos
	"""
	conn =  sqlite3.connect(
			app.config['DATABASE']
		)
	conn.row_factory = sqlite3.Row
	return conn
def get_post(post_id) -> FashionDoll:
    """Obtiene una doll por su id
    Args:
		post_id (int): id de la doll a obtener
	Return:
		FashionDoll: Doll obtenida
	"""
    conn = Get_DB_Connection()
    post = conn.execute('SELECT * FROM Doll WHERE id = ?',
                        (post_id,)).fetchone()
    conn.close()
    if post is None:
        abort(404)
    return FashionDoll(ID=post['id'], Name=post['name'], Type=post['type'], Price=post['price'], Details=post['details'])
def delete_post(post_id) -> None:
	if post_id is None or post_id == "":
		#Evitamos errores al prohibir ingresar Null
		return

	conn = Get_DB_Connection()
	post = conn.execute('SELECT * FROM Doll WHERE id = ?',
					 (post_id,)).fetchone()

	if post is None:
		conn.close()
		abort(404)
	conn.execute('DELETE FROM Doll WHERE id = ?', (post_id,))
	conn.commit()
	conn.close()

#endregion


#region Dummy Data
dolls : list[FashionDoll] = dummy_dolls()
barbie : FashionDoll = dolls[0]
g : FashionDoll = get_post(1)
print(type(g))
dolls.append(g)
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
		delete_post(doll_id)
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
	if app.config['DEBUG']:
		app.run(debug=True, port=5000)
	app.run(port=8080)
