# these are some data dictionaries that are used throughout the addon
# Usually it's for converting things like Amino Acid names into their
# numerical representation in alphabetical order, or converting the name
# of an element to its atomic number etc


# elements dictionary format: 
#   keys are the element symbol for elements up to Lawrencium (a bit overkill)
#   values are a subdictionary filled with keys detailing element information
#       keys in subdicts: 'atomic_number', 'name', 'vdw_radii', and 
#                         'standard_mass'
#       vdw_radii given in picometres
#       atomic masses given in daltons
# 
# this dict is used to convert element symbol to atomic number, vdw_radii, and 
# mass values

elements = {
    "H": {
        "atomic_number": 1,
        "vdw_radii": 120,
        "name": "Hydrogen",
        "standard_mass": 1.00794
    },
    "He": {
        "atomic_number": 2,
        "vdw_radii": 140,
        "name": "Helium",
        "standard_mass": 4.002602
    },
    "Li": {
        "atomic_number": 3,
        "vdw_radii": 182,
        "name": "Lithium",
        "standard_mass": 6.941
    },
    "Be": {
        "atomic_number": 4,
        "vdw_radii": 153,
        "name": "Beryllium",
        "standard_mass": 9.012182
    },
    "B": {
        "atomic_number": 5,
        "vdw_radii": 192,
        "name": "Boron",
        "standard_mass": 10.811
    },
    "C": {
        "atomic_number": 6,
        "vdw_radii": 170,
        "name": "Carbon",
        "standard_mass": 12.0107
    },
    "N": {
        "atomic_number": 7,
        "vdw_radii": 155,
        "name": "Nitrogen",
        "standard_mass": 14.0067
    },
    "O": {
        "atomic_number": 8,
        "vdw_radii": 152,
        "name": "Oxygen",
        "standard_mass": 15.9994
    },
    "F": {
        "atomic_number": 9,
        "vdw_radii": 147,
        "name": "Fluorine",
        "standard_mass": 18.9984032
    },
    "Ne": {
        "atomic_number": 10,
        "vdw_radii": 154,
        "name": "Neon",
        "standard_mass": 20.1797
    },
    "Na": {
        "atomic_number": 11,
        "vdw_radii": 227,
        "name": "Sodium",
        "standard_mass": 22.98977
    },
    "Mg": {
        "atomic_number": 12,
        "vdw_radii": 173,
        "name": "Magnesium",
        "standard_mass": 24.305
    },
    "Al": {
        "atomic_number": 13,
        "vdw_radii": 184,
        "name": "Aluminium",
        "standard_mass": 26.981538
    },
    "Si": {
        "atomic_number": 14,
        "vdw_radii": 210,
        "name": "Silicon",
        "standard_mass": 28.0855
    },
    "P": {
        "atomic_number": 15,
        "vdw_radii": 180,
        "name": "Phosphorus",
        "standard_mass": 30.973761
    },
    "S": {
        "atomic_number": 16,
        "vdw_radii": 180,
        "name": "Sulfur",
        "standard_mass": 32.065
    },
    "Cl": {
        "atomic_number": 17,
        "vdw_radii": 175,
        "name": "Chlorine",
        "standard_mass": 35.453
    },
    "Ar": {
        "atomic_number": 18,
        "vdw_radii": 188,
        "name": "Argon",
        "standard_mass": 39.948
    },
    "K": {
        "atomic_number": 19,
        "vdw_radii": 275,
        "name": "Potassium",
        "standard_mass": 39.0983
    },
    "Ca": {
        "atomic_number": 20,
        "vdw_radii": 231,
        "name": "Calcium",
        "standard_mass": 40.078
    },
    "Sc": {
        "atomic_number": 21,
        "vdw_radii": 211,
        "name": "Scandium",
        "standard_mass": 44.95591
    },
    "Ti": {
        "atomic_number": 22,
        "vdw_radii": 147,
        "name": "Titanium",
        "standard_mass": 47.867
    },
    "V": {
        "atomic_number": 23,
        "vdw_radii": 134,
        "name": "Vanadium",
        "standard_mass": 50.9415
    },
    "Cr": {
        "atomic_number": 24,
        "vdw_radii": 128,
        "name": "Chromium",
        "standard_mass": 51.9961
    },
    "Mn": {
        "atomic_number": 25,
        "vdw_radii": 127,
        "name": "Manganese",
        "standard_mass": 54.938049
    },
    "Fe": {
        "atomic_number": 26,
        "vdw_radii": 126,
        "name": "Iron",
        "standard_mass": 55.845
    },
    "Co": {
        "atomic_number": 27,
        "vdw_radii": 125,
        "name": "Cobalt",
        "standard_mass": 58.9332
    },
    "Ni": {
        "atomic_number": 28,
        "vdw_radii": 163,
        "name": "Nickel",
        "standard_mass": 58.6934
    },
    "Cu": {
        "atomic_number": 29,
        "vdw_radii": 140,
        "name": "Copper",
        "standard_mass": 63.546
    },
    "Zn": {
        "atomic_number": 30,
        "vdw_radii": 139,
        "name": "Zinc",
        "standard_mass": 65.409
    },
    "Ga": {
        "atomic_number": 31,
        "vdw_radii": 187,
        "name": "Gallium",
        "standard_mass": 69.723
    },
    "Ge": {
        "atomic_number": 32,
        "vdw_radii": 211,
        "name": "Germanium",
        "standard_mass": 72.64
    },
    "As": {
        "atomic_number": 33,
        "vdw_radii": 185,
        "name": "Arsenic",
        "standard_mass": 74.9216
    },
    "Se": {
        "atomic_number": 34,
        "vdw_radii": 190,
        "name": "Selenium",
        "standard_mass": 78.96
    },
    "Br": {
        "atomic_number": 35,
        "vdw_radii": 185,
        "name": "Bromine",
        "standard_mass": 79.904
    },
    "Kr": {
        "atomic_number": 36,
        "vdw_radii": 202,
        "name": "Krypton",
        "standard_mass": 83.798
    },
    "Rb": {
        "atomic_number": 37,
        "vdw_radii": 303,
        "name": "Rubidium",
        "standard_mass": 85.4678
    },
    "Sr": {
        "atomic_number": 38,
        "vdw_radii": 249,
        "name": "Strontium",
        "standard_mass": 87.62
    },
    "Y": {
        "atomic_number": 39,
        "vdw_radii": 180,
        "name": "Yttrium",
        "standard_mass": 88.90585
    },
    "Zr": {
        "atomic_number": 40,
        "vdw_radii": 160,
        "name": "Zirconium",
        "standard_mass": 91.224
    },
    "Nb": {
        "atomic_number": 41,
        "vdw_radii": 146,
        "name": "Niobium",
        "standard_mass": 92.90638
    },
    "Mo": {
        "atomic_number": 42,
        "vdw_radii": 239,
        "name": "Molybdenum",
        "standard_mass": 95.94
    },
    "Tc": {
        "atomic_number": 43,
        "vdw_radii": 136,
        "name": "Technetium",
        "standard_mass": 98.9062
    },
    "Ru": {
        "atomic_number": 44,
        "vdw_radii": 134,
        "name": "Ruthenium",
        "standard_mass": 101.07
    },
    "Rh": {
        "atomic_number": 45,
        "vdw_radii": 137,
        "name": "Rhodium",
        "standard_mass": 102.9055
    },
    "Pd": {
        "atomic_number": 46,
        "vdw_radii": 144,
        "name": "Palladium",
        "standard_mass": 106.42
    },
    "Ag": {
        "atomic_number": 47,
        "name": "Silver",
        "standard_mass": 107.8682
    },
    "Cd": {
        "atomic_number": 48,
        "name": "Cadmium",
        "standard_mass": 112.411
    },
    "In": {
        "atomic_number": 49,
        "name": "Indium",
        "standard_mass": 114.818
    },
    "Sn": {
        "atomic_number": 50,
        "name": "Tin",
        "standard_mass": 118.71
    },
    "Sb": {
        "atomic_number": 51,
        "name": "Antimony",
        "standard_mass": 121.76
    },
    "Te": {
        "atomic_number": 52,
        "name": "Tellurium",
        "standard_mass": 127.6
    },
    "I": {
        "atomic_number": 53,
        "name": "Iodine",
        "standard_mass": 126.90447
    },
    "Xe": {
        "atomic_number": 54,
        "name": "Xenon",
        "standard_mass": 131.293
    },
    "Cs": {
        "atomic_number": 55,
        "name": "Caesium",
        "standard_mass": 132.90545
    },
    "Ba": {
        "atomic_number": 56,
        "name": "Barium",
        "standard_mass": 137.327
    },
    "La": {
        "atomic_number": 57,
        "name": "Lanthanum",
        "standard_mass": 138.9055
    },
    "Ce": {
        "atomic_number": 58,
        "name": "Cerium",
        "standard_mass": 140.116
    },
    "Pr": {
        "atomic_number": 59,
        "name": "Praseodymium",
        "standard_mass": 140.90765
    },
    "Nd": {
        "atomic_number": 60,
        "name": "Neodymium",
        "standard_mass": 144.24
    },
    "Pm": {
        "atomic_number": 61,
        "name": "Promethium",
        "standard_mass": 145
    },
    "Sm": {
        "atomic_number": 62,
        "name": "Samarium",
        "standard_mass": 150.36
    },
    "Eu": {
        "atomic_number": 63,
        "name": "Europium",
        "standard_mass": 151.964
    },
    "Gd": {
        "atomic_number": 64,
        "name": "Gadolinium",
        "standard_mass": 157.25
    },
    "Tb": {
        "atomic_number": 65,
        "name": "Terbium",
        "standard_mass": 158.92534
    },
    "Dy": {
        "atomic_number": 66,
        "name": "Dysprosium",
        "standard_mass": 162.5
    },
    "Ho": {
        "atomic_number": 67,
        "name": "Holmium",
        "standard_mass": 164.93032
    },
    "Er": {
        "atomic_number": 68,
        "name": "Erbium",
        "standard_mass": 167.259
    },
    "Tm": {
        "atomic_number": 69,
        "name": "Thulium",
        "standard_mass": 168.93421
    },
    "Yb": {
        "atomic_number": 70,
        "name": "Ytterbium",
        "standard_mass": 173.04
    },
    "Lu": {
        "atomic_number": 71,
        "name": "Lutetium",
        "standard_mass": 174.967
    },
    "Hf": {
        "atomic_number": 72,
        "name": "Hafnium",
        "standard_mass": 178.49
    },
    "Ta": {
        "atomic_number": 73,
        "name": "Tantalum",
        "standard_mass": 180.9479
    },
    "W": {
        "atomic_number": 74,
        "name": "Tungsten",
        "standard_mass": 183.84
    },
    "Re": {
        "atomic_number": 75,
        "name": "Rhenium",
        "standard_mass": 186.207
    },
    "Os": {
        "atomic_number": 76,
        "name": "Osmium",
        "standard_mass": 190.23
    },
    "Ir": {
        "atomic_number": 77,
        "name": "Iridium",
        "standard_mass": 192.217
    },
    "Pt": {
        "atomic_number": 78,
        "name": "Platinum",
        "standard_mass": 195.078
    },
    "Au": {
        "atomic_number": 79,
        "name": "Gold",
        "standard_mass": 196.96655
    },
    "Hg": {
        "atomic_number": 80,
        "name": "Mercury",
        "standard_mass": 200.59
    },
    "Tl": {
        "atomic_number": 81,
        "name": "Thallium",
        "standard_mass": 204.3833
    },
    "Pb": {
        "atomic_number": 82,
        "name": "Lead",
        "standard_mass": 207.2
    },
    "Bi": {
        "atomic_number": 83,
        "name": "Bismuth",
        "standard_mass": 208.98038
    },
    "Po": {
        "atomic_number": 84,
        "name": "Polonium",
        "standard_mass": 209
    },
    "At": {
        "atomic_number": 85,
        "name": "Astatine",
        "standard_mass": 210
    },
    "Rn": {
        "atomic_number": 86,
        "name": "Radon",
        "standard_mass": 222
    },
    "Fr": {
        "atomic_number": 87,
        "name": "Francium",
        "standard_mass": 223
    },
    "Ra": {
        "atomic_number": 88,
        "name": "Radium",
        "standard_mass": 226.0254
    },
    "Ac": {
        "atomic_number": 89,
        "name": "Actinium",
        "standard_mass": 227
    },
    "Th": {
        "atomic_number": 90,
        "name": "Thorium",
        "standard_mass": 232.0381
    },
    "Pa": {
        "atomic_number": 91,
        "name": "Protactinium",
        "standard_mass": 231.03588
    },
    "U": {
        "atomic_number": 92,
        "name": "Uranium",
        "standard_mass": 238.02891
    },
    "Np": {
        "atomic_number": 93,
        "name": "Neptunium",
        "standard_mass": 237.0482
    },
    "Pu": {
        "atomic_number": 94,
        "name": "Plutonium",
        "standard_mass": 244
    },
    "Am": {
        "atomic_number": 95,
        "name": "Americium",
        "standard_mass": 243
    },
    "Cm": {
        "atomic_number": 96,
        "name": "Curium",
        "standard_mass": 243
    },
    "Bk": {
        "atomic_number": 97,
        "name": "Berkelium",
        "standard_mass": 247
    },
    "Cf": {
        "atomic_number": 98,
        "name": "Californium",
        "standard_mass": 251
    },
    "Es": {
        "atomic_number": 99,
        "name": "Einsteinium",
        "standard_mass": 254
    },
    "Fm": {
        "atomic_number": 100,
        "name": "Fermium",
        "standard_mass": 254
    },
    "Md": {
        "atomic_number": 101,
        "name": "Mendelevium",
        "standard_mass": 258
    },
    "No": {
        "atomic_number": 102,
        "name": "Nobelium",
        "standard_mass": 259
    },
    "Lr": {
        "atomic_number": 103,
        "name": "Lawrencium",
        "standard_mass": 262
    },
    "X": {
        "atomic_number": -1,
        "name": "Unknown",
        "standard_mass": 0
    }
}

# elements_by_atomic_number dictionary format: 
#   keys are integers of the element's atomic number for elements up to 
#   Lawrencium (a bit overkill)
#   values are a subdictionary filled with keys detailing element information
#       keys in subdicts: 'element_symbol', 'name', 'standard_mass', and 
#                         'vdw_radii'
#       vdw_radii given in picometres
#       atomic masses given in daltons
# 
# this dict is used to back-convert atomic numbers to element symbols, 
# vdw_radii, and mass values

elements_by_atomic_number = {
    -1: {
        "element_symbol": "X",
        "name": "Unknown"
    },
    1: {
        "element_symbol": "H",
        "name": "Hydrogen",
        "standard_mass": 1.00794,
        "vdw_radii": 120
    },
    2: {
        "element_symbol": "He",
        "name": "Helium",
        "standard_mass": 4.002602,
        "vdw_radii": 140
    },
    3: {
        "element_symbol": "Li",
        "name": "Lithium",
        "standard_mass": 6.941,
        "vdw_radii": 182
    },
    4: {
        "element_symbol": "Be",
        "name": "Beryllium",
        "standard_mass": 9.012182,
        "vdw_radii": 153
    },
    5: {
        "element_symbol": "B",
        "name": "Boron",
        "standard_mass": 10.811,
        "vdw_radii": 192
    },
    6: {
        "element_symbol": "C",
        "name": "Carbon",
        "standard_mass": 12.0107,
        "vdw_radii": 170
    },
    7: {
        "element_symbol": "N",
        "name": "Nitrogen",
        "standard_mass": 14.0067,
        "vdw_radii": 155
    },
    8: {
        "element_symbol": "O",
        "name": "Oxygen",
        "standard_mass": 15.9994,
        "vdw_radii": 152
    },
    9: {
        "element_symbol": "F",
        "name": "Fluorine",
        "standard_mass": 18.9984032,
        "vdw_radii": 147
    },
    10: {
        "element_symbol": "Ne",
        "name": "Neon",
        "standard_mass": 20.1797,
        "vdw_radii": 154
    },
    11: {
        "element_symbol": "Na",
        "name": "Sodium",
        "standard_mass": 22.98977,
        "vdw_radii": 227
    },
    12: {
        "element_symbol": "Mg",
        "name": "Magnesium",
        "standard_mass": 24.305,
        "vdw_radii": 173
    },
    13: {
        "element_symbol": "Al",
        "name": "Aluminium",
        "standard_mass": 26.981538,
        "vdw_radii": 184
    },
    14: {
        "element_symbol": "Si",
        "name": "Silicon",
        "standard_mass": 28.0855,
        "vdw_radii": 210
    },
    15: {
        "element_symbol": "P",
        "name": "Phosphorus",
        "standard_mass": 30.973761,
        "vdw_radii": 180
    },
    16: {
        "element_symbol": "S",
        "name": "Sulfur",
        "standard_mass": 32.065,
        "vdw_radii": 180
    },
    17: {
        "element_symbol": "Cl",
        "name": "Chlorine",
        "standard_mass": 35.453,
        "vdw_radii": 175
    },
    18: {
        "element_symbol": "Ar",
        "name": "Argon",
        "standard_mass": 39.948,
        "vdw_radii": 188
    },
    19: {
        "element_symbol": "K",
        "name": "Potassium",
        "standard_mass": 39.0983,
        "vdw_radii": 275
    },
    20: {
        "element_symbol": "Ca",
        "name": "Calcium",
        "standard_mass": 40.078,
        "vdw_radii": 231
    },
    21: {
        "element_symbol": "Sc",
        "name": "Scandium",
        "standard_mass": 44.95591,
        "vdw_radii": 211
    },
    22: {
        "element_symbol": "Ti",
        "name": "Titanium",
        "standard_mass": 47.867,
        "vdw_radii": 147
    },
    23: {
        "element_symbol": "V",
        "name": "Vanadium",
        "standard_mass": 50.9415,
        "vdw_radii": 134
    },
    24: {
        "element_symbol": "Cr",
        "name": "Chromium",
        "standard_mass": 51.9961,
        "vdw_radii": 128
    },
    25: {
        "element_symbol": "Mn",
        "name": "Manganese",
        "standard_mass": 54.938049,
        "vdw_radii": 127
    },
    26: {
        "element_symbol": "Fe",
        "name": "Iron",
        "standard_mass": 55.845,
        "vdw_radii": 126
    },
    27: {
        "element_symbol": "Co",
        "name": "Cobalt",
        "standard_mass": 58.9332,
        "vdw_radii": 125
    },
    28: {
        "element_symbol": "Ni",
        "name": "Nickel",
        "standard_mass": 58.6934,
        "vdw_radii": 163
    },
    29: {
        "element_symbol": "Cu",
        "name": "Copper",
        "standard_mass": 63.546,
        "vdw_radii": 140
    },
    30: {
        "element_symbol": "Zn",
        "name": "Zinc",
        "standard_mass": 65.409,
        "vdw_radii": 139
    },
    31: {
        "element_symbol": "Ga",
        "name": "Gallium",
        "standard_mass": 69.723,
        "vdw_radii": 187
    },
    32: {
        "element_symbol": "Ge",
        "name": "Germanium",
        "standard_mass": 72.64,
        "vdw_radii": 211
    },
    33: {
        "element_symbol": "As",
        "name": "Arsenic",
        "standard_mass": 74.9216,
        "vdw_radii": 185
    },
    34: {
        "element_symbol": "Se",
        "name": "Selenium",
        "standard_mass": 78.96,
        "vdw_radii": 190
    },
    35: {
        "element_symbol": "Br",
        "name": "Bromine",
        "standard_mass": 79.904,
        "vdw_radii": 185
    },
    36: {
        "element_symbol": "Kr",
        "name": "Krypton",
        "standard_mass": 83.798,
        "vdw_radii": 202
    },
    37: {
        "element_symbol": "Rb",
        "name": "Rubidium",
        "standard_mass": 85.4678,
        "vdw_radii": 303
    },
    38: {
        "element_symbol": "Sr",
        "name": "Strontium",
        "standard_mass": 87.62,
        "vdw_radii": 249
    },
    39: {
        "element_symbol": "Y",
        "name": "Yttrium",
        "standard_mass": 88.90585,
        "vdw_radii": 180
    },
    40: {
        "element_symbol": "Zr",
        "name": "Zirconium",
        "standard_mass": 91.224,
        "vdw_radii": 160
    },
    41: {
        "element_symbol": "Nb",
        "name": "Niobium",
        "standard_mass": 92.90638,
        "vdw_radii": 146
    },
    42: {
        "element_symbol": "Mo",
        "name": "Molybdenum",
        "standard_mass": 95.94,
        "vdw_radii": 239
    },
    43: {
        "element_symbol": "Tc",
        "name": "Technetium",
        "standard_mass": 98.9062,
        "vdw_radii": 136
    },
    44: {
        "element_symbol": "Ru",
        "name": "Ruthenium",
        "standard_mass": 101.07,
        "vdw_radii": 134
    },
    45: {
        "element_symbol": "Rh",
        "name": "Rhodium",
        "standard_mass": 102.9055,
        "vdw_radii": 137
    },
    46: {
        "element_symbol": "Pd",
        "name": "Palladium",
        "standard_mass": 106.42,
        "vdw_radii": 144
    },
    47: {
        "element_symbol": "Ag",
        "name": "Silver",
        "standard_mass": 107.8682
    },
    48: {
        "element_symbol": "Cd",
        "name": "Cadmium",
        "standard_mass": 112.411
    },
    49: {
        "element_symbol": "In",
        "name": "Indium",
        "standard_mass": 114.818
    },
    50: {
        "element_symbol": "Sn",
        "name": "Tin",
        "standard_mass": 118.71
    },
    51: {
        "element_symbol": "Sb",
        "name": "Antimony",
        "standard_mass": 121.76
    },
    52: {
        "element_symbol": "Te",
        "name": "Tellurium",
        "standard_mass": 127.6
    },
    53: {
        "element_symbol": "I",
        "name": "Iodine",
        "standard_mass": 126.90447
    },
    54: {
        "element_symbol": "Xe",
        "name": "Xenon",
        "standard_mass": 131.293
    },
    55: {
        "element_symbol": "Cs",
        "name": "Caesium",
        "standard_mass": 132.90545
    },
    56: {
        "element_symbol": "Ba",
        "name": "Barium",
        "standard_mass": 137.327
    },
    57: {
        "element_symbol": "La",
        "name": "Lanthanum",
        "standard_mass": 138.9055
    },
    58: {
        "element_symbol": "Ce",
        "name": "Cerium",
        "standard_mass": 140.116
    },
    59: {
        "element_symbol": "Pr",
        "name": "Praseodymium",
        "standard_mass": 140.90765
    },
    60: {
        "element_symbol": "Nd",
        "name": "Neodymium",
        "standard_mass": 144.24
    },
    61: {
        "element_symbol": "Pm",
        "name": "Promethium",
        "standard_mass": 145
    },
    62: {
        "element_symbol": "Sm",
        "name": "Samarium",
        "standard_mass": 150.36
    },
    63: {
        "element_symbol": "Eu",
        "name": "Europium",
        "standard_mass": 151.964
    },
    64: {
        "element_symbol": "Gd",
        "name": "Gadolinium",
        "standard_mass": 157.25
    },
    65: {
        "element_symbol": "Tb",
        "name": "Terbium",
        "standard_mass": 158.92534
    },
    66: {
        "element_symbol": "Dy",
        "name": "Dysprosium",
        "standard_mass": 162.5
    },
    67: {
        "element_symbol": "Ho",
        "name": "Holmium",
        "standard_mass": 164.93032
    },
    68: {
        "element_symbol": "Er",
        "name": "Erbium",
        "standard_mass": 167.259
    },
    69: {
        "element_symbol": "Tm",
        "name": "Thulium",
        "standard_mass": 168.93421
    },
    70: {
        "element_symbol": "Yb",
        "name": "Ytterbium",
        "standard_mass": 173.04
    },
    71: {
        "element_symbol": "Lu",
        "name": "Lutetium",
        "standard_mass": 174.967
    },
    72: {
        "element_symbol": "Hf",
        "name": "Hafnium",
        "standard_mass": 178.49
    },
    73: {
        "element_symbol": "Ta",
        "name": "Tantalum",
        "standard_mass": 180.9479
    },
    74: {
        "element_symbol": "W",
        "name": "Tungsten",
        "standard_mass": 183.84
    },
    75: {
        "element_symbol": "Re",
        "name": "Rhenium",
        "standard_mass": 186.207
    },
    76: {
        "element_symbol": "Os",
        "name": "Osmium",
        "standard_mass": 190.23
    },
    77: {
        "element_symbol": "Ir",
        "name": "Iridium",
        "standard_mass": 192.217
    },
    78: {
        "element_symbol": "Pt",
        "name": "Platinum",
        "standard_mass": 195.078
    },
    79: {
        "element_symbol": "Au",
        "name": "Gold",
        "standard_mass": 196.96655
    },
    80: {
        "element_symbol": "Hg",
        "name": "Mercury",
        "standard_mass": 200.59
    },
    81: {
        "element_symbol": "Tl",
        "name": "Thallium",
        "standard_mass": 204.3833
    },
    82: {
        "element_symbol": "Pb",
        "name": "Lead",
        "standard_mass": 207.2
    },
    83: {
        "element_symbol": "Bi",
        "name": "Bismuth",
        "standard_mass": 208.98038
    },
    84: {
        "element_symbol": "Po",
        "name": "Polonium",
        "standard_mass": 209
    },
    85: {
        "element_symbol": "At",
        "name": "Astatine",
        "standard_mass": 210
    },
    86: {
        "element_symbol": "Rn",
        "name": "Radon",
        "standard_mass": 222
    },
    87: {
        "element_symbol": "Fr",
        "name": "Francium",
        "standard_mass": 223
    },
    88: {
        "element_symbol": "Ra",
        "name": "Radium",
        "standard_mass": 226.0254
    },
    89: {
        "element_symbol": "Ac",
        "name": "Actinium",
        "standard_mass": 227
    },
    90: {
        "element_symbol": "Th",
        "name": "Thorium",
        "standard_mass": 232.0381
    },
    91: {
        "element_symbol": "Pa",
        "name": "Protactinium",
        "standard_mass": 231.03588
    },
    92: {
        "element_symbol": "U",
        "name": "Uranium",
        "standard_mass": 238.02891
    },
    93: {
        "element_symbol": "Np",
        "name": "Neptunium",
        "standard_mass": 237.0482
    },
    94: {
        "element_symbol": "Pu",
        "name": "Plutonium",
        "standard_mass": 244
    },
    95: {
        "element_symbol": "Am",
        "name": "Americium",
        "standard_mass": 243
    },
    96: {
        "element_symbol": "Cm",
        "name": "Curium",
        "standard_mass": 243
    },
    97: {
        "element_symbol": "Bk",
        "name": "Berkelium",
        "standard_mass": 247
    },
    98: {
        "element_symbol": "Cf",
        "name": "Californium",
        "standard_mass": 251
    },
    99: {
        "element_symbol": "Es",
        "name": "Einsteinium",
        "standard_mass": 254
    },
    100: {
        "element_symbol": "Fm",
        "name": "Fermium",
        "standard_mass": 254
    },
    101: {
        "element_symbol": "Md",
        "name": "Mendelevium",
        "standard_mass": 258
    },
    102: {
        "element_symbol": "No",
        "name": "Nobelium",
        "standard_mass": 259
    },
    103: {
        "element_symbol": "Lr",
        "name": "Lawrencium",
        "standard_mass": 262
    }
}

# coarse_grain_particles dictionary is currently being used as a backup for
# non-standard atom names that were mixed in with the elements dictionary

coarse_grain_particles = {
    "BB": {"atomic_number":  6, 'vdw_radii': 250, "name": "MartiniBB"},
    "CD": {"atomic_number":  6, 'vdw_radii': 170, "name": "MartiniLipidCarbonD"},
    "D" : {"atomic_number":  6, 'vdw_radii': 170, "name": "Carbon"},
    "GL": {"atomic_number":  8, 'vdw_radii': 180, "name": "MartiniGL"},
    "SC": {"atomic_number": 16, 'vdw_radii': 200, "name": "MartiniSC"}#,
    ## just kept since these were entries in the old `elements` dictionary
    #"NA": {"atomic_number": 11, 'vdw_radii': 227, "name": "Sodium"},    
    #"CL": {"atomic_number": 17, 'vdw_radii': 175, "name": "Chlorine"}
    }


residues = {
    # unknown? Came up in one of the structures, haven't looked into it yet
    # TODO look into it!
    "UNK": {"res_name_num": -1, "res_type": "unknown",  "res_type_no": 1},

    # TODO implement an attribute that uses the residue types (basic / polar / acid etc)
    # 20 naturally occurring amino acids
    "ALA": {"res_name_num": 0,  "res_type": "apolar",   "res_type_no": 1},
    "ARG": {"res_name_num": 1,  "res_type": "basic",    "res_type_no": 1},
    "ASN": {"res_name_num": 2,  "res_type": "polar",    "res_type_no": 1},
    "ASP": {"res_name_num": 3,  "res_type": "acid",     "res_type_no": 1},
    # can act as acid, but mostly polar?
    "CYS": {"res_name_num": 4,  "res_type": "polar",    "res_type_no": 1},
    "GLU": {"res_name_num": 5,  "res_type": "acid",     "res_type_no": 1},
    "GLN": {"res_name_num": 6,  "res_type": "polar",    "res_type_no": 1},
    "GLY": {"res_name_num": 7,  "res_type": "apolar",   "res_type_no": 1},
    # ambiguous
    "HIS": {"res_name_num": 8,  "res_type": "polar",    "res_type_no": 1},
    "ILE": {"res_name_num": 9,  "res_type": "apolar",   "res_type_no": 1},
    "LEU": {"res_name_num": 10, "res_type": "apolar",   "res_type_no": 1},
    "LYS": {"res_name_num": 11, "res_type": "basic",    "res_type_no": 1},
    "MET": {"res_name_num": 12, "res_type": "apolar",   "res_type_no": 1},
    "PHE": {"res_name_num": 13, "res_type": "aromatic", "res_type_no": 1},
    "PRO": {"res_name_num": 14, "res_type": "apolar",   "res_type_no": 1},
    "SER": {"res_name_num": 15, "res_type": "polar",    "res_type_no": 1},
    "THR": {"res_name_num": 16, "res_type": "polar",    "res_type_no": 1},
    "TRP": {"res_name_num": 17, "res_type": "aromatic", "res_type_no": 1},
    "TYR": {"res_name_num": 18, "res_type": "aromatic", "res_type_no": 1},
    "VAL": {"res_name_num": 19, "res_type": "apolar",   "res_type_no": 1},

    # modified amino acids, unsure how to deal with but currently will label as the
    # same res_name number
    # S-nitrosylation of cysteine
    "SNC": {"res_name_num": 15, "res_type": "unkown", "res_type_no": 1},
    # selenomethionine
    "MSE": {"res_name_num": 12, "res_type": "unkown", "res_type_no": 1},

    # add conventional AMBER FF residue names with different protonations
    "ASH": {"res_name_num": 3,  "res_type": "acid",     "res_type_no": 1},
    "CYM": {"res_name_num": 4,  "res_type": "polar",    "res_type_no": 1},
    "CYX": {"res_name_num": 4,  "res_type": "polar",    "res_type_no": 1},
    "GLH": {"res_name_num": 5,  "res_type": "acid",     "res_type_no": 1},
    "HID": {"res_name_num": 8,  "res_type": "polar",    "res_type_no": 1},
    "HIE": {"res_name_num": 8,  "res_type": "polar",    "res_type_no": 1},
    "HIP": {"res_name_num": 8,  "res_type": "polar",    "res_type_no": 1},
    "HYP": {"res_name_num": 8,  "res_type": "polar",    "res_type_no": 1},
    "LYN": {"res_name_num": 11, "res_type": "basic",    "res_type_no": 1},

    # nucleic acids
    # DNA
    "DA": {"res_name_num": 30,  "res_type": "unkown",   "res_type_no": 1},
    "DC": {"res_name_num": 31,  "res_type": "unkown",   "res_type_no": 1},
    "DG": {"res_name_num": 32,  "res_type": "unkown",   "res_type_no": 1},
    "DT": {"res_name_num": 33,  "res_type": "unkown",   "res_type_no": 1},

    "PST": {"res_name_num": 33,  "res_type": "unkown",   "res_type_no": 1},
    # RNA
    "A": {"res_name_num": 40,   "res_type": "unkown",   "res_type_no": 1},
    "C": {"res_name_num": 41,   "res_type": "unkown",   "res_type_no": 1},
    "G": {"res_name_num": 42,   "res_type": "unkown",   "res_type_no": 1},
    "U": {"res_name_num": 43,   "res_type": "unkown",   "res_type_no": 1}

    # need to add some sugars and such here as well
}

# Ordering is a mix between the AlphaFold ordering (for proteins) and the original spec
# for nucleic acids from 1992:
# https://cdn.rcsb.org/wwpdb/docs/documentation/file-format/PDB_format_1992.pdf
# rotation points for artificial 'wiggle' are: 5, 6, 12, 20, 25
# rotation point around the alpha carbon is: 2
atom_names = {
    # backbone atoms
    'N': 1,
    'CA': 2,  # rotation point
    'C': 3,
    'O': 4,

    # sidechain atoms
    'CB': 5,  # rotation point
    'CG': 6,  # rotation point
    'CG1': 7,
    'CG2': 8,
    'OG': 9,
    'OG1': 10,
    'SG': 11,
    'CD': 12,  # rotation point
    'CD1': 13,
    'CD2': 14,
    'ND1': 15,
    'ND2': 16,
    'OD1': 17,
    'OD2': 18,
    'SD': 19,
    'CE': 20,  # rotation point
    'CE1': 21,
    'CE2': 23,
    'CE3': 24,
    'NE': 25,  # rotation point
    'NE1': 26,
    'NE2': 27,
    'OE1': 28,
    'OE2': 29,
    'CH2': 30,
    'NH1': 31,
    'NH2': 32,
    'OH': 33,
    'CZ': 34,
    'CZ2': 35,
    'CZ3': 36,
    'NZ': 37,
    # terminus of a peptide chain when it ends in an oxygen, maybe move higher? (in the 'backbone')
    'OXT': 38,


    # DNA
    # currently works for RNA as well, but haven't optimised

    # phosphate
    "P": 50,  # connection to the previous ribose

    # These two atoms can sometimes have their names written different ways,
    # this covers both to ensure their names are assigned properly.
    "O1P": 51,
    "OP1": 51,

    "OP2": 52,
    "O2P": 52,
    # ribose
    "O5'": 53,
    "C5'": 54,
    "C4'": 55,  # ring
    "O4'": 56,  # ring
    "C3'": 57,  # ring
    "O3'": 58,  # connection to the next phosphate
    "C2'": 59,  # ring
    "O2'": 60,
    "C1'": 61,  # ring # connection to the base

    # connection point to the base
    "N1": 62,
    "N9": 63,
    "N3": 64,

    "C8": 65,
    "N7": 66,
    "C5": 67,
    "C6": 68,
    "N6": 69,
    # "N1" : 70
    "C2": 70,
    # "N3" : 71,
    "C4": 71,
    "O6": 72,
    "N2": 73,

    "N4": 74,
    "O2": 75,

    "O4": 76,
    "C7": 77  # another extra carbon?


    # unsure how to proceed past this point, as atom names are reused inside of
    # different bases but represent totally different locations like the N9 and N1 atoms
    # can both be the connecting carbon to the ribose, or a carbon much further into the
    # structure see page 29:
    # https://cdn.rcsb.org/wwpdb/docs/documentation/file-format/PDB_format_1992.pdf
}

# atom charges taken from AMBER force field source code
atom_charge = {
    # peptide charges
    'ALA': {'N': -0.4157,  'H': 0.2719,  'CA': 0.0337,  'HA': 0.0823,  'CB': -0.1825,  'HB1': 0.0603,  'HB2': 0.0603,  'HB3': 0.0603,  'C': 0.5973,  'O': -0.5679},
    'ARG': {'N': -0.3479,  'H': 0.2747,  'CA': -0.2637,  'HA': 0.156,  'CB': -0.0007,  'HB2': 0.0327,  'HB3': 0.0327,  'CG': 0.039,  'HG2': 0.0285,  'HG3': 0.0285,  'CD': 0.0486,  'HD2': 0.0687,  'HD3': 0.0687,  'NE': -0.5295,  'HE': 0.3456,  'CZ': 0.8076,  'NH1': -0.8627,  'HH11': 0.4478,  'HH12': 0.4478,  'NH2': -0.8627,  'HH21': 0.4478,  'HH22': 0.4478,  'C': 0.7341,  'O': -0.5894},
    'ASH': {'N': -0.4157,  'H': 0.2719,  'CA': 0.0341,  'HA': 0.0864,  'CB': -0.0316,  'HB2': 0.0488,  'HB3': 0.0488,  'CG': 0.6462,  'OD1': -0.5554,  'OD2': -0.6376,  'HD2': 0.4747,  'C': 0.5973,  'O': -0.5679},
    'ASN': {'N': -0.4157,  'H': 0.2719,  'CA': 0.0143,  'HA': 0.1048,  'CB': -0.2041,  'HB2': 0.0797,  'HB3': 0.0797,  'CG': 0.713,  'OD1': -0.5931,  'ND2': -0.9191,  'HD21': 0.4196,  'HD22': 0.4196,  'C': 0.5973,  'O': -0.5679},
    'ASP': {'N': -0.5163,  'H': 0.2936,  'CA': 0.0381,  'HA': 0.088,  'CB': -0.0303,  'HB2': -0.0122,  'HB3': -0.0122,  'CG': 0.7994,  'OD1': -0.8014,  'OD2': -0.8014,  'C': 0.5366,  'O': -0.5819},
    'CYM': {'N': -0.4157,  'H': 0.2719,  'CA': -0.0351,  'HA': 0.0508,  'CB': -0.2413,  'HB3': 0.1122,  'HB2': 0.1122,  'SG': -0.8844,  'C': 0.5973,  'O': -0.5679},
    'CYS': {'N': -0.4157,  'H': 0.2719,  'CA': 0.0213,  'HA': 0.1124,  'CB': -0.1231,  'HB2': 0.1112,  'HB3': 0.1112,  'SG': -0.3119,  'HG': 0.1933,  'C': 0.5973,  'O': -0.5679},
    'CYX': {'N': -0.4157,  'H': 0.2719,  'CA': 0.0429,  'HA': 0.0766,  'CB': -0.079,  'HB2': 0.091,  'HB3': 0.091,  'SG': -0.1081,  'C': 0.5973,  'O': -0.5679},
    'GLH': {'N': -0.4157,  'H': 0.2719,  'CA': 0.0145,  'HA': 0.0779,  'CB': -0.0071,  'HB2': 0.0256,  'HB3': 0.0256,  'CG': -0.0174,  'HG2': 0.043,  'HG3': 0.043,  'CD': 0.6801,  'OE1': -0.5838,  'OE2': -0.6511,  'HE2': 0.4641,  'C': 0.5973,  'O': -0.5679},
    'GLN': {'N': -0.4157,  'H': 0.2719,  'CA': -0.0031,  'HA': 0.085,  'CB': -0.0036,  'HB2': 0.0171,  'HB3': 0.0171,  'CG': -0.0645,  'HG2': 0.0352,  'HG3': 0.0352,  'CD': 0.6951,  'OE1': -0.6086,  'NE2': -0.9407,  'HE21': 0.4251,  'HE22': 0.4251,  'C': 0.5973,  'O': -0.5679},
    'GLU': {'N': -0.5163,  'H': 0.2936,  'CA': 0.0397,  'HA': 0.1105,  'CB': 0.056,  'HB2': -0.0173,  'HB3': -0.0173,  'CG': 0.0136,  'HG2': -0.0425,  'HG3': -0.0425,  'CD': 0.8054,  'OE1': -0.8188,  'OE2': -0.8188,  'C': 0.5366,  'O': -0.5819},
    'GLY': {'N': -0.4157,  'H': 0.2719,  'CA': -0.0252,  'HA2': 0.0698,  'HA3': 0.0698,  'C': 0.5973,  'O': -0.5679},
    'HID': {'N': -0.4157,  'H': 0.2719,  'CA': 0.0188,  'HA': 0.0881,  'CB': -0.0462,  'HB2': 0.0402,  'HB3': 0.0402,  'CG': -0.0266,  'ND1': -0.3811,  'HD1': 0.3649,  'CE1': 0.2057,  'HE1': 0.1392,  'NE2': -0.5727,  'CD2': 0.1292,  'HD2': 0.1147,  'C': 0.5973,  'O': -0.5679},
    'HIE': {'N': -0.4157,  'H': 0.2719,  'CA': -0.0581,  'HA': 0.136,  'CB': -0.0074,  'HB2': 0.0367,  'HB3': 0.0367,  'CG': 0.1868,  'ND1': -0.5432,  'CE1': 0.1635,  'HE1': 0.1435,  'NE2': -0.2795,  'HE2': 0.3339,  'CD2': -0.2207,  'HD2': 0.1862,  'C': 0.5973,  'O': -0.5679},
    'HIP': {'N': -0.3479,  'H': 0.2747,  'CA': -0.1354,  'HA': 0.1212,  'CB': -0.0414,  'HB2': 0.081,  'HB3': 0.081,  'CG': -0.0012,  'ND1': -0.1513,  'HD1': 0.3866,  'CE1': -0.017,  'HE1': 0.2681,  'NE2': -0.1718,  'HE2': 0.3911,  'CD2': -0.1141,  'HD2': 0.2317,  'C': 0.7341,  'O': -0.5894},
    'ILE': {'N': -0.4157,  'H': 0.2719,  'CA': -0.0597,  'HA': 0.0869,  'CB': 0.1303,  'HB': 0.0187,  'CG2': -0.3204,  'HG21': 0.0882,  'HG22': 0.0882,  'HG23': 0.0882,  'CG1': -0.043,  'HG12': 0.0236,  'HG13': 0.0236,  'CD1': -0.066,  'HD11': 0.0186,  'HD12': 0.0186,  'HD13': 0.0186,  'C': 0.5973,  'O': -0.5679},
    'LEU': {'N': -0.4157,  'H': 0.2719,  'CA': -0.0518,  'HA': 0.0922,  'CB': -0.1102,  'HB2': 0.0457,  'HB3': 0.0457,  'CG': 0.3531,  'HG': -0.0361,  'CD1': -0.4121,  'HD11': 0.1,  'HD12': 0.1,  'HD13': 0.1,  'CD2': -0.4121,  'HD21': 0.1,  'HD22': 0.1,  'HD23': 0.1,  'C': 0.5973,  'O': -0.5679},
    'LYN': {'N': -0.4157,  'H': 0.2719,  'CA': -0.07206,  'HA': 0.0994,  'CB': -0.04845,  'HB2': 0.034,  'HB3': 0.034,  'CG': 0.06612,  'HG2': 0.01041,  'HG3': 0.01041,  'CD': -0.03768,  'HD2': 0.01155,  'HD3': 0.01155,  'CE': 0.32604,  'HE2': -0.03358,  'HE3': -0.03358,  'NZ': -1.03581,  'HZ2': 0.38604,  'HZ3': 0.38604,  'C': 0.5973,  'O': -0.5679},
    'LYS': {'N': -0.3479,  'H': 0.2747,  'CA': -0.24,  'HA': 0.1426,  'CB': -0.0094,  'HB2': 0.0362,  'HB3': 0.0362,  'CG': 0.0187,  'HG2': 0.0103,  'HG3': 0.0103,  'CD': -0.0479,  'HD2': 0.0621,  'HD3': 0.0621,  'CE': -0.0143,  'HE2': 0.1135,  'HE3': 0.1135,  'NZ': -0.3854,  'HZ1': 0.34,  'HZ2': 0.34,  'HZ3': 0.34,  'C': 0.7341,  'O': -0.5894},
    'MET': {'N': -0.4157,  'H': 0.2719,  'CA': -0.0237,  'HA': 0.088,  'CB': 0.0342,  'HB2': 0.0241,  'HB3': 0.0241,  'CG': 0.0018,  'HG2': 0.044,  'HG3': 0.044,  'SD': -0.2737,  'CE': -0.0536,  'HE1': 0.0684,  'HE2': 0.0684,  'HE3': 0.0684,  'C': 0.5973,  'O': -0.5679},
    'PHE': {'N': -0.4157,  'H': 0.2719,  'CA': -0.0024,  'HA': 0.0978,  'CB': -0.0343,  'HB2': 0.0295,  'HB3': 0.0295,  'CG': 0.0118,  'CD1': -0.1256,  'HD1': 0.133,  'CE1': -0.1704,  'HE1': 0.143,  'CZ': -0.1072,  'HZ': 0.1297,  'CE2': -0.1704,  'HE2': 0.143,  'CD2': -0.1256,  'HD2': 0.133,  'C': 0.5973,  'O': -0.5679},
    'PRO': {'N': -0.2548,  'CD': 0.0192,  'HD2': 0.0391,  'HD3': 0.0391,  'CG': 0.0189,  'HG2': 0.0213,  'HG3': 0.0213,  'CB': -0.007,  'HB2': 0.0253,  'HB3': 0.0253,  'CA': -0.0266,  'HA': 0.0641,  'C': 0.5896,  'O': -0.5748},
    'SER': {'N': -0.4157,  'H': 0.2719,  'CA': -0.0249,  'HA': 0.0843,  'CB': 0.2117,  'HB2': 0.0352,  'HB3': 0.0352,  'OG': -0.6546,  'HG': 0.4275,  'C': 0.5973,  'O': -0.5679},
    'THR': {'N': -0.4157,  'H': 0.2719,  'CA': -0.0389,  'HA': 0.1007,  'CB': 0.3654,  'HB': 0.0043,  'CG2': -0.2438,  'HG21': 0.0642,  'HG22': 0.0642,  'HG23': 0.0642,  'OG1': -0.6761,  'HG1': 0.4102,  'C': 0.5973,  'O': -0.5679},
    'TRP': {'N': -0.4157,  'H': 0.2719,  'CA': -0.0275,  'HA': 0.1123,  'CB': -0.005,  'HB2': 0.0339,  'HB3': 0.0339,  'CG': -0.1415,  'CD1': -0.1638,  'HD1': 0.2062,  'NE1': -0.3418,  'HE1': 0.3412,  'CE2': 0.138,  'CZ2': -0.2601,  'HZ2': 0.1572,  'CH2': -0.1134,  'HH2': 0.1417,  'CZ3': -0.1972,  'HZ3': 0.1447,  'CE3': -0.2387,  'HE3': 0.17,  'CD2': 0.1243,  'C': 0.5973,  'O': -0.5679},
    'TYR': {'N': -0.4157,  'H': 0.2719,  'CA': -0.0014,  'HA': 0.0876,  'CB': -0.0152,  'HB2': 0.0295,  'HB3': 0.0295,  'CG': -0.0011,  'CD1': -0.1906,  'HD1': 0.1699,  'CE1': -0.2341,  'HE1': 0.1656,  'CZ': 0.3226,  'OH': -0.5579,  'HH': 0.3992,  'CE2': -0.2341,  'HE2': 0.1656,  'CD2': -0.1906,  'HD2': 0.1699,  'C': 0.5973,  'O': -0.5679},
    'VAL': {'N': -0.4157,  'H': 0.2719,  'CA': -0.0875,  'HA': 0.0969,  'CB': 0.2985,  'HB': -0.0297,  'CG1': -0.3192,  'HG11': 0.0791,  'HG12': 0.0791,  'HG13': 0.0791,  'CG2': -0.3192,  'HG21': 0.0791,  'HG22': 0.0791,  'HG23': 0.0791,  'C': 0.5973,  'O': -0.5679},

    # nucleic acid charges
    "DA": {"P": 1.1659,  "O1P": -0.7761,  "O2P": -0.7761,  "O5'": -0.4954,  "C5'": -0.0069,  "H5'1": 0.0754,  "H5'2": 0.0754,  "C4'": 0.1629,  "H4'": 0.1176,  "O4'": -0.3691,  "C1'": 0.0431,  "H1'": 0.1838,  "N9": -0.0268,  "C8": 0.1607,  "H8": 0.1877,  "N7": -0.6175,  "C5": 0.0725,  "C6": 0.6897,  "N6": -0.9123,  "H61": 0.4167,  "H62": 0.4167,  "N1": -0.7624,  "C2": 0.5716,  "H2": 0.0598,  "N3": -0.7417,  "C4": 0.38,  "C3'": 0.0713,  "H3'": 0.0985,  "C2'": -0.0854,  "H2'1": 0.0718,  "H2'2": 0.0718,  "O3'": -0.5232},
    "DA3": {"P": 1.1659,  "O1P": -0.7761,  "O2P": -0.7761,  "O5'": -0.4954,  "C5'": -0.0069,  "H5'1": 0.0754,  "H5'2": 0.0754,  "C4'": 0.1629,  "H4'": 0.1176,  "O4'": -0.3691,  "C1'": 0.0431,  "H1'": 0.1838,  "N9": -0.0268,  "C8": 0.1607,  "H8": 0.1877,  "N7": -0.6175,  "C5": 0.0725,  "C6": 0.6897,  "N6": -0.9123,  "H61": 0.4167,  "H62": 0.4167,  "N1": -0.7624,  "C2": 0.5716,  "H2": 0.0598,  "N3": -0.7417,  "C4": 0.38,  "C3'": 0.0713,  "H3'": 0.0985,  "C2'": -0.0854,  "H2'1": 0.0718,  "H2'2": 0.0718,  "O3'": -0.6549,  "H3T": 0.4396},
    "DA5": {"H5T": 0.4422,  "O5'": -0.6318,  "C5'": -0.0069,  "H5'1": 0.0754,  "H5'2": 0.0754,  "C4'": 0.1629,  "H4'": 0.1176,  "O4'": -0.3691,  "C1'": 0.0431,  "H1'": 0.1838,  "N9": -0.0268,  "C8": 0.1607,  "H8": 0.1877,  "N7": -0.6175,  "C5": 0.0725,  "C6": 0.6897,  "N6": -0.9123,  "H61": 0.4167,  "H62": 0.4167,  "N1": -0.7624,  "C2": 0.5716,  "H2": 0.0598,  "N3": -0.7417,  "C4": 0.38,  "C3'": 0.0713,  "H3'": 0.0985,  "C2'": -0.0854,  "H2'1": 0.0718,  "H2'2": 0.0718,  "O3'": -0.5232},
    "DAN": {"H5T": 0.4422,  "O5'": -0.6318,  "C5'": -0.0069,  "H5'1": 0.0754,  "H5'2": 0.0754,  "C4'": 0.1629,  "H4'": 0.1176,  "O4'": -0.3691,  "C1'": 0.0431,  "H1'": 0.1838,  "N9": -0.0268,  "C8": 0.1607,  "H8": 0.1877,  "N7": -0.6175,  "C5": 0.0725,  "C6": 0.6897,  "N6": -0.9123,  "H61": 0.4167,  "H62": 0.4167,  "N1": -0.7624,  "C2": 0.5716,  "H2": 0.0598,  "N3": -0.7417,  "C4": 0.38,  "C3'": 0.0713,  "H3'": 0.0985,  "C2'": -0.0854,  "H2'1": 0.0718,  "H2'2": 0.0718,  "O3'": -0.6549,  "H3T": 0.4396},
    "DC": {"P": 1.1659,  "O1P": -0.7761,  "O2P": -0.7761,  "O5'": -0.4954,  "C5'": -0.0069,  "H5'1": 0.0754,  "H5'2": 0.0754,  "C4'": 0.1629,  "H4'": 0.1176,  "O4'": -0.3691,  "C1'": -0.0116,  "H1'": 0.1963,  "N1": -0.0339,  "C6": -0.0183,  "H6": 0.2293,  "C5": -0.5222,  "H5": 0.1863,  "C4": 0.8439,  "N4": -0.9773,  "H41": 0.4314,  "H42": 0.4314,  "N3": -0.7748,  "C2": 0.7959,  "O2": -0.6548,  "C3'": 0.0713,  "H3'": 0.0985,  "C2'": -0.0854,  "H2'1": 0.0718,  "H2'2": 0.0718,  "O3'": -0.5232},
    "DC3": {"P": 1.1659,  "O1P": -0.7761,  "O2P": -0.7761,  "O5'": -0.4954,  "C5'": -0.0069,  "H5'1": 0.0754,  "H5'2": 0.0754,  "C4'": 0.1629,  "H4'": 0.1176,  "O4'": -0.3691,  "C1'": -0.0116,  "H1'": 0.1963,  "N1": -0.0339,  "C6": -0.0183,  "H6": 0.2293,  "C5": -0.5222,  "H5": 0.1863,  "C4": 0.8439,  "N4": -0.9773,  "H41": 0.4314,  "H42": 0.4314,  "N3": -0.7748,  "C2": 0.7959,  "O2": -0.6548,  "C3'": 0.0713,  "H3'": 0.0985,  "C2'": -0.0854,  "H2'1": 0.0718,  "H2'2": 0.0718,  "O3'": -0.6549,  "H3T": 0.4396},
    "DC5": {"H5T": 0.4422,  "O5'": -0.6318,  "C5'": -0.0069,  "H5'1": 0.0754,  "H5'2": 0.0754,  "C4'": 0.1629,  "H4'": 0.1176,  "O4'": -0.3691,  "C1'": -0.0116,  "H1'": 0.1963,  "N1": -0.0339,  "C6": -0.0183,  "H6": 0.2293,  "C5": -0.5222,  "H5": 0.1863,  "C4": 0.8439,  "N4": -0.9773,  "H41": 0.4314,  "H42": 0.4314,  "N3": -0.7748,  "C2": 0.7959,  "O2": -0.6548,  "C3'": 0.0713,  "H3'": 0.0985,  "C2'": -0.0854,  "H2'1": 0.0718,  "H2'2": 0.0718,  "O3'": -0.5232},
    "DCN": {"H5T": 0.4422,  "O5'": -0.6318,  "C5'": -0.0069,  "H5'1": 0.0754,  "H5'2": 0.0754,  "C4'": 0.1629,  "H4'": 0.1176,  "O4'": -0.3691,  "C1'": -0.0116,  "H1'": 0.1963,  "N1": -0.0339,  "C6": -0.0183,  "H6": 0.2293,  "C5": -0.5222,  "H5": 0.1863,  "C4": 0.8439,  "N4": -0.9773,  "H41": 0.4314,  "H42": 0.4314,  "N3": -0.7748,  "C2": 0.7959,  "O2": -0.6548,  "C3'": 0.0713,  "H3'": 0.0985,  "C2'": -0.0854,  "H2'1": 0.0718,  "H2'2": 0.0718,  "O3'": -0.6549,  "H3T": 0.4396},
    "DG": {"P": 1.1659,  "O1P": -0.7761,  "O2P": -0.7761,  "O5'": -0.4954,  "C5'": -0.0069,  "H5'1": 0.0754,  "H5'2": 0.0754,  "C4'": 0.1629,  "H4'": 0.1176,  "O4'": -0.3691,  "C1'": 0.0358,  "H1'": 0.1746,  "N9": 0.0577,  "C8": 0.0736,  "H8": 0.1997,  "N7": -0.5725,  "C5": 0.1991,  "C6": 0.4918,  "O6": -0.5699,  "N1": -0.5053,  "H1": 0.352,  "C2": 0.7432,  "N2": -0.923,  "H21": 0.4235,  "H22": 0.4235,  "N3": -0.6636,  "C4": 0.1814,  "C3'": 0.0713,  "H3'": 0.0985,  "C2'": -0.0854,  "H2'1": 0.0718,  "H2'2": 0.0718,  "O3'": -0.5232},
    "DG3": {"P": 1.1659,  "O1P": -0.7761,  "O2P": -0.7761,  "O5'": -0.4954,  "C5'": -0.0069,  "H5'1": 0.0754,  "H5'2": 0.0754,  "C4'": 0.1629,  "H4'": 0.1176,  "O4'": -0.3691,  "C1'": 0.0358,  "H1'": 0.1746,  "N9": 0.0577,  "C8": 0.0736,  "H8": 0.1997,  "N7": -0.5725,  "C5": 0.1991,  "C6": 0.4918,  "O6": -0.5699,  "N1": -0.5053,  "H1": 0.352,  "C2": 0.7432,  "N2": -0.923,  "H21": 0.4235,  "H22": 0.4235,  "N3": -0.6636,  "C4": 0.1814,  "C3'": 0.0713,  "H3'": 0.0985,  "C2'": -0.0854,  "H2'1": 0.0718,  "H2'2": 0.0718,  "O3'": -0.6549,  "H3T": 0.4396},
    "DG5": {"H5T": 0.4422,  "O5'": -0.6318,  "C5'": -0.0069,  "H5'1": 0.0754,  "H5'2": 0.0754,  "C4'": 0.1629,  "H4'": 0.1176,  "O4'": -0.3691,  "C1'": 0.0358,  "H1'": 0.1746,  "N9": 0.0577,  "C8": 0.0736,  "H8": 0.1997,  "N7": -0.5725,  "C5": 0.1991,  "C6": 0.4918,  "O6": -0.5699,  "N1": -0.5053,  "H1": 0.352,  "C2": 0.7432,  "N2": -0.923,  "H21": 0.4235,  "H22": 0.4235,  "N3": -0.6636,  "C4": 0.1814,  "C3'": 0.0713,  "H3'": 0.0985,  "C2'": -0.0854,  "H2'1": 0.0718,  "H2'2": 0.0718,  "O3'": -0.5232},
    "DGN": {"H5T": 0.4422,  "O5'": -0.6318,  "C5'": -0.0069,  "H5'1": 0.0754,  "H5'2": 0.0754,  "C4'": 0.1629,  "H4'": 0.1176,  "O4'": -0.3691,  "C1'": 0.0358,  "H1'": 0.1746,  "N9": 0.0577,  "C8": 0.0736,  "H8": 0.1997,  "N7": -0.5725,  "C5": 0.1991,  "C6": 0.4918,  "O6": -0.5699,  "N1": -0.5053,  "H1": 0.352,  "C2": 0.7432,  "N2": -0.923,  "H21": 0.4235,  "H22": 0.4235,  "N3": -0.6636,  "C4": 0.1814,  "C3'": 0.0713,  "H3'": 0.0985,  "C2'": -0.0854,  "H2'1": 0.0718,  "H2'2": 0.0718,  "O3'": -0.6549,  "H3T": 0.4396},
    "DT": {"P": 1.1659,  "O1P": -0.7761,  "O2P": -0.7761,  "O5'": -0.4954,  "C5'": -0.0069,  "H5'1": 0.0754,  "H5'2": 0.0754,  "C4'": 0.1629,  "H4'": 0.1176,  "O4'": -0.3691,  "C1'": 0.068,  "H1'": 0.1804,  "N1": -0.0239,  "C6": -0.2209,  "H6": 0.2607,  "C5": 0.0025,  "C7": -0.2269,  "H71": 0.077,  "H72": 0.077,  "H73": 0.077,  "C4": 0.5194,  "O4": -0.5563,  "N3": -0.434,  "H3": 0.342,  "C2": 0.5677,  "O2": -0.5881,  "C3'": 0.0713,  "H3'": 0.0985,  "C2'": -0.0854,  "H2'1": 0.0718,  "H2'2": 0.0718,  "O3'": -0.5232},
    "DT3": {"P": 1.1659,  "O1P": -0.7761,  "O2P": -0.7761,  "O5'": -0.4954,  "C5'": -0.0069,  "H5'1": 0.0754,  "H5'2": 0.0754,  "C4'": 0.1629,  "H4'": 0.1176,  "O4'": -0.3691,  "C1'": 0.068,  "H1'": 0.1804,  "N1": -0.0239,  "C6": -0.2209,  "H6": 0.2607,  "C5": 0.0025,  "C7": -0.2269,  "H71": 0.077,  "H72": 0.077,  "H73": 0.077,  "C4": 0.5194,  "O4": -0.5563,  "N3": -0.434,  "H3": 0.342,  "C2": 0.5677,  "O2": -0.5881,  "C3'": 0.0713,  "H3'": 0.0985,  "C2'": -0.0854,  "H2'1": 0.0718,  "H2'2": 0.0718,  "O3'": -0.6549,  "H3T": 0.4396},
    "DT5": {"H5T": 0.4422,  "O5'": -0.6318,  "C5'": -0.0069,  "H5'1": 0.0754,  "H5'2": 0.0754,  "C4'": 0.1629,  "H4'": 0.1176,  "O4'": -0.3691,  "C1'": 0.068,  "H1'": 0.1804,  "N1": -0.0239,  "C6": -0.2209,  "H6": 0.2607,  "C5": 0.0025,  "C7": -0.2269,  "H71": 0.077,  "H72": 0.077,  "H73": 0.077,  "C4": 0.5194,  "O4": -0.5563,  "N3": -0.434,  "H3": 0.342,  "C2": 0.5677,  "O2": -0.5881,  "C3'": 0.0713,  "H3'": 0.0985,  "C2'": -0.0854,  "H2'1": 0.0718,  "H2'2": 0.0718,  "O3'": -0.5232},
    "DTN": {"H5T": 0.4422,  "O5'": -0.6318,  "C5'": -0.0069,  "H5'1": 0.0754,  "H5'2": 0.0754,  "C4'": 0.1629,  "H4'": 0.1176,  "O4'": -0.3691,  "C1'": 0.068,  "H1'": 0.1804,  "N1": -0.0239,  "C6": -0.2209,  "H6": 0.2607,  "C5": 0.0025,  "C7": -0.2269,  "H71": 0.077,  "H72": 0.077,  "H73": 0.077,  "C4": 0.5194,  "O4": -0.5563,  "N3": -0.434,  "H3": 0.342,  "C2": 0.5677,  "O2": -0.5881,  "C3'": 0.0713,  "H3'": 0.0985,  "C2'": -0.0854,  "H2'1": 0.0718,  "H2'2": 0.0718,  "O3'": -0.6549,  "H3T": 0.4396},
    "RA": {"P": 1.1662,  "O1P": -0.776,  "O2P": -0.776,  "O5'": -0.4989,  "C5'": 0.0558,  "H5'1": 0.0679,  "H5'2": 0.0679,  "C4'": 0.1065,  "H4'": 0.1174,  "O4'": -0.3548,  "C1'": 0.0394,  "H1'": 0.2007,  "N9": -0.0251,  "C8": 0.2006,  "H8": 0.1553,  "N7": -0.6073,  "C5": 0.0515,  "C6": 0.7009,  "N6": -0.9019,  "H61": 0.4115,  "H62": 0.4115,  "N1": -0.7615,  "C2": 0.5875,  "H2": 0.0473,  "N3": -0.6997,  "C4": 0.3053,  "C3'": 0.2022,  "H3'": 0.0615,  "C2'": 0.067,  "H2'1": 0.0972,  "O2'": -0.6139,  "HO'2": 0.4186,  "O3'": -0.5246},
    "RA3": {"P": 1.1662,  "O1P": -0.776,  "O2P": -0.776,  "O5'": -0.4989,  "C5'": 0.0558,  "H5'1": 0.0679,  "H5'2": 0.0679,  "C4'": 0.1065,  "H4'": 0.1174,  "O4'": -0.3548,  "C1'": 0.0394,  "H1'": 0.2007,  "N9": -0.0251,  "C8": 0.2006,  "H8": 0.1553,  "N7": -0.6073,  "C5": 0.0515,  "C6": 0.7009,  "N6": -0.9019,  "H61": 0.4115,  "H62": 0.4115,  "N1": -0.7615,  "C2": 0.5875,  "H2": 0.0473,  "N3": -0.6997,  "C4": 0.3053,  "C3'": 0.2022,  "H3'": 0.0615,  "C2'": 0.067,  "H2'1": 0.0972,  "O2'": -0.6139,  "HO'2": 0.4186,  "O3'": -0.6541,  "H3T": 0.4376},
    "RA5": {"H5T": 0.4295,  "O5'": -0.6223,  "C5'": 0.0558,  "H5'1": 0.0679,  "H5'2": 0.0679,  "C4'": 0.1065,  "H4'": 0.1174,  "O4'": -0.3548,  "C1'": 0.0394,  "H1'": 0.2007,  "N9": -0.0251,  "C8": 0.2006,  "H8": 0.1553,  "N7": -0.6073,  "C5": 0.0515,  "C6": 0.7009,  "N6": -0.9019,  "H61": 0.4115,  "H62": 0.4115,  "N1": -0.7615,  "C2": 0.5875,  "H2": 0.0473,  "N3": -0.6997,  "C4": 0.3053,  "C3'": 0.2022,  "H3'": 0.0615,  "C2'": 0.067,  "H2'1": 0.0972,  "O2'": -0.6139,  "HO'2": 0.4186,  "O3'": -0.5246},
    "RAN": {"H5T": 0.4295,  "O5'": -0.6223,  "C5'": 0.0558,  "H5'1": 0.0679,  "H5'2": 0.0679,  "C4'": 0.1065,  "H4'": 0.1174,  "O4'": -0.3548,  "C1'": 0.0394,  "H1'": 0.2007,  "N9": -0.0251,  "C8": 0.2006,  "H8": 0.1553,  "N7": -0.6073,  "C5": 0.0515,  "C6": 0.7009,  "N6": -0.9019,  "H61": 0.4115,  "H62": 0.4115,  "N1": -0.7615,  "C2": 0.5875,  "H2": 0.0473,  "N3": -0.6997,  "C4": 0.3053,  "C3'": 0.2022,  "H3'": 0.0615,  "C2'": 0.067,  "H2'1": 0.0972,  "O2'": -0.6139,  "HO'2": 0.4186,  "O3'": -0.6541,  "H3T": 0.4376},
    "RC": {"P": 1.1662,  "O1P": -0.776,  "O2P": -0.776,  "O5'": -0.4989,  "C5'": 0.0558,  "H5'1": 0.0679,  "H5'2": 0.0679,  "C4'": 0.1065,  "H4'": 0.1174,  "O4'": -0.3548,  "C1'": 0.0066,  "H1'": 0.2029,  "N1": -0.0484,  "C6": 0.0053,  "H6": 0.1958,  "C5": -0.5215,  "H5": 0.1928,  "C4": 0.8185,  "N4": -0.953,  "H41": 0.4234,  "H42": 0.4234,  "N3": -0.7584,  "C2": 0.7538,  "O2": -0.6252,  "C3'": 0.2022,  "H3'": 0.0615,  "C2'": 0.067,  "H2'1": 0.0972,  "O2'": -0.6139,  "HO'2": 0.4186,  "O3'": -0.5246},
    "RC3": {"P": 1.1662,  "O1P": -0.776,  "O2P": -0.776,  "O5'": -0.4989,  "C5'": 0.0558,  "H5'1": 0.0679,  "H5'2": 0.0679,  "C4'": 0.1065,  "H4'": 0.1174,  "O4'": -0.3548,  "C1'": 0.0066,  "H1'": 0.2029,  "N1": -0.0484,  "C6": 0.0053,  "H6": 0.1958,  "C5": -0.5215,  "H5": 0.1928,  "C4": 0.8185,  "N4": -0.953,  "H41": 0.4234,  "H42": 0.4234,  "N3": -0.7584,  "C2": 0.7538,  "O2": -0.6252,  "C3'": 0.2022,  "H3'": 0.0615,  "C2'": 0.067,  "H2'1": 0.0972,  "O2'": -0.6139,  "HO'2": 0.4186,  "O3'": -0.6541,  "H3T": 0.4376},
    "RC5": {"H5T": 0.4295,  "O5'": -0.6223,  "C5'": 0.0558,  "H5'1": 0.0679,  "H5'2": 0.0679,  "C4'": 0.1065,  "H4'": 0.1174,  "O4'": -0.3548,  "C1'": 0.0066,  "H1'": 0.2029,  "N1": -0.0484,  "C6": 0.0053,  "H6": 0.1958,  "C5": -0.5215,  "H5": 0.1928,  "C4": 0.8185,  "N4": -0.953,  "H41": 0.4234,  "H42": 0.4234,  "N3": -0.7584,  "C2": 0.7538,  "O2": -0.6252,  "C3'": 0.2022,  "H3'": 0.0615,  "C2'": 0.067,  "H2'1": 0.0972,  "O2'": -0.6139,  "HO'2": 0.4186,  "O3'": -0.5246},
    "RCN": {"H5T": 0.4295,  "O5'": -0.6223,  "C5'": 0.0558,  "H5'1": 0.0679,  "H5'2": 0.0679,  "C4'": 0.1065,  "H4'": 0.1174,  "O4'": -0.3548,  "C1'": 0.0066,  "H1'": 0.2029,  "N1": -0.0484,  "C6": 0.0053,  "H6": 0.1958,  "C5": -0.5215,  "H5": 0.1928,  "C4": 0.8185,  "N4": -0.953,  "H41": 0.4234,  "H42": 0.4234,  "N3": -0.7584,  "C2": 0.7538,  "O2": -0.6252,  "C3'": 0.2022,  "H3'": 0.0615,  "C2'": 0.067,  "H2'1": 0.0972,  "O2'": -0.6139,  "HO'2": 0.4186,  "O3'": -0.6541,  "H3T": 0.4376},
    "RG": {"P": 1.1662,  "O1P": -0.776,  "O2P": -0.776,  "O5'": -0.4989,  "C5'": 0.0558,  "H5'1": 0.0679,  "H5'2": 0.0679,  "C4'": 0.1065,  "H4'": 0.1174,  "O4'": -0.3548,  "C1'": 0.0191,  "H1'": 0.2006,  "N9": 0.0492,  "C8": 0.1374,  "H8": 0.164,  "N7": -0.5709,  "C5": 0.1744,  "C6": 0.477,  "O6": -0.5597,  "N1": -0.4787,  "H1": 0.3424,  "C2": 0.7657,  "N2": -0.9672,  "H21": 0.4364,  "H22": 0.4364,  "N3": -0.6323,  "C4": 0.1222,  "C3'": 0.2022,  "H3'": 0.0615,  "C2'": 0.067,  "H2'1": 0.0972,  "O2'": -0.6139,  "HO'2": 0.4186,  "O3'": -0.5246},
    "RG3": {"P": 1.1662,  "O1P": -0.776,  "O2P": -0.776,  "O5'": -0.4989,  "C5'": 0.0558,  "H5'1": 0.0679,  "H5'2": 0.0679,  "C4'": 0.1065,  "H4'": 0.1174,  "O4'": -0.3548,  "C1'": 0.0191,  "H1'": 0.2006,  "N9": 0.0492,  "C8": 0.1374,  "H8": 0.164,  "N7": -0.5709,  "C5": 0.1744,  "C6": 0.477,  "O6": -0.5597,  "N1": -0.4787,  "H1": 0.3424,  "C2": 0.7657,  "N2": -0.9672,  "H21": 0.4364,  "H22": 0.4364,  "N3": -0.6323,  "C4": 0.1222,  "C3'": 0.2022,  "H3'": 0.0615,  "C2'": 0.067,  "H2'1": 0.0972,  "O2'": -0.6139,  "HO'2": 0.4186,  "O3'": -0.6541,  "H3T": 0.4376},
    "RG5": {"H5T": 0.4295,  "O5'": -0.6223,  "C5'": 0.0558,  "H5'1": 0.0679,  "H5'2": 0.0679,  "C4'": 0.1065,  "H4'": 0.1174,  "O4'": -0.3548,  "C1'": 0.0191,  "H1'": 0.2006,  "N9": 0.0492,  "C8": 0.1374,  "H8": 0.164,  "N7": -0.5709,  "C5": 0.1744,  "C6": 0.477,  "O6": -0.5597,  "N1": -0.4787,  "H1": 0.3424,  "C2": 0.7657,  "N2": -0.9672,  "H21": 0.4364,  "H22": 0.4364,  "N3": -0.6323,  "C4": 0.1222,  "C3'": 0.2022,  "H3'": 0.0615,  "C2'": 0.067,  "H2'1": 0.0972,  "O2'": -0.6139,  "HO'2": 0.4186,  "O3'": -0.5246},
    "RGN": {"H5T": 0.4295,  "O5'": -0.6223,  "C5'": 0.0558,  "H5'1": 0.0679,  "H5'2": 0.0679,  "C4'": 0.1065,  "H4'": 0.1174,  "O4'": -0.3548,  "C1'": 0.0191,  "H1'": 0.2006,  "N9": 0.0492,  "C8": 0.1374,  "H8": 0.164,  "N7": -0.5709,  "C5": 0.1744,  "C6": 0.477,  "O6": -0.5597,  "N1": -0.4787,  "H1": 0.3424,  "C2": 0.7657,  "N2": -0.9672,  "H21": 0.4364,  "H22": 0.4364,  "N3": -0.6323,  "C4": 0.1222,  "C3'": 0.2022,  "H3'": 0.0615,  "C2'": 0.067,  "H2'1": 0.0972,  "O2'": -0.6139,  "HO'2": 0.4186,  "O3'": -0.6541,  "H3T": 0.4376},
    "RU": {"P": 1.1662,  "O1P": -0.776,  "O2P": -0.776,  "O5'": -0.4989,  "C5'": 0.0558,  "H5'1": 0.0679,  "H5'2": 0.0679,  "C4'": 0.1065,  "H4'": 0.1174,  "O4'": -0.3548,  "C1'": 0.0674,  "H1'": 0.1824,  "N1": 0.0418,  "C6": -0.1126,  "H6": 0.2188,  "C5": -0.3635,  "H5": 0.1811,  "C4": 0.5952,  "O4": -0.5761,  "N3": -0.3549,  "H3": 0.3154,  "C2": 0.4687,  "O2": -0.5477,  "C3'": 0.2022,  "H3'": 0.0615,  "C2'": 0.067,  "H2'1": 0.0972,  "O2'": -0.6139,  "HO'2": 0.4186,  "O3'": -0.5246},
    "RU3": {"P": 1.1662,  "O1P": -0.776,  "O2P": -0.776,  "O5'": -0.4989,  "C5'": 0.0558,  "H5'1": 0.0679,  "H5'2": 0.0679,  "C4'": 0.1065,  "H4'": 0.1174,  "O4'": -0.3548,  "C1'": 0.0674,  "H1'": 0.1824,  "N1": 0.0418,  "C6": -0.1126,  "H6": 0.2188,  "C5": -0.3635,  "H5": 0.1811,  "C4": 0.5952,  "O4": -0.5761,  "N3": -0.3549,  "H3": 0.3154,  "C2": 0.4687,  "O2": -0.5477,  "C3'": 0.2022,  "H3'": 0.0615,  "C2'": 0.067,  "H2'1": 0.0972,  "O2'": -0.6139,  "HO'2": 0.4186,  "O3'": -0.6541,  "H3T": 0.4376},
    "RU5": {"H5T": 0.4295,  "O5'": -0.6223,  "C5'": 0.0558,  "H5'1": 0.0679,  "H5'2": 0.0679,  "C4'": 0.1065,  "H4'": 0.1174,  "O4'": -0.3548,  "C1'": 0.0674,  "H1'": 0.1824,  "N1": 0.0418,  "C6": -0.1126,  "H6": 0.2188,  "C5": -0.3635,  "H5": 0.1811,  "C4": 0.5952,  "O4": -0.5761,  "N3": -0.3549,  "H3": 0.3154,  "C2": 0.4687,  "O2": -0.5477,  "C3'": 0.2022,  "H3'": 0.0615,  "C2'": 0.067,  "H2'1": 0.0972,  "O2'": -0.6139,  "HO'2": 0.4186,  "O3'": -0.5246},
    "RUN": {"H5T": 0.4295,  "O5'": -0.6223,  "C5'": 0.0558,  "H5'1": 0.0679,  "H5'2": 0.0679,  "C4'": 0.1065,  "H4'": 0.1174,  "O4'": -0.3548,  "C1'": 0.0674,  "H1'": 0.1824,  "N1": 0.0418,  "C6": -0.1126,  "H6": 0.2188,  "C5": -0.3635,  "H5": 0.1811,  "C4": 0.5952,  "O4": -0.5761,  "N3": -0.3549,  "H3": 0.3154,  "C2": 0.4687,  "O2": -0.5477,  "C3'": 0.2022,  "H3'": 0.0615,  "C2'": 0.067,  "H2'1": 0.0972,  "O2'": -0.6139,  "HO'2": 0.4186,  "O3'": -0.6541,  "H3T": 0.4376}
}


lipophobicity = {
    # standard amino acids
    'ALA': {'C': -0.61, 'CA': 0.02, 'CB': 0.62, 'O': -0.58, 'N': -0.49, 'H': -0.5, 'HA': -0.25, 'HB1': 0.0, 'HB2': 0.0, 'HB3': 0.0, 'OXT': 0.49},
    'ARG': {'C': -0.61, 'CA': 0.02, 'CB': 0.45, 'CD':  0.45, 'CG': 0.45, 'CZ': -0.61, 'N': -0.49, 'NE': -0.49, 'NH1': -0.14, 'NH2': -0.69, 'O': -0.58, 'H': -0.5, 'HA': -0.25, 'HB2': 0.0, 'HB3': 0.0, 'HG2': 0.0, 'HG3': 0.0, 'HD2': -0.25, 'HD3': -0.25, 'HE': -0.5, 'HH11': -0.5, 'HH12': -0.5, 'HH21': -0.5, 'HH22': -0.5, '1HH1': -0.5, '2HH1': -0.5, '1HH2': -0.5, '2HH2': -0.5, 'OXT': 0.49},
    'ASN': {'C': -0.61, 'CA': 0.02, 'CB': 0.02, 'CG': -0.61, 'N': -0.49, 'ND2': -0.14, 'O': -0.58, 'OD1': -0.58, 'H': -0.5, 'HA': -0.25, 'HB2': 0.0, 'HB3': 0.0, 'HD21': -0.5, 'HD22': -0.5, '1HD2': -0.5, '2HD2': -0.5, 'OXT': 0.49},
    'ASP': {'C': -0.61, 'CA': 0.02, 'CB': 0.45, 'CG': -0.61, 'N': -0.49, 'O': -0.58, 'OD1': -0.58, 'OD2': 0.49, 'H': -0.5, 'HA': -0.25, 'HB2': 0.0, 'HB3': 0.0, 'OXT': 0.49},
    'CYS': {'C': -0.61, 'CA': 0.02, 'CB': 0.45, 'N': -0.49, 'O': -0.58, 'SG': 0.29, 'H': -0.5, 'HA': -0.25, 'HB2': 0.0, 'HB3': 0.0, 'OXT': 0.49},
    'GLN': {'C': -0.61, 'CA': 0.02, 'CB': 0.45, 'CD': -0.54, 'CG': 0.45, 'N': -0.49, 'NE2': -0.14, 'O': -0.58, 'OE1': -0.58, 'H': -0.5, 'HA': -0.25, 'HB2': 0.0, 'HB3': 0.0, 'HG2': 0.0, 'HG3': 0.0, 'HE21': -0.5, 'HE22': -0.5, '1HE2': -0.5, '2HE2': -0.5, 'OXT': 0.49},
    'GLU': {'C': -0.61, 'CA': 0.02, 'CB': 0.45, 'CD': -0.54, 'CG': 0.45, 'N': -0.49, 'O': -0.58, 'OE1': -0.58, 'OE2': 0.49, 'H': -0.5, 'HA': -0.25, 'HB2': 0.0, 'HB3': 0.0, 'HG2': 0.0, 'HG3': 0.0, 'OXT': 0.49},
    'GLY': {'C': -0.61, 'CA': 0.45, 'O': -0.58, 'N': -0.57, 'H': -0.5, 'HA': -0.25, 'HA2': 0.0, 'HA3': 0.0, 'OXT': 0.49},
    'HIS': {'C': -0.61, 'CA': 0.02, 'CB': 0.45, 'CD2': 0.31, 'CE1': 0.31, 'CG': 0.1, 'N': -0.49, 'ND1': 0.08, 'NE2': -1.14, 'O': -0.58, 'H': -0.5, 'HA': -0.25, 'HB2': 0.0, 'HB3': 0.0, 'HD1': -0.5, 'HD2': -0.25, 'HE1': -0.25, 'OXT': 0.49},
    'ILE': {'C': -0.61, 'CA': 0.02, 'CB': 0.02, 'CD':  0.63, 'CD1': 0.63, 'CG1': 0.45, 'CG2': 0.63, 'N': -0.49, 'O': -0.58, 'H': -0.5, 'HA': -0.25, 'HB': 0.0, 'HG12': 0.0, 'HG13': 0.0, 'HG21': 0.0, 'HG22': 0.0, 'HG23': 0.0, 'HD11': 0.0, 'HD12': 0.0, 'HD13': 0.0, '2HG1': 0.0, '3HG1': 0.0, '1HG2': 0.0, '2HG2': 0.0, '3HG2': 0.0, '1HD1': 0.0, '2HD1': 0.0, '3HD1': 0.0, 'OXT': 0.49},
    'LEU': {'C': -0.61, 'CA': 0.02, 'CB': 0.45, 'CD1': 0.63, 'CD2': 0.63, 'CG': 0.02, 'N': -0.49, 'O': -0.58, 'H': -0.5, 'HA': -0.25, 'HB2': 0.0, 'HB3': 0.0, 'HG': 0.0, 'HD11': 0.0, 'HD12': 0.0, 'HD13': 0.0, 'HD21': 0.0, 'HD22': 0.0, 'HD23': 0.0, '1HD1': 0.0, '2HD1': 0.0, '3HD1': 0.0, '1HD2': 0.0, '2HD2': 0.0, '3HD2': 0.0, 'OXT': 0.49},
    'LYS': {'C': -0.61, 'CA': 0.02, 'CB': 0.45, 'CD':  0.45, 'CE': 0.45, 'CG': 0.45, 'N': -0.49, 'NZ': -1.07, 'O': -0.58, 'H': -0.5, 'HA': -0.25, 'HB2': 0.0, 'HB3': 0.0, 'HG2': 0.0, 'HG3': 0.0, 'HD2': 0.0, 'HD3': 0.0, 'HE2': -0.2, 'HE3': -0.2, 'HZ1': -0.5, 'HZ2': -0.5, 'HZ3': -0.5, 'OXT': 0.49, },
    'MET': {'C': -0.61, 'CA': 0.02, 'CB': 0.45, 'CE':  0.63, 'CG': 0.45, 'N': -0.49, 'O': -0.58, 'SD': -0.30, 'H': -0.5, 'HA': -0.25, 'HB2': 0.0, 'HB3': 0.0, 'HG2': 0.0, 'HG3': 0.0, 'HE1': 0.0, 'HE2': 0.0, 'HE3': -0.5, 'OXT': 0.49, },
    'PHE': {'C': -0.61, 'CA': 0.02, 'CB': 0.45, 'CD1': 0.31, 'CD2': 0.31, 'CE1': 0.31, 'CE2': 0.31, 'CG': 0.1, 'CZ': 0.31, 'N': -0.49, 'O': -0.58, 'H': -0.5, 'HA': -0.25, 'HB2': 0.0, 'HB3': 0.0, 'HD1': 0.0, 'HD2': 0.0, 'HE1': 0.0, 'HE2': 0.0, 'HZ': 0.0, 'OXT': 0.49},
    'PRO': {'C': -0.61, 'CA': 0.02, 'CB': 0.45, 'CD':  0.45, 'CG': 0.45, 'N': -0.92, 'O': -0.58, 'HA': -0.25, 'HB2': 0.0, 'HB3': 0.0, 'HG2': 0.0, 'HG3': 0.0, 'HD2': -0.2, 'HD3': -0.2, 'OXT': 0.49, },
    'SER': {'C': -0.61, 'CA': 0.02, 'CB': 0.45, 'N': -0.49, 'O': -0.58, 'OG': -0.99, 'H': -0.5, 'HA': -0.25, 'HB2': 0.0, 'HB3': 0.0, 'HG': 0.0, 'OXT': 0.49, },
    'THR': {'C': -0.61, 'CA': 0.02, 'CB': 0.02, 'CG2': 0.62, 'N': -0.49, 'O': -0.58, 'OG1': -0.9, 'H': -0.5, 'HA': -0.25, 'HB': 0.0, 'HG1': 0.0, 'HG21': 0.0, 'HG22': 0.0, 'HG23': 0.0, '1HG2': 0.0, '2HG2': 0.0, '3HG2': 0.0, 'OXT': 0.49, },
    'TRP': {'C': -0.61, 'CA': 0.02, 'CB': 0.45, 'CD1': 0.31, 'CD2': 0.25, 'CE2': 0.25, 'CE3': 0.31, 'CG': 0.1, 'CH2': 0.31, 'CZ2': 0.31, 'CZ3': 0.31, 'N': -0.49, 'NE1': 0.08, 'O': -0.58, 'H': -0.5, 'HA': -0.25, 'HB2': 0.0, 'HB3': 0.0, 'HE1': -0.5, 'HD1': -0.2, 'HE3': 0.0, 'HZ2': 0.0, 'HZ3': 0.0, 'HH2': 0.0, 'OXT': 0.49, },
    'TYR': {'C': -0.61, 'CA': 0.02, 'CB': 0.45, 'CD1': 0.31, 'CD2': 0.31, 'CE1': 0.31, 'CE2': 0.31, 'CG': 0.1, 'CZ': 0.1, 'N': -0.49, 'O': -0.58, 'OH': -0.17, 'H': -0.5, 'HA': -0.25, 'HB2': 0.0, 'HB3': 0.0, 'HD1': 0.0, 'HD2': 0.0, 'HE1': 0.0, 'HE2': 0.0, 'HH': 0.0, 'OXT': 0.49, },
    'VAL': {'C': -0.61, 'CA': 0.02, 'CB': 0.02, 'CG1': 0.62, 'CG2': 0.62, 'N': -0.49, 'O': -0.58, 'H': -0.5, 'HA': -0.25, 'HB': 0.0, 'HG11': 0.0, 'HG12': 0.0, 'HG13': 0.0, 'HG21': 0.0, 'HG22': 0.0, 'HG23': 0.0, '1HG1': 0.0, '2HG1': 0.0, '3HG1': 0.0, '1HG2': 0.0, '2HG2': 0.0, '3HG2': 0.0, 'OXT': 0.49, },

    # other potential residues
    'CA': {'CA': -1.0},
    'NAG': {'C1': 0.02, 'C2': 0.02, 'C3': 0.02, 'C4': 0.02, 'C5': 0.02, 'C6': 0.31, 'C7': -0.61, 'C8': 0.62, 'O1': -0.92, 'O2': -0.92, 'O3': -0.92, 'O4': -0.92, 'O5': -1.14, 'O6': -0.99, 'O7': -0.58, 'N2': -0.49, 'H2': -0.25, 'HN2': -0.5, },
    'NDG': {'C1': 0.02, 'C2': 0.02, 'C3': 0.02, 'C4': 0.02, 'C5': 0.02, 'C6': 0.031, 'C7': -0.61, 'C8': 0.62, 'O1L': -0.9, 'O3': -0.92, 'O4': -0.92, 'O': -1.14, 'O6': -0.99, 'O7': -0.58, 'N2': -0.29, },
    'BMA': {'C1': 0.02, 'C2': 0.02, 'C3': 0.02, 'C4': 0.02, 'C5': 0.02, 'C6': 0.31, 'O1': -0.92, 'O2': -0.92, 'O3': -0.92, 'O4': -0.92, 'O5': -1.14, 'O6': -0.58, },
    'MAN': {'C1': 0.02, 'C2': 0.02, 'C3': 0.02, 'C4': 0.02, 'C5': 0.02, 'C6': 0.31, 'O1': -0.92, 'O2': -0.92, 'O3': -0.92, 'O4': -0.92, 'O5': -1.14, 'O6': -0.58, },
    'GAL': {'C1': 0.02, 'C2': 0.02, 'C3': 0.02, 'C4': 0.02, 'C5': 0.02, 'C6': 0.31, 'O1': -0.92, 'O2': -0.92, 'O3': -0.92, 'O4': -0.92, 'O5': -1.14, 'O6': -0.58, },
    'NAN': {'C1': -0.61, 'C2': 0.02, 'C3': 0.62, 'C4': 0.02, 'C5': 0.02, 'C6': 0.02, 'C7': 0.02, 'C8': 0.02, 'C9': 0.31, 'C10': -0.6, 'C11': 0.62, 'O1A': -0.2, 'O1B': -0.4, 'O2': -0.92, 'O4': -0.92, 'O6': -1.14, 'O7': -0.92, 'O8': -0.92, 'O9': -0.7, 'O10': -0.2, 'N5': -0.49, 'NH5': -0.5, },
    'DG': {'P': -0.94, 'O1P': -0.7, 'O2P': -0.22, "O5'": -0.5, "C5'": 0.45, "C4'": 0.02, "O4'": -1.14, "C1'": 0.02, "C2'": 0.45, "C3'": 0.02, "O3'": -0.92, 'N9': -1.66, 'C8': 0.31, 'N7': -0.55, 'C5': 0.25, 'C6': 0.1, 'O6': -0.58, 'N1': -0.49, 'C2': 0.1, 'N2': -0.6, 'N3': -0.07, 'C4': -0.25, },
    'DA': {'P': -0.94, 'O1P': -0.7, 'O2P': -0.22, "O5'": -0.5, "C5'": 0.45, "C4'": 0.02, "O4'": -1.14, "C1'": 0.02, "C2'": 0.45, "C3'": 0.02, "O3'": -0.92, 'N9': -1.66, 'C8': 0.31, 'N7': -0.55, 'C5': 0.25, 'C6': 0.1, 'N6': -0.6, 'N1': -0.49, 'C2': 0.31, 'N2': -0.6, 'N3': -0.07, 'C4': -0.25, },
    'DC': {'P': -0.94, 'O1P': -0.7, 'O2P': -0.22, "O5'": -0.5, "C5'": 0.45, "C4'": 0.02, "O4'": -1.14, "C1'": 0.02, "C2'": 0.45, "C3'": 0.02, "O3'": -0.92, 'N1': -1.66, 'C2': 0.1, 'O2': -0.58, 'N3': -0.29, 'C4': 0.1, 'N4': -0.6, 'C5': 0.31, 'C6': 0.31},
    'DT': {'P': -0.94, 'O1P': -0.7, 'O2P': -0.22, "O5'": -0.5, "C5'": 0.45, "C4'": 0.02, "O4'": -1.14, "C1'": 0.02, "C2'": 0.45, "C3'": 0.02, "O3'": -0.92, 'N1': -1.66, 'C2': 0.1, 'O2': -0.58, 'N3': 0.16, 'C4': 0.25, 'O4': -0.58, 'C5': 0.1, 'C6': 0.31, 'C7': 0.45},
    'G': {'P': -0.94, 'O1P': -0.7, 'O2P': -0.22, "O5'": -0.5, "C5'": 0.45, "C4'": 0.02, "O4'": -1.14, "C1'": 0.02, "C2'": 0.02, "O2'": -0.92, "C3'": 0.02, "O3'": -0.92, 'N9': -1.66, 'C8': 0.31, 'N7': -0.55, 'C5': 0.25, 'C6': 0.1, 'O6': -0.58, 'N1': -0.49, 'C2': 0.1, 'N2': -0.6, 'N3': -0.07, 'C4': -0.25},
    'A': {'P': -0.94, 'O1P': -0.7, 'O2P': -0.22, "O5'": -0.5, "C5'": 0.45, "C4'": 0.02, "O4'": -1.14, "C1'": 0.02, "C2'": 0.02, "O2'": -0.92, "C3'": 0.02, "O3'": -0.92, 'N9': -1.66, 'C8': 0.31, 'N7': -0.55, 'C5': 0.25, 'C6': 0.1, 'N6': -0.6, 'N1': -0.49, 'C2': 0.31, 'N2': -0.6, 'N3': -0.07, 'C4': -0.25},
    'C': {'P': -0.94, 'O1P': -0.7, 'O2P': -0.22, "O5'": -0.5, "C5'": 0.45, "C4'": 0.02, "O4'": -1.14, "C1'": 0.02, "C2'": 0.02, "O2'": -0.92, "C3'": 0.02, "O3'": -0.92, 'N1': -1.66, 'C2': 0.1, 'O2': -0.58, 'N3': -0.29, 'C4': 0.1, 'N4': -0.6, 'C5': 0.31, 'C6': 0.31},
    'U': {'P': -0.94, 'O1P': -0.7, 'O2P': -0.22, "O5'": -0.5, "C5'": 0.45, "C4'": 0.02, "O4'": -1.14, "C1'": 0.02, "C2'": 0.02, "O2'": -0.92, "C3'": 0.02, "O3'": -0.92, 'N1': -1.66, 'C2': 0.1, 'O2': -0.58, 'N3': 0.16, 'C4': 0.25, 'O4': -0.58, 'C5': 0.1, 'C6': 0.31},
}

# taken from biotite code: https://www.biotite-python.org/examples/gallery/structure/glycan_visualization.html
# originally adapted from "Mol*" Software
# The dictionary maps residue names of saccharides to their common names
SACCHARIDE_NAMES = {
    res_name: common_name for common_name, res_names in [
        ("Glc", ["GLC", "BGC", "Z8T", "TRE", "MLR"]),
        ("Man", ["MAN", "BMA"]),
        ("Gal", ["GLA", "GAL", "GZL", "GXL", "GIV"]),
        ("Gul", ["4GL", "GL0", "GUP", "Z8H"]),
        ("Alt", ["Z6H", "3MK", "SHD"]),
        ("All", ["AFD", "ALL", "WOO", "Z2D"]),
        ("Tal", ["ZEE", "A5C"]),
        ("Ido", ["ZCD", "Z0F", "4N2"]),
        ("GlcNAc", ["NDG", "NAG", "NGZ"]),
        ("ManNAc", ["BM3", "BM7"]),
        ("GalNAc", ["A2G", "NGA", "YYQ"]),
        ("GulNAc", ["LXB"]),
        ("AllNAc", ["NAA"]),
        ("IdoNAc", ["LXZ"]),
        ("GlcN", ["PA1", "GCS"]),
        ("ManN", ["95Z"]),
        ("GalN", ["X6X", "1GN"]),
        ("GlcA", ["GCU", "BDP"]),
        ("ManA", ["MAV", "BEM"]),
        ("GalA", ["ADA", "GTR", "GTK"]),
        ("GulA", ["LGU"]),
        ("TalA", ["X1X", "X0X"]),
        ("IdoA", ["IDR"]),
        ("Qui", ["G6D", "YYK"]),
        ("Rha", ["RAM", "RM4", "XXR"]),
        ("6dGul", ["66O"]),
        ("Fuc", ["FUC", "FUL", "FCA", "FCB"]),
        ("QuiNAc", ["Z9W"]),
        ("FucNAc", ["49T"]),
        ("Oli", ["DDA", "RAE", "Z5J"]),
        ("Tyv", ["TYV"]),
        ("Abe", ["ABE"]),
        ("Par", ["PZU"]),
        ("Dig", ["Z3U"]),
        ("Ara", ["64K", "ARA", "ARB", "AHR", "FUB", "BXY", "BXX"]),
        ("Lyx", ["LDY", "Z4W"]),
        ("Xyl", ["XYS", "XYP", "XYZ", "HSY", "LXC"]),
        ("Rib", ["YYM", "RIP", "RIB", "BDR", "0MK", "Z6J", "32O"]),
        ("Kdn", ["KDM", "KDN"]),
        ("Neu5Ac", ["SIA", "SLB"]),
        ("Neu5Gc", ["NGC", "NGE"]),
        ("LDManHep", ["GMH"]),
        ("Kdo", ["KDO"]),
        ("DDManHep", ["289"]),
        ("MurNAc", ["MUB", "AMU"]),
        ("Mur", ["1S4", "MUR"]),
        ("Api", ["XXM"]),
        ("Fru", ["BDF", "Z9N", "FRU", "LFR"]),
        ("Tag", ["T6T"]),
        ("Sor", ["SOE"]),
        ("Psi", ["PSV", "SF6", "SF9"]),
    ]
    for res_name in res_names
}

# currently not useing this, but potential for colouring / default colour glycans
# or maybe also adding simplified representations of the glycans through GN
# currently just data storage for potential future projects
SACCHARIDE_REPRESENTATION = {
    "Glc": ("o", "royalblue"),
    "Man": ("o", "forestgreen"),
    "Gal": ("o", "gold"),
    "Gul": ("o", "darkorange"),
    "Alt": ("o", "pink"),
    "All": ("o", "purple"),
    "Tal": ("o", "lightsteelblue"),
    "Ido": ("o", "chocolate"),

    "GlcNAc": ("s", "royalblue"),
    "ManNAc": ("s", "forestgreen"),
    "GalNAc": ("s", "gold"),
    "GulNAc": ("s", "darkorange"),
    "AllNAc": ("s", "purple"),
    "IdoNAc": ("s", "chocolate"),

    "GlcN": ("1", "royalblue"),
    "ManN": ("1", "forestgreen"),
    "GalN": ("1", "gold"),

    "GlcA": ("v", "royalblue"),
    "ManA": ("v", "forestgreen"),
    "GalA": ("v", "gold"),
    "GulA": ("v", "darkorange"),
    "TalA": ("v", "lightsteelblue"),
    "IdoA": ("v", "chocolate"),

    "Qui": ("^", "royalblue"),
    "Rha": ("^", "forestgreen"),
    "6dGul": ("^", "darkorange"),
    "Fuc": ("^", "crimson"),

    "QuiNAc": ("P", "royalblue"),
    "FucNAc": ("P", "crimson"),

    "Oli": ("X", "royalblue"),
    "Tyv": ("X", "forestgreen"),
    "Abe": ("X", "darkorange"),
    "Par": ("X", "pink"),
    "Dig": ("X", "purple"),

    "Ara": ("*", "forestgreen"),
    "Lyx": ("*", "gold"),
    "Xyl": ("*", "darkorange"),
    "Rib": ("*", "pink"),

    "Kdn": ("D", "forestgreen"),
    "Neu5Ac": ("D", "mediumvioletred"),
    "Neu5Gc": ("D", "turquoise"),

    "LDManHep": ("H", "forestgreen"),
    "Kdo": ("H", "gold"),
    "DDManHep": ("H", "pink"),
    "MurNAc": ("H", "purple"),
    "Mur": ("H", "chocolate"),

    "Api": ("p", "royalblue"),
    "Fru": ("p", "forestgreen"),
    "Tag": ("p", "gold"),
    "Sor": ("p", "darkorange"),
    "Psi": ("p", "pink"),

    # Default representation
    None: ("h", "black")
}

# Lipid names to match against for the `is_lipid` attribute
lipid_names = (
    '23SM', 'CDL1', 'CDL2', 'ABLIPA', 'ABLIPB', 'ADR', 'ADRP', 'ALIN', 'ALINP',
    'APC', 'APPC', 'ARA', 'ARAN', 'ARANP', 'ARAP', 'ASM', 'BCLIPA', 'BCLIPB', 'BCLIPC',
    'BEH', 'BEHP', 'BNSM', 'BSM', 'C6DHPC', 'C7DHPC', 'CER160', 'CER180', 'CER181',
    'CER2', 'CER200', 'CER220', 'CER240', 'CER241', 'CER3E', 'CHAPS', 'CHAPSO', 'CHL1',
    'CHM1', 'CHNS', 'CHOA', 'CHSD', 'CHSP', 'CJLIPA', 'CPC', 'CTLIPA', 'CYFOS3', 'CYFOS4',
    'CYFOS5', 'CYFOS6', 'CYFOS7', 'CYSF', 'CYSG', 'CYSL', 'CYSP', 'DAPA', 'DAPA', 'DAPC',
    'DAPC', 'DAPE', 'DAPE', 'DAPG', 'DAPG', 'DAPS', 'DAPS', 'DBPA', 'DBPC', 'DBPE',
    'DBPG', 'DBPS', 'DBSM', 'DCPC', 'DDA', 'DDAO', 'DDAOP', 'DDAP', 'DDMG', 'DDOPC',
    'DDOPE', 'DDOPS', 'DDPC', 'DEPA', 'DEPC', 'DEPE', 'DEPG', 'DEPS', 'DFPA', 'DFPC',
    'DFPE', 'DFPG', 'DFPS', 'DGLA', 'DGLAP', 'DGPA', 'DGPA', 'DGPC', 'DGPC', 'DGPE',
    'DGPE', 'DGPG', 'DGPG', 'DGPS', 'DGPS', 'DHA', 'DHAP', 'DHPC', 'DHPCE', 'DIPA',
    'DIPA', 'DIPC', 'DIPE', 'DIPG', 'DIPS', 'DLIPC', 'DLIPE', 'DLIPI', 'DLPA', 'DLPA',
    'DLPC', 'DLPC', 'DLPE', 'DLPE', 'DLPG', 'DLPG', 'DLPS', 'DLPS', 'DMPA', 'DMPC',
    'DMPCE', 'DMPE', 'DMPEE', 'DMPG', 'DMPI', 'DMPI13', 'DMPI14', 'DMPI15', 'DMPI24',
    'DMPI25', 'DMPI2A', 'DMPI2B', 'DMPI2C', 'DMPI2D', 'DMPI33', 'DMPI34', 'DMPI35',
    'DMPS', 'DNPA', 'DNPA', 'DNPC', 'DNPC', 'DNPE', 'DNPE', 'DNPG', 'DNPG', 'DNPS',
    'DNPS', 'DOMG', 'DOPA', 'DOPA', 'DOPC', 'DOPC', 'DOPCE', 'DOPE', 'DOPE', 'DOPEE',
    'DOPG', 'DOPG', 'DOPP1', 'DOPP2', 'DOPP3', 'DOPS', 'DOPS', 'DPA', 'DPAP', 'DPC',
    'DPCE', 'DPP1', 'DPP2', 'DPPA', 'DPPA', 'DPPC', 'DPPC', 'DPPE', 'DPPE', 'DPPEE',
    'DPPG', 'DPPG', 'DPPGK', 'DPPI', 'DPPS', 'DPPS', 'DPSM', 'DPT', 'DPTP', 'DRPA',
    'DRPC', 'DRPE', 'DRPG', 'DRPS', 'DSPA', 'DSPC', 'DSPE', 'DSPG', 'DSPS', 'DTPA',
    'DTPA', 'DTPC', 'DTPE', 'DTPG', 'DTPS', 'DUPC', 'DUPE', 'DUPS', 'DVPA', 'DVPC',
    'DVPE', 'DVPG', 'DVPS', 'DXCE', 'DXPA', 'DXPA', 'DXPC', 'DXPC', 'DXPE', 'DXPE',
    'DXPG', 'DXPG', 'DXPS', 'DXPS', 'DXSM', 'DYPA', 'DYPA', 'DYPC', 'DYPC', 'DYPE',
    'DYPE', 'DYPG', 'DYPG', 'DYPS', 'DYPS', 'ECLIPA', 'ECLIPB', 'ECLIPC', 'EDA', 'EDAP',
    'EICO', 'EICOP', 'EPA', 'EPAP', 'ERG', 'ERU', 'ERUP', 'ETA', 'ETAP', 'ETE', 'ETEP',
    'FOIS11', 'FOIS9', 'FOS10', 'FOS12', 'FOS13', 'FOS14', 'FOS15', 'FOS16', 'GLA',
    'GLAP', 'GLYM', 'HPA', 'HPAP', 'HPLIPA', 'HPLIPB', 'HTA', 'HTAP', 'IPC', 'IPPC',
    'KPLIPA', 'KPLIPB', 'KPLIPC', 'LAPAO', 'LAPAOP', 'LAU', 'LAUP', 'LDAO', 'LDAOP',
    'LIGN', 'LIGNP', 'LILIPA', 'LIN', 'LINP', 'LLPA', 'LLPC', 'LLPE', 'LLPS', 'LMPG',
    'LNACL1', 'LNACL2', 'LNBCL1', 'LNBCL2', 'LNCCL1', 'LNCCL2', 'LNDCL1', 'LNDCL2',
    'LOACL1', 'LOACL2', 'LOCCL1', 'LOCCL2', 'LPC', 'LPC12', 'LPC14', 'LPPA', 'LPPC',
    'LPPC', 'LPPE', 'LPPG', 'LPPG', 'LPPS', 'LSM', 'LYSM', 'MCLIPA', 'MEA', 'MEAP', 'MYR',
    'MYRO', 'MYROP', 'MYRP', 'NER', 'NERP', 'NGLIPA', 'NGLIPB', 'NGLIPC', 'NSM', 'OLE',
    'OLEP', 'OPC', 'OSM', 'OSPE', 'OYPE', 'PADG', 'PAL', 'PALIPA', 'PALIPB', 'PALIPC',
    'PALIPD', 'PALIPE', 'PALO', 'PALOP', 'PALP', 'PAPA', 'PAPC', 'PAPE', 'PAPG', 'PAPI',
    'PAPS', 'PDOPC', 'PDOPE', 'PEPC', 'PGPA', 'PGPC', 'PGPE', 'PGPG', 'PGPS', 'PGSM',
    'PIDG', 'PIM1', 'PIM2', 'PIPA', 'PIPC', 'PIPE', 'PIPG', 'PIPI', 'PIPS', 'PLPA',
    'PLPC', 'PLPE', 'PLPG', 'PLPI', 'PLPI13', 'PLPI14', 'PLPI15', 'PLPI24', 'PLPI25',
    'PLPI2A', 'PLPI2B', 'PLPI2C', 'PLPI2D', 'PLPI33', 'PLPI34', 'PLPI35', 'PLPS', 'PMCL1',
    'PMCL2', 'PMPE', 'PMPG', 'PNCE', 'PNPI', 'PNPI13', 'PNPI14', 'PNPI15', 'PNPI24',
    'PNPI25', 'PNPI2A', 'PNPI2B', 'PNPI2C', 'PNPI2D', 'PNPI33', 'PNPI34', 'PNPI35',
    'PNSM', 'PODG', 'POP1', 'POP2', 'POP3', 'POPA', 'POPA', 'POPC', 'POPC', 'POPCE',
    'POPE', 'POPE', 'POPEE', 'POPG', 'POPG', 'POPI', 'POPI', 'POPI13', 'POPI14', 'POPI15',
    'POPI24', 'POPI25', 'POPI2A', 'POPI2B', 'POPI2C', 'POPI2D', 'POPI33', 'POPI34',
    'POPI35', 'POPP1', 'POPP2', 'POPP3', 'POPS', 'POPS', 'POSM', 'PPC', 'PPPE', 'PQPE',
    'PQPS', 'PRPA', 'PRPC', 'PRPE', 'PRPG', 'PRPS', 'PSM', 'PSPG', 'PUDG', 'PUPA', 'PUPC',
    'PUPE', 'PUPI', 'PUPS', 'PVCL2', 'PVDG', 'PVP1', 'PVP2', 'PVP3', 'PVPE', 'PVPG',
    'PVPI', 'PVSM', 'PYPE', 'PYPG', 'PYPI', 'PhPC', 'QMPE', 'SAPA', 'SAPC', 'SAPE',
    'SAPG', 'SAPI', 'SAPI13', 'SAPI14', 'SAPI15', 'SAPI24', 'SAPI25', 'SAPI2A', 'SAPI2B',
    'SAPI2C', 'SAPI2D', 'SAPI33', 'SAPI34', 'SAPI35', 'SAPS', 'SB3-10', 'SB3-12',
    'SB3-14', 'SDA', 'SDAP', 'SDPA', 'SDPC', 'SDPE', 'SDPG', 'SDPS', 'SDS', 'SELIPA',
    'SELIPB', 'SELIPC', 'SFLIPA', 'SITO', 'SLPA', 'SLPC', 'SLPE', 'SLPG', 'SLPS', 'SOPA',
    'SOPC', 'SOPE', 'SOPG', 'SOPS', 'SSM', 'STE', 'STEP', 'STIG', 'THA', 'THAP', 'THCHL',
    'THDPPC', 'TIPA', 'TLCL1', 'TLCL2', 'TMCL1', 'TMCL2', 'TOCL1', 'TOCL2', 'TPA', 'TPAP',
    'TPC', 'TPC', 'TPT', 'TPTP', 'TRI', 'TRIP', 'TRIPAO', 'TRPAOP', 'TSPC', 'TTA', 'TTAP',
    'TXCL1', 'TXCL2', 'TYCL1', 'TYCL2', 'UDAO', 'UDAOP', 'UFOS10', 'UPC', 'VCLIPA',
    'VCLIPB', 'VCLIPC', 'VCLIPD', 'VCLIPE', 'VPC', 'XNCE', 'XNSM', 'YOPA', 'YOPC', 'YOPE',
    'YOPS', 'YPLIPA', 'YPLIPB', 'bondedtypes'
)
