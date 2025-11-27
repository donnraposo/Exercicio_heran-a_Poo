# main.py

from models.cars import Cars

def menu():
    print("\n=== SISTEMA DE CADASTRO DE CARROS ===")
    print("1 - Cadastrar carro")
    print("2 - Listar carros")
    print("0 - Sair")
    return input("Escolha uma opção: ")

while True:
    opcao = menu()

    if opcao == "1":
        print("\n--- CADASTRAR CARRO ---")
        brand = Cars.load_brand()
        model = input("Modelo: ")
        year = input("Ano: ")
        color = input("Cor: ")
        price = float(input("Preço: "))

        car = Cars(brand, model, year, color, price)

        car.save_car()

        print("Carro salvo com sucesso!")

    elif opcao == "2":
        print("\n--- LISTA DE CARROS ---")

        temp = Cars("", "", "", "", "")
        cars = temp.load_all()

        if not cars:
            print("Nenhum carro cadastrado ainda.")
        else:
            for c in cars:
                print(f"""
        Marca: {c['brand']}
        Modelo: {c['model']}
        Ano: {c['year']}
        Cor: {c['color']}
        Preço: R$ {c['price']}""")
                
    elif opcao == "0":
        print("Saindo...")
        break

    else:
        print("Opção inválida!")

