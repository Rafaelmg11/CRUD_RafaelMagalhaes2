import tkinter as tk
from tkinter import messagebox
from crud import create_user, read_users, update_user, delete_user

# C = Create
# R = Read
# U = Update
# D = Delete

class CRUDApp:
    def __init__(self, root):
        self.root = root
        self.root.title("CRUD USUÁRIOS")
        
        # Criação de Widgets
        
        self.create_widgets()
    
    def create_widgets(self):

        #Label
        tk.Label(self.root, text = "Nome: ").grid (row = 0, column = 0)
        tk.Label(self.root, text = "Telefone: ").grid (row = 1, column = 0)
        tk.Label(self.root, text = "E-mail: ").grid (row = 2, column = 0)
        tk.Label(self.root, text = "Usuario: ").grid (row = 3, column = 0)
        tk.Label(self.root, text = "Senha: ").grid (row = 4, column = 0)

        tk.Label(self.root, text = "UserID(for update/delete): ").grid (row = 5, column = 0)

        # CRIAR AS CAIXAS PARA DIGITAR OS VALORES E POSICIONAR

        self.nome_entry = tk.Entry(self.root)
        self.telefone_entry = tk.Entry(self.root)
        self.email_entry = tk.Entry(self.root)
        self.usuario_entry = tk.Entry(self.root)
        self.senha_entry = tk.Entry(self.root)
        self.userID_entry = tk.Entry(self.root)

        self.nome_entry.grid(row = 0, column = 1)
        self.telefone_entry.grid(row = 1, column = 1)
        self.email_entry.grid(row = 2, column = 1)
        self.usuario_entry.grid(row = 3, column = 1)
        self.senha_entry.grid(row = 4, column = 1)
        self.userID_entry.grid(row = 5, column = 1)


        # BOTÕES DO CRUID

        tk.Button(self.root, text = "Criar usuário", command = self.create_user).grid(row = 6, column = 0, columnspan = 1)
        tk.Button(self.root, text = "Listar usuário", command = self.read_users).grid(row = 6, column = 1, columnspan = 1)
        tk.Button(self.root, text = "Alterar usuário", command = self.update_user).grid(row = 7, column = 0, columnspan = 1)
        tk.Button(self.root, text = "Excluir usuário", command = self.delete_user).grid(row = 7, column = 1, columnspan = 1)

    def create_user(self):

        nome = self.nome_entry.get()
        telefone = self.telefone_entry.get()
        email = self.email_entry.get()
        usuario = self.usuario_entry.get()
        senha = self.senha_entry.get()

        if nome and telefone and email and usuario and senha:
            create_user(nome, telefone, email, usuario, senha)
            self.nome_entry.delete(0, tk.END)
            self.telefone_entry.delete(0, tk.END)
            self.email_entry.delete(0, tk.END)
            self.usuario_entry.delete(0, tk.END)
            self.senha_entry.delete(0, tk.END)
            messagebox.showerror("Success", "Usuario criado com sucesso!")
        else:
            messagebox.showerror("Error","Todos os campos são obrigatórios")

    def read_users(self):

        users = read_users()
        self.text_area.delete(1.0, tk.END)
        for user in users:
            self.text_area.insert(tk.END, f"ID: {user[0]}, Nome: {user[1]}, Telefone: {user[2]}, E-mail: {user[3]}\n")

    def update_user(self):

        userID = self.userID_entry.get()
        nome = self.nome_entry.get()
        telefone = self.telefone_entry.get()
        email = self.email_entry.get()
        usuario = self.usuario_entry.get()
        senha = self.senha_entry.get()

        if userID and nome and telefone and email and usuario and senha:
            update_user(nome, telefone, email, usuario, senha, userID)
            self.nome_entry.delete(0,tk.END)
            self.telefone_entry.delete(0,tk.END)
            self.email_entry.delete(0,tk.END)
            self.usuario_entry.delete(0,tk.END)
            self.senha_entry.delete(0,tk.END)
            messagebox.showerror("Success", "Usuario alterado com sucesso!")
        else:
            messagebox.showerror("Error","Todos os campos são obrigatórios")

    def delete_user(self):

        userID = self.userID_entry.get()
        if userID:
            delete_user(userID)
            self.userID_entry.delete(0, tk.END)
            messagebox.showerror("Success","Usuário excluido com sucesso!")
        else:
            messagebox.showerror("Error","O ID do Usuário é obrigatório!")

if __name__ == "__main__":
    root = tk.Tk()
    app = CRUDApp(root)
    root.mainloop()