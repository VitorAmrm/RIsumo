import tkinter as tk
from tkinter import ttk, filedialog, messagebox
from extrativo import gerar_resumo_extrativo
from abstrativo import gerar_resumo_abstrativo
from nuvem_module import gerar_nuvem_palavras

# Função para chamar a geração da nuvem
def selecionar_arquivo():
    # Selecionar arquivo
    filepath = filedialog.askopenfilename(
        title="Selecione o arquivo de texto",
        filetypes=(("Arquivos de texto", "*.txt"), ("Todos os arquivos", "*.*"))
    )
    if not filepath:
        return

    # Selecionar onde salvar a nuvem de palavras
    output_path = filedialog.asksaveasfilename(
        title="Salvar Nuvem de Palavras",
        defaultextension=".png",
        filetypes=(("Imagem PNG", "*.png"),)
    )
    if not output_path:
        return

    try:
        # Obter palavras adicionais a serem removidas
        palavras_extras = caixa_palavras.get("1.0", tk.END).strip().split(",")
        palavras_extras = [p.strip() for p in palavras_extras if p.strip()]  # Remover espaços em branco

        # Obter quantidade máxima de palavras
        try:
            max_palavras = int(caixa_quantidade.get())
            if max_palavras <= 0:
                raise ValueError
        except ValueError:
            messagebox.showerror("Erro", "Por favor, insira um número válido para a quantidade de palavras.")
            return

        # Gerar nuvem de palavras
        gerar_nuvem_palavras(filepath, output_path, palavras_extras, max_palavras)
        messagebox.showinfo("Sucesso", f"Nuvem de palavras salva em:\n{output_path}")
    except Exception as e:
        messagebox.showerror("Erro", f"Erro ao gerar nuvem de palavras:\n{e}")

# Função para gerar resumo extrativo
def gerar_resumo_extrativo_fun():
    texto = caixa_texto_extrativo.get("1.0", tk.END)
    resumo = gerar_resumo_extrativo(texto)
    caixa_resumo_extrativo.delete("1.0", tk.END)
    caixa_resumo_extrativo.insert(tk.END, resumo)

# Função para gerar resumo abstrativo
def gerar_resumo_abstrativo_fun():
    texto = caixa_texto_abstrativo.get("1.0", tk.END)
    resumo = gerar_resumo_abstrativo(texto)
    caixa_resumo_abstrativo.delete("1.0", tk.END)
    caixa_resumo_abstrativo.insert(tk.END, resumo)

# Configuração da interface
def main():
    global caixa_palavras, caixa_quantidade, caixa_texto_extrativo, caixa_resumo_extrativo, caixa_texto_abstrativo, caixa_resumo_abstrativo

    # Criação da janela principal
    root = tk.Tk()
    root.title("Gerador de Resumo e Nuvem de Palavras")
    root.geometry("700x500")

    # Notebook (abas)
    notebook = ttk.Notebook(root)
    notebook.pack(fill='both', expand=True)

    # Aba de Resumo Extrativo
    aba_extrativo = ttk.Frame(notebook)
    notebook.add(aba_extrativo, text="Resumo Extrativo")
    
    caixa_texto_extrativo = tk.Text(aba_extrativo, height=10, width=50)
    caixa_texto_extrativo.pack(pady=10)

    caixa_resumo_extrativo = tk.Text(aba_extrativo, height=10, width=50)
    caixa_resumo_extrativo.pack(pady=10)
    
    botao_extrativo = tk.Button(aba_extrativo, text="Gerar Resumo Extrativo", command=gerar_resumo_extrativo_fun)
    botao_extrativo.pack(pady=10)

    # Aba de Resumo Abstrativo
    aba_abstrativo = ttk.Frame(notebook)
    notebook.add(aba_abstrativo, text="Resumo Abstrativo")
    
    caixa_texto_abstrativo = tk.Text(aba_abstrativo, height=10, width=50)
    caixa_texto_abstrativo.pack(pady=10)

    caixa_resumo_abstrativo = tk.Text(aba_abstrativo, height=10, width=50)
    caixa_resumo_abstrativo.pack(pady=10)
    
    botao_abstrativo = tk.Button(aba_abstrativo, text="Gerar Resumo Abstrativo", command=gerar_resumo_abstrativo_fun)
    botao_abstrativo.pack(pady=10)

    # Aba de Nuvem de Palavras
    aba_wordcloud = ttk.Frame(notebook)
    notebook.add(aba_wordcloud, text="Nuvem de Palavras")

    # Caixa de texto para palavras adicionais
    lbl_palavras = tk.Label(aba_wordcloud, text="Palavras adicionais a remover (separadas por vírgulas):")
    lbl_palavras.pack(pady=5)

    caixa_palavras = tk.Text(aba_wordcloud, height=5, width=50)
    caixa_palavras.pack(pady=5)

    # Caixa para quantidade de palavras
    lbl_quantidade = tk.Label(aba_wordcloud, text="Quantidade máxima de palavras na nuvem:")
    lbl_quantidade.pack(pady=5)

    caixa_quantidade = tk.Entry(aba_wordcloud, width=10)
    caixa_quantidade.pack(pady=5)
    caixa_quantidade.insert(0, "100")  # Valor padrão
    
    # Botão para selecionar arquivo e gerar a nuvem
    btn_selecionar = tk.Button(
        aba_wordcloud, text="Selecionar Arquivo de Texto", command=selecionar_arquivo, height=2, width=30
    )
    btn_selecionar.pack(pady=10)

    root.mainloop()

if __name__ == "__main__":
    main()
