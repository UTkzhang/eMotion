#include "MeMegaPi.h"
#include <MeLEDMatrix.h>
#include <MePort.h>
#include <SoftwareSerial.h>

MeBluetooth bluetooth(PORT_3);

uint8_t motorSpeed = 200;
char val;
float dist;

void face(char emotion);

MeMegaPiDCMotor motor1(PORT2B);
MeMegaPiDCMotor motor2(PORT1B);
MeMegaPiDCMotor motor3(PORT3B);
MeMegaPiDCMotor motor4(PORT4B);
MeUltrasonicSensor ultraSensor(PORT_6);

MeLEDMatrix Matrix_1(PORT_5);

uint8_t Heart[16]= {0x00,0x38,0x3c,0x1e,0x3c,0x38,0x00,0x00,0x00,0x00,0x38,0x3c,0x1e,0x3c,0x38,0x00}; 
uint8_t Happy[16] = {0x00,0x08,0x10,0x20,0x10,0x08,0x00,0x00,0x00,0x00,0x08,0x10,0x20,0x10,0x08,0x00}; 
uint8_t Sad[16] = {0x00,0x04,0x08,0x08,0x18,0x00,0x00, 0x00,0x00,0x00,0x00,0x18,0x08,0x08,0x04,0x00}; 
uint8_t Mad[16] = {0x00,0x20,0x10,0x08,0x04,0x00,0x00,0x00, 0x00, 0x00,0x00,0x04,0x08,0x10,0x20,0x00}; 
uint8_t Dead[16] = {0x00,0x22,0x14,0x08,0x14,0x22,0x00,0x00,0x00,0x00,0x22,0x14,0x08,0x14,0x22,0x00};
uint8_t RIP[16] = {0x00,0x7e,0x48,0x4c,0x32,0x00,0x00,0x7e,0x00,0x00,0x7e,0x48,0x48,0x48,0x30,0x00};
uint8_t RestL[16] = {0x00,0x1c,0x2e,0x2e,0x22,0x1c,0x00,0x00,0x00,0x00,0x1c,0x2e,0x2e,0x22,0x1c,0x00};
uint8_t RestR[16] = {0x00,0x1c,0x22,0x2e,0x2e,0x1c,0x00,0x00,0x00,0x00,0x1c,0x22,0x2e,0x2e,0x1c,0x00};

void setup()
{
 Matrix_1.setBrightness(Brightness_4);//
 Serial.begin(115200);
 bluetooth.begin(115200);
}

void loop()
{

  //demo
  
   Matrix_1.setColorIndex(1);

   for (int i=0; i<20; i++){
    face('1');
   }
 
    face('p');
    motor3.run(-motorSpeed);
    delay(500);
    motor3.stop();
    motor3.run(motorSpeed);
    delay(550);
    motor3.stop();
    motor3.run(-motorSpeed);
    delay(500);
    motor3.stop();
    motor3.run(motorSpeed);
    delay(550);
    motor3.stop();
    motor3.run(-motorSpeed);
    delay(500);
    motor3.stop();
    motor3.run(motorSpeed);
    delay(550);
    motor3.stop();

   for (int i=0; i<20; i++){
    face('1');
   }
   
   face('2');
   motor3.run(-motorSpeed);
   delay(1500);
   motor3.stop();
   motor3.run(motorSpeed);
   delay(1400);
   motor3.stop();
   motor4.run(motorSpeed);
   delay(1500);
   motor4.stop();
   delay(200);
}
 /*

  if (bluetooth.available()){
    val = bluetooth.read();
    Serial.println("Available");
    Serial.println(val);
    }

  if (Serial.available()){
    val = Serial.read();
    Serial.println(val);
  }
   
  if (val== 'x') { //move forwards
      motor2.run(motorSpeed);
      motor1.run(-motorSpeed);
      delay(1000); 
      motor2.stop();
      motor1.stop(); 
    }

    else if (val== 'y') { // move backwards
 
      motor2.run(-motorSpeed);
      motor1.run(motorSpeed);
      delay(1000); 
      motor2.stop();
      motor1.stop(); 
    }

    else if (val== 'q') { //turn left and move forward
      motor2.run(-motorSpeed);
      motor1.run(-motorSpeed);
      delay(2200);
      motor2.stop();
      motor1.stop();
      motor2.run(motorSpeed);
      motor1.run(-motorSpeed);
      delay(1000); 
      motor2.stop();
      motor1.stop(); 
    }

    else if (val == 'i') {
      face('2');
      motor3.run(-motorSpeed);
      delay(1500);
      motor3.stop();
      motor3.run(motorSpeed);
      delay(1400);
      motor3.stop();
      motor4.run(motorSpeed);
      delay(1500);
      motor4.stop();
      delay(200);
    }

    if (val== 'f') { //move forwards until you reach can
      
      dist = ultraSensor.distanceCm();

      while(dist > 23.80){
        motor2.run(motorSpeed);
        motor1.run(-motorSpeed);
        delay(250);
        motor2.stop();
        motor1.stop();
        dist = ultraSensor.distanceCm();
        Serial.print(ultraSensor.distanceCm());
      }
      
    }

    else if (val == 't') {
      face('2');
      dist = ultraSensor.distanceCm();

      while(dist > 15.80){
        motor2.run(motorSpeed);
        motor1.run(-motorSpeed);
        delay(250);
        motor2.stop();
        motor1.stop();
        dist = ultraSensor.distanceCm();
        Serial.print(ultraSensor.distanceCm());
      }
      
      motor4.run(-motorSpeed);
      delay(1700);
      motor4.stop();
      motor3.run(-motorSpeed);
      delay(700);
      motor3.stop();


      motor2.run(motorSpeed);
      motor1.run(-motorSpeed);
      delay(400);
      motor2.stop();
      motor1.stop();

      motor4.run(motorSpeed);
      delay(500);
      motor4.stop();

      motor3.run(motorSpeed);
      delay(1000);
      motor3.stop();

      delay(3000);
    }
    
    else if (val == 'l') {
      motor2.run(-motorSpeed);
      motor1.run(-motorSpeed);
      delay(450);
      motor2.stop();
      motor1.stop();
    }
      else if (val == 'o') {
      motor2.run(-motorSpeed);
      motor1.run(-motorSpeed);
      delay(2200);
      motor2.stop();
      motor1.stop();
    }

    else if (val == 'r') {
      motor2.run(motorSpeed);
      motor1.run(motorSpeed);
      delay(1000);
      motor2.stop();
      motor1.stop();
    }

    else if (val == 'd') {
      face('p');
      motor3.run(-motorSpeed);
      delay(1000);
      motor3.stop();
      motor4.run(-motorSpeed);
      delay(300);
      motor4.stop();
      motor2.run(-motorSpeed);
      motor1.run(motorSpeed);
      delay(1000);
      motor2.stop();
      motor1.stop();
    }

    else if (val == 'p') {

        face(val);
        motor3.run(-motorSpeed);
        delay(500);
        motor3.stop();
        motor3.run(motorSpeed);
        delay(550);
        motor3.stop();
        motor3.run(-motorSpeed);
        delay(500);
        motor3.stop();
        motor3.run(motorSpeed);
        delay(550);
        motor3.stop();
        motor3.run(-motorSpeed);
        delay(500);
        motor3.stop();
        motor3.run(motorSpeed);
        delay(550);
        motor3.stop();
        //val = '1';

     
    }
    else if (val=='z') {
      motor1.stop();
      motor2.stop();
      motor3.stop();
      motor4.stop();
    }

    else if (val == 'u'){
        face(val);
        motor3.run(motorSpeed);
        delay(700);
        motor3.stop();
      }

    else if (val == 'v'){
        face(val);
        motor3.run(-motorSpeed);
        delay(500);
        motor3.stop();
    }

    else if (val == '5'){
      face(val);
      }

    else if (val != 1){
        face(val);
        delay(3000);
    }
    face('1');
}*/


void face(char emotion){
  /*case : 1 = rest, 2 = happy, 3 = mad, 4 = sad, 5 = dead, 6 = love*/
  switch(emotion){
    case '1': Matrix_1.drawBitmap(0,0,sizeof(RestL), RestL);
              delay(1000);
              Matrix_1.drawBitmap(0,0,sizeof(RestR), RestR); 
              delay(1000); 
              break;
    case '2': Matrix_1.drawBitmap(0,0,sizeof(Happy), Happy);
              break;
    case '3': Matrix_1.drawBitmap(0,0,sizeof(Mad), Mad);
              break;
    case 'p': Matrix_1.drawBitmap(0,0,sizeof(Sad), Sad);
              break;
    case '5': Matrix_1.drawBitmap(0,0,sizeof(Dead), Dead);
              delay(1000);
              Matrix_1.drawBitmap(0,0,sizeof(RIP), RIP);
              delay(1000);
              Matrix_1.drawBitmap(0,0,sizeof(Dead), Dead);
              delay(1000);
              Matrix_1.drawBitmap(0,0,sizeof(RIP), RIP);
              delay(1000);
              break;
    case 'h': Matrix_1.drawBitmap(0,0,sizeof(Heart), Heart);
              break;
    default:  break;
    
      }
  }

void blink(){
    
  for(uint8_t i=4;i>0;i--)
  {
    Matrix_1.setBrightness(i);
    delay(50);
  }
  
  for(uint8_t i=0;i<4;i++)
  {
    Matrix_1.setBrightness(i);
    delay(50);
  }
}


