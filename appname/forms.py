from flask_wtf import Form
from wtforms import StringField
from wtforms.validators import DataRequired, Regexp
from wtforms.widgets import TextArea

# from .models import User


class LoginForm(Form):
    sequence = StringField(u'Sequence',
                           widget=TextArea(),
                           validators=[DataRequired(),
                                       Regexp(r'^[ARNDCQEGHILKMFPSTWYV]+$',
                                              message= "Amino Sequence must only contain capital letters of amino acids [ARNDCQEGHILKMFPSTWYV]")])

    def validate(self):
        check_validate = super(LoginForm, self).validate()

        # if our validators do not pass
        if not check_validate:
            return False

        return True
