from django import forms
from members.models import Member

class MemberForm(forms.ModelForm):
    class Meta:
        model = Member
        fields = ('full_name', 'image', 'phone_number', 'email', 'hometown', 
            'favourite_quote', 'bio', 'your_website', 'facebook_url', 'twitter_url', 
            'github_url', 'instagram_url')

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
        facebook_url = self.cleaned_data.get('facebook_url')
        if not 'facebook.com' in facebook_url:
            raise forms.ValidationError("We don't think this is a facebook URL")

        return facebook_url
    def clean_twitter_url(self):
        twitter_url = self.cleaned_data.get('twitter_url')
        if not 'twitter.com' in twitter_url:
            raise forms.ValidationError("We don't think this is a twitter URL")

        return twitter_url

    def clean_instagram_url(self):
        instagram_url = self.cleaned_data.get('instagram_url')
        if not 'instagram.com' in instagram_url:
            raise forms.ValidationError("We don't think this is a instagram URL")
        return instagram_url

    def clean_github_url(self):
        github_url = self.cleaned_data.get('github_url')
        if not 'github.com' in github_url:
            raise forms.ValidationError("We don't think this is a Github URL")
        return github_url