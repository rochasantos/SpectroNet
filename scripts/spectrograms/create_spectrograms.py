from util.helper import load_config
from .helper import build_transforms, plot_spectrogram
from util.transform_dataset import transform_dataset

list_of_datasets_name = ["CWRU"]

raw_root_dir = "data"
deep_root_dir = "data/deep_dataset0"

def create_spectrogram():

    for dataset_name in list_of_datasets_name:
        filter_config = load_config('configs/transform_config.yaml')[dataset_name]["Filter"]
        spect_config = load_config('configs/transform_config.yaml')[dataset_name]["Spectrogram"]
        
        transforms = build_transforms(filter_config, spect_config)
        dataset = transform_dataset(dataset_name, raw_root_dir, deep_root_dir, transforms)

        for d in dataset:
            # Calculate the spectrogram
            metainfo = d['metainfo']
            Sxx = d['signal'][0]
            plot_spectrogram(metainfo, Sxx)
