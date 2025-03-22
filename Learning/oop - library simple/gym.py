# gym.py

# 1. Definisikan class Member
class Member:
    def __init__(self, name, membership_type="Basic"):
        self.name = name
        self.membership_type = membership_type  # "Basic" atau "Premium"

    def upgrade_membership(self):
        if self.membership_type == "Basic":
            self.membership_type = "Premium"
            return f"{self.name} telah di-upgrade ke Premium."
        return f"{self.name} sudah memiliki membership Premium."

    def downgrade_membership(self):
        if self.membership_type == "Premium":
            self.membership_type = "Basic"
            return f"{self.name} telah di-downgrade ke Basic."
        return f"{self.name} sudah memiliki membership Basic."

    def __str__(self):
        return f"Nama: {self.name}, Membership: {self.membership_type}"


# 2. Definisikan class Gym
class Gym:
    def __init__(self):
        self.members = []  # List untuk menyimpan anggota gym

    def add_member(self, member):
        self.members.append(member)
        print(f"Anggota '{member.name}' telah ditambahkan ke gym.")

    def list_members(self):
        print("\nDaftar Anggota Gym:")
        if not self.members:
            print("Tidak ada anggota terdaftar.")
        else:
            for member in self.members:
                print(member)

    def upgrade_member(self, name):
        for member in self.members:
            if member.name == name:
                print(member.upgrade_membership())
                return
        print(f"Anggota '{name}' tidak ditemukan.")

    def downgrade_member(self, name):
        for member in self.members:
            if member.name == name:
                print(member.downgrade_membership())
                return
        print(f"Anggota '{name}' tidak ditemukan.")

    def remove_member(self, name):
        for member in self.members:
            if member.name == name:
                self.members.remove(member)
                print(f"Anggota '{name}' telah dihapus dari gym.")
                return
        print(f"Anggota '{name}' tidak ditemukan.")


# 3. Fungsi utama untuk mengetes kode
if __name__ == "__main__":
    gym = Gym()

    # Tambahkan beberapa anggota
    member1 = Member("Andi")
    member2 = Member("Budi", "Premium")
    member3 = Member("Citra")

    gym.add_member(member1)
    gym.add_member(member2)
    gym.add_member(member3)

    # Tampilkan daftar anggota
    gym.list_members()

    # Coba upgrade dan downgrade
    gym.upgrade_member("Citra")
    gym.downgrade_member("Budi")

    # List ulang setelah perubahan
    gym.list_members()

    # Hapus anggota
    gym.remove_member("Andi")

    # List ulang setelah penghapusan
    gym.list_members()
