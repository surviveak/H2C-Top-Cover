# H2C Top Cover

A four-panel, interlocking honeycomb cover designed for the Bambu Lab H2C top glass. The cover sits above the glass, includes a front handle opening in the seating lip, and uses removable supports to help prevent the panels from sagging.

**Current version: v1.7.** All six exported meshes passed closed-mesh checks and all source solids passed geometry validation. The preceding v1.6 design was printed by the project owner, who confirmed that the connectors and center junction support worked well. The final v1.7 footprint and enlarged support have not yet been physically verified.

## Download

[Download the complete v1.7 package](downloads/H2C_TopCover_Release_Pack_v1.7.zip), or download the individual STLs below. All dimensions are in millimeters. Import into Bambu Studio at **100% scale**.

| Part | Quantity | STL |
| --- | ---: | --- |
| Front left panel | 1 | [Front left](stl/v1.7/H2C_TopCover_Front_Left_v1.7.stl) |
| Front right panel | 1 | [Front right](stl/v1.7/H2C_TopCover_Front_Right_v1.7.stl) |
| Rear left panel | 1 | [Rear left](stl/v1.7/H2C_TopCover_Rear_Left_v1.7.stl) |
| Rear right panel | 1 | [Rear right](stl/v1.7/H2C_TopCover_Rear_Right_v1.7.stl) |
| Center junction support | 1 | [Center support](stl/v1.7/H2C_TopCover_Center_Junction_Support_v1.7.stl) |
| Honeycomb clip support | 4 | [Clip support](stl/v1.7/H2C_TopCover_Honeycomb_Clip_Support_v1.7.stl) |

The panels are equal in **nominal quarter footprint**, but have different edge details and mating tabs/sockets. They are not interchangeable. Use all four v1.7 panels together. Existing honeycomb clip supports can be reused because their dimensions did not change.

The four panel STLs are saved **top side down, ready to print**. Supports are saved upright.

## Design dimensions

| Feature | v1.7 dimension |
| --- | --- |
| Assembled outside width × depth | 500.5 × 457 |
| Nominal quarter footprint | 250.25 × 228.5 |
| Side/rear retaining wall thickness | 6 |
| Capture width × front-to-rear-wall distance | 488.5 × 451, open at front |
| Seating ledge inside side/rear wall | 10 wide |
| Front seating rail | 10 wide, with centered 127 gap |
| Frame/interlock underside above seating datum | 15 |
| Honeycomb underside above seating datum | 16 |
| Common top surface above seating datum | 20 |
| Honeycomb thickness | 4 |
| Perimeter and seam strip thickness | 5 |
| Honeycomb opening | 8 across flats |
| Honeycomb nominal wall width | 2.25 |
| Main seam clearance | 0.3 |
| Dovetail socket allowance | 0.25 in the sketch |
| Side retaining skirt below seating datum | 3 |
| Center support | 15 high; 40 foot diameter; 36 top pad diameter; 16 stem diameter |
| Honeycomb support | 16 bearing height; 20 foot diameter; 13 shoulder diameter |
| Clip shank / snap bead | 7.65 / 8.3 across flats |
| Clip support total height | 20.9 |

The seating datum is Z=0 in the design. The panels' side skirts extend to Z=-3. The underside heights above glass assume the support and seating surfaces share this datum; actual printer fit should be checked. The panel top continues above the front handle opening: the opening is in the front seating rail, not a cutout through the grille.

The rear edge was shortened by 20 mm in v1.6. Its downward skirt was removed because the shortened rear edge sits over the glass. The rear seating rail remains, while the left and right sides retain their downward skirts. v1.7 then reduces overall width by 4 mm, increases overall depth by 4 mm, and places the seams at the new footprint's midpoint.

## Printing

1. Print one panel and one honeycomb clip support first to check the printer fit, handle clearance, and snap fit with your filament and extrusion settings.
2. The four panel STLs are already rotated 180° around the X axis and translated so their flat top faces sit at Z=0. Import them in their saved orientation: the honeycomb is on the plate and the seating rails point upward. Do not flip them again.
3. Print both support types upright, with their broad circular feet on the plate.
4. Inspect the slice for thin walls, seam tabs, and the split clip tip. Check any overhangs on the clip bead before deciding whether local supports are needed.
5. Use the material and calibrated settings that worked in your test prints. Confirm the chosen material is suitable for your printer's operating environment. Print settings and material were not recorded as a validated profile for this repository.
6. Clean up any burrs on the mating joints and the feet before installation. Avoid scaling individual parts to adjust snap fit; it also changes support height.

The honeycomb is explicit geometry, not slicer infill. Its 4 mm depth reduces material in the grille compared with a 5 mm grille; the frame and seam strips remain 5 mm deep. No load capacity is specified.

## Assembly

1. Identify front left/right from their interrupted front seating rails. The front is the handle side; in the source it is Y=0.
2. Assemble the panels off the printer. Align the dovetail tabs and matching sockets and bring them together vertically. Do not force the tabs sideways into the sockets.
3. Push one honeycomb support upward through a cell near the middle of each panel. Its shoulder bears against the grille underside, and its split bead retains it above the grille. Test one clip before making all four.
4. Place the center support on the glass beneath the four-panel junction. It supports the solid seam strips from below; it does not snap into them.
5. Lower the assembled cover onto the top. Align the centered handle opening and check that all feet sit flat, the side skirts clear the frame, and the handle clears the underside.
6. Confirm the cover rests without rocking or preload. Protective pads under a foot add height and require compensation; the files assume direct contact with clean glass.

The supports reduce unsupported spans. They do not make the cover a shelf or establish a tested load rating.

## Source and regeneration

The [CadQuery build script](source/build_v1.7.py) reproduces the six STL geometries. It writes the STLs next to itself and requires Python and CadQuery:

```bash
python -m pip install cadquery
python source/build_v1.7.py
```

The script validates each solid before exporting. Panel geometry is kept in assembly coordinates internally, then rotated 180° around X and translated to the build plate for STL export. Supports remain upright. It currently exports STL only; v1.7 STEP files are not included. To export STEP for Onshape, add `cq.exporters.export(solid, "part_name_v1.7.step")` while each panel/support solid is available in the script. Retain explicit version numbers when changing the design.

## Version history

| Version | Changes |
| --- | --- |
| v1.1 | Initial four-panel model with frame clearance, seating lip, and honeycomb. |
| v1.2 | Doubled modeled side/rear overhang from 3 to 6 mm. |
| v1.3 | Reduced honeycomb openings from 12 to 8 mm. |
| v1.4 | Raised frame underside from 10 to 15 mm; thinned grille from 5 to 4 mm while retaining 5 mm frame/seam strips. |
| v1.5 | Added 3 mm per side to nominal capture footprint and widened seating ledges from 5 to 10 mm. |
| v1.6 | Shortened rear panels by 20 mm, removed rear downward skirt, and added center and honeycomb clip supports. Owner confirmed printed connectors and junction support worked well. |
| v1.7 | Reduced width by 4 mm; increased depth by 4 mm; made four equal nominal quarters; doubled center-support diameters while keeping its height; panel STL exports rotated 180° around X for top-side-down printing. |

This repository contains the current v1.7 files. Earlier versions are described for context, not bundled as alternate print sets.
