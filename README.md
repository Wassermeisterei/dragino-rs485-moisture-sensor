# dragino-rs485-configuration
This is a quick quide how to configuate Dragino RS485 LB/LS endevice for soil moisture senors (RS485 MODBUS) via PuTTY client.
see also https://wiki.dragino.com/xwiki/bin/view/Main/User%20Manual%20for%20LoRaWAN%20End%20Nodes/RS485-LB_Waterproof_RS485UART_to_LoRaWAN_Converter/

We use Modbus-RTU communication protocol and following sensors: 
- truebner SMT100: https://www.truebner.de/assets/download/AN002.pdf
- no name china sensor (see default setting)
 

For configuration connect the Dragino device via serial reader.
Please note: TXD is connected to RXD, RXD to TXD!!

<img width="506" height="350" alt="grafik" src="https://github.com/user-attachments/assets/d397d77a-61b0-448c-9687-e585fec1951d" />


To read sensor values connect sensor to device as shown below:
<img width="653" height="392" alt="grafik" src="https://github.com/user-attachments/assets/a5a019b7-cceb-4717-a4c3-e19656c37cbd" />


