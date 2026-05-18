"""3.	Elabore um algoritmo para testar se uma senha digitada é igual a “MinhaSenha”. Se a senha estiver correta
escreva “Acesso permitido”, do contrário emita a mensagem “Você não tem acesso ao sistema”."""

senha = input("Insira a sua Senha: ")

if senha == "MinhaSenha":
    print("Acesso Permitido")
else:
    print("Você não tem acesso ao sistema")