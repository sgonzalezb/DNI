from src.table import DataDNI
class Dni:

    letter_legnth = 1
    number_length = 8
    dni_length = 9


    def __init__(self, number):
        self.number = number

    def get_letter(self):
        position = self.number % DataDNI.table_length #El resto es la posición de la letra que debe usar.
        return DataDNI.letter_asign[position]
    
    def get_dni(self):
        return str(self.number) + self.get_letter() #Devuelve el DNI con la letra

    
    def validate_letter(self):
        letter = self.get_letter()
        if letter in DataDNI.letters_forbidden:
            return False
        else:
            return True

    def validate_dni(self):
        if (len(self.numbers == number_length) and len(self.get_dni) == dni_length ):
            return "DNI correcto"
        else:
            return "El DNI no es válido"