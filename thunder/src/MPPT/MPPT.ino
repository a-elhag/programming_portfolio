/////////////////////////////////////////////////////////////////////////////
// Constant Global Variables //
/////////////////////////////////////////////////////////////////////////////
const int Pin_Iout = A4;
const int Pin_Vout = A1;
const int Pin_Vdd = A2;
const int Pin_Ctrl = A5;
const double Frequency = 200;

/////////////////////////////////////////////////////////////////////////////
// Global Variables //
/////////////////////////////////////////////////////////////////////////////
double D; 
double D_Old; 
double D_New;
double Vdd = 4.96;
double Vout_Old; 
double Vout_New; 
double Iout_Old; 
double Iout_New; 
double Pout_Old; 
double Pout_New;
double Jump = 0.05; // How much we change the duty cycle every iteration
double Delta_Compare = 0.0002;
double Jump2 = 0.015;

/////////////////////////////////////////////////////////////////////////////
// Setup //
/////////////////////////////////////////////////////////////////////////////
void setup()
{
  Serial.begin(9600);
  pinMode(Pin_Iout, INPUT);
  pinMode(Pin_Vout, INPUT);
  pinMode(Pin_Vdd, INPUT);
  pinMode(Pin_Ctrl, INPUT);
  pinMode(3, OUTPUT);
  D = 0.1;
  TCCR2A = _BV(COM2B1) | _BV(WGM21) | _BV(WGM20); // Just enable output on Pin 3 and disable it on Pin 11
  TCCR2B = _BV(WGM22) | _BV(CS22);
  OCR2A = Frequency; // defines the frequency 51 = 38.4 KHz, 54 = 36.2 KHz, 58 = 34 KHz, 62 = 32 KHz
  OCR2B = Frequency * D ; // defines the duty cycle - Half the OCR2A value for 50%
  TCCR2B = TCCR2B & 0b00111000 | 0x2; // select a prescale value of 8:1 of the system clock
  Do_Nudge();
  Get_VddV2();
}

void loop()
{
  Get_VddV2();
  Do_MPPT();
  Serial.print("D = ");
  Serial.println(D);
  Serial.print("Vout = ");
  Serial.println(Vout_New);
  Serial.print("Iout = ");
  Serial.println(Iout_New);
  Serial.print("Pout = ");
  Serial.println(Pout_New);
  Serial.println(" ");
  delay(1);
}
/////////////////////////////////////////////////////////////////////////////
// Finding Vdd //
/////////////////////////////////////////////////////////////////////////////
void Get_Vdd() {
  long result;
  // Read 1.1V reference against AVdd
  ADMUX = _BV(REFS0) | _BV(MUX3) | _BV(MUX2) | _BV(MUX1);
  delay(2); // Wait for Vref to settle
  ADCSRA |= _BV(ADSC); // Convert
  while (bit_is_set(ADCSRA, ADSC));
  result = ADCL;
  result |= ADCH << 8;
  result = 1125300L / result; // Back-calculate AVdd in mV
  Vdd = result / 1000.0;
}

double Get_VddV2()
{
  double Error;
  Error = analogRead(Pin_Vdd);
  Vdd = (Error + 826) / (4.04 * 1023);
  Vdd = Vdd - 0.2;
  Vdd = 1 / Vdd;
  return Error;
}

/////////////////////////////////////////////////////////////////////////////
// Here is the Gets! //
/////////////////////////////////////////////////////////////////////////////
double Get_Analog(int Pin)
{
  double ADC;
  double ADC2;
  double V_Pin1 = 0;
  double V_Pin;
  for (int i = 1; i <= 1000; i++)
  {
    ADC = analogRead(Pin);
    ADC2 = (ADC) * (Vdd / 1024.0);
    V_Pin1 = V_Pin1 + ADC2;
    // delay(1);
  }
  V_Pin = V_Pin1 / 1000.0;
  return V_Pin;
}

double Get_Iout()
{
  double Iout1;
  double Iout2;
  Iout1 = Get_Analog(Pin_Iout);
  Iout2 = 1.025 * 10.427 * (Iout1 - (Vdd / 2));
  if (Iout2 < 0.05)
  {
    Iout2 = 0;
  }
  return Iout2;
}

double Get_Vout()
{
  double Vout;
  Vout = Get_Analog(Pin_Vout);
  Vout = 1.15 * ((2.45 + 9.99) / 2.45);
  if (Vout < 0.05)
  {
    Vout = 0;
  }
  return Vout;
}

double Get_Pout(double Vout, double Iout)
{
  double Pout;
  Pout = Vout * Iout;
  return Pout;
}

/////////////////////////////////////////////////////////////////////////////
// Control Algorithms //
/////////////////////////////////////////////////////////////////////////////
void Do_Duty()
{
  if (D > 0.95)
  {
    D = 0.95;
  }
  if (D < 0.05)
  {
    D = 0.05;
  }
  OCR2B = Frequency * (1 - D); // defines the duty cycle - Half the OCR2A value for 50%
}

void Do_Nudge ()
{
  D_Old = D;
  Vout_Old = Get_Vout();
  Iout_Old = Get_Iout();
  Pout_Old = Get_Pout(Vout_Old, Iout_Old);
  D = 0.10;
  Do_Duty();
  delay(1000);
  D_New = D;
  Vout_New = Get_Vout();
  Iout_New = Get_Iout();
  Pout_New = Get_Pout(Vout_New, Iout_New);
}

void Do_Voltage (double V_desired)
{
  double Vout;
  Vout = Get_Vout();
  if (V_desired > Vout)
  {
    D = D + Jump2;
  }
  if (V_desired < Vout)
  {
    D = D - Jump2;
  }
  Do_Duty();
  Iout_New = Get_Iout();
  Vout_New = Get_Vout();
  Pout_New = Get_Pout(Vout_New, Iout_New);
}

void Do_Current (double I_desired)
{
  double Iout;
  Iout = Get_Iout();
  if (I_desired > Iout)
  {
    D = D + Jump2;
  }
  if (I_desired < Iout)
  {
    D = D - Jump2;
  }
  Do_Duty();
  Iout_New = Get_Iout();
  Vout_New = Get_Vout();
  Pout_New = Get_Pout(Vout_New, Iout_New);
}

void Do_MPPT ()
{
  double Vout_Delta;
  Vout_Delta = Vout_New - Vout_Old;
  double Pout_Delta;
  Pout_Delta = Pout_New - Pout_Old;
  double Delta;
  Delta = Vout_Delta * Pout_Delta;
  D_Old = D;
  Vout_Old = Get_Vout();
  Iout_Old = Get_Iout();
  Pout_Old = Get_Pout(Vout_Old, Iout_Old);
  if (Delta > Delta_Compare)
  {
    D = D + Jump;
    if (D_New > D_Old && Vout_New < Vout_Old)
    {
      D = D - 2 * Jump;
    }
  }
  else if (Delta < -Delta_Compare)
  {
    D = D - Jump;
  }
  else
  {
    if (Delta > 0)
    {
      D = D + Jump2;
      if (D_New > D_Old && Vout_New < Vout_Old)
      {
        D = D - 2 * Jump2;
      }
    }
    if (Delta < 0)
    {
      D = D - Jump2;
    }
  }
  Do_Duty();
  D_New = D;
  Vout_New = Get_Vout();
  Iout_New = Get_Iout();
  Pout_New = Get_Pout(Vout_New, Iout_New);
}




