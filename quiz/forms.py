from django import forms
from django.forms.widgets import RadioSelect, SelectMultiple, CheckboxSelectMultiple


class QuestionForm(forms.Form):
    request_type = forms.CharField()

    def __init__(self, question, *args, **kwargs):
        super(QuestionForm, self).__init__(*args, **kwargs)
        choice_list = [x for x in question.get_answers_list()]
        self.fields["answers"] = forms.ChoiceField(choices=choice_list, widget=CheckboxSelectMultiple)




    def clean_request_type(self):
        request_type = self.cleaned_data.get('request_type')
        if 'something' not in request_type:
            raise forms.ValidationError('Something must be in request_type field.')
        return request_type

