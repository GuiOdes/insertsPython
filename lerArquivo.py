nomeTabela = str(input("Nome da tabela: "))
qntInserts = int(input("Quantidade de inserts: "))
count = 0
campos = []
valores = []
files = []
c = 1
campo = ""
valor = ""

while campo != "FIM":
    campo = str(input(f"Digite o nome do {c}º campo ou FIM para terminar: "))
    if campo != "FIM":
        campos.append(campo)
    c += 1

c = 0
while len(files) < len(campos):
    file = str(input(f"Nome do {c}º arquivo: "))
    files.append(file)
    c += 1

count = 1
for i in range(0, len(files)):

    string = "INSERT INTO " + nomeTabela + " ("
    string += ", ".join(campos) + ") VALUES ("

    with open(f"wordlist/{files[i]}", "r") as file:
        line = file.readlines()
        if count < len(campos):
            string += line[i].replace("\n", "") + ","
        elif count == len(campos):
            string += line[i].replace("\n", "")

            count += 1

string += ");"

print(string)
