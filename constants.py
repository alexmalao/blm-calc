SPELL_ABBREVIATIONS = {
    'F3P': 'Fire III w/ Firestarter',
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
    'tp': 'Transpose',
    'sc': 'Swiftcast',
    'tc': 'Triplecast',
}

# represented by main hit and multihit falloff
POTENCY_DICT = {
    'F3P': (280, 0),
    'B1': (180, 0),
    'B2': (100, 100),
    'B3': (290, 0),
    'B4': (300, 0),
    'FZ': (120, 120),
    'F1': (180, 0),
    'F2': (100, 100),
    'F3': (290, 0),
    'F4': (300, 0),
    'FL': (240, 168),
    'FS': (500, 175),
    'PD': (540, 0),
    'DS': (350, 0),
}

# total cast time of the GCD including 0.1s tax in seconds
CAST_TIME_DICT = {
    'F3P': 2.5,
    'B1': 2.5,
    'B2': 3.1,
    'B3': 3.6,
    'B4': 2.5,
    'FZ': 2.5,
    'F1': 2.5,
    'F2': 3.1,
    'F3': 3.6,
    'F4': 2.5,
    'PD': 2.5,
    'DS': 2.5,
    'FL': 2.5,
    'FS': 2.5,
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
    'F3P': 'AF',
    'B1': 'UI',
    'B2': 'UI',
    'B3': 'UI',
    'B4': 'UI',
    'FZ': 'UI',
    'F1': 'AF',
    'F2': 'AF',
    'F3': 'AF',
    'F4': 'AF',
    'FL': 'AF',
    'DS': 'AF',
    'FS': 'AF',
}

# stores how spells modifies how the phase
MAGIC_DICT = {
    'F3P': 3,
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
    'FL': 3,
    'FS': 0,
    'PD': 1,
}
