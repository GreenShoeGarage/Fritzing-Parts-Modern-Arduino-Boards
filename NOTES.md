# NOTES: Arduino GIGA R1 WiFi Fritzing part, v1.0.0

Engineering record. Written for whoever has to decide whether to trust this
footprint.

## 1. Sources

| Source | Status | Supplied |
|---|---|---|
| ABX00063 product reference manual, page footer Modified 09/06/2026, change log latest entry 16/01/2026 (ISED antenna specifications) | fetched, text extracted | every header pin table, pin types, voltage and current limits, board description |
| Arduino EAGLE / design archives | **not fetched** | nothing. The build environment's egress allowlist does not include the Arduino asset host |
| Fritzing core parts repository (github.com/fritzing/fritzing-parts) | cloned | the shield header grid, and the Fritzing SVG conventions this part follows |
| KiCad footprint library (github.com/KiCad/kicad-footprints) | cloned | negative result, it holds no Arduino UNO or Mega through hole shield footprint to cross check against |

The mechanical sections of the datasheets are raster figures inside the PDF, so
their dimensions were not readable from the extracted text. The one exception is
the UNO Q datasheet, which states the board outline in plain text (68.58 mm by
53.34 mm) and lists a set of unlabelled dimensions.

## 2. Geometry provenance

### shield_grid

Shield header positions were measured out of the Fritzing core parts arduino_uno(rev3)-icsp and Arduino_MEGA_2560-Rev3 by parsing their PCB SVGs and converting user units to millimetres. This is the de facto standard shield footprint that the whole shield ecosystem is built against, and it reproduces the two irregular gaps (4.06 mm in the digital row, 5.08 mm between header blocks) that make the UNO layout what it is. It is not a reading of the Arduino EAGLE .brd file.

### outline

Board outline dimensions. UNO family: 68.58 mm by 53.34 mm, stated in plain text in section 12 of the UNO Q datasheet and matching the measured Fritzing core UNO footprint. Mega family: 101.68 mm by 53.34 mm, taken from the Fritzing core Mega 2560 part canvas. Arduino publishes 101.52 mm for the Mega outline, so treat the last 0.16 mm as unconfirmed.

### pads

1.0 mm drill on a 1.8 mm pad, carried over from the MKR WiFi 1010 part in this set for consistency. Not reconciled against Arduino's own published footprints, which were unreachable from the build environment.

### holes

Mounting holes are NOT drawn. The UNO Q datasheet mechanical figure lists dimensions (15.24, 13.97, 7.62, 2.54, 2x 3.01, 4x R1.6 and others) but they are unlabelled in the extracted text, so they cannot be assigned to specific features without the drawing itself.


## 3. Pin map as built

| Datasheet position | Fritzing | Name | Type |
|---|---|---|---|
| JANALOG 1 | connector0 | NC | Other |
| JANALOG 2 | connector1 | IOREF | Power |
| JANALOG 3 | connector2 | RESET | Digital |
| JANALOG 4 | connector3 | +3V3 | Power |
| JANALOG 5 | connector4 | +5V | Power |
| JANALOG 6 | connector5 | GND | Power |
| JANALOG 7 | connector6 | GND | Power |
| JANALOG 8 | connector7 | VIN | Power |
| JANALOG 9 | connector8 | A0 | Analog |
| JANALOG 10 | connector9 | A1 | Analog |
| JANALOG 11 | connector10 | A2 | Analog |
| JANALOG 12 | connector11 | A3 | Analog |
| JANALOG 13 | connector12 | A4 | Analog |
| JANALOG 14 | connector13 | A5 | Analog |
| JANALOG 15 | connector14 | A6 | Analog |
| JANALOG 16 | connector15 | A7 | Analog |
| JANALOG 17 | connector16 | A8 | Analog |
| JANALOG 18 | connector17 | A9 | Analog |
| JANALOG 19 | connector18 | A10 | Analog |
| JANALOG 20 | connector19 | A11 | Analog |
| JANALOG 21 | connector20 | DAC0 | Analog |
| JANALOG 22 | connector21 | DAC1 | Analog |
| JANALOG 23 | connector22 | CANRX | Digital |
| JANALOG 24 | connector23 | CANTX | Digital |
| JDIGITAL 1 | connector24 | D21/SCL1 | Digital |
| JDIGITAL 2 | connector25 | D20/SDA1 | Digital |
| JDIGITAL 3 | connector26 | AREF | Digital |
| JDIGITAL 4 | connector27 | GND | Power |
| JDIGITAL 5 | connector28 | D13/SCK | Digital |
| JDIGITAL 6 | connector29 | D12/CIPO | Digital |
| JDIGITAL 7 | connector30 | D11/COPI | Digital |
| JDIGITAL 8 | connector31 | D10/CS | Digital |
| JDIGITAL 9 | connector32 | D9/SDA2 | Digital |
| JDIGITAL 10 | connector33 | D8/SCL2 | Digital |
| JDIGITAL 11 | connector34 | D7 | Digital |
| JDIGITAL 12 | connector35 | D6 | Digital |
| JDIGITAL 13 | connector36 | D5 | Digital |
| JDIGITAL 14 | connector37 | D4 | Digital |
| JDIGITAL 15 | connector38 | D3 | Digital |
| JDIGITAL 16 | connector39 | D2 | Digital |
| JDIGITAL 17 | connector40 | D1/TX0 | Digital |
| JDIGITAL 18 | connector41 | D0/RX0 | Digital |
| JDIGITAL 19 | connector42 | D14/TX3 | Digital |
| JDIGITAL 20 | connector43 | D15/RX3 | Digital |
| JDIGITAL 21 | connector44 | D16/TX2 | Digital |
| JDIGITAL 22 | connector45 | D17/RX2 | Digital |
| JDIGITAL 23 | connector46 | D18/TX1 | Digital |
| JDIGITAL 24 | connector47 | D19/RX1 | Digital |
| JDIGITAL 25 | connector48 | D20/SDA | Digital |
| JDIGITAL 26 | connector49 | D21/SCL | Digital |
| JSIDE LHS 1 | connector50 | +5V | Power |
| JSIDE LHS 2 | connector51 | D22 | Digital |
| JSIDE LHS 3 | connector52 | D24 | Digital |
| JSIDE LHS 4 | connector53 | D26 | Digital |
| JSIDE LHS 5 | connector54 | D28 | Digital |
| JSIDE LHS 6 | connector55 | D30 | Digital |
| JSIDE LHS 7 | connector56 | D32 | Digital |
| JSIDE LHS 8 | connector57 | D34 | Digital |
| JSIDE LHS 9 | connector58 | D36 | Digital |
| JSIDE LHS 10 | connector59 | D38 | Digital |
| JSIDE LHS 11 | connector60 | D40 | Digital |
| JSIDE LHS 12 | connector61 | D42 | Digital |
| JSIDE LHS 13 | connector62 | D44 | Digital |
| JSIDE LHS 14 | connector63 | D46 | Digital |
| JSIDE LHS 15 | connector64 | D48 | Digital |
| JSIDE LHS 16 | connector65 | D50 | Digital |
| JSIDE LHS 17 | connector66 | D52 | Digital |
| JSIDE LHS 18 | connector67 | GND | Power |
| JSIDE RHS 1 | connector68 | +5V | Power |
| JSIDE RHS 2 | connector69 | D23 | Digital |
| JSIDE RHS 3 | connector70 | D25 | Digital |
| JSIDE RHS 4 | connector71 | D27 | Digital |
| JSIDE RHS 5 | connector72 | D29 | Digital |
| JSIDE RHS 6 | connector73 | D31 | Digital |
| JSIDE RHS 7 | connector74 | D33 | Digital |
| JSIDE RHS 8 | connector75 | D35 | Digital |
| JSIDE RHS 9 | connector76 | D37 | Digital |
| JSIDE RHS 10 | connector77 | D39 | Digital |
| JSIDE RHS 11 | connector78 | D41 | Digital |
| JSIDE RHS 12 | connector79 | D43 | Digital |
| JSIDE RHS 13 | connector80 | D45 | Digital |
| JSIDE RHS 14 | connector81 | D47 | Digital |
| JSIDE RHS 15 | connector82 | D49 | Digital |
| JSIDE RHS 16 | connector83 | D51 | Digital |
| JSIDE RHS 17 | connector84 | D53 | Digital |
| JSIDE RHS 18 | connector85 | GND | Power |

## 4. Datasheet errata

- Section 14.3 lists header pin 18 as D0/TX0 while its own description says Serial 0 Receiver. It is the receive pin. This part names it D0/RX0.

## 5. Judgment calls

**Scope.** Only the shield style header rows are exposed. Everything else is
deferred:

- J1, the three pin OFF / GND / VRTC header (datasheet section 14.1)
- the STM32 ICSP 2x3 header (datasheet section 14.4)
- the JTAG header, the 20 pin Arducam camera connector, the display connector, the 3.5 mm audio jack (J15) and the micro UFL antenna connector

The reasoning is the same as for the MKR WiFi 1010 part in this set. Every one of
those connectors needs a board position, and board positions come from the design
file. A connector at a guessed coordinate inside a footprint whose whole point is
that you could order a board against it is worse than a connector that is
visibly missing.

**Text is geometry.** Every label in every view is emitted as a stroked `<path>`
from a single stroke font written for this build, so the part carries no font
dependency and regenerates deterministically.

**Silkscreen is white.** This follows the published Fritzing graphic standard.
The current Fritzing core part inspected during this build draws silkscreen in
black instead, so if it renders wrong it is one constant in `tools/render.py`.

**Pad geometry** is 1.0 mm drill on a 1.8 mm pad, drawn as a circle with
`fill="none"` and a 0.4 mm stroke so the drill is the inner clear area, which is
what Fritzing expects. Not reconciled against Arduino's own published parts.

## 6. Verification

40 checks pass, 0 fail. Items that need Fritzing itself, a Gerber
viewer or the design file are reported as NOT RUN rather than asserted.

```
PASS breadboard: no banned elements or attributes             
PASS breadboard: stroke-width and fill declared everywhere    
PASS breadboard: real units and matching viewBox aspect       101.68mm x 53.34mm, viewBox 0 0 10168 5334
PASS schematic: no banned elements or attributes              
PASS schematic: stroke-width and fill declared everywhere     
PASS schematic: real units and matching viewBox aspect        2.4in x 5.5in, viewBox 0 0 2400 5500
PASS pcb: no banned elements or attributes                    
PASS pcb: stroke-width and fill declared everywhere           
PASS pcb: real units and matching viewBox aspect              101.68mm x 53.34mm, viewBox 0 0 10168 5334
PASS icon: no banned elements or attributes                   
PASS icon: stroke-width and fill declared everywhere          
PASS icon: real units and matching viewBox aspect             0.32in x 0.32in, viewBox 0 0 320 320
PASS breadboard: layer group ids                              ['breadboard']
PASS schematic: layer group ids                               ['schematic']
PASS pcb: layer group ids                                     ['silkscreen', 'copper1', 'copper0']
PASS icon: layer group ids                                    ['icon']
PASS pcb: copper0 nested inside copper1                       
PASS breadboard: 86 connector pins, each exactly once         found 86
PASS schematic: 86 connector pins, each exactly once          found 86
PASS pcb: 86 connector pins, each exactly once                found 86
PASS schematic: 86 terminals, contiguous                      found 86
PASS fzp: connector ids contiguous from 0                     count 86
PASS fzp: every connector typed male                          
PASS fzp: svgIds agree with connector ids                     []
PASS fzp: names match the spec                                
PASS fzp: every connector description carries its header and pin number 
PASS fzp: moduleId is reverse DNS and not Arduino's           com.greenshoegarage.arduino.giga-r1-wifi-tht-v1
PASS pcb: 2.5400 mm pitch inside every header block           8 blocks, 78 gaps checked
PASS pcb: drill 1.000 mm on a 1.800 mm pad                    drill 1.000, pad 1.800, ring 0.400
PASS pcb: silkscreen outline measures the board size          101.68 x 53.34 mm
PASS pcb: every pad inside the outline                        
PASS pcb: a silkscreen position 1 marker for every header     4 markers, 4 headers
PASS pcb: no silkscreen geometry lands on a pad               []
PASS breadboard: no label geometry sits on a pad              []
PASS breadboard: all pads inside the board outline            86 pads
PASS schematic: every pin on the 0.1 in grid                  []
PASS schematic: every pin line exactly 0.1 in long            []
PASS schematic: every terminal at the free tip of its pin     []
INFO schematic: measured grid step                            100.0 user units per 0.1 in
PASS fzpz: archive holds exactly the five expected members    5 members
PASS style: no em dashes in any generated file                []
INFO NOT RUN: Fritzing loads the part with no console warnings needs Fritzing, a Gerber viewer, or the design file
INFO NOT RUN: hover highlight follows one net across all three views needs Fritzing, a Gerber viewer, or the design file
INFO NOT RUN: Gerber export measured in a Gerber viewer       needs Fritzing, a Gerber viewer, or the design file
INFO NOT RUN: footprint diffed against Arduino's own published part needs Fritzing, a Gerber viewer, or the design file
INFO NOT RUN: mounting hole positions                         needs Fritzing, a Gerber viewer, or the design file
INFO NOT RUN: shield mates with a physical board              needs Fritzing, a Gerber viewer, or the design file

40 passed, 0 failed
```
