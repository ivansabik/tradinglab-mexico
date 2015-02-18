![alt text](https://rawgit.com/mandroslabs/tradinglabmx/master/tradinglabmx/static/img/logo.png "Tradinglab MX")

Tradinglab MX es una app de backtesting y análisis para elaborar y probar estrategias de trading en la bolsa de valores de Mexico (BMV) con datos históricos de Yahoo Finance. Está más enfocada en usuarios principiantes ya que muestra los indicadores básicos para análisis técnico y las gráficas más comunes.

Difiere también de otras aplicaciones porque no permite armar portafolios y con los datos en tiempo real ver los resultados, sino es para realizar backtesting de estrategias con portafolios que construye el usuario seleccionando manualmente las emisoras y las fechas de los movimientos de compra/venta.

Fue conceptualizada y desarrollada como proyecto prototipo para el concurso de Mercados de Valores de la Bolsa Mexicana de Valores, sin embargo se continuará desarrollando para construir una plataforma robusta y de utilidad real. Espera encontrar algunos bugs si la pruebas extensivamente ya que sólo se realizó un prototipo con las funcionalidades mínimas sin tests unitarios.

Como tecnologías usa Python, Flask, Zipline, Pandas, Bootstrap y Highcharts JS, todas open source y así todos felices. 

- Ver listado de emisoras (todas o por sector)
- Ver info historica y grafica de precios de una emisora
- Crear movimientos de compra-venta de distintas acciones para simular una estrategia de trading

## App web

La aplicación web están en Python con el framework Flask. Requiere como dependencias Flask y Zipline, abajo vienen las instrucciones con Ubuntu y el link a un disco con el que se puede crear una máquina virtual en VMWare o Virtualbox.

```cd tradinglabmx```

```python tradinglabmx/app.py```

Esto inicia un server de desarrollo (no apto para producción) en la dirección ```127.0.0.1:5000```

## API Rest

Por el momento no se usa AJAX, se genera directamente el código Javascript en el lado del server usando templates de Jinja2. Aún así se ha ido desarrollando una API para cuando se reimplemente en AJAX o para que se hagan otras apps con ésta.

```cd tradinglabmx```

```python tradinglabmx/api.py```

## Instrucciones instalación (Ubuntu)

Usar virtualenv de Python es mejor, pero para simplificar vamos a instalar globalmente:

```cd ~```

```sudo apt-get install git python python-pip python-all-dev```

```sudo pip install numpy zipline flask```

```git clone https://github.com/mandroslabs/tradinglab-mexico.git```

```python tradinglab-mexico/tradinglabmx/app.py```
