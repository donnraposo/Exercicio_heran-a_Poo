from .base import BaseModel


class Cars(BaseModel):
        
    file = "cars.json"  

    def __init__(self, brand, model, year, color, price):
        self.brand = brand
        self.model = model
        self.year = year
        self.color = color
        self.price = price


    def get_brand(self):
        return self.brand
    
    def get_models(self):
        return self.models
    
    def get_year(self):
        return self.year
    
    def get_color(self):
        return self.color
    
    def save_car(self):

        data = {
        "brand": self.brand,
        "model": self.model,
        "year": self.year,
        "color": self.color,
        "price": self.price
    }
        super().save(data)


    @staticmethod
    def load_brand():

        print("\nEscolha a marca do carro:")
        print("1 - Fiat")
        print("2 - Chevrolet")
        print("3 - Volkswagen")

        brand = input("Digite sua escolha: ")

        
        while brand not in ["1", "2", "3"]:
            print("\nOpção inválida! Tente novamente:")
            print("1 - Fiat")
            print("2 - Chevrolet")
            print("3 - Volkswagen")
            brand = input("Digite sua escolha: ")

        
        match brand:
            case "1":
                return "Fiat"
            case "2":
                return "Chevrolet"
            case "3":
                return "Volkswagen"
        
    @staticmethod
    def load_model(brand):

        models = {
            "Fiat": {
                1: "Uno",
                2: "Argo",
                3: "Mobi"
            },
            "Chevrolet": {
                1: "Onix",
                2: "Prisma",
                3: "Tracker"
            },
            "Volkswagen": {
                1: "Gol",
                2: "Polo",
                3: "T-Cross"
            }
        }

        print("\nEscolha o modelo da marca:", brand)

        for num, model in models[brand].items():
            print(f"{num} - {model}")

        opcao = int(input("Digite sua escolha: "))

        while opcao not in models[brand]:
            print("Opção inválida! Tente novamente.")
            opcao = int(input("Escolha novamente: "))

        return models[brand][opcao]
    @staticmethod
    def validate_year():
        year = input("Ano: ")

        while not year.isdigit() or not (1900 <= int(year) <= 2026):
            print("Ano inválido! Digite um ano entre 1900 e 2024.")
            year = input("Ano: ")  

        return year

        