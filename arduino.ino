#include <SPI.h>
#include <MFRC522.h>

const int brama1 = 6;
const int brama2 = 7;
int status1 = 0;
int status2 = 0;

const int bialy = 2;
const int zielony = 4;
//const int zolty = 5;

#define SS_PIN 10
#define RST_PIN 9
byte Maciej[4] = {0x69, 0x85, 0xBA, 0x07}; //ID karty w HEX
boolean autoryzacja = false;
boolean statusBramy1 = false;
boolean etap1 = false;


void setup() {
pinMode(brama1, INPUT);
pinMode(brama2, INPUT);

pinMode(bialy, OUTPUT);
pinMode(zielony, OUTPUT);
pinMode(13, OUTPUT);
Serial.begin(9600);
}

void loop() {
  autoryzacja = false;
  status1 = digitalRead(brama1);
  status2 = digitalRead(brama2);
  
  if (status1 == LOW && etap1 == false) {
    digitalWrite(bialy, LOW);
    digitalWrite(13, HIGH);
    Serial.println("Kontaktron 1 rozwarty");
    statusBramy1 = true;
    sprawdzenieKarty();
    delay(1000);
  }
  else {
    digitalWrite(bialy, HIGH);
    digitalWrite(13, LOW);
  }

//Etap 1
  if (etap1 == true) {
    Serial.println("Jak do tej pory ok");
    delay(5000);
    Serial.println("Reset booleanow");
    etap1 = false;
  }
    
}

void sprawdzenieKarty() {
MFRC522 mfrc522(SS_PIN, RST_PIN);
SPI.begin();          // Init SPI bus
mfrc522.PCD_Init();     // Init MFRC522 card
Serial.println("Czytanie karty");
if (! mfrc522.PICC_IsNewCardPresent()) return; //poszukuje karty  
if (! mfrc522.PICC_ReadCardSerial()) return; //wybiera kartę, bez tego program reaguje na kążdą kardtę 
//Odznacz wyszystkie Serial.print jeśli chcesz poznać ID nowej karty 
//Serial.begin(9600);  
//Serial.print("Card UID:");
for (int i = 0; i < mfrc522.uid.size; i++) {
//Serial.print(mfrc522.uid.uidByte[i], HEX);
if(mfrc522.uid.uidByte[i]==Maciej[i]) {
  autoryzacja = true;   
  }
}

//odmowa autoryzacji
if(autoryzacja == false) {
  digitalWrite(bialy, HIGH);
  digitalWrite(zielony, LOW);
  Serial.println("Odmowa autoryzacji");
  }
  
//przyznanie autoryzacji 
if(autoryzacja == true) {
  digitalWrite(bialy, LOW);
  digitalWrite(zielony, HIGH);
  Serial.println("Przyznanie autoryzacji");
  etap1 = true;
  }
}
