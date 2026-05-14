# 📑 Curso: Lógica de Programação com Python

Bem-vindo ao repositório de aulas. Aqui você encontrará os conteúdos teóricos, códigos práticos e instruções para versionamento do seu aprendizado.

---

## 📅 Conteúdo Programático das Aulas

### Aula 1: Fundamentos e Variáveis
*   **Conceitos:** O que é lógica, algoritmos e compiladores.
*   **Prática:** Sintaxe básica do Python, tipos de dados (`str`, `int`, `float`, `bool`).
*   **Entrada/Saída:** Uso das funções `print()` e `input()`.

### Aula 2: Estruturas Condicionais
*   **Conceitos:** Tomada de decisão e operadores lógicos (`and`, `or`, `not`).
*   **Operadores de comparação:** `>`, `<`, `==`, `!=`, `>=`, `<=`.
*   **Prática:** Uso de `if`, `elif` e `else`.

### Aula 3: Estruturas de Repetição (Loops)
*   **Conceitos:** Automação de tarefas repetitivas.
*   **Loops:** Uso de `while` (repetição condicional) e `for` (iteração sobre sequências).
*   **Controle:** Comandos `break` e `continue`.

### Aula 4: Coleções de Dados (Listas)
*   **Conceitos:** Armazenamento de múltiplos valores em uma única variável.
*   **Prática:** Criação de listas, indexação, fatiamento e métodos (`append`, `remove`, `len`).

---

## 💻 Códigos de Exemplo

### Exemplo Aula 2: Verificador de Maioridade (Condicional)
```python
# Solicita a idade do usuário
idade = int(input("Digite a sua idade: "))

# Verifica a condição
if idade >= 18:
    print("Acesso liberado: Maior de idade.")
else:
    print("Acesso negado: Menor de idade.")
```

### Exemplo Aula 3: Tabuada Dinâmica (Loop For)
```python
# Solicita o número para calcular a tabuada
numero = int(input("Digite um número para ver a tabuada: "))

print(f"\nTabuada do {numero}:")
for i in range(1, 11):
    resultado = numero * i
    print(f"{numero} x {i} = {resultado}")
```

---

## 🚀 Guia de Comandos Git & GitHub

Utilize estes comandos no terminal para enviar seus códigos das aulas para o GitHub.

### 1. Configuração Inicial (Apenas na primeira vez)
```bash
git config --global user.name "Seu Nome"
git config --global user.email "seu-email@email.com"
```

### 2. Inicializando e Vinculando o Repositório
```bash
git init
git branch -M main
git remote add origin github.com
```

### 3. Enviando Códigos Diários (Fluxo de Trabalho)
```bash
# Passo 1: Verifica o status dos arquivos
git status

# Passo 2: Adiciona todos os arquivos modificados
git add .

# Passo 3: Salva as alterações com uma mensagem explicativa
git commit -m "Doc: Adicionado códigos da Aula 02 sobre estruturas condicionais"

# Passo 4: Envia os arquivos para o GitHub
git push -u origin main
```

---
💡 *Dica: Mantenha seu repositório atualizado após cada aula para criar seu portfólio!*
