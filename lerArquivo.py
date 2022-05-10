nomeTabela = str(input("Nome da tabela: "))
qntInserts = int(input("Quantidade de inserts: "))
count = 0
campos = []
valores = []
c = 1
campo = ""
valor = ""

while campo != "FIM":
    campo = str(input(f"Digite o nome do {c}º campo, digite FIM para terminar: "))
    if campo != "FIM":
        campos.append(campo)
    c += 1


c = 1
while valor != "FIM":
    
    file = str(input("Nome do {c}º arquivo: "))
    c += 1

    count = 0
    for line in file:
        if (count < 1):
            string = f"INSERT INTO ("
    
            string += ", ".join(campos)
            
            string += ")"
    
            string += " VALUES ("
    
            string += ", ".join(valores)
    
            string += ");".replace("\n","")
            
            print(string)
            count += 1
