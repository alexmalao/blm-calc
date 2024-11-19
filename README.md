# BLM Non-standard Lines Calculator

Calculates the effective potency of non-standard lines relative to standard.

Supports fairly naive rotational calculations for total potency, line length, and pps (per target).

Some considerations:
- assumption all F3 and B3 are 2.5 GCD or less (no long casting, always F3P)
- standard line includes using F3P under AF3
- all filler (Thunder, Foul, Paradox) is omitted as part of potency calculation
- no validity checking for lines that would otherwise drop enochian or not have F3Ps e.g. F1 during UI
- assumes 0.1s caster tax on any cast 2.5s or longer
- standard AOE starts at 4 targets to be optimal, only F2, B2, and Freeze are gains

### Arguments

Run by doing `python blm_calc.py --rotation B3 PD B4 F3 F4 F4 F4 PD F4 F4 F4 F3 DS FS`

- `--raw_potency`: overrides the rotation and takes manually calculated potency and length to show efficiency, requires potency and length positional arguments
- `potency`: raw potency value
- `length`: length of the line, should end in same phase as start of line
- `-r` `--rotation`: rotation using abbreviations
- `--ui3`: whether to start in Umbral Ice 3 (not recommended)
- `-a` `--aoe`: total targets, defaults to 1

Abbreviations for basic spells for creating lines:

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
- TP: Transpose
- SC: Swiftcast
- TC: Triplecast
