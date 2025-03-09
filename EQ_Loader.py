import os
import numpy as np
import re

from EQ_Data import EQ_Data


def EQ_Loader(folder_path: str='EQ_List/', files: list[str]=None , normalize=False):

    # folder_path = 'EQ_List/'

    if files is None:
        files = os.listdir(folder_path)

    pattern = r"^(?P<place>[A-Za-z0-9_]+)-(?P<direction>NS|EW|00|90|L|250)-(?P<location>[A-Za-z0-9_]+)-(?P<units>[A-Za-z0-9_]+)\.(?P<extension>[a-z]+)$"

    EQ_List: list[EQ_Data]=[]

    for file_name in files:
        print("Loading: "+file_name)
        file_path = os.path.join(folder_path, file_name)
        eq_data = np.loadtxt(file_path)

        match = re.match(pattern, file_name)

        if match:
            metadata = match.groupdict()
            name = metadata['place']
            direction = metadata['direction']
            location = metadata['location']
            units = metadata['units']
            extension = metadata['extension']
        else:
            print("File name non standard")
            name = "Unknown"
            direction = "Unknown"
            location = "Unknown"
            units = "g"
            extension = "Unknown"

        time_arr = eq_data[:, 0]
        ground_accel = eq_data[:, 1]

        eq=EQ_Data(time_arr, ground_accel, units=units, name=name, orientation=direction, location=location, normalize=normalize)
        EQ_List.append(eq)

    return EQ_List

