import random

class Father:
    def __init__(self, blood_types):
        self.blood_types = blood_types.upper()  # contoh: "AO", "AB", dll.

class Mother:
    def __init__(self, blood_types):
        self.blood_types = blood_types.upper()

class Child:
    def __init__(self, father, mother):
        self.allele_from_father = random.choice(father.blood_types)
        self.allele_from_mother = random.choice(mother.blood_types)
        self.blood_type = self.determine_blood_type()

    def determine_blood_type(self):
        alleles = self.allele_from_father + self.allele_from_mother
        if 'A' in alleles and 'B' in alleles:
            return 'AB'
        elif 'A' in alleles:
            return 'A'
        elif 'B' in alleles:
            return 'B'
        else:
            return 'O'

    def __str__(self):
        return (f"Alel dari Ayah: {self.allele_from_father}\n"
                f"Alel dari Ibu: {self.allele_from_mother}\n"
                f"Golongan darah anak: {self.blood_type}")

# Contoh penggunaan
ayah = Father(input("Masukkan alel golongan darah Ayah (misal AO, AB, OO): "))
ibu = Mother(input("Masukkan alel golongan darah Ibu (misal BO, AA, OO): "))
anak = Child(ayah, ibu)
print(anak)
