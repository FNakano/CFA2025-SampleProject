"""
O que é: Arquivo de configuração do hardware dos LEDs.
O que faz:
  Cria variáveis globais (ao aplicativo) para acesso aos LEDs
  Neste caso, o LED endereçável RGB conectado no pino 8 da
  placa ESP32-C3 supermini plus.
O que espera-se que esteja neste arquivo:
  Criação das variáveis e funções para uso dos LEDs.
Referências:
  https://www.w3schools.com/python/python_classes.asp
  https://docs.micropython.org/en/latest/esp8266/tutorial/neopixel.html

"""
from machine import Pin
import config
import neopixel

class LEDDecorator:
  def __init__(self,r,g,b):
    self.r=r
    self.g=g
    self.b=b
    if config._addrl is None :
      # one for all instances
      config._addrl=neopixel.NeoPixel(Pin(8),1)
  def on (self):  # bitwise OR to mimic mix of R,G,B
    config._addrl[0]= (config._addrl[0][0] | self.r, config._addrl[0][1] | self.g, config._addrl[0][2] | self.b)
    config._addrl.write()
  def off (self): # bitwise AND NOT to mimic mix of R,G,B
    config._addrl[0]= (config._addrl[0][0] & ~self.r, config._addrl[0][1] & ~self.g, config._addrl[0][2] & ~self.b)
    config._addrl.write()
  def value(self):
    if ((config._addrl[0][0] & self.r) | (config._addrl[0][1] & self.g) | (config._addrl[0][2] & self.b)) != 0 :
      return True
    return False

import config
config.redled=LEDDecorator(31,0,0)
config.greenled=LEDDecorator(0,31,0)
config.blueled=LEDDecorator(0,0,31)
# RGB LED colors can be configured dimmer/brighter

def off ():
    config.redled.off()
    config.greenled.off()
    config.blueled.off()

off()
