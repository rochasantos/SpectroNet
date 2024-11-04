from vibdata.deep.DeepDataset import DeepDataset, convertDataset
import vibdata.raw as raw_datasets

def transform_dataset(dataset_name, raw_root_dir, deep_root_dir, transforms):
    raw_dataset = getattr(raw_datasets, dataset_name + "_raw")(raw_root_dir, download=True)
    convertDataset(dataset=raw_dataset, transforms=transforms, dir_path=deep_root_dir)
    # Load the dataset which has been converted
    return DeepDataset(deep_root_dir)