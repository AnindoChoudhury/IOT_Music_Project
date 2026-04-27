#include <WiFi.h>
#include <HTTPClient.h>
#include <Wire.h>
#include <Adafruit_GFX.h>
#include <Adafruit_SSD1306.h>
#include <DHT.h>
#include <MAX30105.h>
#include <heartRate.h>

// ---------------- WIFI ----------------
const char* ssid = "Redmi Note 10 Pro";
const char* password = "11111111";
String apiKey = "8O1DJSXNZ7JASHME";
const char* server = "http://api.thingspeak.com/update";

// ---------------- OLED ----------------
#define SCREEN_WIDTH 128
#define SCREEN_HEIGHT 64
Adafruit_SSD1306 display(SCREEN_WIDTH, SCREEN_HEIGHT, &Wire, -1);

// ---------------- DHT ----------------
#define DHTPIN 4
#define DHTTYPE DHT11
DHT dht(DHTPIN, DHTTYPE);

// ---------------- MAX30102 ----------------
MAX30105 particleSensor;
bool maxSensorOK = false;

const byte RATE_SIZE = 4;
byte rates[RATE_SIZE];
byte rateSpot = 0;
long lastBeat = 0;
float beatsPerMinute;
int currentBPM = 0;

// ---------------- GSR ----------------
#define GSR_PIN 34
long gsrSum = 0;
int gsrCount = 0;
int finalGSRValue = 0;
int GSR_OFFSET = 0;

// ---------------- Timing ----------------
unsigned long lastUploadTime = 0;
unsigned long lastDHTRead = 0;
unsigned long lastGSRRead = 0;
unsigned long lastScreenUpdate = 0;

// ---------------- Buffers ----------------
float bpmSum = 0; int bpmCount = 0;
float tempSum = 0; float humSum = 0; int dhtCount = 0;
long gsrUploadSum = 0; int gsrUploadCount = 0;

// ---------------- Sensor Values ----------------
float temp = 0;
float hum = 0;

void setup() {
  Serial.begin(115200);

  // I2C INIT (VERY IMPORTANT)
  Wire.begin(21, 22);
  delay(100);

  // OLED INIT
  if (!display.begin(SSD1306_SWITCHCAPVCC, 0x3C)) {
    Serial.println(" OLED not found");
  } else {
    Serial.println(" OLED OK");
  }

  display.clearDisplay();
  display.display();

  // DHT
  dht.begin();
  pinMode(GSR_PIN, INPUT);

  // MAX30102 INIT
  if (!particleSensor.begin(Wire, I2C_SPEED_FAST)) {
    Serial.println("MAX30102 not found");
    maxSensorOK = false;
  } else {
    Serial.println(" MAX30102 OK");
    maxSensorOK = true;

    particleSensor.setup();
    particleSensor.setPulseAmplitudeRed(0x7F);
    particleSensor.setPulseAmplitudeGreen(0);
  }

  for (byte i = 0; i < RATE_SIZE; i++) rates[i] = 0;

  // WiFi (NON-BLOCKING STYLE)
  WiFi.begin(ssid, password);
  Serial.print("Connecting WiFi");
  int tries = 0;
  while (WiFi.status() != WL_CONNECTED && tries < 20) {
    delay(500);
    Serial.print(".");
    tries++;
  }

  if (WiFi.status() == WL_CONNECTED)
    Serial.println(" Connected");
  else
    Serial.println(" WiFi Failed (continuing offline)");
}

void loop() {

  Serial.println("Loop running...");

  // ---------------- HEART RATE ----------------
  if (maxSensorOK) {
    long irValue = particleSensor.getIR();

    if (irValue > 30000) {
      if (checkForBeat(irValue)) {
        long delta = millis() - lastBeat;
        lastBeat = millis();
        beatsPerMinute = 60.0 / (delta / 1000.0);

        if (beatsPerMinute > 40 && beatsPerMinute < 200) {
          rates[rateSpot++] = (byte)beatsPerMinute;
          rateSpot %= RATE_SIZE;

          int sum = 0;
          for (byte i = 0; i < RATE_SIZE; i++) sum += rates[i];
          currentBPM = (sum / RATE_SIZE) - 5;

          bpmSum += currentBPM;
          bpmCount++;
        }
      }
    } else {
      currentBPM = 0;
    }
  }

  // ---------------- GSR ----------------
  if (millis() - lastGSRRead > 10) {
    gsrSum += analogRead(GSR_PIN);
    gsrCount++;

    if (gsrCount >= 500) {
      finalGSRValue = (gsrSum / 500);

      gsrUploadSum += finalGSRValue;
      gsrUploadCount++;

      gsrSum = 0;
      gsrCount = 0;
    }
    lastGSRRead = millis();
  }

  // ---------------- DHT ----------------
  if (millis() - lastDHTRead > 2000) {
    temp = dht.readTemperature();
    hum = dht.readHumidity();

    tempSum += temp;
    humSum += hum;
    dhtCount++;

    lastDHTRead = millis();
  }

  // ---------------- OLED ----------------
  if (millis() - lastScreenUpdate > 500) {
    display.clearDisplay();
    display.setCursor(0, 0);
    display.setTextSize(1);
    display.setTextColor(WHITE);

    display.print("Temp: "); display.println(temp);
    display.print("Hum:  "); display.println(hum);

    display.print("BPM:  ");
    if (!maxSensorOK) display.println("Sensor Err");
    else if (currentBPM == 0) display.println("Place finger");
    else display.println(currentBPM);

    display.print("GSR:  "); display.println(finalGSRValue);

    display.display();
    lastScreenUpdate = millis();
  }

  // ---------------- CLOUD ----------------
  if (millis() - lastUploadTime >= 15000) {

    float avgBPM  = (bpmCount > 0) ? bpmSum / bpmCount : 0;
    float avgTemp = (dhtCount > 0) ? tempSum / dhtCount : 0;
    float avgHum  = (dhtCount > 0) ? humSum / dhtCount : 0;
    int avgGSR    = (gsrUploadCount > 0) ? gsrUploadSum / gsrUploadCount : 0;

    if (WiFi.status() == WL_CONNECTED) {
      HTTPClient http;

      String url = String(server) + "?api_key=" + apiKey +
                   "&field1=" + String(avgTemp) +
                   "&field2=" + String(avgHum) +
                   "&field3=" + String(avgBPM) +
                   "&field4=" + String(avgGSR);

      http.begin(url);
      http.GET();
      http.end();

      Serial.println("☁ Data uploaded");
    }

    bpmSum = 0; bpmCount = 0;
    tempSum = 0; humSum = 0; dhtCount = 0;
    gsrUploadSum = 0; gsrUploadCount = 0;

    lastUploadTime = millis();
  }
}