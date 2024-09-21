import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import find_peaks
# import DataQuery
from utils import DataQuery
import json
import pandas as pd  # Assuming data needs handling similar to pandas

def find_waveform_segment(data, threshold=[0.01, 0.01, 0.01, 0.01], extension=0.05):
    values = np.array([d['value'] for d in data])
    bias = values[:len(values) // 10].mean()
    values = values - bias
    
    # Find peaks
    peaks, _ = find_peaks(values, height=threshold[1], width=len(values) // 20, prominence=threshold[1])
    if len(peaks) != 1:
        return None

    peak_index = peaks[0]
    
    # Locate the waveform's start and end around the peak
    start_index = next((i for i in range(peak_index, 0, -1) if values[i] <= 0), 0)
    end_index = next((i for i in range(peak_index, len(values) - 1) if values[i] <= 0), len(values) - 1)
    
    # Add buffer
    buffer_len = int(len(values) * extension)
    start_index = max(0, start_index - buffer_len)
    end_index = min(len(values) - 1, end_index + buffer_len)

    return start_index, end_index, bias

def main():
    metrics = DataQuery.get_file_name_and_content_by_bridge_time_type('武广高铁淦河连续梁桥', '2024-4-10 07:13:17:39899', 'ZZWY1')
    data = json.loads(metrics['FileContent'])

    segment_indices = find_waveform_segment(data)
    if segment_indices:
        # Convert 'time' to appropriate datetime format if necessary
        data = pd.DataFrame(data)
        data['time'] = pd.to_datetime(data['time'])

        start_index, end_index, bias = segment_indices
        values = (data['value']-bias).to_numpy()
        times = data['time'].to_numpy()
        
        plt.figure(figsize=(10, 4))
        plt.plot(times, values, label='Complete Waveform')
        plt.plot(times[start_index:end_index + 1], values[start_index:end_index + 1], color='red', label='Waveform Segment')
        
        plt.title('Waveform Analysis')
        plt.xlabel('Time')
        plt.ylabel('Value')
        plt.legend()
        plt.show()

if __name__ == "__main__":
    main()
