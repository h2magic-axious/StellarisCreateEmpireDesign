from settings import STELLARIS_DIR

SPECIES_TRAITS_DIR = STELLARIS_DIR.joinpath('common').joinpath('traits')

# 蜂巢
TRAIT_HIVE_MIND = 'trait_hive_mind'

# 机器人
TRAIT_MACHINE_UNIT = 'trait_machine_unit'
TRAIT_MECHANICAL = 'trait_mechanical'

# 石头人
TRAIT_LITHOID = 'lithoid'

TRAIT_PRICE = 2
TRAIT_NUMBER = 5


def get_traits(file_path):
    names = []
    costs = []
    with open(file_path, 'r', encoding='utf-8') as f:
        for line in f:
            line = line.strip()
            if line.startswith('trait_'):
                names.append(line.split('=')[0].strip())
                continue

            if line.startswith('cost'):
                c = int(line.split('=')[-1])
                if c:
                    costs.append(c)
                continue

    return {name: cost for name, cost in zip(names, costs)}


if __name__ == '__main__':
    traits = get_traits(SPECIES_TRAITS_DIR.joinpath('04_species_traits.txt'))
    for k in traits:
        print(k, traits[k])
