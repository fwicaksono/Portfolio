"""
📌 PROJECT: Sistem Manajemen Kendaraan 🚗✈️🚢
-------------------------------------------------
🔹 Deskripsi Proyek:
Kamu akan membuat sistem manajemen kendaraan menggunakan konsep Object-Oriented Programming (OOP).
Sistem ini mencakup berbagai jenis kendaraan, termasuk mobil, pesawat, dan kapal.

🔹 Konsep OOP yang Dipelajari:
✅ Encapsulation (Membuat atribut privat)
✅ Inheritance (Pewarisan dari parent class ke subclass)
✅ Polymorphism (Method yang bisa berbeda untuk tiap subclass)
✅ Abstraction (Parent class abstrak untuk memastikan subclass memiliki method tertentu)

🔹 Tugas:
1️⃣ Tambahkan class `Motorcycle` yang memiliki method `wheel_count()`, mengembalikan jumlah roda (biasanya 2).
2️⃣ Buat daftar kendaraan dari input user, lalu cetak informasi kendaraan.
3️⃣ Gunakan `property` decorator agar atribut privat bisa diakses dengan cara yang lebih Pythonic.
"""

from abc import ABC, abstractmethod

# ✅ Abstraction: Class ini hanya sebagai template
class Vehicle(ABC):
    def __init__(self, brand, model, year):
        self.__brand = brand  # 🔒 Encapsulation: Atribut privat
        self.__model = model
        self.__year = year

    @abstractmethod
    def move(self):
        pass  # Harus diimplementasikan oleh subclass

    def get_info(self):
        return f"{self.__year} {self.__brand} {self.__model}"

# ✅ Inheritance: Subclass dari Vehicle
class Car(Vehicle):
    def move(self):
        return f"{self.get_info()} berjalan di jalan."

    def fuel_type(self):
        return "Menggunakan bensin atau listrik."

class Airplane(Vehicle):
    def move(self):
        return f"{self.get_info()} terbang di udara."

    def altitude(self):
        return "Dapat terbang hingga 35.000 kaki."

class Boat(Vehicle):
    def move(self):
        return f"{self.get_info()} berlayar di laut."

    def max_speed(self):
        return "Kecepatan maksimal 50 knot."

# ✅ Polymorphism: Semua class bisa diproses dengan cara yang sama
vehicles = [
    Car("Toyota", "Camry", 2022),
    Airplane("Boeing", "747", 2019),
    Boat("Yamaha", "Speedboat", 2021),
]

# ✅ Menampilkan informasi kendaraan
for vehicle in vehicles:
    print(vehicle.move())  # Memanggil move() sesuai classnya

# ✅ Memanggil method spesifik berdasarkan class
print(vehicles[0].fuel_type())  # ✅ Method dari Car
print(vehicles[1].altitude())   # ✅ Method dari Airplane
print(vehicles[2].max_speed())  # ✅ Method dari Boat


print(vehicles[0].__brand)