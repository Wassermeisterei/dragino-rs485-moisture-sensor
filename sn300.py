#!/usr/bin/env python3
"""
Konfiguration eines Dragino RS485-LN Knotens per AT-Befehlen über UART/USB-Seriell.

Voraussetzung:
    pip install pyserial

Anschluss:
    Der Dragino-Knoten wird per USB (virtueller COM-Port) oder TTL-Seriell-Adapter
    an den Rechner angeschlossen. Baudrate für Dragino AT-Kommandos ist i.d.R. 9600.

Anpassen:
    - SERIAL_PORT auf den tatsächlichen Port setzen (z.B. "COM5" unter Windows
      oder "/dev/ttyUSB0" unter Linux).
    - Die AT_COMMANDS-Liste bei Bedarf ergänzen/ändern.
"""

import sys
import time
import serial

# ---------------------------------------------------------------------------
# Konfiguration
# ---------------------------------------------------------------------------

SERIAL_PORT = "/dev/ttyUSB0"   # ggf. anpassen
BAUDRATE = 9600
TIMEOUT_S = 2                  # Timeout für das Lesen einer Antwort
DELAY_BETWEEN_COMMANDS_S = 0.5 # kurze Pause zwischen den Befehlen

# Reihenfolge wie vom Nutzer vorgegeben
AT_COMMANDS = [
    "AT+5VT=1200",
    "AT+TDC=21600000",

    "AT+COMMAND1=01 03 00 00 00 01,1",
    "AT+COMMAND2=02 03 00 00 00 01,1",
    "AT+COMMAND3=03 03 00 00 00 01,1",
    "AT+COMMAND4=04 03 00 00 00 01,1",
    "AT+COMMAND5=05 03 00 00 00 01,1",
    "AT+COMMAND6=06 03 00 00 00 01,1",
    "AT+COMMAND7=07 03 00 00 00 01,1",
    "AT+COMMAND8=08 03 00 00 00 01,1",
    "AT+COMMAND9=09 03 00 00 00 01,1",
    "AT+COMMANDA=0A 03 00 00 00 01,1",
    "AT+COMMANDB=0B 03 00 00 00 01,1",
    "AT+COMMANDC=0C 03 00 00 00 01,1",

    "AT+DATACUT1=7,1,4+5",
    "AT+DATACUT2=7,1,4+5",
    "AT+DATACUT3=7,1,4+5",
    "AT+DATACUT4=7,1,4+5",
    "AT+DATACUT5=7,1,4+5",
    "AT+DATACUT6=7,1,4+5",
    "AT+DATACUT7=7,1,4+5",
    "AT+DATACUT8=7,1,4+5",
    "AT+DATACUT9=7,1,4+5",
    "AT+DATACUTA=7,1,4+5",
    "AT+DATACUTB=7,1,4+5",
    "AT+DATACUTC=7,1,4+5",

    "AT+CMDDL1=100",
    "AT+CMDDL2=100",
    "AT+CMDDL3=100",
    "AT+CMDDL4=100",
    "AT+CMDDL5=100",
    "AT+CMDDL6=100",
    "AT+CMDDL7=100",
    "AT+CMDDL8=100",
    "AT+CMDDL9=100",
    "AT+CMDDLA=100",
    "AT+CMDDLB=100",
    "AT+CMDDLC=100",
]


def send_at_command(ser: serial.Serial, command: str) -> str:
    """Sendet einen einzelnen AT-Befehl und liest die Antwort des Geräts."""
    ser.reset_input_buffer()
    ser.write((command + "\r\n").encode("utf-8"))

    time.sleep(0.2)
    response = b""
    start = time.time()
    while time.time() - start < TIMEOUT_S:
        if ser.in_waiting:
            response += ser.read(ser.in_waiting)
            # Dragino-Geräte beenden Antworten typischerweise mit "OK"
            if b"OK" in response or b"ERROR" in response:
                break
        time.sleep(0.05)

    return response.decode("utf-8", errors="replace").strip()


def main() -> int:
    try:
        ser = serial.Serial(SERIAL_PORT, BAUDRATE, timeout=TIMEOUT_S)
    except serial.SerialException as exc:
        print(f"Fehler beim Öffnen von {SERIAL_PORT}: {exc}")
        return 1

    # Kurze Wartezeit, damit die serielle Verbindung stabil aufgebaut ist
    time.sleep(1)

    print(f"Verbunden mit {SERIAL_PORT} @ {BAUDRATE} Baud")
    print(f"Sende {len(AT_COMMANDS)} AT-Befehle...\n")

    failed = []

    for idx, cmd in enumerate(AT_COMMANDS, start=1):
        print(f"[{idx:02d}/{len(AT_COMMANDS)}] -> {cmd}")
        response = send_at_command(ser, cmd)

        if response:
            print(f"           <- {response}")
        else:
            print("           <- (keine Antwort)")

        if "OK" not in response:
            failed.append(cmd)

        time.sleep(DELAY_BETWEEN_COMMANDS_S)

    ser.close()

    print("\n--- Zusammenfassung ---")
    if failed:
        print(f"{len(failed)} Befehl(e) ohne 'OK'-Bestätigung:")
        for cmd in failed:
            print(f"  - {cmd}")
        return 2

    print("Alle Befehle wurden bestätigt.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
