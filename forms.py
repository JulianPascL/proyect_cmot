from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, DateField, TextAreaField, FileField, SubmitField
from wtforms.validators import DataRequired, Email, EqualTo

class SolicitudesForm(FlaskForm):
    tipo_persona = SelectField('Tipo de Persona (*)', choices=[('', 'Seleccione...'), ('natural', 'Natural'), ('juridica', 'Jurídica')], validators=[DataRequired()])
    primer_nombre = StringField('Primer Nombre (*)', validators=[DataRequired()])
    segundo_nombre = StringField('Segundo Nombre')
    primer_apellido = StringField('Primer Apellido (*)', validators=[DataRequired()])
    segundo_apellido = StringField('Segundo Apellido')
    tipo_identificacion = SelectField('Tipo de Identificación (*)', choices=[('', 'Seleccione...'), ('cc', 'Cédula de Ciudadanía'), ('ce', 'Cédula de Extranjería'), ('nit', 'NIT')], validators=[DataRequired()])
    numero_identificacion = StringField('Número de Identificación (*)', validators=[DataRequired()])
    fecha_nacimiento = DateField('Fecha de Nacimiento (*)', format='%Y-%m-%d', validators=[DataRequired()])
    genero = SelectField('Género (*)', choices=[('', 'Seleccione...'), ('masculino', 'Masculino'), ('femenino', 'Femenino'), ('otro', 'Otro')], validators=[DataRequired()])
    direccion = StringField('Dirección (*)', validators=[DataRequired()])
    telefono_movil = StringField('Teléfono Móvil (*)', validators=[DataRequired()])
    email = StringField('Email (*)', validators=[DataRequired(), Email()])
    email_confirmacion = StringField('Confirmar Email (*)', validators=[DataRequired(), Email(), EqualTo('email')])
    descripcion = TextAreaField('Descripción (*)', validators=[DataRequired()])
    archivo_adjunto = FileField('Archivo Adjunto')
    submit = SubmitField('Enviar')
