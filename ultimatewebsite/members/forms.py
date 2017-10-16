from django import forms
from members.models import Member

class MemberForm(forms.ModelForm):
    class Meta:
        model = Member
        fields = ('full_name', 'image', 'phone_number', 'email', 'hometown', 
            'favourite_quote', 'bio', 'facebook_url', 'twitter_url', 
            'github_url')