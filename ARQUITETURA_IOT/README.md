# 🌐 Curso: Arquitetura de Internet das Coisas (IoT) com Arduino, C++ e Python

## 📋 Ementa Geral
Este curso aborda a arquitetura de sistemas IoT dividida em camadas (Dispositivo, Redes e Nuvem). O foco prático utiliza o ecossistema Arduino programado em C++ para controle de hardware, e Python para automação, comunicação de rede, tratamento de dados e integração com brokers.

---

## 📅 Conteúdo Pragmático das Aulas

### 🛑 Módulo 1: Camada de Dispositivo (Hardware e C++)
* **Aula 01: Fundamentos da Arquitetura IoT**
  * Conceito de arquitetura em 3 e 4 camadas (Edge, Fog, Cloud).
  * O papel do Arduino na borda da rede.
* **Aula 02: Revisão de C++ para Microcontroladores**
  * Sintaxe essencial: Estrutura do código Arduino (`setup` e `loop`).
  * Gerenciamento de memória: Tipos de dados, ponteiros e escopo de variáveis em C++.
* **Aula 03: Sensores, Atuadores e Sinais**
  * Leitura analógica e digital com C++.
  * Controle de interrupções de hardware para economia de energia.
* **Aula 04: Comunicação Serial com Arduino**
  * Protocolos UART, I2C e SPI em nível de código.
  * Formatação de dados para envio via porta serial.

### 📶 Módulo 2: Camada de Conectividade (C++ e Python)
* **Aula 05: Integração Hardware-Software com Python**
  * Introdução à biblioteca `pySerial` no Python.
  * Leitura e processamento em Python dos dados enviados pelo Arduino.
* **Aula 06: Programação de Redes com Python**
  * Sockets TCP/UDP em Python para recepção de telemetria.
  * Estruturação de payloads em formato JSON.
* **Aula 07: Protocolo MQTT - O Padrão da Indústria**
  * Arquitetura Publish/Subscribe.
  * Configuração do cliente MQTT em C++ (Arduino) e em Python (`paho-mqtt`).
* **Aula 08: Protocolo HTTP e APIs REST**
  * Requisições POST/GET do Arduino para servidores.
  * Criação de uma API básica em Python (Flask ou FastAPI) para receber dados do ecossistema Arduino.

### ☁️ Módulo 3: Processamento de Dados e Dashboards (Python)
* **Aula 09: Armazenamento de Séries Temporais**
  * Conexão do script Python a bancos de dados (SQLite / InfluxDB).
  * Filtragem e limpeza de dados espúrios de sensores com a biblioteca `Pandas`.
* **Aula 10: Dashboards e Visualização Prática**
  * Integração de dados do Python com ferramentas de visualização (Streamlit ou Dash).
  * Criação de gráficos em tempo real de temperatura, umidade e status dos atuadores.

---

## 🛠️ Tecnologias e Ferramentas do Curso

### Hardware e Linguagem C++
* **Placa Principal:** Arduino Uno, Nano ou ESP32 (compatível com IDE Arduino).
* **Linguagem:** C++ (compilado via GCC/Avr-gcc).
* **IDE:** Arduino IDE ou VS Code com extensão PlatformIO.

### Servidor/Gateway e Linguagem Python
* **Ambiente:** Python 3.10+ (PC ou Raspberry Pi atuando como Gateway).
* **Bibliotecas Chave:**
  * `pySerial`: Comunicação direta com o Arduino.
  * `paho-mqtt`: Conectividade com brokers de mensageria.
  * `requests` / `fastapi`: Comunicação Web.
  * `pandas` / `matplotlib`: Manipulação e visualização de dados do sensor.

---

## 🎯 Atividades Práticas Obrigatórias
1. **Lab 1 (C++):** Leitura de um sensor de temperatura com tratamento de ruído via código C++.
2. **Lab 2 (C++ + Python):** Script Python que lê a porta serial do Arduino, valida o dado e salva em um arquivo CSV.
3. **Lab 3 (Arquitetura Completa):** Arduino envia dados via MQTT, um script Python consome esses dados em um servidor local e aciona um alerta visual caso ultrapasse um limite.
