import tkinter as tk
from tkinter import scrolledtext, filedialog
import hashlib

class HashCollisionApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Hash Collision Checker")

        self.message1_label = tk.Label(master, text="Message 1:")
        self.message1_label.grid(row=0, column=0, padx=10, pady=(10, 0), sticky="w")

        self.message1_text = scrolledtext.ScrolledText(master, height=5, width=60)
        self.message1_text.grid(row=1, column=0, padx=10, pady=(0, 10))

        self.browse_button1 = tk.Button(master, text="Browse", command=lambda: self.browse_file(self.message1_text))
        self.browse_button1.grid(row=2, column=0, padx=10, pady=(0, 10), sticky="w")

        self.message2_label = tk.Label(master, text="Message 2:")
        self.message2_label.grid(row=3, column=0, padx=10, pady=(10, 0), sticky="w")

        self.message2_text = scrolledtext.ScrolledText(master, height=5, width=60)
        self.message2_text.grid(row=4, column=0, padx=10, pady=(0, 10))

        self.browse_button2 = tk.Button(master, text="Browse", command=lambda: self.browse_file(self.message2_text))
        self.browse_button2.grid(row=5, column=0, padx=10, pady=(0, 10), sticky="w")

        self.check_button = tk.Button(master, text="Check Collision", command=self.check_collision)
        self.check_button.grid(row=6, column=0, padx=10, pady=(10, 10))

        self.result_label = tk.Label(master, text="Collision Result:")
        self.result_label.grid(row=7, column=0, padx=10, pady=(10, 0), sticky="w")

        self.result_text = tk.Text(master, height=5, width=60, state=tk.DISABLED)
        self.result_text.grid(row=8, column=0, padx=10, pady=(0, 10))

    def browse_file(self, text_widget):
        file_path = filedialog.askopenfilename()
        if file_path:
            with open(file_path, "r") as file:
                content = file.read()
                text_widget.delete("1.0", tk.END)
                text_widget.insert(tk.END, content)

    def calculate_hashes(self, message):
        md5_hash = hashlib.md5(message.encode("utf-8")).hexdigest()
        sha1_hash = hashlib.sha1(message.encode("utf-8")).hexdigest()
        return md5_hash, sha1_hash

    def check_collision(self):
        message1 = self.message1_text.get("1.0", tk.END)
        message2 = self.message2_text.get("1.0", tk.END)

        md5_hash1, sha1_hash1 = self.calculate_hashes(message1)
        md5_hash2, sha1_hash2 = self.calculate_hashes(message2)

        md5_collision = md5_hash1 == md5_hash2
        sha1_collision = sha1_hash1 == sha1_hash2

        collision_result = f"MD5 Collision: {'Yes' if md5_collision else 'No'}\n" \
                           f"SHA-1 Collision: {'Yes' if sha1_collision else 'No'}"

        self.result_text.config(state=tk.NORMAL)
        self.result_text.delete("1.0", tk.END)
        self.result_text.insert(tk.END, collision_result)
        self.result_text.config(state=tk.DISABLED)

if __name__ == "__main__":
    root = tk.Tk()
    app = HashCollisionApp(root)
    root.mainloop()
