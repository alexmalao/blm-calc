SPELL_ABBREVIATIONS = {
    'B1': 'Blizzard I',
    'B2': 'High Blizzard II',
    'B3': 'Blizzard III',
    'B4': 'Blizzard IV',
    'FZ': 'Freeze',
    'F1': 'Fire I',
    'F2': 'High Fire II',
    'F3': 'Fire III',
    'F4': 'Fire IV',
    'FL': 'Flare',
    'FS': 'FLare Star',
    'PD': 'Paradox',
    'DS': 'Despair',
    'TP': 'Transpose',
    'SW': 'Swiftcast',
}

# represented by main hit and multihit falloff
POTENCY_DICT = {
    'B1': (180, 0),
    'B2': (100, 100),
    'B3': (280, 0),
    'B4': (320, 0),
    'FZ': (120, 120),
    'F1': (180, 0),
    'F2': (100, 100),
    'F3': (280, 0),
    'F4': (320, 0),
    'FL': (240, 168),
    'FS': (400, 140),
    'PD': (520, 0),
    'DS': (350, 0),
}

# total cast time of the GCD including 0.1s tax in seconds
CAST_TIME_DICT = {
    'B1': 2.6,
    'B2': 3.1,
    'B3': 2.5,
    'B4': 2.6,
    'FZ': 2.9,
    'F1': 2.6,
    'F2': 3.1,
    'F3': 2.5,
    'F4': 2.9,
    'PD': 2.5,
    'DS': 2.5,
    'FL': 3.1,
    'FS': 3.1,
}

# potency value
ENOCHIAN_DICT = {
    'UI': {
        'UI': {
            1: 1.0,
            2: 1.0,
            3: 1.0,
        },
        'AF': {
            1: 0.9,
            2: 0.8,
            3: 0.7,
        }
    },
    'AF': {
        'AF': {
            1: 1.4,
            2: 1.6,
            3: 1.8,
        },
        'UI': {
            1: 0.9,
            2: 0.8,
            3: 0.7,
        }
    }
}

SPELL_TYPE_DICT = {
    'B1': 'UI',
    'B2': 'UI',
    'B3': 'UI',
    'B4': 'UI',
    'FZ': 'UI',
    'F1': 'AF',
    'F2': 'AF',
    'F3': 'AF',
    'F4': 'AF',
    'DS': 'AF',
    'FS': 'AF',
}

# stores how spells modifies how the phase
MAGIC_DICT = {
    'B1': 1,
    'B2': 3,
    'B3': 3,
    'B4': 0,
    'FZ': 0,
    'F1': 1,
    'F2': 3,
    'F3': 3,
    'F4': 0,
    'DS': 3,
    'FS': 0,
    'PD': 1,
}
