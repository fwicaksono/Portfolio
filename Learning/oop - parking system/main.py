import time
from parking_lot import ParkingLot
from vehicle import Car, Motorcycle

# Inisialisasi parkiran dengan kapasitas 3 kendaraan
parking_lot = ParkingLot(capacity=3)

# Buat kendaraan
car1 = Car("B 1234 AB")
bike1 = Motorcycle("D 5678 XY")

# Simulasi parkir kendaraan
parking_lot.park_vehicle(car1)
parking_lot.park_vehicle(bike1)

# Simulasi kendaraan berada di parkiran selama 2 detik (seharusnya 2 jam untuk real case)
time.sleep(3)

# Tampilkan status parkiran
parking_lot.display_parking_status()

# Mengeluarkan kendaraan (biaya dihitung berdasarkan waktu masuk dan keluar)
parking_lot.remove_vehicle("B 1234 AB")
parking_lot.remove_vehicle("D 5678 XY")

# Tampilkan status parkiran setelah kendaraan keluar
parking_lot.display_parking_status()
