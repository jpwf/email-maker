# encoding: utf-8

import random
from time import sleep

question = 'Siga as instruções'
print("Respostas sempre com s para sim e n para não, sempre entre aspas\nCaso utilize a opção de criação manual, informe o nome desejado entre aspas")
instruc = 'Digite: \n1- Gerar um email automaticamente' 
instruc2 = '2- Gerar um email manualmente\nResposta: '

nomes = ['maria','joao','mariazinha','jonas','joseph','max','marcio','cleo','marcos','marquinhos','beth','michele','kaka','carlos','jones','marcia','lucca','lucas','locoso']
email = ['@gmail.com', '@hotmail.com','@ig.com']
lista1 = ['a','b','c','d','e','f','g','h','i','j','','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
lista2 = ['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20']
lista3 = ['/','.',',','|','?','°','^','´','@','!','#','$','%','&','*','-','_','+','=','§','<','>','~',':',';']

def automatic():
        user = random.choice(nomes)
        autodomain = random.choice(email)
        letter1 = random.choice(lista1)
        number1 = random.choice(lista2)
        letter2 = random.choice(lista1)
        number2 = random.choice(lista2)
        letter3 = random.choice(lista1)
        number3 = random.choice(lista2)
        letter4 = random.choice(lista1)
        number4 = random.choice(lista2)
        letter5 = random.choice(lista1)
        number5 = random.choice(lista2)
        print('_____LOGIN: {}{}_____'.format(user,autodomain))
        print('_____SENHA: {}{}{}{}{}{}{}{}{}_____'.format(letter1,number1,letter2,number2,letter3,number3,letter4,number4,letter5,number5))

def manual1():
        letter1 = random.choice(lista1)
        number1 = random.choice(lista1)
        symbol1 = random.choice(lista1)
        number2 = random.choice(lista1)
        letter3 = random.choice(lista1)
        number3 = random.choice(lista1)
        letter4 = random.choice(lista1)
        symbol2 = random.choice(lista1)
        letter5 = random.choice(lista1)
        number5 = random.choice(lista1)
        senha = ('SENHA: {}{}{}{}{}{}{}{}{}'.format(letter1,number1,symbol1,number2,letter3,number3,letter4,symbol2,letter5,number5))
        print(senha)
def manual2():
        letter1 = random.choice(lista2)
        number1 = random.choice(lista2)
        symbol1 = random.choice(lista2)
        number2 = random.choice(lista2)
        letter3 = random.choice(lista2)
        number3 = random.choice(lista2)
        letter4 = random.choice(lista2)
        symbol2 = random.choice(lista3)
        letter5 = random.choice(lista2)
        number5 = random.choice(lista2)
        senha = ('SENHA: {}{}{}{}{}{}{}{}{}'.format(letter1,number1,symbol1,number2,letter3,number3,letter4,symbol2,letter5,number5))
        print(senha)
def manual3():
        letter1 = random.choice(lista3)
        number1 = random.choice(lista3)
        symbol1 = random.choice(lista3)
        number2 = random.choice(lista3)
        letter3 = random.choice(lista3)
        number3 = random.choice(lista3)
        letter4 = random.choice(lista3)
        symbol2 = random.choice(lista3)
        letter5 = random.choice(lista3)
        number5 = random.choice(lista3)
        senha = ('SENHA: {}{}{}{}{}{}{}{}{}'.format(letter1,number1,symbol1,number2,letter3,number3,letter4,symbol2,letter5,number5))
        print(senha)
def manual4():
        letter1 = random.choice(lista1)
        number1 = random.choice(lista2)
        symbol1 = random.choice(lista3)
        number2 = random.choice(lista2)
        letter3 = random.choice(lista1)
        number3 = random.choice(lista2)
        letter4 = random.choice(lista1)
        symbol2 = random.choice(lista3)
        letter5 = random.choice(lista1)
        number5 = random.choice(lista2)
        senha = ('SENHA: {}{}{}{}{}{}{}{}{}'.format(letter1,number1,symbol1,number2,letter3,number3,letter4,symbol2,letter5,number5))
        print(senha)



while True:
    sleep(1)
    print(question)
    sleep(1)
    print(instruc)
    sleep(1)
    instruction = int(input(instruc2))
    if instruction == 1:
        print('Processando...')
        sleep(1)
        automatic()
        sleep(1)
        repeat = str(input("Deseja algo mais?\nResposta: "))
        if repeat == 'n':
            print("Foi um prazer ajudar")
            sleep(0.8)
            break;
    if instruction == 2:
        print('Vamos juntos criar seu email')
        sleep(1)
        name = str(input("Primeiro, qual nome gostaria no seu email?\nResposta: " ))
        sleep(1)
        print("Ok, guardei o nome que você escolheu para usarmos na finalização do seu email")
        sleep(1)
        domain = str(input("Agora vamos ao domínio desejado(gmail, hotmail, ig, etc..)\nResposta:"))
        sleep(0.5)
        print("Ok tudo certo, domínio guardado")
        password = "Agora a parte mais importante, você gostaria que sua senha seja feita de letras, números ou símbolos especiais\n1- Letras\n2- Números\n3- Símbolos especiais\n4- Mix dos 3\nResposta:"
        sleep(1)
       

        # question2 = str(input("Bom, tudo certo até agora, sua senha terá 9 caracteres, deseja reduzir seu tamanho?\nResposta: "))
        # if question2 == 'n':
        print("Ok, gerando sua senha....")
        sleep(0.4)
        # manual()
        sleep(1)
        print('')
        emaill = ("Email: {}@{}.com".format(name, domain))
        passwordd = int(input(password))
        if passwordd == 1:
                print(emaill)
                manual1()
        if passwordd == 2:
                print(emaill)
                manual2()
        if passwordd == 3:
                print(emaill)
                manual3()
        if passwordd == 4:
                print(emaill)
                manual4()
        
        print('Foi um prazer ajudar na criação do seu email, tenha um bom dia!!!!')
        sleep(0.4)
        break;
        # if question == 's'


        
                    