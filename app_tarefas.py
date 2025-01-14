import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from tkinter import filedialog
import pandas as pd
import os

FILENAME = "tasks.xlsx"

tasks = pd.DataFrame()

def load_tasks():
    """Carrega as tarefas do arquivo Excel, ou cria um arquivo padrão se não existir."""
    if not os.path.exists(FILENAME):
        df = pd.DataFrame(columns=["ID", "Tarefa", "Status"])
        df.to_excel(FILENAME, index=False, engine='openpyxl')
    else:
        df = pd.read_excel(FILENAME)
    return df

def save_tasks(df):
    """Salva as tarefas no arquivo Excel."""
    df.to_excel(FILENAME, index=False, engine='openpyxl')

def save_as_file():
    """Permite ao usuário salvar o arquivo em um local diferente."""
    filepath = filedialog.asksaveasfilename(defaultextension=".xlsx", 
                                            filetypes=[("Excel files", "*.xlsx")])
    if filepath:
        tasks.to_excel(filepath, index=False, engine='openpyxl')
        messagebox.showinfo("Salvo", f"Tarefas salvas em: {filepath}")

def refresh_tasks():
    """Atualiza a exibição das tarefas na interface gráfica."""
    for row in tree.get_children():
        tree.delete(row)

    for _, row in tasks.iterrows():
        tree.insert("", tk.END, values=(row["ID"], row["Tarefa"], row["Status"]))

def add_task():
    """Adiciona uma nova tarefa com confirmação do usuário."""
    global tasks 
    task_name = task_entry.get()
    if not task_name.strip():
        messagebox.showerror("Erro", "O nome da tarefa não pode estar vazio!")
        return

    if not messagebox.askyesno("Confirmação", f"Você deseja adicionar a tarefa: '{task_name}'?"):
        return

    new_id = tasks["ID"].max() + 1 if not tasks.empty else 1
    new_task = {"ID": new_id, "Tarefa": task_name.strip(), "Status": "Pendente"}
    tasks.loc[len(tasks)] = new_task
    save_tasks(tasks)
    refresh_tasks()
    task_entry.delete(0, tk.END)

def edit_task():
    """Edita uma tarefa selecionada."""
    global tasks 
    selected_item = tree.selection()
    if not selected_item:
        messagebox.showerror("Erro", "Nenhuma tarefa selecionada!")
        return

    task_id = int(tree.item(selected_item)["values"][0])
    current_name = tasks.loc[tasks["ID"] == task_id, "Tarefa"].values[0]

    def save_edited_task():
        new_name = edit_entry.get()
        if not new_name.strip():
            messagebox.showerror("Erro", "O nome da tarefa não pode estar vazio!")
            return

        if not messagebox.askyesno("Confirmação", f"Você deseja alterar a tarefa '{current_name}' para '{new_name}'?"):
            return

        tasks.loc[tasks["ID"] == task_id, "Tarefa"] = new_name.strip()
        save_tasks(tasks)
        refresh_tasks()
        edit_window.destroy()

    edit_window = tk.Toplevel(root)
    edit_window.title("Editar Tarefa")
    edit_window.geometry("400x200")
    edit_window.resizable(False, False)

    tk.Label(edit_window, text="Editar Tarefa:", font=("Arial", 14)).pack(pady=10)
    edit_entry = tk.Entry(edit_window, width=30, font=("Arial", 14))
    edit_entry.insert(0, current_name)
    edit_entry.pack(pady=10)

    tk.Button(edit_window, text="Salvar", font=("Arial", 12), command=save_edited_task).pack(pady=10)

def remove_task():
    """Remove a tarefa selecionada com confirmação do usuário."""
    global tasks 
    selected_item = tree.selection()
    if not selected_item:
        messagebox.showerror("Erro", "Nenhuma tarefa selecionada!")
        return

    task_id = int(tree.item(selected_item)["values"][0])
    task_name = tasks.loc[tasks["ID"] == task_id, "Tarefa"].values[0]

    if not messagebox.askyesno("Confirmação", f"Você deseja remover a tarefa: '{task_name}'?"):
        return

    tasks = tasks[tasks["ID"] != task_id]
    save_tasks(tasks)
    refresh_tasks()

def change_status():
    """Permite alterar o status da tarefa selecionada."""
    global tasks
    selected_item = tree.selection()
    if not selected_item:
        messagebox.showerror("Erro", "Nenhuma tarefa selecionada!")
        return

    task_id = int(tree.item(selected_item)["values"][0])
    current_status = tasks.loc[tasks["ID"] == task_id, "Status"].values[0]

    def save_new_status():
        new_status = status_var.get()
        if not new_status.strip():
            messagebox.showerror("Erro", "O status não pode estar vazio!")
            return

        if not messagebox.askyesno("Confirmação", f"Você deseja alterar o status de '{current_status}' para '{new_status}'?"):
            return

        tasks.loc[tasks["ID"] == task_id, "Status"] = new_status.strip()
        save_tasks(tasks)
        refresh_tasks()
        status_window.destroy()

    status_window = tk.Toplevel(root)
    status_window.title("Alterar Status")
    status_window.geometry("400x200")
    status_window.resizable(False, False)

    tk.Label(status_window, text="Alterar Status:", font=("Arial", 14)).pack(pady=10)

    status_var = tk.StringVar(value=current_status)
    status_dropdown = ttk.Combobox(status_window, textvariable=status_var, font=("Arial", 12), state="readonly")
    status_dropdown['values'] = ("Pendente", "Em Progresso", "Concluído")
    status_dropdown.pack(pady=10)

    tk.Button(status_window, text="Salvar", font=("Arial", 12), command=save_new_status).pack(pady=10)

root = tk.Tk()
root.title("TaskMaster Pro")
root.geometry("700x500")
root.resizable(False, False)

style = ttk.Style()
style.theme_use("clam")
style.configure("Treeview", font=("Arial", 12), rowheight=25)
style.configure("Treeview.Heading", font=("Arial", 14, "bold"))
style.configure("TButton", font=("Arial", 12))

tasks = load_tasks()

title = tk.Label(root, text="TaskMaster Pro", font=("Arial", 20, "bold"), fg="#4A90E2")
title.pack(pady=10)

frame = tk.Frame(root)
frame.pack(pady=10)

task_entry = tk.Entry(frame, width=40, font=("Arial", 14))
task_entry.grid(row=0, column=0, padx=5, pady=5)

btn_add = ttk.Button(frame, text="Adicionar", command=add_task)
btn_add.grid(row=0, column=1, padx=5)

btn_edit = ttk.Button(frame, text="Editar", command=edit_task)
btn_edit.grid(row=1, column=0, pady=5)

btn_remove = ttk.Button(frame, text="Remover", command=remove_task)
btn_remove.grid(row=1, column=1, pady=5)

btn_change_status = ttk.Button(frame, text="Alterar Status", command=change_status)
btn_change_status.grid(row=2, column=0, pady=5)

btn_save_as = ttk.Button(frame, text="Salvar Como", command=save_as_file)
btn_save_as.grid(row=2, column=1, pady=5)

columns = ("ID", "Tarefa", "Status")
tree = ttk.Treeview(root, columns=columns, show="headings", height=15)
tree.heading("ID", text="ID")
tree.heading("Tarefa", text="Tarefa")
tree.heading("Status", text="Status")
tree.column("ID", width=50, anchor=tk.CENTER)
tree.column("Tarefa", width=500, anchor=tk.W)
tree.column("Status", width=100, anchor=tk.CENTER)
tree.pack(pady=10)

scrollbar = ttk.Scrollbar(root, orient=tk.VERTICAL, command=tree.yview)
tree.configure(yscroll=scrollbar.set)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

refresh_tasks()

root.mainloop()
