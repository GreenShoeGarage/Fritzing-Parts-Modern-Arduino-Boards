#!/usr/bin/env python3
"""
merge_readme.py

Builds the single README.md that covers all four parts in the set. Pin tables
are pulled straight out of the two generators so the document cannot drift from
the parts it describes.

Licence: GPL-3.0
"""

import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, HERE)
sys.path.insert(0, os.path.join(os.path.dirname(ROOT), "build", "tools"))

from boards import BOARDS  # noqa: E402
import render             # noqa: E402
import build as mkr        # noqa: E402

VERSION = "1.0.0"


def log_counts(slug):
    p = os.path.join(ROOT, slug, "verification-log.txt")
    if not os.path.exists(p):
        return (0, 0)
    m = re.search(r"(\d+) passed, (\d+) failed", open(p).read())
    return (int(m.group(1)), int(m.group(2))) if m else (0, 0)


# ---------------------------------------------------------------------------
# MKR WiFi 1010 described in the same shape as the boards.py specs
# ---------------------------------------------------------------------------
def mkr_spec():
    pins = []
    for p in mkr.PINS:
        x, y = mkr.pad_xy_mm(p["n"])
        pins.append(dict(name=p["name"], type=p["stype"], hdr="Header",
                         dsnum=p["n"], x=x, y=y,
                         extra=("row %s" % ("A" if p["n"] <= 14 else "B"))))
    return dict(
        slug="arduino_mkr_wifi_1010",
        fzpz="arduino_mkr_wifi_1010.fzpz",
        title="Arduino MKR WiFi 1010",
        sku="ABX00023",
        module_id="com.greenshoegarage.arduino.mkr-wifi-1010-tht-v1",
        board=(61.5, 25.0),
        voltage="3.3V",
        processor="SAMD21G18A",
        datasheet="ABX00023 product reference manual, revision 5 (25/04/2024), "
                  "page footer Modified 03/07/2026, plus the official pinout PDF "
                  "(last update 7/08/2020)",
        headers=[("Header", 28, "datasheet section 5.2")],
        key_warnings=[
            "3.3 V I/O and NOT 5 V tolerant. A 5 V signal on any pin will damage the board.",
            "The +5V pin (header pin 28) is not a regulated output. It is jumper "
            "connected to the USB power input, so it only carries voltage when the "
            "board is USB powered.",
            "Header pin 28 sits opposite header pin 1. Row B is numbered from the "
            "far end back toward the USB, which is the single most common way this "
            "part goes wrong.",
        ],
        errata=[
            "Section 5.2 leaves the type cell blank for pin 10 (D1). Every "
            "neighbour is Digital and the pinout PDF shows PA23 with a timer "
            "output, so it is typed Digital here.",
            "Section 5.2 writes D2/PWM through D5/PWM. This part uses the plain "
            "D2 to D5 names with PWM capability in the connector description, "
            "since all of D0 to D5 are PWM capable and decorating four of them "
            "would mislead.",
            "The datasheet uses MISO and MOSI while the pinout PDF uses CIPO and "
            "COPI. This part uses MISO and MOSI as the primary names and carries "
            "both in the descriptions.",
        ],
        deferred=[
            "the debug header (+3V3, SWDIO, RESETN, SWCLK, GND, datasheet section 5.3)",
            "the ESLOV five pin 1.0 mm expansion connector (mating part SHR-05V-S-B)",
            "the Li-Po JST connector (S2B-PH-SM4-TB, mates with PHR-2)",
        ],
        geometry=[
            ("Pad pitch along each row", "2.54 mm", "verified from the datasheet and the MKR header part number"),
            ("Row to row spacing", "17.78 mm (700 mil)", "**derived, not read.** Section 6 states the rows are held to a 100 mil grid so the board seats in a breadboard, and 700 mil is the only multiple of 2.54 mm that leaves a workable margin on a 25 mm wide board"),
            ("Board outline", "61.5 by 25.0 mm", "published figure, not confirmed against the design file"),
            ("Pin 1 offset from the USB end", "14.24 mm", "**assumed.** The 14 position row spans 33.02 mm and this centres it on the board"),
        ],
        pins=pins,
        extra_notes=[
            "The 28 header pins are the whole electrical interface for most uses, "
            "so this part is complete for breadboard and carrier work even without "
            "the three deferred connectors.",
        ],
    )


def other_spec(b):
    render.annotate(b)
    for p in b["pins"]:
        p["extra"] = ""
    L, W = b["board"]
    if "GIGA" in b["title"]:
        geo = [("Pad pitch inside every header block", "2.54 mm", "measured out of the generated footprint"),
               ("Header block positions", "Mega 2560 grid", "measured out of the Fritzing core Arduino_MEGA_2560-Rev3 part"),
               ("Board outline", "101.68 by 53.34 mm", "Fritzing core Mega part canvas. Arduino publishes 101.52 mm for the outline, so treat the last 0.16 mm as unconfirmed")]
    else:
        geo = [("Pad pitch inside every header block", "2.54 mm", "measured out of the generated footprint"),
               ("Header block positions", "UNO R3 grid", "measured out of the Fritzing core arduino_uno(rev3)-icsp part, including the 4.06 mm digital row gap and the 5.08 mm gap between blocks"),
               ("Board outline", "68.58 by 53.34 mm", "stated in plain text in the UNO Q datasheet mechanical section and matching the measured core UNO footprint")]
    return dict(slug=b["slug"], fzpz=b["slug"] + ".fzpz", title=b["title"], sku=b["sku"],
                module_id=b["module_id"], board=b["board"], voltage=b["voltage"],
                processor=b["processor"], datasheet=b["datasheet"],
                headers=b["headers"], key_warnings=b["key_warnings"],
                errata=b["errata"], deferred=b["deferred"], geometry=geo,
                pins=b["pins"], extra_notes=[])


# ---------------------------------------------------------------------------
def section(s):
    L, W = s["board"]
    npins = len(s["pins"])
    passed, failed = log_counts(s["slug"])
    warn = "\n".join("%d. %s" % (i + 1, w) for i, w in enumerate(s["key_warnings"]))
    hdrs = "\n".join("| %s | %d | %s |" % (h, n, src) for (h, n, src) in s["headers"])
    geo = "\n".join("| %s | %s | %s |" % (a, b, c) for (a, b, c) in s["geometry"])
    err = "\n".join("- %s" % e for e in s["errata"]) or "- none found."
    defer = "\n".join("- %s" % d for d in s["deferred"])
    rows = "\n".join(
        "| connector%d | %s %s%s | %s | %s | %.2f, %.2f |"
        % (i, p["hdr"], p["dsnum"], (" (%s)" % p["extra"]) if p.get("extra") else "",
           p["name"], p["type"], p["x"], p["y"])
        for i, p in enumerate(s["pins"]))
    notes = ("\n" + "\n".join("%s" % n for n in s["extra_notes"]) + "\n") if s["extra_notes"] else ""
    return """## {title} ({sku})

`{slug}/{fzpz}` &middot; {npins} connectors &middot; {L} by {W} mm &middot; header logic {volt} &middot; {passed} checks pass, {failed} fail

{warn}
{notes}
**Built from:** {ds}

**Headers exposed**

| Header | Positions | Source |
|---|---|---|
{hdrs}

**Footprint as drawn**

| Property | Value | Confidence |
|---|---|---|
{geo}

Pads are 1.0 mm drill on a 1.8 mm pad throughout the set.

**Not exposed in v{ver}**

{defer}

**Datasheet errata noticed while building this**

{err}

**Connector map**

| Fritzing | Header pin | Name | Type | Position x, y (mm) |
|---|---|---|---|---|
{rows}

`moduleId` is `{mid}`.
""".format(title=s["title"], sku=s["sku"], slug=s["slug"], fzpz=s["fzpz"],
           npins=npins, L=s["board"][0], W=s["board"][1], volt=s["voltage"],
           passed=passed, failed=failed, warn=warn, notes=notes,
           ds=s["datasheet"], hdrs=hdrs, geo=geo, defer=defer, err=err,
           rows=rows, mid=s["module_id"], ver=VERSION)


def main():
    specs = [mkr_spec()] + [other_spec(b) for b in BOARDS]
    tot_p = sum(log_counts(s["slug"])[0] for s in specs)
    tot_f = sum(log_counts(s["slug"])[1] for s in specs)
    def anchor(s):
        head = "%s (%s)" % (s["title"], s["sku"])
        keep = "".join(c for c in head.lower() if c.isalnum() or c in " -")
        return keep.replace(" ", "-")

    index = "\n".join(
        "| [%s](#%s) | %s | %d | %s by %s mm | %s |"
        % (s["title"], anchor(s), s["sku"], len(s["pins"]),
           s["board"][0], s["board"][1], s["voltage"])
        for s in specs)
    body = "\n\n".join(section(s) for s in specs)

    doc = """# Arduino Fritzing parts

Four installable Fritzing parts, all at v{ver}, built to one brief and one
standard: four views each, schematic and PCB held to production quality, part
assets under CC BY-SA 3.0.

| Part | SKU | Connectors | Outline | Header logic |
|---|---|---|---|---|
{index}

{tp} automated checks across the four parts, {tf} failing. Each part folder holds
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

## What the four parts share

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

{body}

## Licence

Part assets (the `.fzp` files and the view SVGs) are licensed CC BY-SA 3.0, which
is the Fritzing parts convention.

The build and verification tooling under `tools/` is licensed GPL-3.0.

Arduino and the Arduino board designs are the property of Arduino S.r.l. These
are independent reimplementations drawn from Arduino's published documentation
and are not official Arduino releases.
""".format(ver=VERSION, index=index, tp=tot_p, tf=tot_f, body=body)
    return doc


if __name__ == "__main__":
    print(main())
