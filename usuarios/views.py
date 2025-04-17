from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import get_user_model, authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ValidationError
from .models import Paciente, Medico, Cidade
from medicos.models import Especialidade
from django.contrib.auth import update_session_auth_hash
import re

Usuario = get_user_model()

def validate_username(username):
    if not re.match(r'^[a-zA-Z0-9_]+$', username):
        raise ValidationError(
            "Username deve conter apenas letras, números e underscores (_). "
            "Não são permitidos espaços, acentos ou caracteres especiais."
        )
    return username.lower()

def register_view(request):
    if request.method == 'POST':
        username = request.POST.get('username', '').strip()
        email = request.POST.get('email', '').strip()
        password = request.POST.get('password', '')
        tipo_usuario = request.POST.get('tipo_usuario')
        primeiro_nome = request.POST.get('primeiro_nome', '').strip()
        ultimo_nome = request.POST.get('ultimo_nome', '').strip()
        cidade_id = request.POST.get('cidade')

        if not all([username, email, password, tipo_usuario, cidade_id]):
            messages.error(request, "Todos os campos obrigatórios devem ser preenchidos!")
            return redirect('cadastro')
        
        try:
            username = validate_username(username)

            if len(password) < 8:
                messages.error(request, "A senha deve ter pelo menos 8 caracteres")
                return redirect('cadastro')

            cidade = Cidade.objects.get(pk=cidade_id)

            user = Usuario.objects.create_user(
                username=username,
                email=email,
                password=password,
                tipo_usuario=tipo_usuario,
                first_name=primeiro_nome,
                last_name=ultimo_nome,
                cidade=cidade
            )
            
            if tipo_usuario == 'medico':
                medico = Medico.objects.create(
                    usuario=user,
                    crm=request.POST.get('crm', '').strip(),
                    clinica=request.POST.get('clinica', '').strip()
                )
                especialidades_ids = request.POST.getlist('especialidades')
                medico.especialidades.set(especialidades_ids)
                
            elif tipo_usuario == 'paciente':
                Paciente.objects.create(
                    usuario=user,
                    data_nascimento=request.POST.get('data_nascimento'),
                    telefone=request.POST.get('telefone', '').strip()
                )
            
            messages.success(request, "Cadastro realizado com sucesso!")
            return redirect('login')
        
        except Cidade.DoesNotExist:
            messages.error(request, "Cidade inválida selecionada.")
        except ValidationError as e:
            messages.error(request, str(e))
        except Exception as e:
            messages.error(request, f"Erro durante o cadastro: {str(e)}")

        return redirect('cadastro')

    especialidades = Especialidade.objects.all().order_by('nome')
    cidades = Cidade.objects.all().order_by('nome')
    return render(request, 'cadastro.html', {
        'especialidades': especialidades,
        'cidades': cidades,
        'form_data': {
            'username': request.POST.get('username', ''),
            'email': request.POST.get('email', ''),
            'tipo_usuario': request.POST.get('tipo_usuario', ''),
            'primeiro_nome': request.POST.get('primeiro_nome', ''),
            'ultimo_nome': request.POST.get('ultimo_nome', '')
        }
    })

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username').lower()
        password = request.POST.get('password')
        
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, "Usuário ou senha incorretos")
    
    return render(request, 'login.html')

def logout_view(request):
    logout(request)
    return redirect('login')

def home_view(request):
    user = request.user if request.user.is_authenticated else None
    return render(request, 'home.html', {'user': user})

@login_required
def editar_perfil_view(request):
    user = request.user
    especialidades = Especialidade.objects.all()
    
    if request.method == 'POST':
        try:
            user.first_name = request.POST.get('primeiro_nome')
            user.last_name = request.POST.get('ultimo_nome')
            user.email = request.POST.get('email')
            
            nova_senha = request.POST.get('nova_senha')
            if nova_senha:
                user.set_password(nova_senha)
                update_session_auth_hash(request, user)
            
            user.save()
            
            if user.tipo_usuario == 'medico':
                medico = user.medico
                medico.crm = request.POST.get('crm')
                medico.clinica = request.POST.get('clinica')
                medico.save()
                medico.especialidades.set(request.POST.getlist('especialidades'))
            elif user.tipo_usuario == 'paciente':
                paciente = user.paciente
                paciente.data_nascimento = request.POST.get('data_nascimento')
                paciente.telefone = request.POST.get('telefone')
                paciente.save()
            
            messages.success(request, "Perfil atualizado com sucesso!")
            return redirect('perfil')
            
        except Exception as e:
            messages.error(request, f"Erro ao atualizar: {str(e)}")
    
    return render(request, 'editar_perfil.html', {
        'user': user,
        'especialidades': especialidades,
    })

@login_required
def perfil_view(request):
    return render(request, 'perfil.html', {'user': request.user})