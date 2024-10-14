#include <Wire.h>
#include <LiquidCrystal_I2C.h>

LiquidCrystal_I2C lcd = LiquidCrystal_I2C(0x27, 16, 2);

String inputString = "";   // A String to hold incoming data
bool stringComplete = false;  // Whether the string is complete

float axis0,axis1,axis2,axis3;
int hat0_0,hat0_1,button1, button2, button3,button4, button5, button6;
int button7,button8, button9, button10, button11, button12;

void setup() {
  lcd.init();
  lcd.backlight();
  lcd.begin (16, 2);
  
  Serial.begin(9600);
  pinMode(13, OUTPUT);  // Pin 13 for LED
}

void loop() {
  // Process serial input when a full string has been received
  if (stringComplete) {
    inputString.trim();  // Remove any extra whitespace or newline
    
    processInput(inputString);
    lcd_print_commad();
    control_with_command();
    
    inputString = "";  // Clear the string
    stringComplete = false;
  }
}

void serialEvent() {
  while (Serial.available()) {
    char inChar = (char)Serial.read();
    inputString += inChar;
    if (inChar == '\n') {
      stringComplete = true;
    }
  }
}

void processInput(String data) {
  // Split the data by commas
  String commands[18];
  int index = 0;
  int lastIndex = 0;
  for (int i = 0; i < data.length(); i++) {
    if (data[i] == ',') {
      commands[index++] = data.substring(lastIndex, i);
      lastIndex = i + 1;
    }
  }
  commands[index] = data.substring(lastIndex);

  // Use the received data and map it with joystick touch
  axis0 = commands[0].toFloat();
  axis1 = commands[1].toFloat();
  axis2 = commands[2].toFloat();
  axis3 = commands[3].toFloat();

  hat0_0 = commands[4].toInt(); 
  hat0_1 = commands[5].toInt();
  
  button1 = commands[6].toInt();
  button2 = commands[7].toInt();
  button3 = commands[8].toInt();
  button4 = commands[9].toInt();
  button5 = commands[10].toInt();
  button6 = commands[11].toInt();
  button7 = commands[12].toInt();
  button8 = commands[13].toInt();
  button9 = commands[14].toInt();
  button10 = commands[15].toInt();
  button11 = commands[16].toInt();
  button12 = commands[17].toInt();
}

//funtion that use command data to control led can be modify with another hardware like motor ...
void control_with_command(){
  // Control an LED based on button1
  if (button1 == 1) {
    digitalWrite(13, HIGH);  // Turn on LED/motor
  } else {
    digitalWrite(13, LOW);   // Turn off LED/motor
  }
}

//using 16x2 lcd screen for debuging
void lcd_print_commad(){
  lcd.setCursor(0, 0);
  lcd.print("button12: ");
  lcd.print(button12);
  lcd.print("   ");
  lcd.setCursor(0, 1);
  lcd.print("axis0:");
  lcd.print(axis0);
  lcd.print("   ");
}
