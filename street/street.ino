#define r1 6
#define r2 7
#define r3 8
#define LDR A0
void setup() {
  Serial.begin(9600);
  pinMode(r1,OUTPUT);
  pinMode(r2,OUTPUT);
  pinMode(r3,OUTPUT);
  digitalWrite(r1,HIGH);
  digitalWrite(r2,HIGH);
  digitalWrite(r3,HIGH);
  // put your setup code here, to run once:
}
String s;
void loop() {
  Serial.print("xxxxxxxx");
  Serial.println(map(analogRead(LDR),1025,900,0,100));
  if(Serial.available()){
    s=Serial.readString();
    char x[s.length()];
    s.toCharArray(x,s.length());
    if (x[0]=='1'){
      digitalWrite(r1,LOW);
    }
    else{
      digitalWrite(r1,HIGH);
    }
    if (x[1]=='1'){
      digitalWrite(r2,LOW);
    }
    else{
      digitalWrite(r2,HIGH);
    }
    if (x[2]=='1'){
      digitalWrite(r3,LOW);
    }
    else{
      digitalWrite(r3,HIGH);
    }
  }
  // put your main code here, to run repeatedly:

}
