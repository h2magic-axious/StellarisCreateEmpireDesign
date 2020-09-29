from pathlib import Path
import os

BASE_DIR = Path(__file__).parent.absolute()

STELLARIS_DIR = Path(r'D:\Steam\steamapps\common\Stellaris')
FLAGS_DIR = STELLARIS_DIR.joinpath('flags')


SPECIES_CLASS_DIR = STELLARIS_DIR.joinpath('species_classes')
SPECIES_NAMES_DIR = STELLARIS_DIR.joinpath('species_names')


if __name__ == '__main__':
    for file in os.listdir(STELLARIS_DIR):
        print(file)