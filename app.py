from flask import Flask, render_template, redirect, url_for, flash, request, jsonify
from config import Config
from models import db, Solicitudes
from forms import SolicitudesForm
from datetime import datetime

app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/pqrsd', methods=['GET', 'POST'])
def pqrsd_form():
    tipo = request.args.get('tipo', 'peticion')
    form = SolicitudesForm()
    return render_template('pqrsd_form.html', form=form, tipo=tipo)

@app.route('/submit_pqrsd', methods=['POST'])
def submit_pqrsd():
    form = SolicitudesForm()
    if form.validate_on_submit():
        try:
            archivo = form.archivo_adjunto.data
            archivo_nombre = archivo.filename if archivo else None
            solicitud = Solicitudes(
                tipo_solicitud=request.form.get('tipo'),
                tipo_persona=form.tipo_persona.data,
                primer_nombre=form.primer_nombre.data,
                segundo_nombre=form.segundo_nombre.data,
                primer_apellido=form.primer_apellido.data,
                segundo_apellido=form.segundo_apellido.data,
                tipo_identificacion=form.tipo_identificacion.data,
                numero_identificacion=form.numero_identificacion.data,
                fecha_nacimiento=form.fecha_nacimiento.data,
                genero=form.genero.data,
                direccion=form.direccion.data,
                telefono_movil=form.telefono_movil.data,
                email=form.email.data,
                descripcion=form.descripcion.data,
                archivo_adjunto=archivo_nombre
            )
            db.session.add(solicitud)
            db.session.commit()
            current_time = datetime.now().strftime("%H:%M:%S")
            return jsonify({"message": "Solicitud enviada con éxito", "time": current_time}), 200
        except Exception as e:
            db.session.rollback()
            return jsonify({"error": f"Error al guardar en la base de datos: {str(e)}"}), 500
    else:
        return jsonify({"error": "Error en la validación, los email no coinciden", "errors": form.errors}), 400

if __name__ == '__main__':
    app.run(debug=True)