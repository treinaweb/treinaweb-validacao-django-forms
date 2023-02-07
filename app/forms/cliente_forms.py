import re
from django.forms import ModelForm
from django import forms
from app.models import Cliente, Endereco


def nome_completo_validator(value):
    regex = "^[a-zA-Z\u00C0-\u017F´]+\s+[a-zA-Z\u00C0-\u017F´]{0,}$"
    if not re.match(regex, value):
        raise forms.ValidationError("O nome precisa de um sobrenome")

class ClienteForm(ModelForm):
    nome = forms.CharField(validators=[nome_completo_validator])

    class Meta:
        model = Cliente
        exclude = ("endereco", )

    def clean(self):
        cleaned_data = super().clean()
        email = cleaned_data.get("email")
        profissao = cleaned_data.get("profissao")
        if email and not profissao:
            raise forms.ValidationError("A profisao é obrigatória quando o email existir")

    def clean_email(self):
        email = self.cleaned_data["email"]
        regex = r'\b[A-Za-z0-9._-]+@treinaweb.com\b'
        if not re.match(regex, email):
            raise forms.ValidationError("O email precisa ser da treinaweb")
        return email

class EnderecoForm(ModelForm):
    class Meta:
        model = Endereco
        fields = "__all__"