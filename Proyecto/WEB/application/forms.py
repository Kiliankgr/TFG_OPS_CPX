from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SelectField, SubmitField
from wtforms.validators import DataRequired

class Add_Instancia_Form(FlaskForm):
    nombre = StringField('Nombre fichero', validators=[DataRequired()])
    contenido = TextAreaField('Contenido',validators=[DataRequired()])    
    confirmar_btn = SubmitField("Confirmar")