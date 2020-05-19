/*
 * Routine to receive a command from the RPi and slew the camera turret
 * 
*/

#include <Servo.h>

Servo cameraservo;  // create servo object to control a servo

int pos = 90;    // variable to store the servo position
String angle;

 
void setup() {
    cameraservo.attach(9);  // attaches the servo on pin 9 to the servo object
    cameraservo.write(pos); // slew to nominal (zero) position with will align forward on center axis of robot

// this section to be replaced with receipt of angle from RPi over i2c    
    Serial.begin(9600); 
    delay(2000); 
    Serial.println("Enter degrees:");
}
 
 
void loop() {
    if(Serial.available()){
        angle = Serial.readStringUntil('\n');
        int pos = angle.toInt();
        cameraservo.write(pos); // slew to input angle
        delay (500);    // wait 1/2 second

        String a = String(pos);
 
        Serial.println("Degrees is: " + a + "!");
    }
}
