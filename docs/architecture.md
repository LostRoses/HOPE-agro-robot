# Arquitetura do Sistema

A arquitetura do robô móvel é dividida em quatro módulos principais, cada um responsável por funções específicas:

---

## 1️ Módulo de Controle
Responsável pelo processamento das decisões, acionamento dos motores e integração geral dos módulos.  
**Componentes**:
- Arduino Uno (controle de motores e sensores simples)
- ESP32-CAM (processamento auxiliar, câmera e conectividade)  

**Funções**:
- Executa a lógica de navegação e reação a obstáculos  
- Coordena sensores e atuadores  
- Sincroniza dados com o módulo de comunicação  

---

## 2️ Módulo de Sensores
Permite a captação de informações ambientais e espaciais.  
**Sensores**:
- HC-SR04 (ultrassônico) – mede distância para evitar colisões  
- Sensor de umidade do solo – coleta dados sobre irrigação  
- DHT22 ou BME280 (opcional) – temperatura e umidade do ar  

**Funções**:
- Monitorar microclima e condições do solo  
- Alimentar o sistema de decisão com variáveis ambientais  

---

## 3️ Módulo de Movimento
Permite que o robô se desloque com autonomia e reaja ao ambiente.  
**Componentes**:
- 4 motores DC com caixa de redução  
- Driver L298N  
- Rodas acopladas ao chassi  

**Funções**:
- Executar comandos de direção e velocidade  
- Realizar desvios em tempo real  
- Controlar força e sentido dos motores via PWM  

---

## 4️ Módulo de Comunicação
Garante a transmissão de dados e recepção de comandos remotos.  
**Interfaces**:
- Wi-Fi (ESP32-CAM) → controle via web, envio de dados, streaming de imagem  
- Bluetooth (ESP32 ou módulo externo) → controle por app no celular  

**Funções**:
- Transmitir dados dos sensores em tempo real  
- Permitir controle remoto manual  
- Exibir visualizações via página web ou app  
