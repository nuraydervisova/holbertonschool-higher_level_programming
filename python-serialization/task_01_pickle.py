#!/usr/bin/env python3
import pickle

class CustomObject:
    def __init__(self, name, age, is_student):
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Is Student: {self.is_student}")

    def serialize(self, filename):
        """Obyektin vəziyyətini fayla yazır."""
        try:
            with open(filename, 'wb') as f:
                pickle.dump(self, f)
            print(f"Obyekt '{filename}' faylına yazıldı.")
        except Exception as e:
            print(f"Xəta baş verdi: {e}")

    @classmethod
    def deserialize(cls, filename):
        """Fayldan obyektin vəziyyətini oxuyur və obyekt yaradır."""
        try:
            with open(filename, 'rb') as f:
                obj = pickle.load(f)
            print(f"Obyekt '{filename}' faylından oxundu.")
            return obj
        except (FileNotFoundError, pickle.UnpicklingError) as e:
            print(f"Xəta baş verdi: {e}")
            return None

if __name__ == "__main__":
    # Orijinal obyektin yaradılması
    obj = CustomObject(name="John", age=25, is_student=True)
    print("Orijinal Obyekt:")
    obj.display()

    # Obyekti seriyalaşdırmaq
    obj.serialize("object.pkl")

    # Obyekti deserializasiya etmək
    new_obj = CustomObject.deserialize("object.pkl")
    if new_obj:
        print("\nDeserializasiya olunmuş Obyekt:")
        new_obj.display()
