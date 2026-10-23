// C++ code
//
int animationSpeed = 0;

void setup()
{
  pinMode(LED_BUILTIN, OUTPUT);
  pinMode(12, OUTPUT);
  pinMode(11, OUTPUT);
}

void loop()
{
  animationSpeed = 400;
  digitalWrite(LED_BUILTIN, HIGH);
  delay(animationSpeed); // Wait for animationSpeed millisecond(s)
  digitalWrite(LED_BUILTIN, LOW);
  delay(animationSpeed); // Wait for animationSpeed millisecond(s)
  digitalWrite(12, HIGH);
  delay(animationSpeed); // Wait for animationSpeed millisecond(s)
  digitalWrite(12, LOW);
  delay(animationSpeed); // Wait for animationSpeed millisecond(s)
  digitalWrite(11, HIGH);
  delay(animationSpeed); // Wait for animationSpeed millisecond(s)
  digitalWrite(11, LOW);
  delay(animationSpeed); // Wait for animationSpeed millisecond(s)
}