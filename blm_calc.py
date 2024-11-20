import argparse

from constants import POTENCY_DICT
from constants import CAST_TIME_DICT
from constants import ENOCHIAN_DICT
from constants import SPELL_TYPE_DICT
from constants import MAGIC_DICT

GLOBAL_GCD = 2.5
FORM_MAX = 3

# oGCDs lowercase for readability
TRANSPOSE = 'tp'
SWIFT = 'sc'
TRIPLE_CAST = 'tc'


STANDARD_ROTATION = ['B3', 'B4', 'PD', 'F3', 'F4', 'F4', 'F4', 'PD', 'F3P', 'F4', 'F4', 'F4', 'DS', 'FS']
STANDARD_AOE_ROTATION = ['B2', 'FZ', 'F2', 'FL', 'FL', 'FS']


def generate_potency_length(
        spells: list[str],
        astral_start: bool = True,
        targets: int = 1,
        debug: bool = False) -> tuple[int, float]:
    """
    Generate the potency and line length of per target.

    :return: total potency and length of the line
    """
    form_val = 3
    form = 'AF' if astral_start else 'UI'

    potency = 0
    length = 0.0
    swift = 0  # amount of instacasts
    for gcd in spells:
        if gcd not in CAST_TIME_DICT:
            if gcd == TRANSPOSE:
                form = 'UI' if form == 'AF' else 'AF'
                form_val = 1
            elif gcd == SWIFT:
                swift += 1
            elif gcd == TRIPLE_CAST:
                swift += 3
            else:
                raise ValueError('Incorrect spell value')
            continue

        # include the potency and length
        gcd_form = SPELL_TYPE_DICT.get(gcd)
        main, fall_off = POTENCY_DICT[gcd]
        if gcd_form is not None:
            element_modifier = ENOCHIAN_DICT[form][gcd_form][form_val]
            potency += (main + fall_off * (targets - 1)) * element_modifier
            if debug:
                print(f'DEBUG: total potency: {int(potency)} for {gcd} under {form}{form_val}', end=' ')

            # modify the enochian form and value
            if form == gcd_form:
                form_val = min(form_val + MAGIC_DICT[gcd], FORM_MAX)
            else:
                form = gcd_form
                # swapping forms with form swappers should be global GCD
                if gcd in ('F2', 'B2', 'F3', 'B3') and form_val == 3:
                    length += GLOBAL_GCD
                    form_val = MAGIC_DICT[gcd]
                    continue

                form_val = MAGIC_DICT[gcd]
        elif gcd == 'PD':
            potency += main + fall_off * (targets - 1)
            if debug:
                print(f'DEBUG: total potency: {int(potency)} for {gcd} under {form}{form_val}', end=' ')
            # make exception for paradox to advance the gauge
            form_val = min(form_val + MAGIC_DICT[gcd], FORM_MAX)

        if swift > 0 and gcd not in ('PD', 'DS', 'F3P'):
            length += GLOBAL_GCD
            if debug:
                print(f'DEBUG: used swiftcast on {gcd}', end=' ')
            swift -= 1
        else:
            length += CAST_TIME_DICT[gcd]
        if debug:
            print(f'at length {round(length, 1)}s')

    assert form == 'AF' if astral_start else 'UI', 'Final elemental gauge should match start of line'

    return int(potency), length


def generate_line_data(potency: int, length: float, targets: int = 1):

    if targets in (1, 2):
        standard_potency, standard_length = generate_potency_length(STANDARD_ROTATION, targets=targets)
        standard_pps = standard_potency / standard_length
    elif targets > 2:
        standard_potency, standard_length = generate_potency_length(STANDARD_AOE_ROTATION, targets=targets)
        standard_pps = standard_potency / standard_length
    else:
        raise ValueError(f'{targets} is not a valid amount of targets')

    # calculates line data values
    pps = potency / length
    percent_efficiency = pps / standard_pps * 100
    time_gain = (potency - (length * standard_pps)) / standard_pps

    print(f'Total potency: {potency}')
    print(f'Line length: {round(length, 1)}s')
    print(f'Total PPS: {round(pps, 2)}')
    print(f'Relative percent: {round(percent_efficiency, 2)}%')
    print(f'Time gain: {round(time_gain, 2)}s')
    if targets > 1:
        print(f'Targets: {targets}')


if __name__ == '__main__':

    parser = argparse.ArgumentParser(
        prog='BLM Line Efficiency Calculator',
        description='Calculates information for non-standard lines',
    )

    parser.add_argument('--raw_potency', action='store_true',
                        help='Optional to omit the rotation and submit raw potency and length as positional'
                             'arguments. Usage: --raw_potency POTENCY LENGTH')
    parser.add_argument('potency', nargs='?', type=int, default=0)
    parser.add_argument('length', nargs='?', type=float, default=0.0)
    parser.add_argument('-r', '--rotation',
                        type=str,
                        nargs='+',
                        help="Rotation as list: 'B3 PD F3 DS' will make a rotation B3 FD F3 DS"
                        )

    parser.add_argument('--ui3', dest='start_ice', action='store_false',
                        help='Starts in Umbral Ice 3, otherwise Astral Fire 3')
    parser.add_argument('-a', '--aoe', dest='targets', type=int, default=1,
                        help='whether you want to include more targets')
    parser.add_argument('--debug', action='store_true',
                        help='if you know what you are doing')

    args = parser.parse_args()

    if args.raw_potency:
        # do the math only, no rotation
        generate_line_data(args.potency, args.length, targets=args.targets)
    else:
        potency, length = generate_potency_length(
            args.rotation,
            astral_start=args.start_ice,
            targets=args.targets,
            debug=args.debug,
        )
        generate_line_data(potency, length, args.targets)
