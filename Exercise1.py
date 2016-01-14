__author__ = 'javier'

#def createString(self, N, K):
def createString():
    Lista = ['a,b','c']
    print(Lista)

def createString2(self, N, K):

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
    else:
        result = ''
        print('N-K:')
        print(N-K)
        print('N-K:')
        print(K)
        print('**********************')

        for i in range(1,N+1):
            if (i < (N-K)):
                result = result + 'B'
                print(i)
            if (i==N-K):
                result = result + 'A'
                print (i)
            if (i>N-K):
                result = result + 'B'
                print (i)
        if ((K > N)):
            result2 = result.
            result[2].
    #Lista = ['a,b','c']
    return result

pepe =''
print(createString2(pepe,8,7))



