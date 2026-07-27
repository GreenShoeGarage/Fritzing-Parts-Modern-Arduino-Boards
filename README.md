# Arduino Fritzing parts: GIGA R1 WiFi, UNO R4 WiFi, UNO Q

Three installable Fritzing parts built to the same brief and the same standard as
the MKR WiFi 1010 part: four views each, schematic and PCB held to production
quality, versioned from v1.0.0, part assets under CC BY-SA 3.0.

| Part | SKU | Connectors | Outline | Header logic level |
|---|---|---|---|---|
| `arduino_giga_r1_wifi` | ABX00063 | 86 | 101.68 x 53.34 mm | 3.3 V |
| `arduino_uno_r4_wifi` | ABX00087 | 32 | 68.58 x 53.34 mm | 5 V |
| `arduino_uno_q` | ABX00162 / ABX00173 | 32 | 68.58 x 53.34 mm | 3.3 V |

Each folder holds the `.fzpz` you install, the flat `src/` tree so the part stays
diffable in git, a README with the connector map and the Known Limitations, a
NOTES.md engineering record, the verification log, and PNG previews of all four
views.

120 automated checks across the three parts, all passing. Rebuild everything with
`python3 tools/make.py`.

## The three logic levels are the point

These boards look interchangeable and are not. The UNO R4 WiFi runs its headers
at 5 V for shield compatibility. The UNO Q takes the same shields on the same
footprint at 3.3 V, with D3 not tolerant above 3.6 V in any mode and the analog
pins not 5 V tolerant at all. The GIGA is a 3.3 V board in a Mega shaped
package. Every one of those facts is written into the `.fzp` description and into
the individual connector descriptions so it shows up in Fritzing's inspector
rather than only in a README nobody opens.

## What these parts share

- Header geometry measured out of the Fritzing core UNO R3 and Mega 2560 parts,
  which is the de facto shield footprint the whole ecosystem is built against,
  including the irregular 4.06 mm and 5.08 mm gaps.
- 1.0 mm drill on a 1.8 mm pad, 2.54 mm pitch, `copper0` nested inside `copper1`.
- All text is stroked path geometry from a single stroke font written for this
  build, so no view depends on a font being installed.
- Shield style header rows only. Debug, ICSP, Qwiic, JSPI, JMEDIA, JMISC, JCTL,
  OFF and VRTC headers are deferred because their board positions come from the
  EAGLE design files, which were unreachable from the build environment. Guessing
  those coordinates would produce a footprint that looks authoritative and is
  wrong. Each part's README lists exactly what is missing.

## Licence

Part assets: CC BY-SA 3.0, the Fritzing parts convention.
Tooling under `tools/`: GPL-3.0.

Arduino and the Arduino board designs are the property of Arduino S.r.l. These
are independent reimplementations drawn from Arduino's published documentation
and are not official Arduino releases.
