'''09 - Escreva um programa em Python que implemente um jogo com as seguintes regras:
- O computador deve gerar um número aleatório entre 1 e 100;
- O usuário terá uma certa quantidade de chances (de acordo com um nível de dificuldade) para acertar o número sorteado pelo computador;
- Quando o usuário acertar o valor sorteado ou quando o número de tentativas for atingido, programa deve informar o resultado adequado;'''

                
from random import randint
def jogar(tentativas):
    sorteado = (randint(1,100))
    print(f'--- Caro usuário, você terá {tentativas} tentativas de acertos! Digite valores no intervalo de 1 a 100') 
    for i in range(1,tentativas+1,1):
        try:
            num = int(input('Digite um número|')) 
            #AQUI FAZ UMA VERIFICACAO DE VALUE ERROR, O CONTINUE VOLTA PARA O INPUT NOVAMENTE. 
        except ValueError:
            print('\033[31mPOR FAVOR! DIGITE UM VALOR DO TIPO INTEIRO\033[m')
            continue
        if  num < 1 or num > 100:
            print('\033[31mDigite um valor no intervalo de 1 a 100!!!\033[m')
            continue
        
        if num != sorteado:
            if tentativas - i  != 0:
                print(f'Não desanime! Você tem {tentativas - i } tentativas de acertar ainda')

        else:
            print(f'Parabéns,você acertou o valor!!! {sorteado}')
            exit()
        
    print(f'Que pena! O número sorteado foi: {sorteado}')


'''N É UMA VAR QUE VAI RECEBER OS NIVEIS DE DIFICULDADE, QUE SAO TRES, SE POR ACASO O USUARIO DIGITAR UM VALOR DIFERENTE DE 1,2,3
NA TELA VAI MOSTRAR ATRAVES DO ELSE print("Opção inválida!"). MAS SE O USUARIO DIGITAR N IGUAL UMAS DAS OPÇOES, LOGO A FUNÇAO JOGO VAI RECEBER O ARGUMENTO DO BLOCO IF (BEM, POSSO IMPLEMENTAR UM try-except, POREM O CODIGO VAI FICAR MAIS ENORME) PARA O PARAMETRO TENTATIVA'''

n = int(input("Escolha o nível de dificuldade (1 - Fácil, 2 - Médio, 3 - Difícil): "))
if n == 1:
    jogar(20)
elif n == 2:
    jogar(10)
elif n == 3:
    jogar(5)
else:
    print("Opção inválida!")



