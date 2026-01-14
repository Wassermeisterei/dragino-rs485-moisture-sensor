# dragino-rs485-configuration & connection
This is a quick quide how to configuate Dragino RS485 LB/LS endevice for soil moisture senors (RS485 MODBUS) via PuTTY client.
see also https://wiki.dragino.com/xwiki/bin/view/Main/User%20Manual%20for%20LoRaWAN%20End%20Nodes/RS485-LB_Waterproof_RS485UART_to_LoRaWAN_Converter/
<img width="800" height="882" alt="grafik" src="https://github.com/user-attachments/assets/66c783df-49d7-4440-8f45-c55e450959f9" />


We use Modbus-RTU communication protocol and following sensors: 


- truebner SMT100:

![OIP-3304996835](https://github.com/user-attachments/assets/f5a1cad1-49c1-43ab-9c1e-bae5f6ced59f)

https://www.truebner.de/assets/download/AN002.pdf

- SN 300 SD TR No1 (alternative sensor from china):

<img width="471" height="400" alt="grafik" src="https://github.com/user-attachments/assets/2cd84823-621e-4058-9f8a-785e3f7a54f3" />

https://schaeferei-arensnest.de/wp-content/uploads/2025/12/SN-3000-TR-N01_Soil-temperature-and-moisture-transmitter-485-type-manual-1.pdf
 

For configuration connect the Dragino device via serial reader.
Please note: TXD is connected to RXD, RXD to TXD!!

<img width="506" height="350" alt="grafik" src="https://github.com/user-attachments/assets/d397d77a-61b0-448c-9687-e585fec1951d" />


To read sensor values connect sensor to device as shown below:

<img width="500" height="300" alt="grafik" src="https://github.com/user-attachments/assets/5dd9dc19-f084-4461-9362-6838036efa9c" />

To change sensorsettings in Modpoll use follwing commands:
![modpol-config](https://github.com/user-attachments/assets/92b15d0a-c626-48d9-ba57-4bcdb07751ce)


