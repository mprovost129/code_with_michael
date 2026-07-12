from django import forms

from .models import CommunityPost, EmailSubscriber


class EmailSubscriberForm(forms.ModelForm):
    class Meta:
        model = EmailSubscriber
        fields = ('email', 'first_name')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['email'].widget.attrs.update({
            'placeholder': 'Email address',
        })
        self.fields['first_name'].widget.attrs.update({
            'placeholder': 'First name (optional)',
        })
        self.fields['email'].help_text = 'Get the next beginner lesson, challenge, and recap in your inbox.'

    def clean_email(self):
        return self.cleaned_data['email'].strip().lower()


class CommunityPostForm(forms.ModelForm):
    class Meta:
        model = CommunityPost
        fields = ('post_type', 'body')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['body'].widget.attrs.update({
            'placeholder': 'Share a win, ask a question, or shout out something you built...',
            'rows': 4,
        })
