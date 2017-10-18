from django import forms
from members.models import Member
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from crispy_forms.layout import Field, Layout, Fieldset, ButtonHolder, Submit, HTML
from crispy_forms.bootstrap import *
class MemberForm(forms.ModelForm):
    favourite_quote = forms.CharField(
        widget = forms.Textarea)
    class Meta:
        model = Member
        fields = ('full_name', 'image', 'phone_number', 'email', 'hometown', 
            'favourite_quote', 'bio', 'your_website', 'facebook_url', 'twitter_url', 
            'github_url', 'instagram_url')

    def __init__(self, *args, **kwargs):
        super(MemberForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = 'id-MemberForm'
        self.helper.form_class = 'form'
        self.helper.form_method = 'POST'
        self.helper.form_action = ''

        # self.helper.add_input(Submit('submit', 'Submit'))
        self.helper = FormHelper()
        self.helper.layout = Layout(
                    Fieldset(
                        'Member Form',
                        'full_name',
                        'image',
                        Alert(content='<strong>Warning!</strong> All Info Are Public', css_class = 'alert alert-info'),
                        PrependedText('phone_number', '+977', placeholder = '9818681689'),
                        'your_website',                        # HTML("""
                        # <p>We use notes to get better, <strong>please help us {{ username }}</strong></p>"""),
                        # 'phone_number',
                        Field('email', css_class = 'ffffffffff'),
                        'hometown',
                        'favourite_quote',
                        'bio',
                        PrependedText('facebook_url', 'https://www.facebook.com/', placeholder="username"),
                        PrependedText('twitter_url', 'https://www.twitter.com/', placeholder="username"),
                        PrependedText('github_url', 'https://www.github.com/', placeholder="username"),
                        PrependedText('instagram_url', 'https://www.github.com/', placeholder="username"),



                    ),
                    ButtonHolder(
                        Submit('submit', 'Submit', css_class='btn btn-warning')
                    )
                )






    def clean_full_name(self):
        full_name = self.cleaned_data.get('full_name')
        length = len(full_name)
        if length <= 3 or length >=30:
            raise forms.ValidationError("WoW, Your Name is So Boring!!message")
        return full_name
        
    def clean_phone_number(self):
        phone_number = self.cleaned_data.get('phone_number')
        if len(phone_number) != 10 or not phone_number.startswith('9'):
            raise forms.ValidationError("Sorry! We Cannot Accept This SHIT!!")
        return phone_number

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if not '@' in email or '@.' in email:
            raise forms.ValidationError("ERROR AT ITS BEST")
        elif not '.' in email:
            raise forms.ValidationError("Something Missing E.G '.com', '.edu', '.me', '.org'")

        return email

    def clean_facebook_url(self):
        username = self.cleaned_data.get('facebook_url')
        if username:
            return 'https://www.facebook.com/' + username
        else:
            return username

    def clean_twitter_url(self):
        username = self.cleaned_data.get('twitter_url')
        if username:
            return 'https://www.twitter.com/' + username
        else:
            return username

    def clean_instagram_url(self):
        username = self.cleaned_data.get('instagram_url')
        if username:
            return 'https://www.instagram.com/' + username
        else:
            return username

    def clean_github_url(self):
        username = self.cleaned_data.get('github_url')
        if username:
            return 'https://www.github.com/' + username
        else:
            return username