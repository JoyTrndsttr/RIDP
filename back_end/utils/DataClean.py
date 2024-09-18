def check_overall_std(data):
    overall_std = data['数据'].std() # 计算整体方差
    threshold = 0.001  # 方差的阈值
    print(f"overall_std:{overall_std}   threshold:{threshold}")
    if overall_std < threshold:
        return False
    return True

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
