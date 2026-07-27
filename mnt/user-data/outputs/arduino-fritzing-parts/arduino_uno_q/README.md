# Arduino UNO Q (ABX00162 / ABX00173) Fritzing part

Version 1.0.0

An installable Fritzing part with all four views present: breadboard, schematic,
PCB and icon. The schematic is a wireable symbol on the 0.1 inch grid and the
PCB view is a through hole footprint on 2.54 mm pitch.

This part exposes 32 header pins as `connector0` through `connector31`.

## Read this before wiring anything

1. The headers are 3.3 V even though the board takes UNO shields.
2. D3 (PB0) is 3.6 V tolerant only, in every mode including digital.
3. A0 through A5 are not 5 V tolerant. Absolute maximum is about 3.6 V.
4. IOREF mirrors the 3.3 V rail and is an output. Do not feed power back into it.

These points are carried in the `.fzp` description and in the per connector
descriptions, so they appear in Fritzing's inspector and not only here.

## Built from

| Item | Revision used |
|---|---|
| Board | Arduino UNO Q, SKU ABX00162 / ABX00173 |
| Datasheet | ABX00162-ABX00173 product reference manual, page footer Modified 28/05/2026 |
| Shield header geometry | Fritzing core parts, measured (see NOTES.md) |
| EAGLE reference design | **not fetched**, see Known Limitations |

## Install

Fritzing 1.0.x or newer. File, then Open, then select `arduino_uno_q.fzpz`. The part
lands in the MINE bin. The `moduleId` is `com.greenshoegarage.arduino.uno-q-tht-v1`, so it will not collide with
any Arduino published part.

The `src/` tree holds the same five files the archive contains, kept flat so the
part stays diffable in git. Rebuild with `python3 tools/render.py`.

## Headers exposed

| Header | Positions | Source |
|---|---|---|
| JANALOG (A3) | 14 | datasheet section 9.7 |
| JDIGITAL (A2) | 18 | datasheet section 9.6 |

Board outline as drawn: 68.58 mm by 53.34 mm. Pads: 1.0 mm drill on a 1.8 mm
pad, 2.54 mm pitch.

## Connector map

| Fritzing | Header pin | Name | Type | Position x, y (mm) |
|---|---|---|---|---|
| connector0 | JANALOG (A3) 1 | BOOT | Other | 27.94, 50.80 |
| connector1 | JANALOG (A3) 2 | IOREF | Power | 30.48, 50.80 |
| connector2 | JANALOG (A3) 3 | RESET | Digital | 33.02, 50.80 |
| connector3 | JANALOG (A3) 4 | +3V3 | Power | 35.56, 50.80 |
| connector4 | JANALOG (A3) 5 | +5V | Power | 38.10, 50.80 |
| connector5 | JANALOG (A3) 6 | GND | Power | 40.64, 50.80 |
| connector6 | JANALOG (A3) 7 | GND | Power | 43.18, 50.80 |
| connector7 | JANALOG (A3) 8 | VIN | Power | 45.72, 50.80 |
| connector8 | JANALOG (A3) 9 | A0/D14 | Analog | 50.80, 50.80 |
| connector9 | JANALOG (A3) 10 | A1/D15 | Analog | 53.34, 50.80 |
| connector10 | JANALOG (A3) 11 | A2/D16 | Analog | 55.88, 50.80 |
| connector11 | JANALOG (A3) 12 | A3/D17 | Analog | 58.42, 50.80 |
| connector12 | JANALOG (A3) 13 | A4/D18 | Analog | 60.96, 50.80 |
| connector13 | JANALOG (A3) 14 | A5/D19 | Analog | 63.50, 50.80 |
| connector14 | JDIGITAL (A2) 1 | D21/SCL | Digital | 18.80, 2.54 |
| connector15 | JDIGITAL (A2) 2 | D20/SDA | Digital | 21.34, 2.54 |
| connector16 | JDIGITAL (A2) 3 | AREF | Other | 23.88, 2.54 |
| connector17 | JDIGITAL (A2) 4 | GND | Power | 26.42, 2.54 |
| connector18 | JDIGITAL (A2) 5 | D13/SCK | Digital | 28.96, 2.54 |
| connector19 | JDIGITAL (A2) 6 | D12/CIPO | Digital | 31.50, 2.54 |
| connector20 | JDIGITAL (A2) 7 | D11/COPI | Digital | 34.04, 2.54 |
| connector21 | JDIGITAL (A2) 8 | D10/CS | Digital | 36.58, 2.54 |
| connector22 | JDIGITAL (A2) 9 | D9 | Digital | 39.12, 2.54 |
| connector23 | JDIGITAL (A2) 10 | D8 | Digital | 41.66, 2.54 |
| connector24 | JDIGITAL (A2) 11 | D7 | Digital | 45.72, 2.54 |
| connector25 | JDIGITAL (A2) 12 | D6 | Digital | 48.26, 2.54 |
| connector26 | JDIGITAL (A2) 13 | D5 | Digital | 50.80, 2.54 |
| connector27 | JDIGITAL (A2) 14 | D4 | Digital | 53.34, 2.54 |
| connector28 | JDIGITAL (A2) 15 | D3 | Digital | 55.88, 2.54 |
| connector29 | JDIGITAL (A2) 16 | D2 | Digital | 58.42, 2.54 |
| connector30 | JDIGITAL (A2) 17 | D1/TX | Digital | 60.96, 2.54 |
| connector31 | JDIGITAL (A2) 18 | D0/RX | Digital | 63.50, 2.54 |

## Datasheet errata noticed while building this

- Section 9.6 lists JDIGITAL from D0 to D21. On the physical UNO shield row that order runs right to left, so this part places D0 at the right hand end next to the USB, matching every other UNO form factor board.

## Known Limitations

1. **The EAGLE reference design was never opened.** The build environment could
   not reach the Arduino asset host for the design archives, so no dimension in
   this part is a reading of the board's own design file.
2. **Header positions come from the Fritzing core shield footprint**, measured
   out of the published core parts rather than from Arduino's design files. That
   footprint is the one the shield ecosystem is built against, including the two
   irregular gaps, so it should be right. It is not first party data.
3. **No mounting holes are drawn.** See NOTES.md section 2 for why.
4. **These connectors are not exposed in v1.0.0:**
- JMEDIA (60 pin, MIPI CSI and DSI) and JMISC (60 pin, mixed 1.8 V and 3.3 V) board to board connectors
- JSPI (6 pin), JCTL (10 pin) and the Qwiic I2C connector
- the power button (JBTN1) and the USB-C connector as electrical connectors
   Each of them needs a board position that only the design file supplies.
5. **The part has not been opened in Fritzing** and no Gerber has been exported.
   40 automated checks were run against the files themselves and all pass,
   but load behaviour, hover highlighting and Gerber measurements are unverified.
6. **Nothing has been checked against physical hardware.**

## Licence

Part assets (the `.fzp` and the four view SVGs) are licensed CC BY-SA 3.0, the
Fritzing parts convention. The build and verification tooling is licensed
GPL-3.0.

Arduino and the Arduino board designs are the property of Arduino S.r.l. This is
an independent reimplementation drawn from Arduino's published documentation and
is not an official Arduino release.
