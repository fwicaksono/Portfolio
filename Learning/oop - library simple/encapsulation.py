class BankAccount:
    def __init__(self, account_number, balance):
        self.account_number = account_number  # Public attribute
        self.__balance = balance  # Private attribute (tidak bisa diakses langsung)

    def deposit(self, amount):
        """Menambah saldo"""
        if amount > 0:
            self.__balance += amount
            return f"Saldo bertambah: {amount}"
        return "Jumlah harus lebih dari 0"

    def withdraw(self, amount):
        """Mengurangi saldo dengan batasan"""
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            return f"Berhasil tarik tunai: {amount}"
        return "Saldo tidak mencukupi"

    def get_balance(self):
        """Getter untuk saldo"""
        return self.__balance

# Pemakaian
account = BankAccount("123456", 1000)

# Tidak bisa akses langsung karena private:
# print(account.__balance)  # AttributeError!

# Bisa akses dengan metode yang disediakan:
print(account.get_balance())  # ✅ 1000
print(account.deposit(500))   # ✅ Saldo bertambah: 500
print(account.withdraw(300))  # ✅ Berhasil tarik tunai: 300
print(account.get_balance())  # ✅ 1200
