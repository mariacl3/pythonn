n1 = float (input ("digite a primeira nota "))
n2 = float (input ("digite a segunda nota "))
n3 = float (input ("digite a terceira nota "))
media = (n1+n2+n3)/3
print(f"A média é: {media:.2f}")
if media >= 7:
    print("Aluno aprovado")
elif media >= 5:
    print("Aluno recuperação")
else: 
    print("Aluno reprovado")









