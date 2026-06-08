import pandas as pd


def parse_line(line):
    elm = []
    line = line.strip()
    fields = line.split('|')
    for i in range(len(fields) - 1):
        elm.append(float(fields[i]))
    elm.append(fields[4])
    return elm


def add_to_dict(parsed_line, data_dict):
    if len(parsed_line) != len(data_dict.keys()):
        raise ValueError("number of fields does not match dictionary keys.")
    for i in list(data_dict.keys()):
        data_dict[i] = parsed_line[i]



def load_data(filename):
    data_dict = {sepal_length:[],
                 sepal_width:[],
                 petal_length:[],
                 petal_width:[],
                 species:[]}
    open(filename, 'r')
    for i in list(a.keys()):
        parsed = parse_line(a[i])
        add_to_dict(parsed, data_dict)
    return pd.DataFrame(data_dict)


def species_mean(data, species, measurement):
    data.loc(data["species"] == species)
    return data[measurement].mean()