# 💧  Controle de Níveis de Água

Um sistema simples via terminal para simular o monitoramento de um reservatório de água, emitindo alertas visuais coloridos conforme o nível de risco.

---

## 🛠️ Tecnologias 
<img width="48" height="48" alt="Python" src="https://github.com/user-attachments/assets/290dee08-55dc-467e-8e7a-c50aff5bb869" /> 
<img width="48" height="48" alt="Vscode" src="https://github.com/user-attachments/assets/6e49349f-02ce-4bb7-921b-c081ec378c88" /> 
<img width="48" height="48" alt="GIT" src="https://github.com/user-attachments/assets/3f419076-3161-42c1-80a8-55ad8c3037ac" /> 

## 📋 Descrição

Este programa foi desenvolvido em Python com o objetivo de praticar o uso de **listas**, **funções** e **bibliotecas externas**. O sistema avalia o nível de água (de 1 a 5) e exibe uma mensagem de alerta no terminal com a cor correspondente ao risco, facilitando a visualização rápida da situação.

O projeto utiliza a biblioteca `colorama` para colorir a saída no terminal e garantir que o estilo seja restaurado ao final da execução.

---

## ⚡ Funcionalidades

- ✅ Avaliação de 5 níveis de alerta (Crítico a Alerta).
- ✅ Exibição de mensagens coloridas de acordo com o nível.
- ✅ Tratamento de níveis inválidos (fora do intervalo de 1 a 5).
- ✅ Restauração automática da cor padrão do terminal (evita que o terminal fique "pintado").
- ✅ Código organizado em função reutilizável.

---

## 🚀 Como executar

### Pré-requisitos
- Python 3.x instalado.
- Biblioteca `colorama` instalada.

### Passo a passo

1. **Clone o repositório:**
   ```bash
   git clone https://github.com/seuusuario/controle-niveis-agua.git
    ```
2. **Acesse a pasta do projeto:**
   ```bash
   cd controle-niveis-agua
   ```
3. **Execute o programa:**
   ```bash
   python app.py
   ```
---

## ⚙️ Como o sistema funciona

| Nível | Situação | Mensagem Exibida | Cor no Terminal |
| :---: | :--- | :--- | :--- |
| **Nível 1** | Muito baixo (crítico) | Nível 1 - Muito baixo (crítico) | 🔴 Vermelho (`Fore.RED`) |
| **Nível 2** | Baixo | Nível 2 - Baixo | 🟡 Amarelo (`Fore.YELLOW`) |
| **Nível 3** | Médio | Nível 3 - Médio | 🟢 Verde (`Fore.GREEN`) |
| **Nível 4** | Alto | Nível 4 - Alto | 🔵 Ciano (`Fore.CYAN`) |
| **Nível 5** | Muito alto (alerta) | Nível 5 - Muito alto (alerta) | 🔵 Azul (`Fore.BLUE`) |
| **Outro** | Inválido | Nível inválido | ⚪ Padrão do sistema |

--- 

## 📊 Exemplo de uso

exibir_alerta(1) </br>
exibir_alerta(4)  </br>
exibir_alerta(10) </br>

**Saída no terminal:** </br>
(Mensagem 1 em Vermelho) </br>
Nível 1 - Muito baixo (crítico)</br>

(Mensagem 4 em Ciano)</br>
Nível 4 - Alto</br>

(Mensagem de erro)</br>
Nível inválido</br>

(O terminal retorna à cor padrão branca/cinza logo em seguida).

## 🧠 Conceitos Aplicados

Durante o desenvolvimento deste projeto, foram aplicados os seguintes conceitos de programação:

- **Listas (`list`):** Utilizadas para armazenar os níveis e as mensagens de alerta de forma organizada. Acessamos os dados por meio de seus índices.
- **Funções (`def`):** A lógica de verificação e exibição foi isolada na função `exibir_alerta(nivel)`. Isso torna o código reutilizável, organizado e mais fácil de dar manutenção.
- **Estruturas Condicionais (`if`, `elif`, `else`):** Empregadas dentro da função para avaliar qual nível foi recebido e definir qual ação (cor e mensagem) deve ser tomada para cada caso, incluindo o tratamento de erros (nível inválido).
- **Bibliotecas Externas (`import`):** Integração com a biblioteca `colorama` para manipulação de cores no terminal, explorando conceitos de código ANSI de forma facilitada.
- **Boas Práticas:** Uso do `Style.RESET_ALL` para garantir a restauração do terminal e isolamento de responsabilidades (a função é autossuficiente, exibindo, colorindo e limpando).

## 👤 Autor

**Raul Barbosa**

- GitHub: [@oraulbarbosa](https://github.com/oraulbarbosa)

## 📄 Licença

Este projeto está sob a licença MIT.
