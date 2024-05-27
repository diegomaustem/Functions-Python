def validaEntradas(entrada, tipo_entrada):

    if(tipo_entrada == 'sexo'):
        return True
    elif(tipo_entrada == 'peso'):
        try:
            float(entrada)
            valid = True
            return valid
        except:
            print('Formato de peso não aceitável!')
    elif(tipo_entrada == 'altura'):
        try:
            float(entrada)
            valid = True
            return valid
        except:
            print('Formato de altura não aceitável!')
    
    else:
        print('Tipo não reconhecido!')


sexo = input('Digite o seu sexo: ').lower()
entrada_validada = validaEntradas(sexo, 'sexo')
while entrada_validada != True:
    sexo = input('Digite o seu sexo: ').lower()
    entrada_validada = validaEntradas(sexo, 'sexo')

peso = input('Digite seu peso: ')
entrada_validada = validaEntradas(peso, 'peso')
while entrada_validada != True:
    peso = input('Digite seu peso: ')
    entrada_validada = validaEntradas(peso, 'peso')

altura = input('Digite sua altura: ')
entrada_validada = validaEntradas(altura, 'altura')
while entrada_validada != True:
    altura = input('Digite seu peso: ')
    entrada_validada = validaEntradas(altura, 'altura')


def calculaIMC(sexo, peso, altura):
    calculo_imc = (float(peso)/ (float(altura) * float(altura)))

    if(sexo == 'm'):
        if(calculo_imc < 20,7):
            print('Abaixo do peso')
        elif(calculo_imc >= 20,7 and calculo_imc <= 26,4):
            print('No peso normal')
        elif(calculo_imc >= 26,4 and calculo_imc <= 27,8):
            print('Acima do peso')
        elif(calculo_imc >= 27,8 and calculo_imc <= 31,1):
            print('Acima do peso ideal')
        elif(calculo_imc > 31,1):
            print('Obeso')
        else: 
            print('Opção não corresponde: ')
    elif(sexo == 'f'):
        if(calculo_imc < 19,1):
            print('Abaixo do peso')
        elif(calculo_imc >= 19,1 and calculo_imc <= 25,8):
            print('No peso normal')
        elif(calculo_imc >= 25,8 and calculo_imc <= 27,3):
            print('Acima do peso')
        elif(calculo_imc >= 27,3 and calculo_imc <= 32,3):
            print('Acima do peso ideal')
        elif(calculo_imc > 32,3):
            print('Obesa')
        else: 
            print('Opção não corresponde: ')
    else:
        print('Opção não corresponde! Tente novamente: ')

calculaIMC(sexo, peso, altura)
