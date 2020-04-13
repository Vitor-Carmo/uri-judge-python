password = 2002
while True:
    user_password = int(input())
    
    if not user_password == password:
        print('Senha Invalida')
    else:
        print('Acesso Permitido')
        break