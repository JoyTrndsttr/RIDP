import numpy as np
import matplotlib.pyplot as plt
import json
import pandas as pd
from utils import DataQuery
# import DataQuery

def filter_data(data, window_size):
    """Applies a moving average filter to the data and keeps the original data structure."""
    values = np.array([d['value'] for d in data])
    weights = np.ones(window_size) / window_size
    filtered_values = np.convolve(values, weights, mode='same')  # 'same' keeps the original length
    filtered_data = [{'time': d['time'], 'value': fv} for d, fv in zip(data, filtered_values)]
    return filtered_data

def main():
    metrics = DataQuery.get_file_name_and_content_by_bridge_time_type('武广高铁淦河连续梁桥', '2024-4-10 07:13:17:39899', 'ZZWY1')
    data = json.loads(metrics['FileContent'])

    window_size = 100
    filtered_data = filter_data(data, window_size)

    original_df = pd.DataFrame(data)
    original_df['time'] = pd.to_datetime(original_df['time'])
    filtered_df = pd.DataFrame(filtered_data)
    filtered_df['time'] = pd.to_datetime(filtered_df['time'])

    # Plot results
    plt.figure(figsize=(10, 4))
    plt.plot(original_df['time'], original_df['value'], label='Original Data', alpha=0.5)
    plt.plot(filtered_df['time'], filtered_df['value'], label='Filtered Data', color='red', alpha=0.7)

    plt.title('Waveform Analysis with Moving Average Filter')
    plt.xlabel('Time')
    plt.ylabel('Value')
    plt.legend()
    plt.show()

if __name__ == "__main__":
    main()
