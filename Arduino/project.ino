#include "Ubidots.h"
#define input01 15
#define input02 14

const char* UBIDOTS_TOKEN = "BBFF-yxwyI0o8XzN8YMLoDflTqQbm2AtwYk";
const char* WIFI_SSID = "CLARO_8490";
const char* WIFI_PASS = "1950D9888";

Ubidots ubidots(UBIDOTS_TOKEN, UBI_HTTP);

void setup() {
  Serial.begin(9600);
  ubidots.wifiConnect(WIFI_SSID, WIFI_PASS);
  pinMode(15, INPUT);
  pinMode(14, INPUT);
}

void loop() {
  int mesa01, mesa02;
  mesa01 = analogRead(input01);
  mesa02 = analogRead(input02);
  if (mesa01 > 0)
    mesa01 = 1;
  if (mesa02 > 0)
    mesa02 = 1;
  Serial.print("Señal: ");
  Serial.println(mesa01);

  ubidots.add("Mesa 1", mesa01);
  bool bufferSent = false;
  bufferSent = ubidots.send();
  ubidots.add("Mesa 2", mesa02);
  bufferSent = false;
  bufferSent = ubidots.send();
}