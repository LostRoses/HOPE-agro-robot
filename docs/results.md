# Resultados do Projeto

## Testes de Navegação
- O robô conseguiu se deslocar em linha reta e realizar curvas básicas.  
- Testes com sensores ultrassônicos (HC-SR04) mostraram capacidade de **detecção de obstáculos** em até 2 metros.  
- Implementação inicial de lógica de desvio validada em ambiente controlado.  

## Coleta de Dados Ambientais
- Sensores DHT22 e BME280 registraram **temperatura e umidade do ar** com precisão satisfatória.  
- Sensor de umidade do solo apresentou leituras consistentes em diferentes tipos de substrato.  
- Dados coletados foram armazenados e exibidos em tempo real via monitor serial.  

## Integração de Hardware
- Arduino Uno + ESP32-CAM testados em conjunto, confirmando **compatibilidade e comunicação estável**.  
- Motores DC controlados com driver L298N responderam bem a comandos de velocidade e direção.  
- Câmera OV2640 capturou imagens básicas para futura aplicação em visão computacional.  

## Impacto Observado
- O protótipo demonstrou potencial para **reduzir desperdício de água** ao identificar áreas mais secas.  
- Viabilidade de uso em **agricultura de precisão** confirmada em pequena escala.  
- Estrutura modular permite expansão futura com drones e IA embarcada.  

---

## Próximos Passos
- Refinar algoritmos de desvio de obstáculos com base em metaheurísticas.  
- Implementar armazenamento em nuvem para dados ambientais.  
- Testar integração com visão computacional para diagnóstico de plantas.  
