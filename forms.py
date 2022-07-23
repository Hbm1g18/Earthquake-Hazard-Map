import flask_wtf
import wtforms
from flask_wtf import Form
from wtforms.fields import TextField, BooleanField, TextAreaField, SubmitField
from wtforms.validators import Required
 
class ContactForm(Form):
  name = TextField("Name")
  email = TextField("Email")
  subject = TextField("Subject")
  message = TextAreaField("Message")
  submit = SubmitField("Send")