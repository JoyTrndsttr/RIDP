import numpy as np
from scipy.signal import find_peaks

def check_overall_std(data): #判断方差是否在一定范围内
    overall_std = data['数据'].std() # 计算整体方差
    threshold = 0.001  # 方差的阈值
    print(f"overall_std:{overall_std}   threshold:{threshold}")
    if overall_std < threshold:
        return False
    return True

def is_valid_waveform(data, threshold=[0.01,0.1,0.01,0.01]):

    values = np.array([d['value'] for d in data])
    result = {
        "检测结果": True,
        "初始段": "正常",
        "峰值检测": "正常",
        "峰值抖动": "正常",
        "最终段": "正常"
    }
    flag = True

    # 分段检测
    # 1. 初始段判断：前10%数据应在0附近
    initial_values = values[:len(values) // 10]
    if np.abs(initial_values).mean() > threshold[0]:
        result['初始段'] = '初始段不符合'
        result["检测结果"] = False

    # 2. 峰值检测：检测波峰或波谷
    peaks, _ = find_peaks(values, height=threshold[1], width=len(values) // 20, prominence=threshold[1])  # 波峰
    troughs, _ = find_peaks(-values, height=threshold[1], width=len(values) // 20, prominence=threshold[1])  # 波谷
    print(f"peaks:{peaks} troughs:{troughs}")
    if len(peaks) == 0 and len(troughs) == 0:
        result["峰值检测"] = '无峰值或谷值'
        result["峰值抖动"] = '无峰值或谷值'
        result["检测结果"] = False
    elif len(peaks) > 1 or len(troughs) > 1:
        result["峰值检测"] = '有多个峰值或谷值'
        result["峰值抖动"] = '有多个峰值或谷值'
        result["检测结果"] = False
    # 3. 峰值附近的抖动：在峰值或谷值附近进行抖动检测,选取峰值左右10%的数据，检测其标准差
    elif len(peaks) + len(troughs) == 1:
        peak_region = values[max(peaks[0] - len(values) // 10, 0): min(peaks[0] + len(values) // 10, len(values))]
        if np.std(peak_region) > threshold[2]:
            result["峰值抖动"] = '峰值附近波动过大'
            result["检测结果"] = False

    # 4. 结束段判断：最后10%数据应回到0附近
    final_values = values[-len(values) // 10:]
    if np.abs(final_values).mean() > threshold[3]:
        result["最终段"] = '最终段不符合'
        result["检测结果"] = False

    # 若通过所有检查，则为正确波形
    return result

def check_waveform(type, data):
    if type in ["ZZWY1", "ZZWY2", "ZZWY3", "ZZWY4"]: #B/C界面支座纵向/横向位移 要求0附近抖动，上升，峰值附近波动，下降，0附近抖动
        check_overall_std(data)
    if type in ["LFWY"]: #梁缝位移 正波动+正抖动+负抖动
        return True
    if type in ["LDQJ"]: #梁端倾角 小抖动+大抖动+小抖动
        return True
    if type in ["ZDJSD2", "ZDJSD1", "SXJSDX", "SXJSDZ", "SXJSDY"]: #梁体横向/竖向加速度，轨道板横向/竖向/纵向加速度
        return True
    if type in ["XDWY1", "XDWY2"]:#轨道板相对横向位移/相对竖向位移
        return True
    if type in ["ZDWY2", "ZDWY1"]: #梁体横向/纵向振幅 0附近抖动+正弦波+大抖动+正弦波+0附近抖动
        return True
    if type in ["DND", "DYB"]:#梁体动挠度/动应变 目前不知道如何处理
        return True
    if type in ["WD", "SD"]:#温度、湿度 应该不用处理
        return True
