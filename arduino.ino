const int brama1 = 4;
const int brama2 = 5;
const int bialy = 2;
const int zielony = 3;
int status1 = 0;
int status2 = 0;

void setup() {
pinMode(brama1, INPUT);
pinMode(brama2, INPUT);
pinMode(bialy, OUTPUT);
pinMode(zielony, OUTPUT);
pinMode(13, OUTPUT);
}

void loop() {
  status1 = digitalRead(brama1);
  status2 = digitalRead(brama2);
  
  if (status1 == LOW) {
    digitalWrite(bialy, LOW);
    digitalWrite(13, HIGH);
  }
  else {
    digitalWrite(bialy, HIGH);
    digitalWrite(13, LOW);
  }

  if (status2 == LOW) {
    digitalWrite(zielony, LOW);
    digitalWrite(13, HIGH);
  }
  else {
    digitalWrite(zielony, HIGH);
    digitalWrite(13, LOW);
  }
}
