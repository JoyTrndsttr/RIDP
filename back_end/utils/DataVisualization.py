import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import os
from matplotlib import rcParams

# 设置matplotlib以支持中文显示并确保负号显示正确
rcParams['font.sans-serif'] = ['SimHei']  # 设置字体为黑体，以支持中文
rcParams['axes.unicode_minus'] = False  # 确保能正确显示负号

def plot_and_save(data, file_path, output_dir, image_index):
    fig, ax = plt.subplots(figsize=(12, 6))
    fig.patch.set_facecolor('#222830')  # 设置整体背景颜色为深灰
    ax.set_facecolor('#222830')  # 设置图表区域的背景颜色为深灰
    
    # 绘制数据
    ax.plot(data['时间'], data['数据'], marker='', linestyle='-', color='white', linewidth=2)
    
    # 设置日期格式和间隔
    ax.xaxis.set_major_locator(mdates.MinuteLocator(interval=1))
    ax.xaxis.set_major_formatter(mdates.DateFormatter('%H:%M:%S'))
    
    # 设置标题和标签
    ax.set_title(file_path.split('\\')[-1], fontsize=16, fontweight='bold', color='white')
    ax.set_xlabel('时间', fontsize=12, color='white')
    ax.set_ylabel('振幅', fontsize=12, color='white')
    
    # 设置网格
    ax.grid(True, which='both', linestyle='--', linewidth=0.5, color='#666666')
    
    # 其他美化设置
    plt.xticks(rotation=0, color='white')
    plt.yticks(color='white')
    plt.tight_layout()
    
    # 保存图像
    plt.savefig(os.path.join(output_dir, f'图片{image_index}.png'))
    plt.close()

# 主目录
base_dir = r'C:\Users\Administrator\OneDrive - csu.edu.cn\work\开源实验室\横向项目\土木\RIDP\data\武广高铁淦河连续梁桥\2024-4-10'
output_base = r'C:\Users\Administrator\OneDrive - csu.edu.cn\work\开源实验室\横向项目\土木\RIDP\output'

# 数据处理和保存
image_counter = 1  # 图片计数器
for dir_name in os.listdir(base_dir):
    data_dir = os.path.join(base_dir, dir_name)
    if os.path.isdir(data_dir):
        for file_name in os.listdir(data_dir):
            if file_name.endswith('.csv'):
                file_path = os.path.join(data_dir, file_name)
                data = pd.read_csv(file_path)
                data['时间'] = pd.to_datetime(data['时间'])
                data['数据'] = pd.to_numeric(data['数据'], errors='coerce')

                # 输出目录
                output_dir = os.path.join(output_base, file_name.split('.')[0])
                if not os.path.exists(output_dir):
                    os.makedirs(output_dir)
                
                # 绘图并保存
                plot_and_save(data, file_path, output_dir, image_counter)
    image_counter += 1  # 更新图片计数
