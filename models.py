from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Solicitudes(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    tipo_solicitud = db.Column(db.String(50), nullable=False)
    tipo_persona = db.Column(db.String(50), nullable=False)
    primer_nombre = db.Column(db.String(50), nullable=False)
    segundo_nombre = db.Column(db.String(50))
    primer_apellido = db.Column(db.String(50), nullable=False)
    segundo_apellido = db.Column(db.String(50))
    tipo_identificacion = db.Column(db.String(50), nullable=False)
    numero_identificacion = db.Column(db.String(50), nullable=False, unique=True)
    fecha_nacimiento = db.Column(db.Date, nullable=False)
    genero = db.Column(db.String(10), nullable=False)
    direccion = db.Column(db.String(100), nullable=False)
    telefono_movil = db.Column(db.String(20), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    descripcion = db.Column(db.Text, nullable=False)
    archivo_adjunto = db.Column(db.String(100))
    fecha_solicitud = db.Column(db.DateTime, default=db.func.current_timestamp())
