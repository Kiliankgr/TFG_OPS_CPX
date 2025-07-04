from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SelectField, SubmitField
from wtforms.validators import DataRequired

class Add_Instancia_Form(FlaskForm):
    nombre = StringField('Nombre', validators=[DataRequired()],
                         render_kw={"title": "Nombre de la instancia, no añadir extensión"}
                         )
    contenido = TextAreaField('Contenido',validators=[DataRequired()],
                              render_kw={"title": "Introduzca aquí el contenido de la instancia en formato JSON"}
                              )    
    confirmar_btn = SubmitField("Confirmar")


class Mod_Instancia_Form(FlaskForm):
    nombre = StringField('<Nombre>', validators=[DataRequired()],
                         render_kw={"title": "Nombre de la instancia"}
                         )    
    contenido = TextAreaField('Contenido',validators=[DataRequired()],
                              render_kw={"title": "Introduzca aquí el contenido de la instancia en formato JSON"}
                              )
    identificador = StringField("")   #la idea es que no se vea pero que contenga la información del id para modificarse
    modificar_btn = SubmitField("Modificar", 
                                render_kw={"title": "Se modificará el contenido dela instancia en cuestión"})



    
class Instancia_Modelo_Form(FlaskForm):
    nombre = StringField('<Nombre>', validators=[DataRequired()],
                         render_kw={"title": "Nombre de la instancia, no añadir extensión"}
                         )
    resultado = TextAreaField('Contenido',validators=[DataRequired()],
                              render_kw={"title": "Resultado del modelo"}
                              )
    guardar_btn = SubmitField("Guardar", 
                                render_kw={"title": "Guardará el resultado del modelo en la base de datos"})
    