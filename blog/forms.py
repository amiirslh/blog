from django import forms
from .models import Comment

class TicketForm(forms.Form):
    SUBJECT_CHOICES=(
        ('',''),
        (' پیشنهاد','پیشنهاد'),
        ('انتقاد', 'انتقاد'),
        ('گزارش مشکل', 'گزارش مشکل')

    )
    message = forms.CharField(widget=forms.Textarea,required=True)
    name = forms.CharField(max_length=250,required=True,widget=forms.TextInput(attrs={'placeholder':'نام',
                                                                                      'style':'height:50px',}))
    email = forms.EmailField()
    phone = forms.CharField(max_length=11,required=True)
    subject = forms.ChoiceField(choices=SUBJECT_CHOICES,)

    def clean_phone(self):
        phone_num=self.cleaned_data['phone']
        if phone_num:
            if not phone_num.isnumeric():
                raise forms.ValidationError('شماره تماس باید عدد باشد!!')
            else:
                return phone_num




class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['name','body',]
        widgets={
            ''
        }


class LikeForm(forms.ModelForm):
    pass