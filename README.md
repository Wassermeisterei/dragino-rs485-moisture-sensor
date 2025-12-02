# dragino-rs485-configuration
This is a quick quide how to configuate Dragino RS485 LB/LS endevice for soil moisture senors (RS485 MODBUS) via PuTTY client.
see also https://wiki.dragino.com/xwiki/bin/view/Main/User%20Manual%20for%20LoRaWAN%20End%20Nodes/RS485-LB_Waterproof_RS485UART_to_LoRaWAN_Converter/

We use Modbus-RTU communication protocol and following sensors: 
- truebner SMT100: https://www.truebner.de/assets/download/AN002.pdf
- no name china sensor (see default setting)
 

For configuration connect the Dragino device via serial reader.
Please note: TXD is connected to RXD, RXD to TXD!!

<img width="506" height="350" alt="grafik" src="https://github.com/user-attachments/assets/d397d77a-61b0-448c-9687-e585fec1951d" />


To read sensor values connect sensor as shown below:
China Sensor (SN-300SD-TR-NO1)

<img width="896" height="646" alt="grafik" src="https://github.com/user-attachments/assets/e512b2e3-d52e-4a6e-9167-e8a45eb97a1c" /><img width="261" height="185" alt="grafik" src="https://github.com/user-attachments/assets/115cfe30-65e9-4d87-bbe0-4321acf96be2" />


