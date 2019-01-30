const int pingPin = 7; // Trigger Pin of Ultrasonic Sensor
const int echoPin = 6; // Echo Pin of Ultrasonic Sensor
const int ledPin = 12;
void setup() 
{
   Serial.begin(9600); // Starting Serial Terminal
}

void loop() {
   long duration, cm;
   float secs;
   pinMode(pingPin, OUTPUT);
   digitalWrite(pingPin, LOW);
   delayMicroseconds(2);
   digitalWrite(pingPin, HIGH);
   delayMicroseconds(10);
   digitalWrite(pingPin, LOW);
   pinMode(echoPin, INPUT);
   duration = pulseIn(echoPin, HIGH);
   //secs = (duration/2)* 0.000001;
   //cm = microsecondsToCentimeters(duration);
   //Serial.println(duration);
    Serial.println(duration);
  // Serial.print("in, ");
   //Serial.print(cm);
   //Serial.print("cm");
   //Serial.println();
   //delay(100);
   pinMode(ledPin, OUTPUT);
   if(Serial.available())
   {
     char bit1 = Serial.read();
     if(bit1 == 'H')
     {
     digitalWrite(ledPin,HIGH);
     }
     else if(bit1 == 'L')
     {
     digitalWrite(ledPin,LOW);
     }
     
   delay(250);
    }
 }

float microsecondsToInches(long microseconds) {
   return microseconds / 74 / 2;
}

long microsecondsToCentimeters(long microseconds) {
   return microseconds / 29 / 2;
}
	
	

