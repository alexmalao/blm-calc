# BLM Non-standard Lines Calculator

Calculates the effective potency of non-standard lines relative to standard.

Supports fairly naive rotational calculations for total potency, line length, and pps (per target).

Some considerations:

- use F3P for firestarter, standard line includes F3P under AF3
- all filler (Thunder, Foul, Xenoglossy) is omitted as part of potency calculation
- no validity checking for lines that would otherwise drop enochian e.g. F1 during UI
- assumes 0.1s caster tax on any cast 2.5s or longer

### Arguments

Run by doing `python blm_calc.py --rotation B3 PD B4 F3 3xF4 PD 3xF4 F3P DS FS`

- `-r` `--rotation`: rotation using abbreviations, supports multiple spell counts e.g. `4xF4` or `2xFL`
- `--ui3`: whether to start in Umbral Ice 3 (not recommended)
- `-a` `--aoe`: total targets, defaults to 1
- `--raw_potency`: overrides the rotation and takes manually calculated potency and length to show efficiency, requires potency and length positional arguments
- `potency`: raw potency value
- `length`: length of the line, should end in same phase as start of line

Abbreviations for basic spells for creating lines:

- F3P: Fire III w/ Firestarter
- B1: Blizzard I
- B2: High Blizzard II
- B3: Blizzard III 
- B4: Blizzard IV
- FZ: Freeze
- F1: Fire I, 
- F2: High Fire II
- F3: Fire III
- F4: Fire IV
- FL: Flare
- FS: Flare Star
- PD: Paradox
- DS: Despair
- tp: Transpose
- sc: Swiftcast
- tc: Triplecast
