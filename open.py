import csv # Importerar ifrån ditt biblioteket för att kunna arbeta med CSV-filer
import os # Importerar fån din biblioteket därmed kunna interagera med ditt operativsystemet
import locale # Importerar från biblioteket för lokalisering (valuta etc.)
from time import sleep # Importerar en funktionen sleep ifrån time-biblioteket


def load_data(filename): # En Funktion för att läsa data från en CSV-fil och skapa en lista av produkter
    products = [] # Initierar en tom lista för att lagra produkterna
    
    with open(filename, 'r') as file: # Öppnar CSV-filen för läsning
        reader = csv.DictReader(file) # Skapar en läsare som läser raderna som ordböcker
        for row in reader:
            id = int(row['id']) # Konverterar 'id' till ett heltal
            name = row['name'] # Hämtar 'name' som en sträng
            desc = row['desc'] # Hämtar 'desc' som en sträng
            price = float(row['price']) # Konverterar 'price' till ett flyttal
            quantity = int(row['quantity']) # Konverterar 'quantity' till ett heltal
            
            products.append(        #list # Lägger till en ny produkt i listan
                {                    #dictionary
                    "id": id, # ID för produkten       
                    "name": name, # Namn på produkten
                    "desc": desc, # Beskrivning av produkten
                    "price": price, # Pris på produkten
                    "quantity": quantity # Antal av produkten
                }
            )
    return products # Returnerar listan av produkter

products = [ # Skapar en lista med produkter (här är produkterna inlagda manuellt)
    {"id": 1, "name": "iPad 1st Generation", "desc": "The original iPad.", "price": 4999.99, "quantity": 20},
    {"id": 2, "name": "iPad 2nd Generation", "desc": "The second generation iPad.", "price": 5999.99, "quantity": 30},
    {"id": 3, "name": "iPad 3rd Generation", "desc": "The third generation iPad.", "price": 6999.99, "quantity": 40},
    {"id": 4, "name": "iPad 4th Generation", "desc": "The fourth generation iPad.", "price": 7999.99, "quantity": 50},
    {"id": 5, "name": "iPad 5th Generation", "desc": "The fifth generation iPad.", "price": 8999.99, "quantity": 60},
    {"id": 6, "name": "iPad 6th Generation", "desc": "The sixth generation iPad.", "price": 9999.99, "quantity": 70},
    {"id": 7, "name": "iPad 7th Generation", "desc": "The seventh generation iPad.", "price": 10999.99, "quantity": 80},
    {"id": 8, "name": "iPad 8th Generation", "desc": "The eighth generation iPad.", "price": 11999.99, "quantity": 90},
    {"id": 9, "name": "iPad 9th Generation", "desc": "The ninth generation iPad.", "price": 12999.99, "quantity": 100},
    {"id": 10, "name": "iPad 10th Generation", "desc": "The tenth generation iPad.", "price": 13999.99, "quantity": 110}
]

def get_product(products, id): #gör en funktion som hämtar en produkt  # Funktion för att hämta en specifik produkt med hjälp av dess ID
    for product in products:
        if product["id"] == id:
            return product
    return None
def remove_product(products, id): # En funktion gjord för att ta bort en produkt baserat på dess ID
    temp_product = None

    for product in products:
        if product["id"] == id:
            temp_product = product
            break  # Avslutar självaste loopen snarast produkten hittas

    if temp_product:
        products.remove(temp_product)
        return f"Product: {id} {temp_product['name']} was removed"
    else:
        return f"Product with id {id} not found"


def view_product(products, id):
    product = get_product(products, id)# Go through each product in the list
    for product in products:
        # Check if the product's id matches the given id
        if product["id"] == id:# If it matches, return the product's name and description
            if product:
                 return f"Visar produkt: {product['name']} {product['desc']}"# If no matching product is found, return this message
    return "Produkten hittas inte"
                          
def view_products(products):
    product_list = []
    for index, product in enumerate(products,1 ):
        product_info = f"{index}) (#{product['id']}) {product['name']} \t {product['desc']} \t {locale.currency(product['price'], grouping=True)}"
        product_list.append(product_info)
    
    return "\n".join(product_list)

#TODO: gör om så du slipper använda global-keyword (flytta inte "product = []")
#TODO: skriv en funktion som returnerar en specifik produkt med hjälp av id


locale.setlocale(locale.LC_ALL, 'sv_SE.UTF-8')  # Sätter in en  lokalisering för valutasymboler och format

os.system('cls' if os.name == 'nt' else 'clear') # Rensar konsolfönstret beroende på operativsystem
products = load_data('db_products.csv') # Laddar data från din CSV-fil
while True: # Startar självaste huvudloopen för användarens interaktion med
    try:
        os.system('cls' if os.name == 'nt' else 'clear')

        print(view_products(products))  # Show ordered list of products # Visar den ordnade listan av produkter

        choice = input("Vill du (V)isa eller (T)a bort en produkt? ").strip().upper()

        if choice in ["V", "T"]:
            index = int(input("Enter product ID: "))
            
            if choice == "V":   #visa product
                if 1 <= index <= len(products):  # Ensure the index is within the valid range
                    selected_product = products[index - 1]  # Get the product using the list index
                    id = selected_product['id']  # Extract the actual ID of the product
                    print(view_product(products, id))  # Remove product using the actual ID
                    done = input()
                    
                else:
                    print("Ogiltig produkt")
                    sleep(0.3)

            elif choice == "T": #ta bort producterna
                if 1 <= index <= len(products):  # Ensure the index is within the valid range
                    selected_product = products[index - 1]  # Get the product using the list index
                    id = selected_product['id']  # Extract the actual ID of the product

                    print(remove_product(products, id))  # Remove product using the actual ID
                    sleep(0.5)            

                else:
                    print("Ogiltig produkt")
                    sleep(0.3)
        
    except ValueError:
        print("Välj en produkt med siffor")
        sleep(0.5)
