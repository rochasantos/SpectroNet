from vibdata.deep.DeepDataset import DeepDataset, convertDataset
import vibdata.raw as raw_datasets
from vibdata.deep.signal.transforms import Spectrogram, FilterByValue, Sequential

import os

import numpy as np
import matplotlib.pyplot as plt


def build_transforms(filter_config, spect_config):
    # Get the transforms to be applied

    return Sequential(
        [ 
            FilterByValue(on_field, values) for on_field, values in filter_config.items() 
        ] + [
            Spectrogram(**spect_config)
        ]
    )


def plot_spectrogram(metainfo, Sxx):
    delta_t = metainfo["delta_t"]
    delta_f = metainfo["delta_f"]
    
    # Determinar as escalas dos eixos de tempo e frequência
    num_time_steps = Sxx.shape[1]
    num_freq_bins = Sxx.shape[0]
    time_extent = [0, delta_t * num_time_steps]
    freq_extent = [0, delta_f * num_freq_bins]

    # Plot do espectrograma
    fig=plt.figure(figsize=(10, 6))
    plt.imshow(np.fliplr(abs(Sxx).T).T, aspect='auto', cmap='viridis', 
               extent=[time_extent[0], time_extent[1], freq_extent[0], freq_extent[1]])
    # plt.imshow(np.log(np.abs(Sxx[: 382, :]**2)), cmap='jet',
    #            extent=[time_extent[0], time_extent[1], freq_extent[0], freq_extent[1]])
    # plt.ylabel('Frequency [Hz]')
    # plt.xlabel('Time [s]')
    # plt.colorbar(label="Power/Frequency (dB/Hz)")
    # plt.title("Spectrogram")
    plt.axis('off')
    plt.gca().invert_yaxis()
    # Save the spectrogram
    filename = metainfo["file_name"][:-4]+'.png'
    output = os.path.join('data/spectrograms', filename)
    plt.savefig(output, bbox_inches='tight', pad_inches=0)
    plt.close(fig)
    