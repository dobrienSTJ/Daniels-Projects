//We need to add on requests inside a void loop (like an if statement)
//We also need to finish construction of our project!

#include <Servo.h>
#include <SharpIR.h>

Servo myservo;  // create servo object to control a servo
// twelve servo objects can be created on most boards

#define ir A0
#define model 20150
// ir: the pin where your sensor is attached
// model: an int that determines your sensor:  1080 for GP2Y0A21Y
//                                            20150 for GP2Y0A02Y
//                                            (working distance range according to the datasheets)

SharpIR sharp(ir, model);


int pos = 0;    // variable to store the servo position
int rled = 13;
int yled = 12;
int gled = 11;

// the setup routine runs once when you press reset:
void setup() {
// initialize the digital pin as an output.
pinMode(rled, OUTPUT);
pinMode(yled, OUTPUT);
pinMode(gled, OUTPUT);
}

// put your setup code here, to run once:
Serial.begin(9600);

// the loop routine runs over and over again forever:
void loop()
  for (pos = 0; pos <= 180; pos += 10) { // goes from 0 degrees to 180 degrees
    // in steps of 10 degree
    myservo.write(pos);              // tell servo to go to position in variable 'pos'
    delay(15);                       // waits 15ms for the servo to reach the position
  }
  for (pos = 180; pos >= 0; pos -= 1) { // goes from 180 degrees to 0 degrees
    myservo.write(pos);              // tell servo to go to position in variable 'pos'
    delay(15);                       // waits 15ms for the servo to reach the position
  }

  
unsigned long pepe1=millis();  // takes the time before the loop on the library begins


int dis=SharpIR.distance();  // this returns the distance to the object you're measuring

Serial.print("Mean distance: ");  // returns it to the serial monitor
Serial.println(dis);

  
//  if(dis>0<10)
//  {//Code for Red Light HERE

//    }

// if(dis>10)
    {//Stay Green for Road Traffic
      
//    }


{
digitalWrite(gled, HIGH); // turn the LED on (HIGH is the voltage level)
delay(4000);
// wait for a second
digitalWrite(gled, LOW); // turn the LED off by making the voltage LOW
delay(1000);
// wait for a second

digitalWrite(yled, HIGH); // turn the LED on (HIGH is the voltage level)
delay(1000);
// wait for a second
digitalWrite(yled, LOW); // turn the LED off by making the voltage LOW
delay(1000);
// wait for a second

digitalWrite(rled, HIGH); // turn the LED on (HIGH is the voltage level)
delay(4000);
// wait for a second
digitalWrite(rled, LOW); // turn the LED off by making the voltage LOW
delay(1000);
// wait for a second


}
