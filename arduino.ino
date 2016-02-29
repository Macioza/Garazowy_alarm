const int brama1 = 4;
const int brama1out = 2;
int status1 = 0;

void setup() {
pinMode(brama1, INPUT);
pinMode(brama1out, OUTPUT);
}

void loop() {
  status1 = digitalRead(brama1);
  if (status1 == LOW) {
    digitalWrite(brama1out, LOW);
  }
  else {
    digitalWrite(brama1out, HIGH);
  }
}
