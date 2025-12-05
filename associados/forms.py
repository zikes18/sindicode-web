from django import forms
class AssociadoForm(forms.Form):
    GENERO_CHOICES = (
        ('F', 'Mulher'),
        ('M', 'Homem'),
        ('NB', 'Não Binário'),
        ('O', 'Outro'),
        ('PND', 'Prefiro Não Declarar'),
    )
    nome_completo = forms.CharField(
        label="Nome completo",
        required=True,
        max_length=100,
        widget = forms.TextInput(attrs={'class': 'form-control'})
    )
    nome_social = forms.CharField(
        label="Nome social (como você prefere ser chamado (a)",
        required=False,
        max_length=100,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    cpf = forms.CharField(
        label="CPF",
        required=True,
        max_length=14,
        widget=forms.TextInput(attrs={'class': 'form-control',
                                      'placeholder': 'Digite seu CPF'})
    )
    rg = forms.CharField(
        label="RG",
        required=True,
        max_length=7,
        widget=forms.TextInput(attrs={'class': 'form-control',
                                      'placeholder': 'Digite seu RG'})
    )
    # --- CAMPO 3: IDENTIDADE DE GÊNERO ---
    identidade_genero = forms.ChoiceField(
        label='Qual sua identidade de gênero?',
        choices=GENERO_CHOICES,
        widget=forms.Select(attrs={'class': 'form-control',
                                   'placeholder': 'Identifique sua identidade'}),
        required=True  # Permitir que a pessoa não declare, embora haja 'Prefiro Não Declarar'
    )

    # Campo para a opção 'Outro'
    genero_outro = forms.CharField(
        label='Selecione "Outro" acima e especifique',
        max_length=100,
        required=False,
        help_text='Use apenas se a opção "Outro" tiver sido selecionada.',
    )
    email = forms.EmailField(
        label='E-mail',
        required=True,
        max_length=100,
        widget=forms.EmailInput(attrs={'class': 'form-control',
                                       'placeholder': 'Digite seu e-mail'}),
    )
    senha_1 = forms.CharField(
        label='Senha',
        required=True,
        max_length=70,
        widget=forms.PasswordInput(
            attrs={'class': 'form-control',
                'placeholder': 'Digite sua senha'}
        ),
    )

    senha_2 = forms.CharField(
        label='Senha',
        required=True,
        max_length=70,
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Digite sua senha novamente',
            }
        ),
    )

class LoginForm(forms.Form):
    nome_login = forms.CharField(
        label='Nome de Login',
        required=True,
        max_length=100
    )

    senha = forms.CharField(
        label='Senha',
        required=True,
        max_length=70,
    widget = forms.PasswordInput()
    )