import tkinter as tk

class FolhaDePagamento:
    def __init__(self, master):
        self.master = master
        master.title("Folha de Pagamento")

        root.geometry("600x400")

        menu_bar = tk.Menu(root)
        root.config(menu=menu_bar)

        arquivo_menu = tk.Menu(menu_bar)
        menu_bar.add_cascade(label="Arquivo", menu=arquivo_menu)
        arquivo_menu.add_command(label="Sair", command=root.quit)

    
        self.label_salario = tk.Label(master, text="Salário:")
        self.label_salario.pack()

        self.entry_salario = tk.Entry(master)
        self.entry_salario.pack()

        self.label_dependentes = tk.Label(master, text="Número de dependentes:")
        self.label_dependentes.pack()

        self.entry_dependentes = tk.Entry(master)
        self.entry_dependentes.pack()

        self.button_calcular = tk.Button(master, text="Calcular", command=self.calcular)
        self.button_calcular.pack()

        self.label_resultado = tk.Label(master, text="")
        self.label_resultado.pack()

    def calcular(self):
        
        salario = float(self.entry_salario.get())
        dependentes = int(self.entry_dependentes.get())
        
        if salario <= 1100:
            inss = salario * 0.075
        elif salario <= 2203.48:
            inss = salario * 0.09
        elif salario <= 3305.22:
            inss = salario * 0.12
        elif salario <= 6433.57:
            inss = salario * 0.14
        else:
            inss = 751.97
        
        base_de_calculo = salario - inss - (dependentes * 189.59)

        if base_de_calculo <= 1903.98:
            irrf = 0
        elif base_de_calculo <= 2826.65:
            irrf = (base_de_calculo * 0.075) - 142.80
        elif base_de_calculo <= 3751.05:
            irrf = (base_de_calculo * 0.15) - 354.80
        elif base_de_calculo <= 4664.68:
            irrf = (base_de_calculo * 0.225) - 636.13
        else:
            irrf = (base_de_calculo * 0.275) - 869.36

       
        resultado = f"Salário líquido: R$ {salario - inss - irrf:.2f}"
        self.label_resultado.config(text=resultado)

        scrollbar = tk.Scrollbar(root)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)


root = tk.Tk()
app = FolhaDePagamento(root)
root.mainloop()