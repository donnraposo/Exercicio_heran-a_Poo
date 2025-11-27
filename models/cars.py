from .base import BaseModel


class Cars(BaseModel):
        
    file = "cars.json"   # <<< OBRIGATÓRIO

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

        brand = int(input("Digite sua escolha: "))

        while brand not in [1, 2, 3]:
            brand = int(input("Escolha a marca do carro:"))
            print(
                "Escolha a marca: " \
                "1 - Fiat " \
                "2 - Chevrolet  "
                "3- Volkswagen")
            match brand:
                case 1:
                    return "Fiat"
                case 2:
                    return "Chevrolet"
                case 3:
                    return "Volkswagen"

    