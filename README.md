# Arduino Fritzing parts

Five installable Fritzing parts built to one brief and one standard: four views
each, schematic and PCB held to production quality, part assets under
CC BY-SA 3.0. Four of the five are at v1.0.0. The GIGA Display Shield is at
v0.9.0 because its published documentation does not support the same standard,
which is explained in its section below.

| Part | SKU | Version | Connectors | Outline | Header logic |
|---|---|---|---|---|---|
| [Arduino MKR WiFi 1010](#arduino-mkr-wifi-1010-abx00023) | ABX00023 | v1.0.0 | 28 | 61.5 by 25.0 mm | 3.3V |
| [Arduino GIGA R1 WiFi](#arduino-giga-r1-wifi-abx00063) | ABX00063 | v1.0.0 | 86 | 101.68 by 53.34 mm | 3.3V |
| [Arduino UNO R4 WiFi](#arduino-uno-r4-wifi-abx00087) | ABX00087 | v1.0.0 | 32 | 68.58 by 53.34 mm | 5V |
| [Arduino UNO Q](#arduino-uno-q-abx00162--abx00173) | ABX00162 / ABX00173 | v1.0.0 | 32 | 68.58 by 53.34 mm | 3.3V |
| [Arduino GIGA Display Shield](#arduino-giga-display-shield-asx00039) | ASX00039 | v0.9.0 | 44 | 48.0 by 46.0 mm | 3.3V |

217 automated checks across the five parts, 0 failing. Each part folder holds
the `.fzpz` you install, a flat `src/` tree so the part stays diffable in git, a
NOTES.md engineering record, the verification log, and PNG previews of all four
views. This file is the merged README for the whole set.

## The logic levels are the point

These boards are not interchangeable and two of them look like they should be.
The UNO R4 WiFi runs its headers at 5 V for shield compatibility. The UNO Q takes
the same shields on the same footprint at 3.3 V, with D3 not tolerant above
3.6 V in any mode and the analog pins not 5 V tolerant at all. The GIGA is a
3.3 V board in a Mega shaped package. The MKR WiFi 1010 is 3.3 V and its 5V pin
is not a supply at all.

Every one of those facts is written into the `.fzp` description and into the
individual connector descriptions, so it shows up in Fritzing's inspector rather
than only in a README nobody opens.

## Install

Fritzing 1.0.x or newer. File, then Open, then select the `.fzpz`. The part lands
in the MINE bin. Alternatively use the bin menu at the top right of the Parts
palette, then Import.

Every `moduleId` is reverse DNS under `com.greenshoegarage.arduino.`, so these
sit alongside Arduino's own published parts without collision.

Rebuild the three shield format parts with `python3 tools/make.py` from the set
root. The MKR WiFi 1010 predates that generator and keeps its own, so rebuild it
with `python3 tools/build.py` from inside `arduino_mkr_wifi_1010/`.

## What the parts share

- 2.54 mm pitch, 1.0 mm drill on a 1.8 mm pad, drawn as a circle with
  `fill="none"` and a 0.4 mm stroke so the drill is the inner clear area.
- `copper1` containing a nested `copper0`, so the parts work on one sided and two
  sided boards, with `id="connectorNpin"` on every pad.
- Schematic pins exactly 0.1 in long on the 0.1 in grid, with the
  `connectorNterminal` element at the free tip so wires attach at the tip and not
  the body edge.
- All text in all views is stroked path geometry from a single stroke font
  written for this build. No view depends on a font being installed anywhere.
- No CSS classes, no style blocks, no clipPath, no mask, no filters, no embedded
  raster, no cross layer `<use>`, no unitless dimensions, no nested transforms on
  connector elements.
- No em dashes anywhere in the parts, the tooling or the documentation.

## Known Limitations for the whole set

1. **No Arduino EAGLE or design archive was ever opened.** The build
   environment's network egress allowlist does not include the Arduino asset
   host, so no dimension in any of these parts is a reading of a board's own
   design file. Everything mechanical comes from datasheet text, published
   figures, measurement of the Fritzing core parts, or derivation, and each part
   section above says which.
2. **Shield style header rows only.** Debug, ICSP, Qwiic, ESLOV, JSPI, JMEDIA,
   JMISC, JCTL, Li-Po, OFF and VRTC connectors are deferred across the set for
   one reason: each needs a board position, board positions come from the design
   file, and a connector at a guessed coordinate inside a footprint whose whole
   point is that you could order a board against it is worse than a connector
   that is visibly missing. Per part lists are above.
3. **No mounting holes are drawn** on any part, for the same reason. The UNO Q
   datasheet does list mechanical dimensions in text (15.24, 13.97, 7.62, 2.54,
   2x 3.01, 4x R1.6 and others) but they are unlabelled in the extracted text and
   cannot be assigned to features without the drawing.
4. **None of the parts has been opened in Fritzing** and no Gerber has been
   exported. The checks that pass are structural and dimensional checks run
   against the files themselves. Load behaviour, hover highlighting across views,
   and Gerber measurements are unverified.
5. **Nothing has been checked against physical hardware.** No board was seated on
   a breadboard and nothing was measured with calipers.
6. **No footprint was diffed against Arduino's own published Fritzing parts**,
   which live on the same unreachable host.

## Verification

Each part folder carries `verification-log.txt` with the measured results, not
checkmarks. Rerun for the shield format parts with `python3 tools/make.py` from
the set root, and for the MKR with `python3 tools/verify.py` from inside
`arduino_mkr_wifi_1010/`.

What is actually measured: pad pitch inside every header block, drill and pad
diameter recovered from the drawn geometry, silkscreen outline size, every pad
inside the outline, no silkscreen or label geometry landing on a pad, connector
id contiguity and uniqueness in each view, agreement between the `.fzp` and every
SVG, schematic grid snapping, pin line length, terminal position, archive
contents, and prose style rules.

## Arduino MKR WiFi 1010 (ABX00023)

`arduino_mkr_wifi_1010/arduino_mkr_wifi_1010.fzpz` &middot; v1.0.0 &middot; 28 connectors &middot; 61.5 by 25.0 mm &middot; header logic 3.3V &middot; 57 checks pass, 0 fail

1. 3.3 V I/O and NOT 5 V tolerant. A 5 V signal on any pin will damage the board.
2. The +5V pin (header pin 28) is not a regulated output. It is jumper connected to the USB power input, so it only carries voltage when the board is USB powered.
3. Header pin 28 sits opposite header pin 1. Row B is numbered from the far end back toward the USB, which is the single most common way this part goes wrong.

The 28 header pins are the whole electrical interface for most uses, so this part is complete for breadboard and carrier work even without the three deferred connectors.

**Built from:** ABX00023 product reference manual, revision 5 (25/04/2024), page footer Modified 03/07/2026, plus the official pinout PDF (last update 7/08/2020)

**Headers exposed**

| Header | Positions | Source |
|---|---|---|
| Header | 28 | datasheet section 5.2 |

**Footprint as drawn**

| Property | Value | Confidence |
|---|---|---|
| Pad pitch along each row | 2.54 mm | verified from the datasheet and the MKR header part number |
| Row to row spacing | 17.78 mm (700 mil) | **derived, not read.** Section 6 states the rows are held to a 100 mil grid so the board seats in a breadboard, and 700 mil is the only multiple of 2.54 mm that leaves a workable margin on a 25 mm wide board |
| Board outline | 61.5 by 25.0 mm | published figure, not confirmed against the design file |
| Pin 1 offset from the USB end | 14.24 mm | **assumed.** The 14 position row spans 33.02 mm and this centres it on the board |

Pads are 1.0 mm drill on a 1.8 mm pad throughout the set.

**Not exposed in v1.0.0**

- the debug header (+3V3, SWDIO, RESETN, SWCLK, GND, datasheet section 5.3)
- the ESLOV five pin 1.0 mm expansion connector (mating part SHR-05V-S-B)
- the Li-Po JST connector (S2B-PH-SM4-TB, mates with PHR-2)

**Datasheet errata noticed while building this**

- Section 5.2 leaves the type cell blank for pin 10 (D1). Every neighbour is Digital and the pinout PDF shows PA23 with a timer output, so it is typed Digital here.
- Section 5.2 writes D2/PWM through D5/PWM. This part uses the plain D2 to D5 names with PWM capability in the connector description, since all of D0 to D5 are PWM capable and decorating four of them would mislead.
- The datasheet uses MISO and MOSI while the pinout PDF uses CIPO and COPI. This part uses MISO and MOSI as the primary names and carries both in the descriptions.

**Connector map**

| Fritzing | Header pin | Name | Type | Position x, y (mm) |
|---|---|---|---|---|
| connector0 | Header 1 (row A) | AREF | Analog | 14.24, 3.61 |
| connector1 | Header 2 (row A) | A0/DAC0 | Analog | 16.78, 3.61 |
| connector2 | Header 3 (row A) | A1 | Analog | 19.32, 3.61 |
| connector3 | Header 4 (row A) | A2 | Analog | 21.86, 3.61 |
| connector4 | Header 5 (row A) | A3 | Analog | 24.40, 3.61 |
| connector5 | Header 6 (row A) | A4/SDA | Analog | 26.94, 3.61 |
| connector6 | Header 7 (row A) | A5/SCL | Analog | 29.48, 3.61 |
| connector7 | Header 8 (row A) | A6 | Analog | 32.02, 3.61 |
| connector8 | Header 9 (row A) | D0 | Digital | 34.56, 3.61 |
| connector9 | Header 10 (row A) | D1 | Digital | 37.10, 3.61 |
| connector10 | Header 11 (row A) | D2 | Digital | 39.64, 3.61 |
| connector11 | Header 12 (row A) | D3 | Digital | 42.18, 3.61 |
| connector12 | Header 13 (row A) | D4 | Digital | 44.72, 3.61 |
| connector13 | Header 14 (row A) | D5 | Digital | 47.26, 3.61 |
| connector14 | Header 15 (row B) | D6 | Digital | 47.26, 21.39 |
| connector15 | Header 16 (row B) | D7 | Digital | 44.72, 21.39 |
| connector16 | Header 17 (row B) | D8/MOSI | Digital | 42.18, 21.39 |
| connector17 | Header 18 (row B) | D9/SCK | Digital | 39.64, 21.39 |
| connector18 | Header 19 (row B) | D10/MISO | Digital | 37.10, 21.39 |
| connector19 | Header 20 (row B) | D11/SDA | Digital | 34.56, 21.39 |
| connector20 | Header 21 (row B) | D12/SCL | Digital | 32.02, 21.39 |
| connector21 | Header 22 (row B) | D13/RX | Digital | 29.48, 21.39 |
| connector22 | Header 23 (row B) | D14/TX | Digital | 26.94, 21.39 |
| connector23 | Header 24 (row B) | RESETN | Digital | 24.40, 21.39 |
| connector24 | Header 25 (row B) | GND | Power | 21.86, 21.39 |
| connector25 | Header 26 (row B) | +3V3 | Power | 19.32, 21.39 |
| connector26 | Header 27 (row B) | VIN | Power | 16.78, 21.39 |
| connector27 | Header 28 (row B) | +5V | Power | 14.24, 21.39 |

`moduleId` is `com.greenshoegarage.arduino.mkr-wifi-1010-tht-v1`.


## Arduino GIGA R1 WiFi (ABX00063)

`arduino_giga_r1_wifi/arduino_giga_r1_wifi.fzpz` &middot; v1.0.0 &middot; 86 connectors &middot; 101.68 by 53.34 mm &middot; header logic 3.3V &middot; 40 checks pass, 0 fail

1. 3.3 V logic in a Mega shaped board. A 5 V shield can damage it.
2. 8 mA maximum per I/O pin.
3. VIN range is 6 V to 24 V.

**Built from:** ABX00063 product reference manual, page footer Modified 09/06/2026, change log latest entry 16/01/2026 (ISED antenna specifications)

**Headers exposed**

| Header | Positions | Source |
|---|---|---|
| JANALOG | 24 | datasheet section 14.2 |
| JDIGITAL | 26 | datasheet section 14.3 |
| JSIDE LHS | 18 | datasheet section 14.5 |
| JSIDE RHS | 18 | datasheet section 14.6 |

**Footprint as drawn**

| Property | Value | Confidence |
|---|---|---|
| Pad pitch inside every header block | 2.54 mm | measured out of the generated footprint |
| Header block positions | Mega 2560 grid | measured out of the Fritzing core Arduino_MEGA_2560-Rev3 part |
| Board outline | 101.68 by 53.34 mm | Fritzing core Mega part canvas. Arduino publishes 101.52 mm for the outline, so treat the last 0.16 mm as unconfirmed |

Pads are 1.0 mm drill on a 1.8 mm pad throughout the set.

**Not exposed in v1.0.0**

- J1, the three pin OFF / GND / VRTC header (datasheet section 14.1)
- the STM32 ICSP 2x3 header (datasheet section 14.4)
- the JTAG header, the 20 pin Arducam camera connector, the display connector, the 3.5 mm audio jack (J15) and the micro UFL antenna connector

**Datasheet errata noticed while building this**

- Section 14.3 lists header pin 18 as D0/TX0 while its own description says Serial 0 Receiver. It is the receive pin. This part names it D0/RX0.

**Connector map**

| Fritzing | Header pin | Name | Type | Position x, y (mm) |
|---|---|---|---|---|
| connector0 | JANALOG 1 | NC | Other | 27.94, 50.80 |
| connector1 | JANALOG 2 | IOREF | Power | 30.48, 50.80 |
| connector2 | JANALOG 3 | RESET | Digital | 33.02, 50.80 |
| connector3 | JANALOG 4 | +3V3 | Power | 35.56, 50.80 |
| connector4 | JANALOG 5 | +5V | Power | 38.10, 50.80 |
| connector5 | JANALOG 6 | GND | Power | 40.64, 50.80 |
| connector6 | JANALOG 7 | GND | Power | 43.18, 50.80 |
| connector7 | JANALOG 8 | VIN | Power | 45.72, 50.80 |
| connector8 | JANALOG 9 | A0 | Analog | 50.80, 50.80 |
| connector9 | JANALOG 10 | A1 | Analog | 53.34, 50.80 |
| connector10 | JANALOG 11 | A2 | Analog | 55.88, 50.80 |
| connector11 | JANALOG 12 | A3 | Analog | 58.42, 50.80 |
| connector12 | JANALOG 13 | A4 | Analog | 60.96, 50.80 |
| connector13 | JANALOG 14 | A5 | Analog | 63.50, 50.80 |
| connector14 | JANALOG 15 | A6 | Analog | 66.04, 50.80 |
| connector15 | JANALOG 16 | A7 | Analog | 68.58, 50.80 |
| connector16 | JANALOG 17 | A8 | Analog | 73.66, 50.80 |
| connector17 | JANALOG 18 | A9 | Analog | 76.20, 50.80 |
| connector18 | JANALOG 19 | A10 | Analog | 78.74, 50.80 |
| connector19 | JANALOG 20 | A11 | Analog | 81.28, 50.80 |
| connector20 | JANALOG 21 | DAC0 | Analog | 83.82, 50.80 |
| connector21 | JANALOG 22 | DAC1 | Analog | 86.36, 50.80 |
| connector22 | JANALOG 23 | CANRX | Digital | 88.90, 50.80 |
| connector23 | JANALOG 24 | CANTX | Digital | 91.44, 50.80 |
| connector24 | JDIGITAL 1 | D21/SCL1 | Digital | 18.80, 2.54 |
| connector25 | JDIGITAL 2 | D20/SDA1 | Digital | 21.34, 2.54 |
| connector26 | JDIGITAL 3 | AREF | Digital | 23.88, 2.54 |
| connector27 | JDIGITAL 4 | GND | Power | 26.42, 2.54 |
| connector28 | JDIGITAL 5 | D13/SCK | Digital | 28.96, 2.54 |
| connector29 | JDIGITAL 6 | D12/CIPO | Digital | 31.50, 2.54 |
| connector30 | JDIGITAL 7 | D11/COPI | Digital | 34.04, 2.54 |
| connector31 | JDIGITAL 8 | D10/CS | Digital | 36.58, 2.54 |
| connector32 | JDIGITAL 9 | D9/SDA2 | Digital | 39.12, 2.54 |
| connector33 | JDIGITAL 10 | D8/SCL2 | Digital | 41.66, 2.54 |
| connector34 | JDIGITAL 11 | D7 | Digital | 45.72, 2.54 |
| connector35 | JDIGITAL 12 | D6 | Digital | 48.26, 2.54 |
| connector36 | JDIGITAL 13 | D5 | Digital | 50.80, 2.54 |
| connector37 | JDIGITAL 14 | D4 | Digital | 53.34, 2.54 |
| connector38 | JDIGITAL 15 | D3 | Digital | 55.88, 2.54 |
| connector39 | JDIGITAL 16 | D2 | Digital | 58.42, 2.54 |
| connector40 | JDIGITAL 17 | D1/TX0 | Digital | 60.96, 2.54 |
| connector41 | JDIGITAL 18 | D0/RX0 | Digital | 63.50, 2.54 |
| connector42 | JDIGITAL 19 | D14/TX3 | Digital | 68.58, 2.54 |
| connector43 | JDIGITAL 20 | D15/RX3 | Digital | 71.12, 2.54 |
| connector44 | JDIGITAL 21 | D16/TX2 | Digital | 73.66, 2.54 |
| connector45 | JDIGITAL 22 | D17/RX2 | Digital | 76.20, 2.54 |
| connector46 | JDIGITAL 23 | D18/TX1 | Digital | 78.74, 2.54 |
| connector47 | JDIGITAL 24 | D19/RX1 | Digital | 81.28, 2.54 |
| connector48 | JDIGITAL 25 | D20/SDA | Digital | 83.82, 2.54 |
| connector49 | JDIGITAL 26 | D21/SCL | Digital | 86.36, 2.54 |
| connector50 | JSIDE LHS 1 | +5V | Power | 93.98, 2.54 |
| connector51 | JSIDE LHS 2 | D22 | Digital | 93.98, 5.08 |
| connector52 | JSIDE LHS 3 | D24 | Digital | 93.98, 7.62 |
| connector53 | JSIDE LHS 4 | D26 | Digital | 93.98, 10.16 |
| connector54 | JSIDE LHS 5 | D28 | Digital | 93.98, 12.70 |
| connector55 | JSIDE LHS 6 | D30 | Digital | 93.98, 15.24 |
| connector56 | JSIDE LHS 7 | D32 | Digital | 93.98, 17.78 |
| connector57 | JSIDE LHS 8 | D34 | Digital | 93.98, 20.32 |
| connector58 | JSIDE LHS 9 | D36 | Digital | 93.98, 22.86 |
| connector59 | JSIDE LHS 10 | D38 | Digital | 93.98, 25.40 |
| connector60 | JSIDE LHS 11 | D40 | Digital | 93.98, 27.94 |
| connector61 | JSIDE LHS 12 | D42 | Digital | 93.98, 30.48 |
| connector62 | JSIDE LHS 13 | D44 | Digital | 93.98, 33.02 |
| connector63 | JSIDE LHS 14 | D46 | Digital | 93.98, 35.56 |
| connector64 | JSIDE LHS 15 | D48 | Digital | 93.98, 38.10 |
| connector65 | JSIDE LHS 16 | D50 | Digital | 93.98, 40.64 |
| connector66 | JSIDE LHS 17 | D52 | Digital | 93.98, 43.18 |
| connector67 | JSIDE LHS 18 | GND | Power | 93.98, 45.72 |
| connector68 | JSIDE RHS 1 | +5V | Power | 96.52, 2.54 |
| connector69 | JSIDE RHS 2 | D23 | Digital | 96.52, 5.08 |
| connector70 | JSIDE RHS 3 | D25 | Digital | 96.52, 7.62 |
| connector71 | JSIDE RHS 4 | D27 | Digital | 96.52, 10.16 |
| connector72 | JSIDE RHS 5 | D29 | Digital | 96.52, 12.70 |
| connector73 | JSIDE RHS 6 | D31 | Digital | 96.52, 15.24 |
| connector74 | JSIDE RHS 7 | D33 | Digital | 96.52, 17.78 |
| connector75 | JSIDE RHS 8 | D35 | Digital | 96.52, 20.32 |
| connector76 | JSIDE RHS 9 | D37 | Digital | 96.52, 22.86 |
| connector77 | JSIDE RHS 10 | D39 | Digital | 96.52, 25.40 |
| connector78 | JSIDE RHS 11 | D41 | Digital | 96.52, 27.94 |
| connector79 | JSIDE RHS 12 | D43 | Digital | 96.52, 30.48 |
| connector80 | JSIDE RHS 13 | D45 | Digital | 96.52, 33.02 |
| connector81 | JSIDE RHS 14 | D47 | Digital | 96.52, 35.56 |
| connector82 | JSIDE RHS 15 | D49 | Digital | 96.52, 38.10 |
| connector83 | JSIDE RHS 16 | D51 | Digital | 96.52, 40.64 |
| connector84 | JSIDE RHS 17 | D53 | Digital | 96.52, 43.18 |
| connector85 | JSIDE RHS 18 | GND | Power | 96.52, 45.72 |

`moduleId` is `com.greenshoegarage.arduino.giga-r1-wifi-tht-v1`.


## Arduino UNO R4 WiFi (ABX00087)

`arduino_uno_r4_wifi/arduino_uno_r4_wifi.fzpz` &middot; v1.0.0 &middot; 32 connectors &middot; 68.58 by 53.34 mm &middot; header logic 5V &middot; 40 checks pass, 0 fail

1. 5 V logic on the headers, unlike most recent Arduino boards.
2. The ESP32-S3 module is 3.3 V. Keep its pins away from the 5 V domain.
3. 8 mA maximum per GPIO.

**Built from:** ABX00087 product reference manual, page footer Modified 28/05/2026, change log revision 8 (29/10/2025, mechanical drawing update)

**Headers exposed**

| Header | Positions | Source |
|---|---|---|
| JANALOG | 14 | datasheet section 12.1 |
| JDIGITAL | 18 | datasheet section 12.2 |

**Footprint as drawn**

| Property | Value | Confidence |
|---|---|---|
| Pad pitch inside every header block | 2.54 mm | measured out of the generated footprint |
| Header block positions | UNO R3 grid | measured out of the Fritzing core arduino_uno(rev3)-icsp part, including the 4.06 mm digital row gap and the 5.08 mm gap between blocks |
| Board outline | 68.58 by 53.34 mm | stated in plain text in the UNO Q datasheet mechanical section and matching the measured core UNO footprint |

Pads are 1.0 mm drill on a 1.8 mm pad throughout the set.

**Not exposed in v1.0.0**

- JOFF, the OFF / GND / VRTC header (datasheet section 12.3)
- the ICSP 2x3 header (datasheet section 12.4)
- the Qwiic I2C connector (SM04B-SRSS-TB) and the six pin ESP header

**Datasheet errata noticed while building this**

- Section 12.2 lists header pin 18 as D0/TX0 while its own description says Serial 0 Receiver. It is the receive pin. This part names it D0/RX0.
- Section 12.1 pin 1 is BOOT in the English table and not connected in the Chinese table of the same document. This part names it BOOT and types it Other.
- Section 12.3 numbers its three rows 1, 2, 1. Read as a three position header carrying OFF, GND and VRTC.

**Connector map**

| Fritzing | Header pin | Name | Type | Position x, y (mm) |
|---|---|---|---|---|
| connector0 | JANALOG 1 | BOOT | Other | 27.94, 50.80 |
| connector1 | JANALOG 2 | IOREF | Power | 30.48, 50.80 |
| connector2 | JANALOG 3 | RESET | Digital | 33.02, 50.80 |
| connector3 | JANALOG 4 | +3V3 | Power | 35.56, 50.80 |
| connector4 | JANALOG 5 | +5V | Power | 38.10, 50.80 |
| connector5 | JANALOG 6 | GND | Power | 40.64, 50.80 |
| connector6 | JANALOG 7 | GND | Power | 43.18, 50.80 |
| connector7 | JANALOG 8 | VIN | Power | 45.72, 50.80 |
| connector8 | JANALOG 9 | A0 | Analog | 50.80, 50.80 |
| connector9 | JANALOG 10 | A1 | Analog | 53.34, 50.80 |
| connector10 | JANALOG 11 | A2 | Analog | 55.88, 50.80 |
| connector11 | JANALOG 12 | A3 | Analog | 58.42, 50.80 |
| connector12 | JANALOG 13 | A4/SDA | Analog | 60.96, 50.80 |
| connector13 | JANALOG 14 | A5/SCL | Analog | 63.50, 50.80 |
| connector14 | JDIGITAL 1 | SCL | Digital | 18.80, 2.54 |
| connector15 | JDIGITAL 2 | SDA | Digital | 21.34, 2.54 |
| connector16 | JDIGITAL 3 | AREF | Digital | 23.88, 2.54 |
| connector17 | JDIGITAL 4 | GND | Power | 26.42, 2.54 |
| connector18 | JDIGITAL 5 | D13/SCK | Digital | 28.96, 2.54 |
| connector19 | JDIGITAL 6 | D12/CIPO | Digital | 31.50, 2.54 |
| connector20 | JDIGITAL 7 | D11/COPI | Digital | 34.04, 2.54 |
| connector21 | JDIGITAL 8 | D10/CS | Digital | 36.58, 2.54 |
| connector22 | JDIGITAL 9 | D9 | Digital | 39.12, 2.54 |
| connector23 | JDIGITAL 10 | D8 | Digital | 41.66, 2.54 |
| connector24 | JDIGITAL 11 | D7 | Digital | 45.72, 2.54 |
| connector25 | JDIGITAL 12 | D6 | Digital | 48.26, 2.54 |
| connector26 | JDIGITAL 13 | D5 | Digital | 50.80, 2.54 |
| connector27 | JDIGITAL 14 | D4 | Digital | 53.34, 2.54 |
| connector28 | JDIGITAL 15 | D3 | Digital | 55.88, 2.54 |
| connector29 | JDIGITAL 16 | D2 | Digital | 58.42, 2.54 |
| connector30 | JDIGITAL 17 | D1/TX0 | Digital | 60.96, 2.54 |
| connector31 | JDIGITAL 18 | D0/RX0 | Digital | 63.50, 2.54 |

`moduleId` is `com.greenshoegarage.arduino.uno-r4-wifi-tht-v1`.


## Arduino UNO Q (ABX00162 / ABX00173)

`arduino_uno_q/arduino_uno_q.fzpz` &middot; v1.0.0 &middot; 32 connectors &middot; 68.58 by 53.34 mm &middot; header logic 3.3V &middot; 40 checks pass, 0 fail

1. The headers are 3.3 V even though the board takes UNO shields.
2. D3 (PB0) is 3.6 V tolerant only, in every mode including digital.
3. A0 through A5 are not 5 V tolerant. Absolute maximum is about 3.6 V.
4. IOREF mirrors the 3.3 V rail and is an output. Do not feed power back into it.

**Built from:** ABX00162-ABX00173 product reference manual, page footer Modified 28/05/2026

**Headers exposed**

| Header | Positions | Source |
|---|---|---|
| JANALOG (A3) | 14 | datasheet section 9.7 |
| JDIGITAL (A2) | 18 | datasheet section 9.6 |

**Footprint as drawn**

| Property | Value | Confidence |
|---|---|---|
| Pad pitch inside every header block | 2.54 mm | measured out of the generated footprint |
| Header block positions | UNO R3 grid | measured out of the Fritzing core arduino_uno(rev3)-icsp part, including the 4.06 mm digital row gap and the 5.08 mm gap between blocks |
| Board outline | 68.58 by 53.34 mm | stated in plain text in the UNO Q datasheet mechanical section and matching the measured core UNO footprint |

Pads are 1.0 mm drill on a 1.8 mm pad throughout the set.

**Not exposed in v1.0.0**

- JMEDIA (60 pin, MIPI CSI and DSI) and JMISC (60 pin, mixed 1.8 V and 3.3 V) board to board connectors
- JSPI (6 pin), JCTL (10 pin) and the Qwiic I2C connector
- the power button (JBTN1) and the USB-C connector as electrical connectors

**Datasheet errata noticed while building this**

- Section 9.6 lists JDIGITAL from D0 to D21. On the physical UNO shield row that order runs right to left, so this part places D0 at the right hand end next to the USB, matching every other UNO form factor board.

**Connector map**

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

`moduleId` is `com.greenshoegarage.arduino.uno-q-tht-v1`.


## Arduino GIGA Display Shield (ASX00039)

`arduino_giga_display_shield/arduino_giga_display_shield.fzpz` &middot; v0.9.0 &middot; 44 connectors &middot; 48.0 by 46.0 mm &middot; header logic 3.3V &middot; 40 checks pass, 0 fail

1. This part is v0.9.0. It does not meet the standard of the other four parts in this set, for the reasons in the description and below.
2. The shield needs a GIGA R1 WiFi. It has no microcontroller of its own.
3. Eight of the 44 pins are supply or ground pins whose net could not be resolved from the published schematic. They are named by designator, not guessed. Meter them before connecting anything.
4. Connector positions and the board outline in PCB view are nominal. Do not order a board against this footprint.
5. Logic is 3.3 V. The VIN header input range is 6 V to 32 V.

**Built from:** ASX00039 product reference manual, page footer Modified 17/07/2026, plus ASX00039-schematics.pdf revision V0.5 dated 17/10/2024, which is where every pin identity below comes from

**Headers exposed**

| Header | Positions | Source |
|---|---|---|
| J6 | 24 | schematic sheet 2, GIGA HEADERS |
| J7 | 20 | schematic sheet 2, GIGA HEADERS |

**Footprint as drawn**

| Property | Value | Confidence |
|---|---|---|
| Pad grid inside J6 and J7 | 2.54 mm | read from the schematic symbols, 2x12 on J6 and 2x10 on J7 |
| Position of J6 relative to J7 | nominal | **not dimensioned.** No published document gives it |
| Board outline | nominal 48 by 46 mm canvas | **not dimensioned.** The datasheet mechanical section is a raster figure and states no dimensions in text |

Pads are 1.0 mm drill on a 1.8 mm pad throughout the set.

**Not exposed in v0.9.0**

- J3, the 20 pin 2.54 mm Arducam camera header (pin map is in the schematic, but its board position is not)
- J4 display video and J5 touch flex connectors, which are internal to the shield and not user wiring points
- the two alignment posts on J6 and J7

**Datasheet errata noticed while building this**

- The ASX00039 datasheet has no pinout section. Sections 6.1 and 6.2 name the connectors by reference designator only. Every pin identity in this part therefore comes from the schematic PDF rather than from the datasheet.
- The schematic shows STM32 port PA1 on J7 pins 17 and 19, and port PD4 on J7 pins 18 and 20. Both are reproduced as drawn rather than corrected.
- The camera bus lines on J7 are identified by STM32 port name. The schematic lists the camera signal names (DOUT0 to DOUT7, VSYNC, HREF, PCLK, XCLK) as a group without a per pin pairing that survives text extraction, so no per pin camera signal name is claimed here.

**Connector map**

| Fritzing | Header pin | Name | Type | Position x, y (mm) |
|---|---|---|---|---|
| connector0 | J6 1 | DSI_D1_N | Digital | 14.00, 9.00 |
| connector1 | J6 2 | DSI_D1_P | Digital | 16.54, 9.00 |
| connector2 | J6 3 | J6-3 | Power | 14.00, 11.54 |
| connector3 | J6 4 | J6-4 | Power | 16.54, 11.54 |
| connector4 | J6 5 | DSI_CK_N | Digital | 14.00, 14.08 |
| connector5 | J6 6 | DSI_CK_P | Digital | 16.54, 14.08 |
| connector6 | J6 7 | J6-7 | Power | 14.00, 16.62 |
| connector7 | J6 8 | J6-8 | Power | 16.54, 16.62 |
| connector8 | J6 9 | DSI_D0_N | Digital | 14.00, 19.16 |
| connector9 | J6 10 | DSI_D0_P | Digital | 16.54, 19.16 |
| connector10 | J6 11 | J6-11 | Power | 14.00, 21.70 |
| connector11 | J6 12 | J6-12 | Power | 16.54, 21.70 |
| connector12 | J6 13 | PC6 | Digital | 14.00, 24.24 |
| connector13 | J6 14 | PI0 | Digital | 16.54, 24.24 |
| connector14 | J6 15 | PI1 | Digital | 14.00, 26.78 |
| connector15 | J6 16 | PI2 | Digital | 16.54, 26.78 |
| connector16 | J6 17 | PI3 | Digital | 14.00, 29.32 |
| connector17 | J6 18 | PC1 | Digital | 16.54, 29.32 |
| connector18 | J6 19 | PB12 | Digital | 14.00, 31.86 |
| connector19 | J6 20 | PD3 | Digital | 16.54, 31.86 |
| connector20 | J6 21 | J6-21 | Power | 14.00, 34.40 |
| connector21 | J6 22 | J6-22 | Power | 16.54, 34.40 |
| connector22 | J6 23 | J6-23 | Power | 14.00, 36.94 |
| connector23 | J6 24 | J6-24 | Power | 16.54, 36.94 |
| connector24 | J7 1 | J7-1 | Power | 30.00, 9.00 |
| connector25 | J7 2 | J7-2 | Power | 32.54, 9.00 |
| connector26 | J7 3 | PB6 | Digital | 30.00, 11.54 |
| connector27 | J7 4 | PH12 | Digital | 32.54, 11.54 |
| connector28 | J7 5 | PI5 | Digital | 30.00, 14.08 |
| connector29 | J7 6 | PH8 | Digital | 32.54, 14.08 |
| connector30 | J7 7 | PA6 | Digital | 30.00, 16.62 |
| connector31 | J7 8 | PJ9 | Digital | 32.54, 16.62 |
| connector32 | J7 9 | PI7 | Digital | 30.00, 19.16 |
| connector33 | J7 10 | PI6 | Digital | 32.54, 19.16 |
| connector34 | J7 11 | PI4 | Digital | 30.00, 21.70 |
| connector35 | J7 12 | PH14 | Digital | 32.54, 21.70 |
| connector36 | J7 13 | PG11 | Digital | 30.00, 24.24 |
| connector37 | J7 14 | PH11 | Digital | 32.54, 24.24 |
| connector38 | J7 15 | PH10 | Digital | 30.00, 26.78 |
| connector39 | J7 16 | PH9 | Digital | 32.54, 26.78 |
| connector40 | J7 17 | PA1 | Digital | 30.00, 29.32 |
| connector41 | J7 18 | PD4 | Digital | 32.54, 29.32 |
| connector42 | J7 19 | PA1 | Digital | 30.00, 31.86 |
| connector43 | J7 20 | PD4 | Digital | 32.54, 31.86 |

`moduleId` is `com.greenshoegarage.arduino.giga-display-shield-tht-v0`.


## Licence

Part assets (the `.fzp` files and the view SVGs) are licensed CC BY-SA 3.0, which
is the Fritzing parts convention.

The build and verification tooling under `tools/` is licensed GPL-3.0.

Arduino and the Arduino board designs are the property of Arduino S.r.l. These
are independent reimplementations drawn from Arduino's published documentation
and are not official Arduino releases.

