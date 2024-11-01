import re

def validate_name(name):
    if not name.strip():
        return False, 'Por favor, insira um nome válido.'
    elif len(name) < 3:
        return False, 'Por favor, um nome com pelo menos 3 caracteres.'
    return True, ''

def validate_password(password):
    if len(password) < 6:
        return False, 'A senha deve ter pelo menos 6 caracteres.'
    return True, ''

def validate_password_match(password, password2):
    if password != password2:
        return False, 'As senhas não coincidem'
    return True, ''

def validate_email_exists(controller, email):
    if not email.strip():
        return False, 'Por favor, insira um e-mail válido.'

    email_regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    if not re.match(email_regex, email):
        return False, 'Por favor, insira um e-mail no formato válido.'

    if controller.email_exists(email):
        return False, 'Já existe uma conta com esse e-mail.'

    return True, ''
