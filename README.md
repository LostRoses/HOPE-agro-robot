# HOPE-agro-robot

O HOPE-agro-robot é um protótipo de robô agrícola autônomo desenvolvido com **Arduino** e **ESP32-CAM**.  
Ele foi criado para demonstrar como soluções acessíveis podem apoiar a agricultura com navegação inteligente e transmissão de imagens em tempo real.

## O que ele faz
- Se locomove de forma autônoma
- Detecta obstáculos com sensor ultrassônico (HC-SR04)
- Ajusta a velocidade conforme a distância para evitar colisões
- Transmite imagens e vídeo via Wi-Fi usando ESP32-CAM
- Pode ser controlado manualmente por controle remoto IR

## Componentes principais
- Arduino Uno  
- ESP32-CAM  
- Sensor ultrassônico HC-SR04  
- Driver L298N + motores DC  
- Estrutura acrílica com rodas e bateria  

## Código
O código principal está em [`src/carrinho.ino`](src/carrinho.ino).  
Ele inclui:
- Funções de movimentação (frente, trás, esquerda, direita)  
- Lógica de desvio de obstáculos  
- Ajuste de velocidade proporcional à distância  
- Controle manual via IR  

## Testes
- Vídeo curto mostrando o carrinho desviando de obstáculos: [`docs/video`](docs/video)  
- Fotos da montagem: [`docs/fotos`](docs/fotos)  

## Resultados
- O carrinho conseguiu evitar colisões em diferentes cenários  
- A desaceleração deixou os movimentos mais naturais  
- A ESP32-CAM transmitiu imagens de forma estável  

## Próximos passos
- Explorar visão computacional embarcada  
- Testar algoritmos simples de IA para reconhecimento de padrões  
- Melhorar autonomia energética com painel solar  

## Documentação completa
Mais detalhes estão disponíveis no meu Notion: [link para o Notion](https://seu-link-do-notion)
