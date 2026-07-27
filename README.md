# Arduino MKR WiFi 1010 (ABX00023) Fritzing part

Version 1.0.0

An installable Fritzing part for the Arduino MKR WiFi 1010, with all four views
present: breadboard, schematic, PCB and icon. The schematic is a real wireable
symbol on the 0.1 inch grid, and the PCB view is a two row through hole
footprint on 2.54 mm pitch.

The part exposes the 28 header pins as `connector0` through `connector27`, where
`connector0` is header pin 1 (AREF) and `connector27` is header pin 28 (+5V).

## Two facts this part is built to keep you out of trouble on

1. The I/O is 3.3 V and is **not 5 V tolerant**. Connecting a 5 V signal
   directly to any pin will damage the board.
2. The `+5V` pin (header pin 28) is **not a regulated output**. It is jumper
   connected to the USB power input, so it only carries voltage when the board
   is powered over USB.

Both statements are carried in the `.fzp` description and in the per connector
descriptions, so they show up in Fritzing's inspector rather than only here.

## Built from

| Item | Revision used |
|---|---|
| Board | Arduino MKR WiFi 1010, SKU ABX00023 |
| Datasheet / user manual | `ABX00023-datasheet.pdf`, revision 5 (25/04/2024), page footer "Modified: 03/07/2026" |
| Pinout diagram | `Pinout-MKRwifi1010_latest.pdf`, last update 7/08/2020 |
| Schematic PDF | MKRWiFi1010 V2.0 (referenced, not fetched, see NOTES.md) |
| EAGLE reference design | **not fetched**, see Known Limitations |

## Install

Fritzing 1.0.x or newer.

1. Open Fritzing.
2. File, then Open, then select `mkr-wifi-1010.fzpz`. Fritzing imports the part
   and drops it into the MINE bin.
3. Alternatively, in the Parts palette use the bin menu (the small icon at the
   top right of the bin), then Import, and select the same file.

The part's `moduleId` is `com.greenshoegarage.arduino.mkr-wifi-1010-tht-v1`, so
it will sit alongside Arduino's own published part without colliding with it.

The unzipped source tree under `src/` is the same five files the archive
contains, kept flat so the part stays diffable in git. Rebuild the archive with
`python3 tools/build.py`.

## Connector map

Row A runs left to right starting at the USB end. Row B is numbered from the
far end back toward the USB end, so header pin 28 sits physically opposite
header pin 1.

| Fritzing | Header pin | Row | Name | Type | SAMD21 port | Also known as |
|---|---|---|---|---|---|---|
| connector0 | 1 | A | AREF | Analog | PA03 | |
| connector1 | 2 | A | A0/DAC0 | Analog | PA02 | D15 |
| connector2 | 3 | A | A1 | Analog | PB02 | D16 |
| connector3 | 4 | A | A2 | Analog | PB03 | D17 |
| connector4 | 5 | A | A3 | Analog | PA04 | D18 |
| connector5 | 6 | A | A4/SDA | Analog | PA05 | D19 |
| connector6 | 7 | A | A5/SCL | Analog | PA06 | D20 |
| connector7 | 8 | A | A6 | Analog | PA07 | D21 |
| connector8 | 9 | A | D0 | Digital | PA22 | |
| connector9 | 10 | A | D1 | Digital | PA23 | |
| connector10 | 11 | A | D2 | Digital | PA10 | |
| connector11 | 12 | A | D3 | Digital | PA11 | |
| connector12 | 13 | A | D4 | Digital | PB10 | |
| connector13 | 14 | A | D5 | Digital | PB11 | |
| connector14 | 15 | B | D6 | Digital | PA20 | LED_BUILTIN |
| connector15 | 16 | B | D7 | Digital | PA21 | |
| connector16 | 17 | B | D8/MOSI | Digital | PA16 | COPI |
| connector17 | 18 | B | D9/SCK | Digital | PA17 | |
| connector18 | 19 | B | D10/MISO | Digital | PA19 | CIPO |
| connector19 | 20 | B | D11/SDA | Digital | PA08 | primary I2C SDA |
| connector20 | 21 | B | D12/SCL | Digital | PA09 | primary I2C SCL |
| connector21 | 22 | B | D13/RX | Digital | PB23 | Serial1 RX |
| connector22 | 23 | B | D14/TX | Digital | PB22 | Serial1 TX |
| connector23 | 24 | B | RESETN | Digital | | active low |
| connector24 | 25 | B | GND | Power | | |
| connector25 | 26 | B | +3V3 | Power out | | regulator output |
| connector26 | 27 | B | VIN | Power in | | 5 V to 6 V max |
| connector27 | 28 | B | +5V | Power | | jumper tied to USB power |

## Footprint as drawn

| Property | Value | Confidence |
|---|---|---|
| Pad pitch along each row | 2.54 mm | verified against the datasheet and the header part number |
| Row to row spacing | 17.78 mm (700 mil) | **derived, not read from the .brd** |
| Drill | 1.0 mm | starting value from the build brief |
| Pad outer diameter | 1.8 mm | starting value from the build brief |
| Board outline | 61.5 mm by 25.0 mm | published figure, not confirmed against the .brd |
| Pin 1 offset from the USB end | 14.24 mm | **assumed, header span centred on the board** |
| Mounting holes | not included | positions unknown, see below |

Pin 1 is identified three ways in PCB view: a chamfered corner on the
silkscreen outline at that end of the board, a filled silkscreen dot outboard
of the pad, and the fact that `connector0` is AREF everywhere in the part.

## Known Limitations

Read this section before you order a board against this footprint.

1. **The EAGLE `.brd` was never opened.** The build environment could not reach
   `content.arduino.cc`, so the file that is the authority for row spacing,
   mounting hole positions, connector positions and the true board outline was
   unavailable. Every mechanical number in this part therefore comes from the
   datasheet text, the published product figures, or derivation. None of it has
   been read off the reference design.
2. **Row spacing of 17.78 mm is derived, not verified.** The datasheet states
   the rows are held to a 100 mil grid so the board seats in a breadboard, and
   700 mil is the only multiple of 2.54 mm that leaves a workable margin on a
   25 mm wide board. It is very likely right. It is not confirmed. If it turns
   out to be wrong, change `row_spacing_mm` in `tools/build.py` and rebuild.
3. **The longitudinal position of pin 1 is an assumption.** The 14 position row
   spans 33.02 mm, and this part centres that span on the 61.5 mm outline. The
   pad grid itself is unaffected by this choice, but the silkscreen outline may
   sit a few millimetres off relative to the pads, which matters if you are
   checking whether the USB connector clears the edge of a carrier board.
4. **No mounting holes.** Their positions could not be read from the `.brd`, and
   drawing them at a plausible guess would be worse than leaving them out.
5. **Debug header, ESLOV connector and Li-Po JST connector are not exposed.**
   The build brief's default recommendation was to expose all three. They are
   deliberately deferred to a later version for the same reason as the mounting
   holes: their board positions come from the `.brd`, and placing them by eye
   would produce a footprint that looks authoritative and is not. The reasoning
   is written up in NOTES.md along with what is needed to add them.
6. **The part has not been opened in Fritzing.** No Fritzing binary was
   available in the build environment. Fifty seven structural and dimensional
   checks were run against the files themselves, and they all pass, but the
   load with no console warnings, the hover highlighting behaviour and the
   Gerber export measurements are all unverified.
7. **Not diffed against Arduino's own published part.** Their `.fzpz` is hosted
   on the same unreachable domain.
8. **Nothing has been checked against physical hardware.** No board was seated
   on a breadboard and no part was measured with calipers.

## Licence

Part assets (the `.fzp` and the four view SVGs) are licensed CC BY-SA 3.0, which
is the Fritzing parts convention.

The build and verification tooling under `tools/` is licensed GPL-3.0.

Arduino, MKR and the Arduino board designs are the property of Arduino S.r.l.
This part is an independent reimplementation drawn from Arduino's published
documentation and is not an official Arduino release.
