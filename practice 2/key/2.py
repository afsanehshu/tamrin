String = input("Enter sentence : ")

print('Len : ',len(String))

S = String.upper()

S = S.replace('A', '_') 
S = S.replace('E', '_')
S = S.replace('I', '_')
S = S.replace('O', '_')
S = S.replace('U', '_')

print(S)
