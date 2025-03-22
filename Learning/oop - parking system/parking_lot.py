import sys

# Pastikan encoding UTF-8 di Windows
if sys.platform.startswith("win"):
    import os
    os.system("chcp 65001 > nul")

class ParkingLot:
    def __init__(self, capacity):
        self.capacity = capacity
        self.vehicles = []

    def park_vehicle(self, vehicle):
        if len(self.vehicles) < self.capacity:
            vehicle.enter_parking()
            self.vehicles.append(vehicle)
            print(f"[✔] {vehicle.__class__.__name__} {vehicle.plate_number} masuk parkiran.")  # ✔ lebih aman
        else:
            print("[X] Parkiran penuh! Tidak bisa masuk.")

    def remove_vehicle(self, plate_number):
        for vehicle in self.vehicles:
            if vehicle.plate_number == plate_number:
                vehicle.exit_parking()
                fee = vehicle.calculate_parking_fee()
                self.vehicles.remove(vehicle)
                print(f"[✔] {vehicle.__class__.__name__} {plate_number} keluar parkiran. Biaya parkir: Rp {fee:,}")
                return
        print("[X] Kendaraan tidak ditemukan di parkiran.")

    def display_parking_status(self):
        print("\n=== Status Parkiran ===")
        if self.vehicles:
            for vehicle in self.vehicles:
                print(f"- {vehicle.__class__.__name__}: {vehicle.plate_number} (Masuk: {vehicle.entry_time.strftime('%H:%M')})")
        else:
            print("Parkiran kosong.")
        print("=======================")
