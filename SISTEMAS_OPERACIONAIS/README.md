# 🖥️ Curso: Sistemas Operacionais & Segurança Cibernética

## 🗓️ Conteúdo Temático das Aulas

### 1. Introdução aos Sistemas Operacionais (SO)
*   **Conceito:** Gerenciamento de hardware e software.
*   **Interface:** Linha de comando (CLI) vs Interface Gráfica (GUI).
*   **Arquitetura:** Kernel, drivers e modo usuário/kernel.

### 2. Segurança Cibernética em SO
*   **Princípio do Menor Privilégio:** Limitação de acessos de usuários.
*   **Ameaças Comuns:** Malware, ransomware e engenharia social.
*   **Mecanismos de Defesa:** Criptografia de disco, firewalls e auditoria.
*   **Atualizações:** Importância do patch management contra exploits.

---

## 🪟 Ecossistema Windows

### 📁 Pastas Estruturais (Diretórios)
*   `C:\Windows`: Arquivos centrais do sistema operacional.
*   `C:\Windows\System32`: Bibliotecas cruciais (`.dll`) e executáveis do kernel.
*   `C:\Users`: Perfis, dados e configurações locais dos usuários.
*   `C:\Program Files`: Instalação de softwares nativos de 64 bits.

### ⚙️ Variáveis de Ambiente Comuns
*   `%USERPROFILE%`: Caminho da pasta do usuário logado.
*   `%WINDIR%`: Aponta para o diretório de instalação do Windows.
*   `%PATH%`: Lista de caminhos para execução de comandos diretos.

---

## 🐧 Ecossistema Linux (Foco: Debian)

### 📁 Pastas Estruturais (FHS - Filesystem Hierarchy Standard)
*   `/`: Diretório raiz que contém todo o sistema.
*   `/etc`: Arquivos de configuração globais do sistema.
*   `/home`: Diretórios pessoais dos usuários comuns.
*   `/var/log`: Registro de eventos e logs do sistema.
*   `/bin` e `/sbin`: Comandos essenciais do sistema e do superusuário.

### ⚙️ Variáveis de Ambiente Comuns
*   `$HOME`: Caminho do diretório do usuário atual.
*   `$USER`: Nome do usuário conectado no momento.
*   `$PATH`: Diretórios verificados ao digitar um comando.

### 🎯 Peculiaridades do Debian
*   **Estabilidade:** Foco em pacotes testados e homologados.
*   **Gerenciador APT:** Uso de `apt update` e `apt install` para softwares.
*   **Segurança:** Separação rígida entre conta `root` e usuários `sudo`.

