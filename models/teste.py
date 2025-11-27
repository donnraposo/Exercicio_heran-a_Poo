choice = int(input("Digite a marca do carro que você deseja: "))

while choice not in [1, 2, 3]:
    match choice:
        case 1:
            choice = "Fiat"
        case 2:
            choice = "Chevrolet"
        case 3:
            choice = "Volkswagen"

    choice = int(input("Digite a marca do carro que você deseja: "))