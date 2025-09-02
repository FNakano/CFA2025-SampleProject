"""
O que é:
  Arquivo de configuração do hardware display OLED
  com controlador SSD1306.
O que faz:
  Cria variáveis globais (ao aplicativo) uso do display OLED
  Usa i2c.py através da variável config.i2c
  Trata sileciosamente caso o display não esteja presente 
O que espera-se que esteja neste arquivo:
  Criação das variáveis e funções para uso do display.
Referências:
  https://www.w3schools.com/python/python_try_except.asp
"""
import config
import ssd1306
from machine import Pin, I2C, ADC

try :
  config.disp=ssd1306.SSD1306_I2C(config.disp_width,config.disp_height,config.i2c)
except AttributeError as e:
  print(f"{e} ocurred when trying to instantiate display. Probably i2c handler was not instantiated.")
except OSError as e:
  print(f"{e} ocurred when trying to instantiate display. Probably no display attached to devboard.")
except Exception as e:
  # Catch any other unhandled exception
  print(f"An unexpected error {type(e)} occurred: {e}")

# mess is a list
def message(mess) :
  config.messages=mess
  try:
    config.disp.fill(0)
    lin=0
    for m in mess :
      config.disp.text(m, 0, lin,1)
      lin=(lin+10)%config.disp_height
    config.disp.show()
  except AttributeError as e:
    print(f"{e} ocurred when trying to message display. Probably display is not attached to devboard.")
