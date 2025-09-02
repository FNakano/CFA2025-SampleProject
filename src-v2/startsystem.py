"""
O que é: Arquivo de início de execução do aplicativo.
O que faz:
  Executa a inicialização de todos os módulos globais (ao aplicativo)
  Se o display OLED estiver montado, mostra informação
sobre wifi no display mas não a mantém atualizada
O que espera-se que esteja neste arquivo:
  definição da co-rotina principal (main()) e sua execução
  (asyncio.run(main()))
  Documentação sucinta sobre o desenvolvimento do aplicativo:
  2025-09-02: Tratei os casos em que o display não está
    conectado e em que não há LEDs para que mensagens de
    erro não interrompam a execução do(s) script(s). A meta
    é iniciar o servidor web.
    Mensagens para algum terminal REPL (ex. Thonny) são
    enviadas para informar o estado da placa.
    Estas "melhorias" fazem o código ficar um pouco menos
    simples.
    Para acessar o servidor web, use <myhostname>.local:5000
    ou, se o AP estiver com DNS desabilitado, <IP>.local:5000
    Caso não consiga iniciar o servidor web, o arquivo
    index.html está na pasta /static e contém link para o
    repositório de onde este código se originou.
"""

import config   # set this app global variables
import led      # setup built-in LEDs
import wifi     # setup wifi communication
import i2c      # setup i2c bus
import display  # setup display

display.message([config.myhostname, config.wifi_if.ifconfig()[0]])
led.off()

# going async...

import asyncio
import aiorepl
import httpserver

async def main():
    print("Starting tasks...")

    # Start other program tasks.

    tm = asyncio.create_task(config.app.start_server()) # criar esta tarefa para executar microdot

    # Start the aiorepl task.
    repl = asyncio.create_task(aiorepl.task())

#    await asyncio.gather(t1, repl)  # mesmo sem ter gather tm o servidor microdot funciona
    await asyncio.gather( repl, tm) # colocar as tarefas no loop de "processos"


asyncio.run(main())  # executar o loop de "processos"

