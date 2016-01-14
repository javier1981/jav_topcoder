class AB:
    def createString(self, N, K):
        EncontradoAi =False
        Ai = N//2
        Bi = (N - (N//2))

        if(N%2==1):
            k_max = ((N//2)+1) *(N//2)

        if(N%2==0):
            k_max = (N//2)*(N//2)

        if (K ==0):
            return ''

        if (K >k_max):
            return ''

        else:

            while (EncontradoAi == False and (Ai>0)):
                Bi = (N - (N//2))

                K_temp = Ai * Bi

                EncontradoBi = False

                while ((EncontradoBi == False) and (Bi>0)):
                    K_temp = Ai * Bi
                    if (K_temp <= K):
                        EncontradoBi = True
                    else:
                        Bi = Bi-1

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
            x=""

            for i in range(int(round(Bj))):
                x = 'B' + x
            for i in range(int(round(Aj))):
                x = 'A' + x
            for i in range(int(round(Bi-Bj))):
                x = 'B' + x
            for i in range(int(round(Ai))):
                x = 'A' + x
            for i in range(int(round(R))):
                 x = 'B' + x
            return (x)
