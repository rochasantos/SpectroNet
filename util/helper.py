import yaml

def load_config(file_path):
    with open(file_path, 'r') as file:
        return yaml.safe_load(file)


def filter_data(metadata, filter_config):
    indexes_metainfo = []

    for index, row in metadata.iterrows():
        matches = all(
            row[key] in value if isinstance(value, list) 
            else row[key] == value for key, value in filter_config.items()
        )
        if matches:
            indexes_metainfo.append(index)
    
    return indexes_metainfo