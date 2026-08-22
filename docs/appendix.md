# Apêndice Técnico

## Algoritmos de Desvio de Obstáculos

Para fundamentar a lógica de navegação e evasão de obstáculos, este projeto se inspira em estudos recentes sobre algoritmos metaheurísticos aplicados a veículos inteligentes.

**Referência:**
- *Otimizando o Planejamento do Caminho para Veículos Inteligentes: Uma Revisão Completa dos Algoritmos Metaheurísticos.*  
Journal of Electrical, Mechanical and Systems Engineering (JEMSE), Vol. 2, No. 4, 2023.  
Disponível em: [Link para o artigo](https://www.acadlore.com/article/JEMSE/2023_2_4/jemse020405)

**Relevância para o projeto:**
- Orienta a lógica de desvio de obstáculos do robô.  
- Aponta algoritmos que podem ser aplicados futuramente para otimização de rotas.  
- Serve como base teórica para evolução em direção à inteligência embarcada.  
- Complementa os conhecimentos adquiridos na disciplina de **Análise de Algoritmos**, aplicados para avaliar eficiência e escolher a melhor abordagem de navegação.

---

## Referências para Robô Agrícola

1. **Sistema robótico para plantio automatizado**  
Fonte: Dissertação de Mestrado – Universidade Federal do Ceará (2024)  
Contribuição: Robô agrícola com Arduino + visão computacional, integração de sensores ambientais e conectividade IoT.  
Aplicação: Agricultura de precisão, coleta de dados ambientais e automação de tarefas agrícolas.  

2. **Rover para detectar doenças em soja**  
Fonte: Projeto acadêmico (2025)  
Contribuição: Veículo terrestre com ESP32, motores DC e câmera OV2640, usando IA para identificar doenças em plantações.  
Aplicação: Monitoramento visual de lavouras, integração de hardware de baixo custo com algoritmos de detecção.  

3. **Automação de irrigação via Arduino e IA**  
Fonte: Revisão sistemática (2026)  
Contribuição: Uso de Arduino + Machine Learning para irrigação inteligente.  
Resultados: Redução de até 90% no consumo de água, integração com previsões meteorológicas.  
Aplicação: Sustentabilidade e eficiência hídrica em agricultura.  

---

## Observações Técnicas

- Arduino Uno + ESP32-CAM → combinação validada em protótipos agrícolas por ser barata e flexível.  
- Sensores ambientais (HC-SR04, DHT22, BME280, umidade do solo) → já testados em campo para monitoramento de microclima e irrigação.  
- Visão computacional embarcada → viável com ESP32-CAM para tarefas simples; para análises complexas, recomenda-se NVIDIA Jetson.  
- IA aplicada à agricultura → já demonstra resultados práticos em detecção de pragas, doenças e otimização de irrigação.
