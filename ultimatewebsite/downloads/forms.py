from django import forms
from downloads.models import DownloadItem
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from crispy_forms.layout import Field, Layout, Fieldset, ButtonHolder, Submit, HTML
from crispy_forms.bootstrap import *
class DownloadItemForm(forms.ModelForm):
    class Meta:
        model = DownloadItem
        fields = ('file',)


    def __init__(self, *args, **kwargs):
        super(DownloadItemForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = 'id-DownloadItemForm'
        self.helper.form_class = 'form'
        self.helper.form_method = 'POST'
        self.helper.form_action = ''

        # self.helper.add_input(Submit('submit', 'Submit'))
        self.helper = FormHelper()
        self.helper.layout = Layout(
                    Fieldset(
                        'Upload New File',
                        Alert(content='<strong>WoW!</strong> You are doing great', css_class = 'alert alert-info'),
                        'file'


                    ),
                    ButtonHolder(
                        Submit('submit', 'Submit', css_class='btn btn-warning')
                    )
                )

            