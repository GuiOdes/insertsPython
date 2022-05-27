nomeTabela = str(input("Nome da tabela: "))
qntInserts = int(input("Quantidade de inserts: "))
count = 0
campos = []
files = []
c = 1
campo = ""
valor = ""

while campo != "FIM":
    campo = str(input(f"Digite o nome do {c}º campo ou FIM para terminar: ")).upper()
    if campo != "FIM":
        campos.append(campo)
    c += 1

c = 0
while len(files) < len(campos):
    file = str(input(f"Nome do {c}º arquivo: "))
    files.append(file+'.txt')
    c += 1

contar = 0
for x in range(qntInserts):   
    count = 1
    string = "INSERT INTO " + nomeTabela + " ("
    string += ", ".join(campos) + ") VALUES (" 
    for i in range(0, len(files)):
        with open(f"wordlist/{files[i]}", "r") as file:
            line = file.readlines()
            if count < len(campos):
                string += line[contar].replace("\n", ", ")
                count += 1
            elif count == len(campos):
                string += line[contar].replace("\n", "")
                count += 1
        if (i+1) == len(files):
            contar += 1
    string += ");"
    print(string)
