#!/usr/bin/env python3
"""
boards.py

Board specifications for the Arduino Fritzing part set.

Every pin position in this file is expressed in millimetres from the top left
corner of the board as drawn, with the USB end at the left. Provenance for each
class of number is recorded in GEOMETRY_SOURCES and reproduced in each board's
NOTES.md.

Licence: CC BY-SA 3.0
"""

PITCH = 2.54

GEOMETRY_SOURCES = {
    "shield_grid": (
        "Shield header positions were measured out of the Fritzing core parts "
        "arduino_uno(rev3)-icsp and Arduino_MEGA_2560-Rev3 by parsing their PCB "
        "SVGs and converting user units to millimetres. This is the de facto "
        "standard shield footprint that the whole shield ecosystem is built "
        "against, and it reproduces the two irregular gaps (4.06 mm in the "
        "digital row, 5.08 mm between header blocks) that make the UNO layout "
        "what it is. It is not a reading of the Arduino EAGLE .brd file."),
    "outline": (
        "Board outline dimensions. UNO family: 68.58 mm by 53.34 mm, stated in "
        "plain text in section 12 of the UNO Q datasheet and matching the "
        "measured Fritzing core UNO footprint. Mega family: 101.68 mm by 53.34 "
        "mm, taken from the Fritzing core Mega 2560 part canvas. Arduino "
        "publishes 101.52 mm for the Mega outline, so treat the last 0.16 mm as "
        "unconfirmed."),
    "pads": (
        "1.0 mm drill on a 1.8 mm pad, carried over from the MKR WiFi 1010 part "
        "in this set for consistency. Not reconciled against Arduino's own "
        "published footprints, which were unreachable from the build "
        "environment."),
    "holes": (
        "Mounting holes are NOT drawn. The UNO Q datasheet mechanical figure "
        "lists dimensions (15.24, 13.97, 7.62, 2.54, 2x 3.01, 4x R1.6 and "
        "others) but they are unlabelled in the extracted text, so they cannot "
        "be assigned to specific features without the drawing itself."),
}

# ---------------------------------------------------------------------------
# UNO family shield grid, measured from the Fritzing core UNO R3 part
# ---------------------------------------------------------------------------
UNO_L, UNO_W = 68.58, 53.34
UNO_TOP_Y, UNO_BOT_Y = 2.54, 50.80
UNO_DIG_A = 18.80          # SCL end of the 10 way digital block
UNO_DIG_B = 45.72          # D7 end of the 8 way digital block
UNO_PWR_X = 27.94          # first position of the 8 way power block
UNO_ANA_X = 50.80          # first position of the 6 way analog block

# Mega family grid, measured from the Fritzing core Mega 2560 part
MEGA_L, MEGA_W = 101.68, 53.34
MEGA_DIG_A = 18.80         # SCL1 end of the 10 way block
MEGA_DIG_B = 45.72         # D7 end of the 8 way block
MEGA_DIG_C = 68.58         # D14 end of the 8 way block
MEGA_PWR_X = 27.94
MEGA_ANA_A = 50.80         # A0 block
MEGA_ANA_B = 73.66         # second analog block
MEGA_SIDE_XL, MEGA_SIDE_XR = 93.98, 96.52
MEGA_SIDE_Y0 = 2.54


def P(name, typ, desc, x, y, side, col, group, short=None):
    return dict(name=name, type=typ, desc=desc, x=round(x, 3), y=round(y, 3),
                side=side, col=col, group=group, short=short or name.split("/")[0])


def row(entries, x0, y, side, col, group):
    """entries: list of (name, type, desc, short_or_None)"""
    out = []
    for i, e in enumerate(entries):
        nm, ty, de = e[0], e[1], e[2]
        sh = e[3] if len(e) > 3 else None
        out.append(P(nm, ty, de, x0 + i * PITCH, y, side, col, group, sh))
    return out


D3V3 = "3.3 V logic. Do not drive this pin from a 5 V source."
D5V0 = "5 V logic, hardware compatible with UNO R3 shields."

# ===========================================================================
# Arduino GIGA R1 WiFi (ABX00063)
# ===========================================================================
def giga_pins():
    p = []
    # JANALOG, datasheet section 14.2, 24 positions across three blocks
    a1 = [("NC", "Other", "Not connected.", "NC"),
          ("IOREF", "Power", "Digital logic voltage reference, tied to 3.3 V.", "IORF"),
          ("RESET", "Digital", "Board reset.", "RST"),
          ("+3V3", "Power", "3.3 V power rail.", "3V3"),
          ("+5V", "Power", "5 V power rail.", "5V"),
          ("GND", "Power", "Ground.", "GND"),
          ("GND", "Power", "Ground.", "GND"),
          ("VIN", "Power", "Voltage input, 6 V to 24 V.", "VIN")]
    a2 = [("A%d" % i, "Analog", "Analog input %d, usable as GPIO. %s" % (i, D3V3), "A%d" % i)
          for i in range(0, 8)]
    a3 = [("A%d" % i, "Analog", "Analog input %d, usable as GPIO. %s" % (i, D3V3), "A%d" % i)
          for i in range(8, 12)]
    a3 += [("DAC0", "Analog", "Digital to analog converter 0, up to 12 bit. Also the right audio channel on the 3.5 mm jack.", "DAC0"),
           ("DAC1", "Analog", "Digital to analog converter 1, up to 12 bit. Also the left audio channel on the 3.5 mm jack.", "DAC1"),
           ("CANRX", "Digital", "CAN bus receive. An external transceiver is required.", "CANRX"),
           ("CANTX", "Digital", "CAN bus transmit. An external transceiver is required.", "CANTX")]
    p += row(a1, MEGA_PWR_X, MEGA_W - 2.54, "bottom", "L", "power")
    p += row(a2, MEGA_ANA_A, MEGA_W - 2.54, "bottom", "L", "analog")
    p += row(a3, MEGA_ANA_B, MEGA_W - 2.54, "bottom", "L", "analog2")

    # JDIGITAL, datasheet section 14.3, 26 positions across three blocks
    d1 = [("D21/SCL1", "Digital", "GPIO 21, I2C 1 clock. " + D3V3, "D21"),
          ("D20/SDA1", "Digital", "GPIO 20, I2C 1 data. " + D3V3, "D20"),
          ("AREF", "Digital", "Analog reference voltage.", "AREF"),
          ("GND", "Power", "Ground.", "GND"),
          ("D13/SCK", "Digital", "GPIO 13, SPI clock, PWM capable. " + D3V3, "D13"),
          ("D12/CIPO", "Digital", "GPIO 12, SPI CIPO (MISO), PWM capable. " + D3V3, "D12"),
          ("D11/COPI", "Digital", "GPIO 11, SPI COPI (MOSI), PWM capable. " + D3V3, "D11"),
          ("D10/CS", "Digital", "GPIO 10, SPI chip select, PWM capable. " + D3V3, "D10"),
          ("D9/SDA2", "Digital", "GPIO 9, I2C 2 data, PWM capable. " + D3V3, "D9"),
          ("D8/SCL2", "Digital", "GPIO 8, I2C 2 clock, PWM capable. " + D3V3, "D8")]
    d2 = [("D%d" % i, "Digital", "GPIO %d, PWM capable. %s" % (i, D3V3), "D%d" % i)
          for i in (7, 6, 5, 4, 3, 2)]
    d2 += [("D1/TX0", "Digital", "GPIO 1, Serial 0 transmit. " + D3V3, "D1"),
           ("D0/RX0", "Digital", "GPIO 0, Serial 0 receive. " + D3V3, "D0")]
    d3 = [("D14/TX3", "Digital", "GPIO 14, Serial 3 transmit. " + D3V3, "D14"),
          ("D15/RX3", "Digital", "GPIO 15, Serial 3 receive. " + D3V3, "D15"),
          ("D16/TX2", "Digital", "GPIO 16, Serial 2 transmit. " + D3V3, "D16"),
          ("D17/RX2", "Digital", "GPIO 17, Serial 2 receive. " + D3V3, "D17"),
          ("D18/TX1", "Digital", "GPIO 18, Serial 1 transmit. " + D3V3, "D18"),
          ("D19/RX1", "Digital", "GPIO 19, Serial 1 receive. " + D3V3, "D19"),
          ("D20/SDA", "Digital", "GPIO 20, I2C 0 data. " + D3V3, "D20"),
          ("D21/SCL", "Digital", "GPIO 21, I2C 0 clock. " + D3V3, "D21")]
    p += row(d1, MEGA_DIG_A, 2.54, "top", "R", "dig1")
    p += row(d2, MEGA_DIG_B, 2.54, "top", "R", "dig2")
    p += row(d3, MEGA_DIG_C, 2.54, "top", "R", "serial")

    # JSIDE, datasheet sections 14.5 and 14.6, two columns of 18
    lhs = [("+5V", "Power", "5 V power rail.", "5V")]
    lhs += [("D%d" % i, "Digital", "GPIO %d. %s" % (i, D3V3), "D%d" % i)
            for i in range(22, 54, 2)]
    lhs += [("GND", "Power", "Ground.", "GND")]
    rhs = [("+5V", "Power", "5 V power rail.", "5V")]
    rhs += [("D%d" % i, "Digital", "GPIO %d. %s" % (i, D3V3), "D%d" % i)
            for i in range(23, 54, 2)]
    rhs += [("GND", "Power", "Ground.", "GND")]
    for i, e in enumerate(lhs):
        p.append(P(e[0], e[1], e[2], MEGA_SIDE_XL, MEGA_SIDE_Y0 + i * PITCH,
                   "right", "L", "side_even", e[3]))
    for i, e in enumerate(rhs):
        p.append(P(e[0], e[1], e[2], MEGA_SIDE_XR, MEGA_SIDE_Y0 + i * PITCH,
                   "right", "R", "side_odd", e[3]))
    return p


GIGA = dict(
    slug="arduino_giga_r1_wifi",
    title="Arduino GIGA R1 WiFi",
    label="GIGA",
    sku="ABX00063",
    module_id="com.greenshoegarage.arduino.giga-r1-wifi-tht-v1",
    board=(MEGA_L, MEGA_W),
    family="microcontroller board (arduino)",
    processor="STM32H747XIH6",
    voltage="3.3V",
    url="https://store.arduino.cc/products/giga-r1-wifi",
    datasheet="ABX00063 product reference manual, page footer Modified 09/06/2026, "
              "change log latest entry 16/01/2026 (ISED antenna specifications)",
    tags=["arduino", "GIGA", "STM32H747", "Mega form factor", "WiFi", "Bluetooth",
          "IoT", "ABX00063"],
    description=(
        "Arduino GIGA R1 WiFi (SKU ABX00063), the STM32H747XI in the Mega form "
        "factor: a dual core Arm Cortex-M7 at 480 MHz plus Cortex-M4 at 240 MHz, "
        "with a Murata 1DX (CYW4343W) WiFi and Bluetooth module and an ATECC608A "
        "secure element. 76 digital I/O, 12 analog inputs and 2 DAC outputs on "
        "headers. The thing to keep in mind when wiring it: the logic level is "
        "3.3 V, not the 5 V of the Mega 2560 it physically resembles, so a Mega "
        "era shield that drives signals at 5 V will damage this board. VIN "
        "accepts 6 V to 24 V. The DC current per I/O pin is only 8 mA."),
    key_warnings=[
        "3.3 V logic in a Mega shaped board. A 5 V shield can damage it.",
        "8 mA maximum per I/O pin.",
        "VIN range is 6 V to 24 V.",
    ],
    art=dict(usb="usbc_and_a", module_x=(62, 80), matrix=None, jack=True),
    pins=giga_pins(),
    headers=[("JANALOG", 24, "datasheet section 14.2"),
             ("JDIGITAL", 26, "datasheet section 14.3"),
             ("JSIDE LHS", 18, "datasheet section 14.5"),
             ("JSIDE RHS", 18, "datasheet section 14.6")],
    deferred=[
        "J1, the three pin OFF / GND / VRTC header (datasheet section 14.1)",
        "the STM32 ICSP 2x3 header (datasheet section 14.4)",
        "the JTAG header, the 20 pin Arducam camera connector, the display "
        "connector, the 3.5 mm audio jack (J15) and the micro UFL antenna connector",
    ],
    errata=[
        "Section 14.3 lists header pin 18 as D0/TX0 while its own description "
        "says Serial 0 Receiver. It is the receive pin. This part names it "
        "D0/RX0.",
    ],
)

# ===========================================================================
# Arduino UNO R4 WiFi (ABX00087)
# ===========================================================================
def uno_analog_row(entries):
    return (row(entries[:8], UNO_PWR_X, UNO_BOT_Y, "bottom", "L", "power")
            + row(entries[8:], UNO_ANA_X, UNO_BOT_Y, "bottom", "L", "analog"))


def uno_digital_row(entries):
    return (row(entries[:10], UNO_DIG_A, UNO_TOP_Y, "top", "R", "dig1")
            + row(entries[10:], UNO_DIG_B, UNO_TOP_Y, "top", "R", "dig2"))


def r4_pins():
    a = [("BOOT", "Other", "Boot mode selection. The datasheet English table calls this Mode selection and the Chinese table calls it not connected.", "BOOT"),
         ("IOREF", "Power", "Digital logic voltage reference, tied to the 5 V rail.", "IORF"),
         ("RESET", "Digital", "Board reset.", "RST"),
         ("+3V3", "Power", "3.3 V power rail.", "3V3"),
         ("+5V", "Power", "5 V power rail.", "5V"),
         ("GND", "Power", "Ground.", "GND"),
         ("GND", "Power", "Ground.", "GND"),
         ("VIN", "Power", "Voltage input, 6 V to 24 V, shared with the DC barrel jack.", "VIN"),
         ("A0", "Analog", "Analog input 0, also the 12 bit DAC output. " + D5V0, "A0"),
         ("A1", "Analog", "Analog input 1, OPAMP non inverting input. " + D5V0, "A1"),
         ("A2", "Analog", "Analog input 2, OPAMP inverting input. " + D5V0, "A2"),
         ("A3", "Analog", "Analog input 3, OPAMP output. " + D5V0, "A3"),
         ("A4/SDA", "Analog", "Analog input 4, primary I2C SDA. Not usable as an ADC input while the bus is active.", "A4"),
         ("A5/SCL", "Analog", "Analog input 5, primary I2C SCL. Not usable as an ADC input while the bus is active.", "A5")]
    d = [("SCL", "Digital", "Primary I2C clock, same bus as A5.", "SCL"),
         ("SDA", "Digital", "Primary I2C data, same bus as A4.", "SDA"),
         ("AREF", "Digital", "Analog reference voltage.", "AREF"),
         ("GND", "Power", "Ground.", "GND"),
         ("D13/SCK", "Digital", "GPIO 13, SPI clock, CAN receive. " + D5V0, "D13"),
         ("D12/CIPO", "Digital", "GPIO 12, SPI CIPO (MISO). " + D5V0, "D12"),
         ("D11/COPI", "Digital", "GPIO 11, SPI COPI (MOSI), PWM capable. " + D5V0, "D11"),
         ("D10/CS", "Digital", "GPIO 10, SPI chip select, CAN transmit, PWM capable. " + D5V0, "D10"),
         ("D9", "Digital", "GPIO 9, PWM capable. " + D5V0, "D9"),
         ("D8", "Digital", "GPIO 8. " + D5V0, "D8"),
         ("D7", "Digital", "GPIO 7. " + D5V0, "D7"),
         ("D6", "Digital", "GPIO 6, PWM capable. " + D5V0, "D6"),
         ("D5", "Digital", "GPIO 5, PWM capable. " + D5V0, "D5"),
         ("D4", "Digital", "GPIO 4. " + D5V0, "D4"),
         ("D3", "Digital", "GPIO 3, PWM capable, interrupt pin. " + D5V0, "D3"),
         ("D2", "Digital", "GPIO 2, interrupt pin. " + D5V0, "D2"),
         ("D1/TX0", "Digital", "GPIO 1, Serial 0 transmit. " + D5V0, "D1"),
         ("D0/RX0", "Digital", "GPIO 0, Serial 0 receive. " + D5V0, "D0")]
    return uno_analog_row(a) + uno_digital_row(d)


R4 = dict(
    slug="arduino_uno_r4_wifi",
    title="Arduino UNO R4 WiFi",
    label="UNO R4",
    sku="ABX00087",
    module_id="com.greenshoegarage.arduino.uno-r4-wifi-tht-v1",
    board=(UNO_L, UNO_W),
    family="microcontroller board (arduino)",
    processor="R7FA4M1AB3CFM (RA4M1)",
    voltage="5V",
    url="https://store.arduino.cc/products/uno-r4-wifi",
    datasheet="ABX00087 product reference manual, page footer Modified 28/05/2026, "
              "change log revision 8 (29/10/2025, mechanical drawing update)",
    tags=["arduino", "UNO", "UNO R4", "RA4M1", "ESP32-S3", "WiFi", "Bluetooth",
          "LED matrix", "ABX00087"],
    description=(
        "Arduino UNO R4 WiFi (SKU ABX00087). A Renesas RA4M1 (48 MHz Arm "
        "Cortex-M4) as the main MCU with an ESP32-S3-MINI-1-N8 as a secondary "
        "MCU for WiFi and Bluetooth, in the UNO form factor and pinout. The "
        "RA4M1 runs at 5 V so existing UNO R3 shields and accessories still "
        "work, but the ESP32-S3 side of the board is 3.3 V and the two must not "
        "be brought into contact. GPIO current is limited to 8 mA per pin. VIN "
        "and the barrel jack accept 6 V to 24 V, while USB-C must not exceed "
        "5 V. This part exposes the two shield headers. The same footprint "
        "applies to the UNO R4 Minima (ABX00080), which lacks the radio, the "
        "LED matrix and the Qwiic connector."),
    key_warnings=[
        "5 V logic on the headers, unlike most recent Arduino boards.",
        "The ESP32-S3 module is 3.3 V. Keep its pins away from the 5 V domain.",
        "8 mA maximum per GPIO.",
    ],
    art=dict(usb="usbc", module_x=(44, 60), matrix=(24, 40), jack=True),
    pins=r4_pins(),
    headers=[("JANALOG", 14, "datasheet section 12.1"),
             ("JDIGITAL", 18, "datasheet section 12.2")],
    deferred=[
        "JOFF, the OFF / GND / VRTC header (datasheet section 12.3)",
        "the ICSP 2x3 header (datasheet section 12.4)",
        "the Qwiic I2C connector (SM04B-SRSS-TB) and the six pin ESP header",
    ],
    errata=[
        "Section 12.2 lists header pin 18 as D0/TX0 while its own description "
        "says Serial 0 Receiver. It is the receive pin. This part names it "
        "D0/RX0.",
        "Section 12.1 pin 1 is BOOT in the English table and not connected in "
        "the Chinese table of the same document. This part names it BOOT and "
        "types it Other.",
        "Section 12.3 numbers its three rows 1, 2, 1. Read as a three position "
        "header carrying OFF, GND and VRTC.",
    ],
)

# ===========================================================================
# Arduino UNO Q (ABX00162 / ABX00173)
# ===========================================================================
def q_pins():
    a = [("BOOT", "Other", "MCU_BOOT0 boot strap. 3.3 V.", "BOOT"),
         ("IOREF", "Power", "I/O voltage reference, mirrors the 3.3 V rail. Output only, do not back feed.", "IORF"),
         ("RESET", "Digital", "STM32U585 reset (MCU_NRST).", "RST"),
         ("+3V3", "Power", "3.3 V supply out.", "3V3"),
         ("+5V", "Power", "5 V USB VBUS pass through. Power only.", "5V"),
         ("GND", "Power", "Ground.", "GND"),
         ("GND", "Power", "Ground.", "GND"),
         ("VIN", "Power", "7 V to 24 V DC input. Power only.", "VIN"),
         ("A0/D14", "Analog", "ADC input and DAC0 on PA4. Direct ADC input, NOT 5 V tolerant, absolute maximum about 3.6 V.", "A0"),
         ("A1/D15", "Analog", "ADC input and DAC1 on PA5. Direct ADC input, NOT 5 V tolerant, absolute maximum about 3.6 V.", "A1"),
         ("A2/D16", "Analog", "ADC input on PA6, OPAMP2 positive input. Not 5 V tolerant in analog mode.", "A2"),
         ("A3/D17", "Analog", "ADC input on PA7, OPAMP2 negative input. Not 5 V tolerant in analog mode.", "A3"),
         ("A4/D18", "Analog", "ADC input on PC1, I2C3 SDA. Pull up to 3.3 V only.", "A4"),
         ("A5/D19", "Analog", "ADC input on PC0, I2C3 SCL. Pull up to 3.3 V only.", "A5")]
    # JDIGITAL, datasheet section 9.6, listed D0 first. The UNO shield row runs
    # SCL, SDA, AREF, GND, D13 down to D0 from left to right, so the datasheet
    # order is reversed onto the physical row here.
    d = [("D21/SCL", "Digital", "GPIO 21 on PB10, I2C2 clock. 3.3 V, 5 V tolerant as an input.", "SCL"),
         ("D20/SDA", "Digital", "GPIO 20 on PB11, I2C2 data. 3.3 V, 5 V tolerant as an input.", "SDA"),
         ("AREF", "Other", "Analog reference pin. Not a GPIO.", "AREF"),
         ("GND", "Power", "Ground.", "GND"),
         ("D13/SCK", "Digital", "GPIO 13 on PB13, SPI2 SCK. 3.3 V, 5 V tolerant as an input.", "D13"),
         ("D12/CIPO", "Digital", "GPIO 12 on PB14, SPI2 MISO. 3.3 V, 5 V tolerant as an input.", "D12"),
         ("D11/COPI", "Digital", "GPIO 11 on PB15, SPI2 MOSI, PWM capable. 3.3 V, 5 V tolerant as an input.", "D11"),
         ("D10/CS", "Digital", "GPIO 10 on PB9, SPI2 chip select, PWM capable. 3.3 V, 5 V tolerant as an input.", "D10"),
         ("D9", "Digital", "GPIO 9 on PB8, PWM capable. 3.3 V, 5 V tolerant as an input.", "D9"),
         ("D8", "Digital", "GPIO 8 on PB4. 3.3 V, 5 V tolerant as an input.", "D8"),
         ("D7", "Digital", "GPIO 7 on PB2. 3.3 V, 5 V tolerant as an input.", "D7"),
         ("D6", "Digital", "GPIO 6 on PB1, PWM capable. 3.3 V, 5 V tolerant as an input.", "D6"),
         ("D5", "Digital", "GPIO 5 on PA11, FDCAN1 RX, PWM capable. 3.3 V, 5 V tolerant as an input.", "D5"),
         ("D4", "Digital", "GPIO 4 on PA12, FDCAN1 TX. 3.3 V, 5 V tolerant as an input.", "D4"),
         ("D3", "Digital", "GPIO 3 on PB0, OPAMP2 output, PWM capable. TT type I/O, 3.6 V tolerant only, NOT 5 V tolerant in any mode.", "D3"),
         ("D2", "Digital", "GPIO 2 on PB3. 3.3 V, 5 V tolerant as an input.", "D2"),
         ("D1/TX", "Digital", "GPIO 1 on PB6, USART1 TX. 3.3 V, 5 V tolerant as an input.", "D1"),
         ("D0/RX", "Digital", "GPIO 0 on PB7, USART1 RX. 3.3 V, 5 V tolerant as an input.", "D0")]
    return uno_analog_row(a) + uno_digital_row(d)


UNOQ = dict(
    slug="arduino_uno_q",
    title="Arduino UNO Q",
    label="UNO Q",
    sku="ABX00162 / ABX00173",
    module_id="com.greenshoegarage.arduino.uno-q-tht-v1",
    board=(UNO_L, UNO_W),
    family="single board computer (arduino)",
    processor="Qualcomm Dragonwing QRB2210 plus STM32U585",
    voltage="3.3V",
    url="https://store.arduino.cc/products/uno-q",
    datasheet="ABX00162-ABX00173 product reference manual, page footer Modified 28/05/2026",
    tags=["arduino", "UNO", "UNO Q", "QRB2210", "STM32U585", "Linux", "SBC",
          "WiFi", "Bluetooth", "ABX00162"],
    description=(
        "Arduino UNO Q (SKU ABX00162 with 2 GB / 16 GB, ABX00173 with 4 GB / "
        "32 GB). A single board computer in the UNO form factor: a quad core "
        "Qualcomm Dragonwing QRB2210 Cortex-A53 running Debian alongside an "
        "STM32U585 Cortex-M33 running the Arduino core on Zephyr. The UNO "
        "shaped headers are driven by the STM32U585 and they are 3.3 V, not the "
        "5 V of an UNO R3 or an UNO R4. Most digital pins are 5 V tolerant as "
        "inputs, but D3 is not tolerant above 3.6 V in any mode and the analog "
        "pins are not 5 V tolerant at all. IOREF reports 3.3 V and is an output "
        "only. This part exposes JDIGITAL and JANALOG, the two headers that "
        "carry UNO shields."),
    key_warnings=[
        "The headers are 3.3 V even though the board takes UNO shields.",
        "D3 (PB0) is 3.6 V tolerant only, in every mode including digital.",
        "A0 through A5 are not 5 V tolerant. Absolute maximum is about 3.6 V.",
        "IOREF mirrors the 3.3 V rail and is an output. Do not feed power back into it.",
    ],
    art=dict(usb="usbc", module_x=(40, 62), matrix=(20, 36), jack=False),
    pins=q_pins(),
    headers=[("JANALOG (A3)", 14, "datasheet section 9.7"),
             ("JDIGITAL (A2)", 18, "datasheet section 9.6")],
    deferred=[
        "JMEDIA (60 pin, MIPI CSI and DSI) and JMISC (60 pin, mixed 1.8 V and "
        "3.3 V) board to board connectors",
        "JSPI (6 pin), JCTL (10 pin) and the Qwiic I2C connector",
        "the power button (JBTN1) and the USB-C connector as electrical connectors",
    ],
    errata=[
        "Section 9.6 lists JDIGITAL from D0 to D21. On the physical UNO shield "
        "row that order runs right to left, so this part places D0 at the right "
        "hand end next to the USB, matching every other UNO form factor board.",
    ],
)

BOARDS = [GIGA, R4, UNOQ]


# ===========================================================================
# Arduino GIGA Display Shield (ASX00039)
#
# This board is not like the other four. Its datasheet has no pinout section at
# all: it names connectors by reference designator (J3 camera, J4 display,
# J5 touch, J6 and J7 "2.54 mm Header GIGA Connector") and gives no pin counts,
# no signal names, no positions and no outline dimensions in text.
#
# Everything below was recovered from the netlist annotations in the published
# schematic PDF (ASX00039-schematics.pdf, revision V0.5, 17/10/2024), sheet 2
# of 8, "GIGA HEADERS". Pin designators of the form PIJ60nn / PIJ70nn are paired
# with net labels of the form NLxxx in that file, which is what fixes each pin.
#
# Pins whose net could not be resolved unambiguously are named by designator
# rather than guessed. They are the power and ground pins.
# ===========================================================================
DS_PITCH = 2.54
J6_X, J7_X = 14.0, 30.0     # nominal, see notes
J_Y = 9.0


def display_pins():
    unresolved = ("Power or ground net. The published schematic groups this pin "
                  "with other supply pins but does not label the group, so it is "
                  "NOT resolved. Meter it against the board before connecting "
                  "anything to it.")
    dsi = ("MIPI DSI %s from the GIGA R1 WiFi, routed on the shield to the "
           "KD040WVFID026 display through J4. Differential pair, treat as such "
           "if you carry it anywhere.")
    j6 = {1: ("DSI_D1_N", "Digital", dsi % "data lane 1 negative"),
          2: ("DSI_D1_P", "Digital", dsi % "data lane 1 positive"),
          5: ("DSI_CK_N", "Digital", dsi % "clock negative"),
          6: ("DSI_CK_P", "Digital", dsi % "clock positive"),
          9: ("DSI_D0_N", "Digital", dsi % "data lane 0 negative"),
          10: ("DSI_D0_P", "Digital", dsi % "data lane 0 positive"),
          13: ("PC6", "Digital", "STM32H747 port PC6, in the GPIOS group on the schematic. 3.3 V."),
          14: ("PI0", "Digital", "STM32H747 port PI0, in the GPIOS group on the schematic. 3.3 V."),
          15: ("PI1", "Digital", "STM32H747 port PI1, in the GPIOS group on the schematic. 3.3 V."),
          16: ("PI2", "Digital", "STM32H747 port PI2, in the GPIOS group on the schematic. 3.3 V."),
          17: ("PI3", "Digital", "STM32H747 port PI3, in the GPIOS group on the schematic. 3.3 V."),
          18: ("PC1", "Digital", "STM32H747 port PC1, one of the two DFSDM1 lines that carry the MP34DT06 PDM microphone (clock or data, not resolved). 3.3 V."),
          19: ("PB12", "Digital", "STM32H747 port PB12, in the GPIOS group on the schematic. 3.3 V."),
          20: ("PD3", "Digital", "STM32H747 port PD3, one of the two DFSDM1 lines that carry the MP34DT06 PDM microphone (clock or data, not resolved). 3.3 V.")}
    j7 = {3: ("PB6", "Digital", "STM32H747 port PB6, on the I2C4 bus. The schematic notes that on the GIGA the camera shares I2C4 with JDIGITAL. SDA or SCL, not resolved. 3.3 V."),
          4: ("PH12", "Digital", "STM32H747 port PH12, on the I2C4 bus. SDA or SCL, not resolved. 3.3 V."),
          5: ("PI5", "Digital", "STM32H747 port PI5, one line of the parallel camera bus. 3.3 V."),
          6: ("PH8", "Digital", "STM32H747 port PH8, one line of the parallel camera bus. 3.3 V."),
          7: ("PA6", "Digital", "STM32H747 port PA6, one line of the parallel camera bus. 3.3 V."),
          8: ("PJ9", "Digital", "STM32H747 port PJ9, one line of the parallel camera bus. 3.3 V."),
          9: ("PI7", "Digital", "STM32H747 port PI7, one line of the parallel camera bus. 3.3 V."),
          10: ("PI6", "Digital", "STM32H747 port PI6, one line of the parallel camera bus. 3.3 V."),
          11: ("PI4", "Digital", "STM32H747 port PI4, one line of the parallel camera bus. 3.3 V."),
          12: ("PH14", "Digital", "STM32H747 port PH14, one line of the parallel camera bus. 3.3 V."),
          13: ("PG11", "Digital", "STM32H747 port PG11, one line of the parallel camera bus. 3.3 V."),
          14: ("PH11", "Digital", "STM32H747 port PH11, one line of the parallel camera bus. 3.3 V."),
          15: ("PH10", "Digital", "STM32H747 port PH10, one line of the parallel camera bus. 3.3 V."),
          16: ("PH9", "Digital", "STM32H747 port PH9, one line of the parallel camera bus. 3.3 V."),
          17: ("PA1", "Digital", "STM32H747 port PA1, a camera control line (POWER_EN or PWDN, not resolved). The schematic shows this net on J7 pins 17 and 19. 3.3 V."),
          18: ("PD4", "Digital", "STM32H747 port PD4, a camera control line (POWER_EN or PWDN, not resolved). The schematic shows this net on J7 pins 18 and 20. 3.3 V."),
          19: ("PA1", "Digital", "STM32H747 port PA1 again. The schematic shows the same net on J7 pins 17 and 19. 3.3 V."),
          20: ("PD4", "Digital", "STM32H747 port PD4 again. The schematic shows the same net on J7 pins 18 and 20. 3.3 V.")}
    out = []
    for (tagname, table, count, x0, group) in (("J6", j6, 24, J6_X, "j6"),
                                               ("J7", j7, 20, J7_X, "j7")):
        for n in range(1, count + 1):
            col_left = (n % 2 == 1)
            x = x0 if col_left else x0 + DS_PITCH
            y = J_Y + ((n - 1) // 2) * DS_PITCH
            if n in table:
                nm, ty, de = table[n]
                short = nm.replace("DSI_", "")
            else:
                nm, ty, de = "%s-%d" % (tagname, n), "Power", unresolved
                short = "%d" % n
            e = P(nm, ty, de, x, y, "right", "L" if group == "j6" else "R",
                  group, short)
            e["lside"] = "L" if col_left else "R"
            out.append(e)
    return out


DISPLAY = dict(
    slug="arduino_giga_display_shield",
    title="Arduino GIGA Display Shield",
    label="GIGA DISP",
    sku="ASX00039",
    version="0.9.0",
    module_id="com.greenshoegarage.arduino.giga-display-shield-tht-v0",
    board=(48.0, 46.0),
    nominal=True,
    connector_type="female",
    family="shield (arduino)",
    processor="none, the shield has no microcontroller",
    voltage="3.3V",
    url="https://store.arduino.cc/products/giga-display-shield",
    datasheet="ASX00039 product reference manual, page footer Modified 17/07/2026, "
              "plus ASX00039-schematics.pdf revision V0.5 dated 17/10/2024, which "
              "is where every pin identity below comes from",
    tags=["arduino", "GIGA", "display shield", "touchscreen", "BMI270", "shield",
          "ASX00039"],
    description=(
        "Arduino GIGA Display Shield (SKU ASX00039). A 3.97 inch 480x800 "
        "capacitive touch TFT with a BMI270 6 axis IMU, an MP34DT06 PDM "
        "microphone, an RGB LED and a 20 pin Arducam connector, for the GIGA R1 "
        "WiFi. It has no microcontroller and cannot be programmed on its own. It "
        "mates with the two 2.54 mm headers in the middle of the GIGA R1 WiFi, "
        "not with the shield rows, so the 54 pins on the outer headers stay "
        "free. IMPORTANT: this part is v0.9.0, not v1.0.0, because the shield's "
        "own datasheet contains no pinout table and no readable mechanical "
        "dimensions. Pin identities were recovered from the published schematic "
        "netlist. The supply and ground pins could not be resolved and are named "
        "by designator (J6-3 and so on). Connector positions and the board "
        "outline are nominal and are NOT dimensioned. Use this for schematic "
        "capture and illustration, not for ordering a carrier board."),
    key_warnings=[
        "This part is v0.9.0. It does not meet the standard of the other four "
        "parts in this set, for the reasons in the description and below.",
        "The shield needs a GIGA R1 WiFi. It has no microcontroller of its own.",
        "Eight of the 44 pins are supply or ground pins whose net could not be "
        "resolved from the published schematic. They are named by designator, "
        "not guessed. Meter them before connecting anything.",
        "Connector positions and the board outline in PCB view are nominal. Do "
        "not order a board against this footprint.",
        "Logic is 3.3 V. The VIN header input range is 6 V to 32 V.",
    ],
    art=dict(usb=None, module_x=None, matrix=None, jack=False, screen=True),
    pins=display_pins(),
    headers=[("J6", 24, "schematic sheet 2, GIGA HEADERS"),
             ("J7", 20, "schematic sheet 2, GIGA HEADERS")],
    group_header={"j6": 0, "j7": 1},
    deferred=[
        "J3, the 20 pin 2.54 mm Arducam camera header (pin map is in the "
        "schematic, but its board position is not)",
        "J4 display video and J5 touch flex connectors, which are internal to "
        "the shield and not user wiring points",
        "the two alignment posts on J6 and J7",
    ],
    errata=[
        "The ASX00039 datasheet has no pinout section. Sections 6.1 and 6.2 name "
        "the connectors by reference designator only. Every pin identity in this "
        "part therefore comes from the schematic PDF rather than from the "
        "datasheet.",
        "The schematic shows STM32 port PA1 on J7 pins 17 and 19, and port PD4 "
        "on J7 pins 18 and 20. Both are reproduced as drawn rather than "
        "corrected.",
        "The camera bus lines on J7 are identified by STM32 port name. The "
        "schematic lists the camera signal names (DOUT0 to DOUT7, VSYNC, HREF, "
        "PCLK, XCLK) as a group without a per pin pairing that survives text "
        "extraction, so no per pin camera signal name is claimed here.",
    ],
)

BOARDS.append(DISPLAY)
