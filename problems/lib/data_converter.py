
def convert_file_to_array(file_name):
    with open(file_name, "r") as data_file:
        data = data_file.read()
    return convert_to_int(parse_data(data))


def _get_data_from_file(file_name):
    with open(file_name, "r") as data_file:
        data = data_file.read()
    return data


def parse_data(str_data, delim_1="\n", delim_2=" "):
    a = str_data.split(delim_1)
    try:
        a.remove("")
    except:
        pass
    b = []
    for i in a:
        b.append(i.split(delim_2))
    return b



def convert_to_int(data_array):
    for i in range(0, len(data_array)):
        if isinstance(data_array[i], list):
            for j in range(0, len(data_array[i])):
                data_array[i][j] = int(data_array[i][j])
        else:
            data_array[i] = int(data_array[i])
    return data_array
