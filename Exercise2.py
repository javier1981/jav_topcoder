__author__ = 'javier'

class AB:
    def createString(self, N, K):
        EncontradoAi =False
        Ai = N//2
        Bi = (N - (N//2))

        if(N%2==1):
            k_max = ((N//2)+1) *(N//2)
            print('K_max:')
            print(k_max)
        if(N%2==0):
            k_max = (N//2)*2
            print('K_max:')
            print(k_max)

        if (K >k_max):
            return ''
        if (K<1):
            return ''
        else:

            while (EncontradoAi == False and (Ai>0)):
                Bi = (N - (N//2))

                K_temp = Ai * Bi
                print("k_temp:")
                print(K_temp)
                EncontradoBi = False

                while ((EncontradoBi == False) and (Bi>0)):
                    K_temp = Ai * Bi
                    if (K_temp <= K):
                        EncontradoBi = True
                    else:
                        Bi = Bi-1
                        print("Bi:")
                        print(Bi)

                print("el valor de k_temp es :")
                print(K_temp)
                if (K_temp <= K):
                    EncontradoAi = True
                else:
                    Ai = Ai-1

            L = Ai + Bi
            Res = N - L
            R = 0
            Aj = N - R - L
            M = Ai*Bi

            ausente = True
            while (R <= Res) and ausente :
                Aj = N - R - L
                M = Ai*Bi

                if(Aj==0):
                    Bj=0
                else:
                    Bj = K - (M / Aj)

                if(Bj==0):
                    Aj=Bj
                Bw = Bi - Bj
                if (Ai*Bi + Aj*Bj) ==K:
                    if(Ai+Bi+Aj+R==N):
                        ausente = False
                R = R +1

            R = R -1
            if(Bj>Bi):
                aux = Ai
                Ai = Bi
                Bi = aux
            print("Ai_final")
            print(Ai)
            print("Bi_final")
            print(Bi)
            print("Aj_final :")
            print(Aj)
            print("Bj_final: ")
            print(Bj)
            print("R_final: ")

            print(R)
            x=''

            for i in range(round(Bj)):
                x = 'B' + x
            for i in range(Aj):
                x = 'A' + x
            for i in range(round(Bi-Bj)):
                x = 'B' + x
            for i in range(Ai):
                x = 'A' + x
            for i in range(R):
                 x = 'B' + x
            print(x)
            return (x)

myobjectx = AB()
a = myobjectx.createString(9,0)
print(a)

## Tenemos el giro en 5