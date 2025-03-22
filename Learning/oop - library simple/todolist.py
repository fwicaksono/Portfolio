# todo.py

# 1. Definisikan class Task
class Task:
    def __init__(self, title, description):
        # Simpan judul dan deskripsi tugas, serta status (default: belum selesai)
        self.title = title
        self.description = description
        self.is_done = "Not Completed"
        
    def mark_completed(self):
        if self.is_done == "Not Completed":
            self.is_done = "Completed"
        return f"{self.title} is already Completed"
            
    
    def mark_pending(self):
        # ubah status tugas menjadi belum selesai
        self.is_done = "Completed"
        if self.is_done == "Completed":
            self.is_done = "Not Completed"
        return f"{self.title} is Not Completed"

    def __str__(self):
        # Kembalikan string "Tugas: <judul>, Status: <Selesai/Belum>"
        return f"{self.title}, status : {self.is_done}"


# 2. Definisikan class TaskManager
class TaskManager:
    def __init__(self):
        # Buat daftar tugas sebagai list kosong
        self.to_do_list = []
        
    def add_task(self, task):
        # Tambahkan tugas baru ke daftar
        self.to_do_list.append(task)
        print(f"Task '{task.title}' telah ditambahkan ke to-do list.")

        
    def list_tasks(self):
        # Tampilkan semua tugas beserta statusnya
        print("Daftar To-Do List :")
        if not self.to_do_list:
            print("tidak ada task")
        else:
            for task in self.to_do_list:
                print(task)

    def complete_task(self, title):
        # Cari tugas berdasarkan judul dan tandai sebagai selesai
        for task in self.to_do_list:
            if task.title == title:
                print(task.mark_completed())
            return
        print(f"task '{title}' tidak ditemukan di list.")

    def remove_task(self, title):
        # Hapus tugas berdasarkan judul
        for task in self.to_do_list:
            if task.title == title:
                self.to_do_list.remove(task)
                print(f"task '{title}' telah dihapus dari list.")
                return
        print (f"task {title} tidak ditemukan")


# 3. Fungsi utama untuk mengetes kode
if __name__ == "__main__":
    # Buat objek TaskManager
    to_do_list = TaskManager()
    
    # Tambahkan beberapa tugas
    task1 = Task("Apply Job", "Apply ke linkedin dan nulis di excel")
    to_do_list.add_task(task1)
    task2 = Task("Revisi Skripsi", "Revisi")
    to_do_list.add_task(task2)
    
    # Tampilkan list tugas
    to_do_list.list_tasks()
    
    # Coba tandai tugas selesai dan hapus tugas
    to_do_list.complete_task("Apply Job")
    to_do_list.remove_task("Revisi Skripsi")
    
