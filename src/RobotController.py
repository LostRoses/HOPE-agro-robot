#include <Servo.h>
#include "IR_remote.h"
#include "Keymap.h"

// Inicializa controle IR e servo
IRremote ir(3);
Servo servo_10;

const int trigPin = 12;
const int echoPin = 13;

const int MotorA_Dir = 2;
const int MotorA_PWM = 5;
const int MotorB_Dir = 4;
const int MotorB_PWM = 6;

bool modoAutomatico = false;
float distancia = 0;

void setup() {
  Serial.begin(9600);
  ir.begin();
  servo_10.attach(10);
  servo_10.write(90);

  pinMode(trigPin, OUTPUT);
  pinMode(echoPin, INPUT);
  pinMode(MotorA_Dir, OUTPUT);
  pinMode(MotorA_PWM, OUTPUT);
  pinMode(MotorB_Dir, OUTPUT);
  pinMode(MotorB_PWM, OUTPUT);

  parar();
  Serial.println("Modo MANUAL ativado");
}

void loop() {
  controleIR();

  if (modoAutomatico) {
    distancia = medirDistancia();
    decidirAcaoPorDistancia(distancia);
  }
}

// 🎮 Controle remoto IR com botão 2 para modo manual
void controleIR() {
  unsigned char tecla = ir.getCode();
  byte comando = ir.getIrKey(tecla, 1);

  switch (comando) {
    case IR_KEYCODE_UP:
      moverFrente(); delay(300); parar(); break;
    case IR_KEYCODE_DOWN:
      moverTras(); delay(300); parar(); break;
    case IR_KEYCODE_LEFT:
      girarEsquerda(); delay(300); parar(); break;
    case IR_KEYCODE_RIGHT:
      girarDireita(); delay(300); parar(); break;
    case IR_KEYCODE_OK:
      parar(); break;
    case IR_KEYCODE_1:
      modoAutomatico = true;
      Serial.println("Modo AUTÔNOMO ativado"); break;
    case IR_KEYCODE_2:
      modoAutomatico = false;
      parar();
      Serial.println("Modo MANUAL ativado"); break;
  }
}

// 📡 Decide ação com base na distância
void decidirAcaoPorDistancia(float d) {
  controleIR(); // garante resposta rápida ao controle

  Serial.print("Distância detectada: ");
  Serial.print(d);
  Serial.println(" cm");

  if (d <= 10) {
    Serial.println("⚠️ Obstáculo muito próximo. Executando desvio alternativo...");
    executarDesvioAlternativo();
  } else {
    int velocidade = calcularVelocidade(d);
    Serial.print("Velocidade ajustada: ");
    Serial.println(velocidade);

    moverFrenteVelocidade(velocidade);
    delay(400);
    controleIR();
    parar();
  }
}

// 🔄 Desvio com tentativa pela direita, depois esquerda se necessário
void executarDesvioAlternativo() {
  // ↪️ Tenta desviar para a direita
  moverTras(); delay(400); controleIR(); parar();

  girarDireita(); delay(400); controleIR();
  moverFrente(); delay(600); controleIR(); parar();
  girarEsquerda(); delay(400); controleIR();

  float distPosDireita = medirDistancia(); controleIR();
  Serial.print("Distância após desvio à direita: ");
  Serial.print(distPosDireita);
  Serial.println(" cm");

  if (distPosDireita <= 15) {
    // ⬅️ Tenta desvio para a esquerda
    Serial.println("Desvio à direita falhou. Tentando esquerda...");

    moverTras(); delay(400); controleIR(); parar();
    girarEsquerda(); delay(400); controleIR();
    moverFrente(); delay(600); controleIR(); parar();
    girarDireita(); delay(400); controleIR();

    float distPosEsquerda = medirDistancia(); controleIR();
    Serial.print("Distância após desvio à esquerda: ");
    Serial.print(distPosEsquerda);
    Serial.println(" cm");

    if (distPosEsquerda <= 15) {
      Serial.println("🚫 Rota continua bloqueada. Parando avanço.");
      parar();
      return;
    } else {
      // ✅ Rota livre após desvio à esquerda
      int velocidade = calcularVelocidade(distPosEsquerda);
      moverFrenteVelocidade(velocidade);
      delay(500); controleIR(); parar();
      return;
    }
  }

  // ✅ Rota livre após desvio à direita
  int velocidade = calcularVelocidade(distPosDireita);
  moverFrenteVelocidade(velocidade);
  delay(500); controleIR(); parar();
}

// 📊 Velocidade proporcional à distância
int calcularVelocidade(float d) {
  if (d > 25) return 120;
  else if (d > 14) return 90;
  else return 60;
}

// 🚗 Movimento com velocidade personalizada
void moverFrenteVelocidade(int pwm) {
  digitalWrite(MotorA_Dir, LOW);
  analogWrite(MotorA_PWM, pwm);
  digitalWrite(MotorB_Dir, HIGH);
  analogWrite(MotorB_PWM, pwm);
}

// 🚙 Funções básicas de movimentação
void moverFrente() {
  moverFrenteVelocidade(120);
}

void moverTras() {
  digitalWrite(MotorA_Dir, HIGH);
  analogWrite(MotorA_PWM, 120);
  digitalWrite(MotorB_Dir, LOW);
  analogWrite(MotorB_PWM, 120);
}

void girarEsquerda() {
  digitalWrite(MotorA_Dir, LOW);
  analogWrite(MotorA_PWM, 100);
  digitalWrite(MotorB_Dir, LOW);
  analogWrite(MotorB_PWM, 100);
}

void girarDireita() {
  digitalWrite(MotorA_Dir, HIGH);
  analogWrite(MotorA_PWM, 100);
  digitalWrite(MotorB_Dir, HIGH);
  analogWrite(MotorB_PWM, 100);
}

void parar() {
  analogWrite(MotorA_PWM, 0);
  analogWrite(MotorB_PWM, 0);
}
 
// 📏 Sensor ultrassônico HC-SR04
float medirDistancia() {
  digitalWrite(trigPin, LOW);
  delayMicroseconds(2);
  digitalWrite(trigPin, HIGH); delayMicroseconds(10);
  digitalWrite(trigPin, LOW);
  long duracao = pulseIn(echoPin, HIGH, 30000);
  return duracao * 0.034 / 2.0;
}
