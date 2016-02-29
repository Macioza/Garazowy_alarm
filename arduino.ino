const int brama1 = 4;
const int brama1out = 2;
int status1 = 0;

void setup() {
pinMode(brama1, INPUT);
pinMode(brama1out, OUTPUT);
pinMode(13, OUTPUT);
}

void loop() {
  status1 = digitalRead(brama1);
  if (status1 == LOW) {
    digitalWrite(brama1out, LOW);
    digitalWrite(13, HIGH);
  }
  else {
    digitalWrite(brama1out, HIGH);
    digitalWrite(13, LOW);
  }
}
