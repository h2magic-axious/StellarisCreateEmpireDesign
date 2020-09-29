from settings import FLAGS_DIR
import os
from pprint import pprint

FLAGS_MAP = dict()
for file_path in os.listdir(FLAGS_DIR):
    abs_file_path = FLAGS_DIR.joinpath(file_path)
    if abs_file_path.is_dir():
        flags_list = list()
        for sub_file_path in os.listdir(abs_file_path):
            if sub_file_path == 'small' or sub_file_path == 'map':
                continue

            if '.dds' in sub_file_path and '.txt' not in sub_file_path:
                flags_list.append(sub_file_path)
        FLAGS_MAP[file_path] = flags_list

FLAGS_BACKGROUNDS = FLAGS_MAP.pop('backgrounds')

COLORS = "dark_brown brown beige yellow light_orange light_orange orange " \
            "red_orange red burgundy pink purple dark_purple indigo dark_blue " \
            "blue light_blue turquoise dark_teal light_green green dark_green " \
            "grey dark_grey black".split()

pprint(FLAGS_BACKGROUNDS)
pprint(FLAGS_MAP)
print(COLORS)
