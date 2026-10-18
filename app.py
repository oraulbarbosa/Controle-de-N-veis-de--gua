# Controle de Níveis de Água

# BIBLIOTECA COLORAMA IMPORTADA
from colorama import Fore, Style

# LISTAS
niveis = ["Nível 1", "Nível 2", "Nível 3", "Nível 4", "Nível 5"]
mensagens = ["Muito baixo (crítico)", "Baixo", "Médio", "Alto", "Muito alto(alerta)"]

def exibir_alerta(nivel):
    if nivel == 1:
        print(Fore.RED + f"{niveis[0]} - {mensagens[0]}")
        
    elif nivel == 2:
        print(Fore.YELLOW + f"{niveis[1]} - {mensagens[1]}")
            
    elif nivel == 3:
        print(Fore.GREEN + f"{niveis[2]} - {mensagens[2]}")
           
    elif nivel == 4:
        print(Fore.CYAN + f"{niveis[3]} - {mensagens[3]}")
            
    elif nivel == 5:
        print(Fore.BLUE + f"{niveis[4]} - {mensagens[4]}")

    else:
        print("Nível inválido")

     # RESTAURA COR PADRÃO DO TERMINAL
    print(Style.RESET_ALL)

# VALOR SIMULADO

exibir_alerta(10)


























