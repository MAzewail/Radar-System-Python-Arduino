#include <Servo.h>
Servo myservo;
#define echo 13
#define trig 12
long dist=0,duration=0;
void setup() {
 pinMode(echo,0);
 pinMode(trig,1);
 pinMode(11,1);
 digitalWrite(11,1);
 Serial.begin(9600);
 myservo.attach(9);
// myservo.write(0);
}

void us(byte angel){
   digitalWrite(trig,0);
 delayMicroseconds(2);
 digitalWrite(trig,1);
 delayMicroseconds(10);
 digitalWrite(trig,0);
 duration = pulseIn(echo,1);
 dist = duration * 0.0343/2 ;
 Serial.println(String(dist)+","+String(angel));
}

void loop() {
 for(byte i =0; i<180; i++){
  myservo.write(i);
  us(i);
  delay(10);
 }
  for(byte i =180; i>0; i--){
  myservo.write(i);
  us(i);
  delay(10);
 }
}
