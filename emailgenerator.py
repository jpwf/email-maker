#importando bibliotecas
import random
from time import sleep
#definindo variaveis
p = 'Deseja gerar um email? '
nomes = ['maria','joao','mariazinha','jonas','joseph','max','marcio','cleo','marcos','marquinhos','beth','michele','kaka','carlos','jones','marcia','lucca','lucas','locoso','vitor','carolzinha','mikael','lucaco','mikie','maximo','marcinha']
#definindo listas
email = ['@gmail.com', '@hotmail.com','@ig.com']
lista1 = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
lista2 = ['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20']
#utilizando function choice da biblioteca random para definir os scripts
def script1():
        a = random.choice(nomes)
        b = random.choice(email)
        c = random.choice(lista1)
        d = random.choice(lista2)
        e = random.choice(lista1)
        f = random.choice(lista2)
        g = random.choice(lista1)
        h = random.choice(lista2)
        i = random.choice(lista1)
        j = random.choice(lista2)
        k = random.choice(lista1)
        print('_____LOGIN: {}{}_____'.format(a,b))
        print('_____SENHA: {}{}{}{}{}{}{}{}{}_____'.format(c,e,f,k,g,d,h,i,j))
def script2():
        l = random.choice(lista1)
        m = random.choice(lista2)
        n = random.choice(lista1)
        o = random.choice(lista2)
        p = random.choice(lista1)
        q = random.choice(lista2)
        r = random.choice(lista1)
        s = random.choice(lista2)
        t = random.choice(lista1)
        print('_____SENHA: {}{}{}{}{}{}{}{}{}_____'.format(l,n,s,q,t,m,r,p,o))
def script3():
        u = random.choice(nomes)
        v = random.choice(email)
        print('_____LOGIN: {}{}_____'.format(u,v))
def script4():
        p3 = int(input('Digite 3 para gerar mais um email e 4 para gerar uma senha ou login: '))
        if p3 == 3:
                print('GERANDO EMAIL.....')
                sleep(1)
                script3()
        if p3 == 4:
                p4 = int(input('Digite 5 para gerar uma senha e 6 para gerar um login: '))
                if p4 == 5:
                        print('GERANDO SENHA.....')
                        sleep(1)
                        script2()
                if p4 == 6:
                        print('GERANDO LOGIN.....')
                        sleep(1)
                        script3()
#montando bloco de loop
while True:
        p1 = str(input(p))
        if p1 == 's':
                print('Processando.....')
                sleep(2)
                script1()
                sleep(1)
        if p1 == 'n':
                q = str(input('Deseja gerar apenas uma senha ou apens um login? '))
                if q == 's':
                        pe = int(input('Digite 1 para gerar uma senha e 2 para gerar um login: '))
                        if pe == 1:
                                print('GERANDO SENHA....')
                                sleep(2)
                                script2()
                        if pe == 2:
                                print('GERANDO LOGIN....')
                                sleep(2)
                                script3()
                p2 = str(input('Deseja algo mais? '))
                if p2 == 's':
                        script4()
                if p2 == 'n':
                        print('OK, Fazendo logoff.....')
                        sleep(1)
                        break 
