import customtkinter as ctk
from tkinter import filedialog, messagebox
from encrypt import encrypt_file
from decrypt import decrypt_file
import os

class CryptoApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Secure File Storage System")
        self.geometry("500x400")
        ctk.set_appearance_mode("dark")
        
        # UI Styling (Monochrome / Tactical)
        self.grid_columnconfigure(0, weight=1)
        self.selected_file = None

        self.label = ctk.CTkLabel(self, text="FILE SECURITY SYSTEM", font=("Consolas", 20, "bold"))
        self.label.pack(pady=20)

        # File Selection
        self.btn_select = ctk.CTkButton(self, text="SELECT FILE", fg_color="transparent", border_width=2, 
                                        command=self.select_file)
        self.btn_select.pack(pady=10)

        self.file_label = ctk.CTkLabel(self, text="No file selected", font=("Consolas", 12))
        self.file_label.pack(pady=5)

        # Password Input
        self.pass_entry = ctk.CTkEntry(self, placeholder_text="Enter Password", show="*", width=300)
        self.pass_entry.pack(pady=20)

        # Action Buttons
        self.btn_encrypt = ctk.CTkButton(self, text="ENCRYPT", command=self.run_encryption, fg_color="#222", hover_color="#333")
        self.btn_encrypt.pack(side="left", padx=50, pady=20)

        self.btn_decrypt = ctk.CTkButton(self, text="DECRYPT", command=self.run_decryption, fg_color="#222", hover_color="#333")
        self.btn_decrypt.pack(side="right", padx=50, pady=20)

    def select_file(self):
        self.selected_file = filedialog.askopenfilename()
        if self.selected_file:
            self.file_label.configure(text=os.path.basename(self.selected_file))

    def run_encryption(self):
        if not self.selected_file or not self.pass_entry.get():
            messagebox.showwarning("Input Error", "Please select a file and enter a password.")
            return
        
        try:
            path = encrypt_file(self.selected_file, self.pass_entry.get())
            messagebox.showinfo("Success", f"File Encrypted!\nSaved to: {path}")
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def run_decryption(self):
        if not self.selected_file or not self.pass_entry.get():
            messagebox.showwarning("Input Error", "Please select a file and enter a password.")
            return

        try:
            path, integrity = decrypt_file(self.selected_file, self.pass_entry.get())
            status = "Verified" if integrity else "FAILED"
            messagebox.showinfo("Success", f"File Decrypted!\nIntegrity: {status}\nSaved to: {path}")
        except Exception as e:
            messagebox.showerror("Error", f"Decryption failed: {str(e)}")

if __name__ == "__main__":
    app = CryptoApp()
    app.mainloop()