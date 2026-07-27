# NOTES: Arduino GIGA Display Shield Fritzing part, v0.9.0

Engineering record. Written for whoever has to decide whether to trust this
footprint.

## 1. Sources

| Source | Status | Supplied |
|---|---|---|
| ASX00039 product reference manual, page footer Modified 17/07/2026, plus ASX00039-schematics.pdf revision V0.5 dated 17/10/2024, which is where every pin identity below comes from | fetched, text extracted | every header pin table, pin types, voltage and current limits, board description |
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
| J6 1 | connector0 | DSI_D1_N | Digital |
| J6 2 | connector1 | DSI_D1_P | Digital |
| J6 3 | connector2 | J6-3 | Power |
| J6 4 | connector3 | J6-4 | Power |
| J6 5 | connector4 | DSI_CK_N | Digital |
| J6 6 | connector5 | DSI_CK_P | Digital |
| J6 7 | connector6 | J6-7 | Power |
| J6 8 | connector7 | J6-8 | Power |
| J6 9 | connector8 | DSI_D0_N | Digital |
| J6 10 | connector9 | DSI_D0_P | Digital |
| J6 11 | connector10 | J6-11 | Power |
| J6 12 | connector11 | J6-12 | Power |
| J6 13 | connector12 | PC6 | Digital |
| J6 14 | connector13 | PI0 | Digital |
| J6 15 | connector14 | PI1 | Digital |
| J6 16 | connector15 | PI2 | Digital |
| J6 17 | connector16 | PI3 | Digital |
| J6 18 | connector17 | PC1 | Digital |
| J6 19 | connector18 | PB12 | Digital |
| J6 20 | connector19 | PD3 | Digital |
| J6 21 | connector20 | J6-21 | Power |
| J6 22 | connector21 | J6-22 | Power |
| J6 23 | connector22 | J6-23 | Power |
| J6 24 | connector23 | J6-24 | Power |
| J7 1 | connector24 | J7-1 | Power |
| J7 2 | connector25 | J7-2 | Power |
| J7 3 | connector26 | PB6 | Digital |
| J7 4 | connector27 | PH12 | Digital |
| J7 5 | connector28 | PI5 | Digital |
| J7 6 | connector29 | PH8 | Digital |
| J7 7 | connector30 | PA6 | Digital |
| J7 8 | connector31 | PJ9 | Digital |
| J7 9 | connector32 | PI7 | Digital |
| J7 10 | connector33 | PI6 | Digital |
| J7 11 | connector34 | PI4 | Digital |
| J7 12 | connector35 | PH14 | Digital |
| J7 13 | connector36 | PG11 | Digital |
| J7 14 | connector37 | PH11 | Digital |
| J7 15 | connector38 | PH10 | Digital |
| J7 16 | connector39 | PH9 | Digital |
| J7 17 | connector40 | PA1 | Digital |
| J7 18 | connector41 | PD4 | Digital |
| J7 19 | connector42 | PA1 | Digital |
| J7 20 | connector43 | PD4 | Digital |

## 4. Datasheet errata

- The ASX00039 datasheet has no pinout section. Sections 6.1 and 6.2 name the connectors by reference designator only. Every pin identity in this part therefore comes from the schematic PDF rather than from the datasheet.
- The schematic shows STM32 port PA1 on J7 pins 17 and 19, and port PD4 on J7 pins 18 and 20. Both are reproduced as drawn rather than corrected.
- The camera bus lines on J7 are identified by STM32 port name. The schematic lists the camera signal names (DOUT0 to DOUT7, VSYNC, HREF, PCLK, XCLK) as a group without a per pin pairing that survives text extraction, so no per pin camera signal name is claimed here.

## 5. Judgment calls

**Scope.** Only the shield style header rows are exposed. Everything else is
deferred:

- J3, the 20 pin 2.54 mm Arducam camera header (pin map is in the schematic, but its board position is not)
- J4 display video and J5 touch flex connectors, which are internal to the shield and not user wiring points
- the two alignment posts on J6 and J7

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
PASS breadboard: real units and matching viewBox aspect       48mm x 46mm, viewBox 0 0 4800 4600
PASS schematic: no banned elements or attributes              
PASS schematic: stroke-width and fill declared everywhere     
PASS schematic: real units and matching viewBox aspect        2.4in x 3.2in, viewBox 0 0 2400 3200
PASS pcb: no banned elements or attributes                    
PASS pcb: stroke-width and fill declared everywhere           
PASS pcb: real units and matching viewBox aspect              48mm x 46mm, viewBox 0 0 4800 4600
PASS icon: no banned elements or attributes                   
PASS icon: stroke-width and fill declared everywhere          
PASS icon: real units and matching viewBox aspect             0.32in x 0.32in, viewBox 0 0 320 320
PASS breadboard: layer group ids                              ['breadboard']
PASS schematic: layer group ids                               ['schematic']
PASS pcb: layer group ids                                     ['silkscreen', 'copper1', 'copper0']
PASS icon: layer group ids                                    ['icon']
PASS pcb: copper0 nested inside copper1                       
PASS breadboard: 44 connector pins, each exactly once         found 44
PASS schematic: 44 connector pins, each exactly once          found 44
PASS pcb: 44 connector pins, each exactly once                found 44
PASS schematic: 44 terminals, contiguous                      found 44
PASS fzp: connector ids contiguous from 0                     count 44
PASS fzp: every connector typed female                        
PASS fzp: svgIds agree with connector ids                     []
PASS fzp: names match the spec                                
PASS fzp: every connector description carries its header and pin number 
PASS fzp: moduleId is reverse DNS and not Arduino's           com.greenshoegarage.arduino.giga-display-shield-tht-v0
PASS pcb: every pad on a 2.5400 mm grid inside its header block 2 blocks, 44 pads checked
PASS pcb: drill 1.000 mm on a 1.800 mm pad                    drill 1.000, pad 1.800, ring 0.400
PASS pcb: silkscreen outline measures the board size          48.00 x 46.00 mm
PASS pcb: every pad inside the outline                        
PASS pcb: a silkscreen position 1 marker for every header     2 markers, 2 headers
PASS pcb: no silkscreen geometry lands on a pad               []
PASS breadboard: no label geometry sits on a pad              []
PASS breadboard: all pads inside the board outline            44 pads
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
