# NOTES: Arduino MKR WiFi 1010 Fritzing part, v1.0.0

Engineering record for the build. Written to be read by whoever has to decide
whether to trust this footprint.

## 1. Sources, what was reachable, and what each one supplied

| Source | Status | What it supplied |
|---|---|---|
| `docs.arduino.cc/resources/datasheets/ABX00023-datasheet.pdf` | **fetched, text extracted** | Section 5.2 header table (all 28 pins, names, types, descriptions), section 5.3 debug header, section 5.1 USB pinout, the 3.3 V and 5 V pin warnings, the 512 mA charger note, section 6 statement that measures are mixed metric and imperial to hold a 100 mil grid between pin rows |
| `content.arduino.cc/assets/Pinout-MKRwifi1010_latest.pdf` | **fetched, text extracted** | SAMD21 port assignment per pin (PA03, PA02, PB02 and so on), the D15 to D21 aliases for A0 to A6, CIPO/COPI naming, confirmation of the two row ordering, ESLOV and battery connector part numbers, debug header order |
| `content.arduino.cc/assets/MKRWiFi1010-reference.zip` (EAGLE) | **not fetched** | nothing. See section 2 |
| `content.arduino.cc/assets/MKRWiFi1010V2.0_sch.pdf` | **not fetched** | nothing. Not required: the header pin table in the datasheet is the same information in tabular form |
| `content.arduino.cc/assets/Arduino MKR WIFI 1010.fzpz` | **not fetched** | nothing. The intended footprint diff did not happen |
| `github.com/fritzing/fritzing-parts` | **cloned** | Fritzing SVG conventions verified empirically against a current core part (`Arduino-nano-rp2040-tht_1`, maintained by the Fritzing parts maintainer, 2023): layer group structure, `copper0` nested in `copper1`, pin as `<line id="connectorNpin">` and terminal as a zero stroke `<rect id="connectorNterminal">` centred on the free end, 1000 user units per inch in schematic |
| `github.com/KiCad/kicad-footprints` | **cloned** | negative result: the KiCad footprint library contains no MKR footprint, so no independent mechanical cross check was available from it |

The section 6 mechanical drawings in the datasheet (board outline, mounting
holes, connector positions) are raster figures inside the PDF. Text extraction
returns the section headings and nothing else, so the dimensions printed on
those drawings were not readable.

## 2. Why the EAGLE .brd is missing, and what that costs

The build environment's network egress is allowlisted. `content.arduino.cc` is
not on the allowlist, so the reference design zip, the schematic PDF and
Arduino's own `.fzpz` could not be downloaded. The two PDFs that were fetched
came through a separate fetch path that does not accept binary archives.

Everything that the `.brd` was supposed to settle is therefore unsettled:

- row to row spacing
- mounting hole diameter and position
- ESLOV, Li-Po JST and debug header positions
- the longitudinal offset of header pin 1 from the board edge
- confirmation of the 61.5 mm by 25.0 mm outline

The build brief says that a fact which cannot be verified should be stated as
unverified rather than filled in with a plausible number. That rule drove three
decisions in section 4.

## 3. Pin by pin diff

Compared against the datasheet section 5.2 table and the official pinout PDF.
"Agrees" means the name, the type and the physical row all match across the
part, the datasheet and the pinout diagram.

| Header pin | Fritzing | Part name | Datasheet 5.2 | Pinout PDF port | Result |
|---|---|---|---|---|---|
| 1 | connector0 | AREF | AREF, Analog | PA03 | agrees |
| 2 | connector1 | A0/DAC0 | A0/DAC0, Analog | PA02, also D15 | agrees |
| 3 | connector2 | A1 | A1, Analog | PB02, also D16 | agrees |
| 4 | connector3 | A2 | A2, Analog | PB03, also D17 | agrees |
| 5 | connector4 | A3 | A3, Analog | PA04, also D18 | agrees |
| 6 | connector5 | A4/SDA | A4/SDA, Analog | PA05, also D19 | agrees |
| 7 | connector6 | A5/SCL | A5/SCL, Analog | PA06, also D20 | agrees |
| 8 | connector7 | A6 | A6, Analog | PA07, also D21 | agrees |
| 9 | connector8 | D0 | D0, Digital | PA22 | agrees |
| 10 | connector9 | D1 | D1 (type cell blank in the datasheet table) | PA23 | agrees, type taken as Digital |
| 11 | connector10 | D2 | D2/PWM, Digital | PA10 | agrees |
| 12 | connector11 | D3 | D3/PWM, Digital | PA11 | agrees |
| 13 | connector12 | D4 | D4/PWM, Digital | PB10 | agrees |
| 14 | connector13 | D5 | D5/PWM, Digital | PB11 | agrees |
| 15 | connector14 | D6 | D6, Digital | PA20 | agrees, LED_BUILTIN |
| 16 | connector15 | D7 | D7, Digital | PA21 | agrees |
| 17 | connector16 | D8/MOSI | D8/MOSI, Digital | PA16, shown as COPI | agrees |
| 18 | connector17 | D9/SCK | D9/SCK, Digital | PA17 | agrees |
| 19 | connector18 | D10/MISO | D10/MISO, Digital | PA19, shown as CIPO | agrees |
| 20 | connector19 | D11/SDA | D11/SDA, Digital | PA08 | agrees |
| 21 | connector20 | D12/SCL | D12/SCL, Digital | PA09 | agrees |
| 22 | connector21 | D13/RX | D13/RX, Digital | PB23 | agrees |
| 23 | connector22 | D14/TX | D14/TX, Digital | PB22 | agrees |
| 24 | connector23 | RESETN | RESETN, Digital | RESET | agrees |
| 25 | connector24 | GND | GND, Power | GND | agrees |
| 26 | connector25 | +3V3 | +3V3, Power Out | +3V3 | agrees |
| 27 | connector26 | VIN | VIN, Power In | VIN | agrees |
| 28 | connector27 | +5V | +5V, Power Out | +5V | agrees |

Naming deltas worth knowing about:

- The datasheet writes `D2/PWM` through `D5/PWM`. This part uses the plain `D2`
  to `D5` names and puts the PWM capability in the connector description, so the
  schematic symbol stays readable. All six of D0 to D5 are PWM capable, so
  decorating four of them and not the other two would be misleading.
- The datasheet's type cell for pin 10 (D1) is blank. Every neighbour is
  Digital and the pinout PDF shows PA23 with a timer output, so it is typed
  Digital here.
- The pinout PDF uses the CIPO and COPI names. The datasheet uses MISO and
  MOSI. The part uses MISO and MOSI as the primary names, since that is what the
  Arduino SPI library and every existing schematic use, with CIPO and COPI in
  the connector descriptions.

### The row B reversal, checked twice

The failure mode called out in the build brief is treating header pins 15 to 28
as if they ran in the same direction as pins 1 to 14. They do not. Two
independent confirmations:

1. The official pinout PDF lists the second row in the order +5V, VIN, +3V3,
   GND, RESET, D14, D13, D12, D11, D10, D9, D8, D7, D6 reading from the USB end.
   Since the datasheet numbers that row 15 (D6) through 28 (+5V), the numbering
   must run from the far end back toward the USB end.
2. The Zephyr `arduino-mkr-header` binding documents the same physical layout
   for the MKR family, with AREF opposite 5V and D5 opposite D6.

So in this part: pin 1 (AREF) and pin 28 (+5V) are both at the USB end and sit
opposite each other, and pin 14 (D5) and pin 15 (D6) are both at the antenna end.
The verification harness asserts this directly by comparing pad x coordinates
read back out of the PCB SVG.

## 4. Judgment calls

**4.1 Row spacing set to 17.78 mm (700 mil), flagged as derived.**
The datasheet says in section 6 that metric and imperial measures are mixed so
that a 100 mil pitch grid is held between the pin rows and the board fits a
breadboard. That constrains the spacing to a multiple of 2.54 mm. On a 25 mm
board, 600 mil (15.24 mm) leaves 4.88 mm from each edge to pad centre, which is
implausibly far inboard for this board, and 900 mil (22.86 mm) leaves 1.07 mm,
which is less than the pad radius. 700 mil leaves 3.61 mm per side and is the
value the build brief expected. It is derived from a constraint, not read from
the reference design, and it is labelled that way in the README.

**4.2 Header span centred longitudinally, flagged as assumed.**
The 14 position row spans 33.02 mm on a 61.5 mm board. Without the `.brd` the
offset of pin 1 from the USB edge is unknown, so the span is centred, giving
14.24 mm. This choice does not affect the pad grid, which is what a carrier
board is actually built against. It only affects where the silkscreen outline
sits relative to the pads.

**4.3 Debug header, ESLOV and Li-Po JST connectors deferred to a later version.**
The build brief's default recommendation was to expose all three as `female`
connector sets after `connector27`, with a GND bus and a +5V bus tying them to
header pins 25 and 28. That is the right end state and the reasoning behind the
recommendation is sound: a custom part should do what the stock one does not.

They are not in v1.0.0 because every one of them needs a board position, and
board positions come from the `.brd`. Exposing them would mean drawing three
connectors at coordinates chosen by eye inside a footprint whose whole selling
point is that you could order a board against it. A missing connector is
visible. A connector in the wrong place is not, until the boards arrive.

What is needed to add them, once the `.brd` is readable:

- ESLOV: 5 positions at 1.0 mm pitch, mating part SHR-05V-S-B, carrying SDA,
  SCL, GND, +5V and an alarm digital pin. The signal set is confirmed by the
  Arduino store page and the pinout PDF (PA08 SDA, PA09 SCL, PA21 as the wake
  pin). The physical pin order on the connector is **not** established by any
  source fetched here and must come from the `.brd` or the connector datasheet.
- Li-Po: JST S2B-PH-SM4-TB(LF)(SN), 2 mm pitch, mates with PHR-2. Position
  unknown.
- Debug: 5 pins, order from datasheet section 5.3 is +3V3, SWDIO, RESETN,
  SWCLK, GND. Pitch and position unknown.
- Buses to add at the same time: GND tying header pin 25 to the debug and ESLOV
  grounds, +5V tying header pin 28 to the ESLOV 5 V pin.

**4.4 No mounting holes.** Same reasoning. The silkscreen would be asserting a
mechanical interface that has not been measured.

**4.5 All text is stroke geometry, not `<text>`.** `tools/strokefont.py` is a
single stroke vector font written for this build. Every label in every view is
emitted as a `<path>` with an explicit `stroke-width` and `fill="none"`. There
is no font dependency anywhere in the part, which satisfies the "convert text to
paths" rule without needing a font conversion step, and it keeps the SVGs
diffable in git because the paths regenerate deterministically.

**4.6 Silkscreen drawn in white (`#FFFFFF`).** This follows the published
Fritzing graphic standard for the silkscreen layer. Worth knowing: the current
Fritzing core part inspected during this build (`Arduino-nano-rp2040-tht_1`)
draws its silkscreen in black. If silkscreen renders wrong on your Fritzing
build, it is one constant in `tools/build.py`.

**4.7 Schematic grouping.** Pins are grouped rather than run in numeric order,
per the brief. Left edge: AREF and A0 to A6, then a gap, then the power group
+5V, VIN, +3V3, GND with the supplies at the top and ground at the bottom.
Right edge: D0 to D7, gap, the SPI and I2C block D8 to D12, gap, the Serial1
pair D13 and D14, gap, RESETN. Every pin also carries its header pin number in
small grey type outside the body, so the physical ordering is still recoverable
from the symbol.

**4.8 Pad geometry left at the brief's starting values.** 1.0 mm drill and
1.8 mm outer pad, drawn as a circle with `fill="none"` and a 0.4 mm stroke, so
the drill is the inner clear area exactly as Fritzing expects. The reconciliation
against Arduino's own footprint did not happen because their `.fzpz` was
unreachable. For reference, the Fritzing core part inspected during this build
uses a 0.965 mm drill on a 1.98 mm pad, so these values sit in the normal range
for a 0.1 inch through hole header.

## 5. Verification checklist, with results

| Check | Result |
|---|---|
| `.fzpz` opens in Fritzing with no console warnings | **NOT RUN.** No Fritzing binary in the build environment |
| All 28 header connectors appear in all four views | **PASS** for breadboard, schematic and PCB, measured by parsing each SVG: 28 `connectorNpin` ids, contiguous from 0, each appearing exactly once. The icon view carries no connectors, which is normal |
| Hover highlight matches across views | **NOT RUN.** Requires Fritzing. The precondition is checked instead: every `svgId` and `terminalId` in the `.fzp` resolves to an element that exists in the named layer, with no mismatches |
| Breadboard seats on a standard breadboard | **NOT RUN** on hardware. Geometrically, the two rows are 17.78 mm apart, an exact multiple of 2.54 mm, which is the condition for straddling the centre channel |
| PCB exports to Gerber, pad grid measures 2.54 mm | **PARTIAL.** Gerber export not run. Measured directly out of the PCB SVG: all 13 gaps in row A and all 13 gaps in row B are 2.5400 mm, row spacing 17.7800 mm |
| Pin 1 in the Gerber matches AREF | **PARTIAL.** Gerber not exported. In the part, `connector0` is named AREF in the `.fzp`, is the leftmost pad in row A in PCB view, and carries the silkscreen dot and the chamfered outline corner |
| Board outline measures 61.5 mm by 25 mm | **PASS** as drawn: the silkscreen outline measures 61.500 mm by 25.000 mm to the outer edge of the stroke. Note this is the published figure, not a figure read from the reference design |
| Schematic pins snap to the grid, wires attach at tips | **PASS.** All 28 pin lines are exactly 100 user units long at 1000 units per inch, both endpoints land on the 100 unit grid, and every `connectorNterminal` rect is centred on the free end of its pin line |
| Every connector ID appears exactly once per view | **PASS.** No duplicates in any view |
| Diff pin ordering against the official pinout PDF | **PASS.** Section 3 above, all 28 pins, no disagreements |
| Diff footprint against Arduino's published `.fzpz` | **NOT RUN.** File unreachable |

Additional checks run beyond the brief's list, all passing: no banned elements
(`style`, `clipPath`, `mask`, `filter`, `image`, `use`, `text`), no banned
attributes (`class`, `style`, `font-family`), every stroked element carries an
explicit `stroke-width`, every drawn element declares `fill`, real units on
`width` and `height` with a matching `viewBox` aspect ratio in all four views,
correct layer group ids with `copper0` nested inside `copper1`, no silkscreen
geometry landing on a pad, no breadboard label geometry landing on a pad, all 28
pads inside the board outline, archive contents exactly the five expected
members, and no em dashes anywhere in the generated files or the tooling.

Total: 57 automated checks, 57 pass, 0 fail, 7 items reported as not run.

Rerun with `python3 tools/verify.py`. The full log follows.

## 6. Verification log

```
PASS breadboard: no banned elements                       
PASS breadboard: no banned attributes                     
PASS breadboard: every stroked element has stroke-width   []
PASS breadboard: every drawn element declares fill        []
PASS breadboard: real units on width and height           61.5mm x 25mm
PASS breadboard: viewBox aspect matches width/height      viewBox 0 0 6150 2500 vs 61.5mm x 25mm
PASS schematic: no banned elements                        
PASS schematic: no banned attributes                      
PASS schematic: every stroked element has stroke-width    []
PASS schematic: every drawn element declares fill         []
PASS schematic: real units on width and height            2.1in x 2.7in
PASS schematic: viewBox aspect matches width/height       viewBox 0 0 2100 2700 vs 2.1in x 2.7in
PASS pcb: no banned elements                              
PASS pcb: no banned attributes                            
PASS pcb: every stroked element has stroke-width          []
PASS pcb: every drawn element declares fill               []
PASS pcb: real units on width and height                  61.5mm x 25mm
PASS pcb: viewBox aspect matches width/height             viewBox 0 0 6150 2500 vs 61.5mm x 25mm
PASS icon: no banned elements                             
PASS icon: no banned attributes                           
PASS icon: every stroked element has stroke-width         []
PASS icon: every drawn element declares fill              []
PASS icon: real units on width and height                 0.32in x 0.32in
PASS icon: viewBox aspect matches width/height            viewBox 0 0 320 320 vs 0.32in x 0.32in
PASS breadboard: layer group ids                          found ['breadboard']
PASS schematic: layer group ids                           found ['schematic']
PASS pcb: layer group ids                                 found ['silkscreen', 'copper1', 'copper0']
PASS icon: layer group ids                                found ['icon']
PASS pcb: copper0 nested inside copper1                   
PASS breadboard: 28 connector pins, each exactly once     count 28, dupes []
PASS schematic: 28 connector pins, each exactly once      count 28, dupes []
PASS pcb: 28 connector pins, each exactly once            count 28, dupes []
PASS schematic: 28 terminals, contiguous                  count 28
PASS fzp: 28 connectors, ids contiguous from 0            count 28
PASS fzp: every connector typed male                      
PASS fzp: svgIds agree with connector ids                 []
PASS fzp: connector0 is AREF (header pin 1)               AREF
PASS fzp: connector27 is +5V (header pin 28)              +5V
PASS fzp: connector14 is D6 (header pin 15, LED_BUILTIN)  D6
PASS fzp: every connector description carries its header pin number 
PASS fzp: description states 3.3 V and not 5 V tolerant   
PASS fzp: description states the 5V pin is jumper connected to USB 
PASS fzp: moduleId is reverse DNS and not Arduino's       com.greenshoegarage.arduino.mkr-wifi-1010-tht-v1
PASS pcb: row A pitch is 2.54 mm at every gap             set [2.54]
PASS pcb: row B pitch is 2.54 mm at every gap             set [2.54]
PASS pcb: row spacing is an integer multiple of 2.54 mm   17.780 mm = 700 mil
PASS pcb: header pin 28 sits opposite header pin 1 (row B reversed) pin1 x 14.24 mm, pin28 x 14.24 mm
PASS pcb: drill 1.000 mm and pad 1.800 mm as drawn        drill 1.000 mm, pad 1.800 mm, ring 0.400 mm
PASS pcb: silkscreen outline measures 61.5 x 25.0 mm to the outer edge 61.500 x 25.000 mm
PASS pcb: no silkscreen geometry lands on a pad           []
PASS breadboard: no label geometry sits on a pad          []
PASS breadboard: all 28 pads inside the board outline     
PASS schematic: every pin lands on the 0.1 in grid        []
PASS schematic: every pin line is exactly 0.1 in long     []
PASS schematic: every terminal sits at the free tip of its pin []
INFO schematic: grid step measured from the file          100.0 user units per 0.1 in
PASS fzpz: archive contains exactly the five expected members ['part.arduino_mkr_wifi_1010.fzp', 'svg.breadboard.arduino_mkr_wifi_1010_breadboard.svg', 'svg.icon.arduino_mkr_wifi_1010_icon.svg', 'svg.pcb.arduino_mkr_wifi_1010_pcb.svg', 'svg.schematic.arduino_mkr_wifi_1010_schematic.svg']
PASS style: no em dashes in any generated or source file  []

INFO NOT RUN: Fritzing loads the part with no console warnings requires Fritzing, a Gerber viewer, or the EAGLE .brd
INFO NOT RUN: hover highlight follows the same net across all three views requires Fritzing, a Gerber viewer, or the EAGLE .brd
INFO NOT RUN: breadboard seating straddles the centre channel on real hardware requires Fritzing, a Gerber viewer, or the EAGLE .brd
INFO NOT RUN: Gerber export measured in a Gerber viewer   requires Fritzing, a Gerber viewer, or the EAGLE .brd
INFO NOT RUN: footprint diffed against Arduino's own published .fzpz requires Fritzing, a Gerber viewer, or the EAGLE .brd
INFO NOT RUN: mounting hole positions                     requires Fritzing, a Gerber viewer, or the EAGLE .brd

57 passed, 0 failed, 7 informational
```
