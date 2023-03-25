import os
import pandas as pd
import matplotlib.pyplot as plt
from PyQt5.QtWidgets import QApplication, QLabel, QVBoxLayout, QWidget, QPushButton, QFileDialog
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure

'''我更新了吗这个项目你能看见'''

# 创建GUI界面
class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Excel Analyzer')
        self.layout = QVBoxLayout()
        self.setLayout(self.layout)

        # 添加路径选择按钮
        self.btn_choose = QPushButton('选择文件')
        self.layout.addWidget(self.btn_choose)
        self.btn_choose.clicked.connect(self.choose_file)

        # 添加波形显示界面
        self.fig = Figure(figsize=(5, 4), dpi=100)
        self.canvas = FigureCanvas(self.fig)
        self.ax = self.fig.add_subplot(111)
        self.layout.addWidget(self.canvas)

        # 添加特征提取按钮
        self.btn_mean = QPushButton('提取均值')
        self.btn_std = QPushButton('提取标准差')
        self.btn_max = QPushButton('提取峰值')
        self.btn_min = QPushButton('提取最小值')
        self.btn_max_min = QPushButton('提取峰峰值')
        self.btn_absolute_mean_value = QPushButton('提取绝对均值')
        self.btn_standard_deviation = QPushButton('提取标准差')
        self.btn_root_mean_score = QPushButton('提取均方根值')
        self.btn_Root_amplitude = QPushButton('提取方根幅值')
        self.btn_skewness_value = QPushButton('提取偏态指标')
        self.btn_Kurtosis_value = QPushButton('提取峭度指标')
        self.btn_shape_factor = QPushButton('提取波形因子')
        self.btn_crest_factor = QPushButton('提取峰值因子')
        self.btn_pulse_factor = QPushButton('提取脉冲因子')
        self.btn_clearance_factor = QPushButton('提取裕度因子')

        self.layout.addWidget(self.btn_mean)
        self.layout.addWidget(self.btn_std)
        self.layout.addWidget(self.btn_max)
        self.layout.addWidget(self.btn_min)
        self.layout.addWidget(self.btn_max_min)
        self.layout.addWidget(self.btn_absolute_mean_value)
        self.layout.addWidget(self.btn_standard_deviation)
        self.layout.addWidget(self.btn_root_mean_score)
        self.layout.addWidget(self.btn_Root_amplitude)
        self.layout.addWidget(self.btn_skewness_value)
        self.layout.addWidget(self.btn_Kurtosis_value)
        self.layout.addWidget(self.btn_shape_factor)
        self.layout.addWidget(self.btn_crest_factor)
        self.layout.addWidget(self.btn_pulse_factor)
        self.layout.addWidget(self.btn_clearance_factor)

        self.btn_mean.clicked.connect(self.extract_mean)
        self.btn_std.clicked.connect(self.extract_std)
        self.btn_max.clicked.connect(self.extract_max)
        self.btn_min.clicked.connect(self.extract_min)
        self.btn_max_min.clicked.connect(self.extract_max_min)
        self.btn_absolute_mean_value.clicked.connect(self.extract_absolute_mean_value)
        self.btn_standard_deviation.clicked.connect(self.extract_standard_deviation)
        self.btn_root_mean_score.clicked.connect(self.extract_root_mean_score)
        self.btn_Root_amplitude.clicked.connect(self.extract_Root_amplitude)
        self.btn_skewness_value.clicked.connect(self.extract_skewness_value)
        self.btn_Kurtosis_value.clicked.connect(self.extract_Kurtosis_value)
        self.btn_shape_factor.clicked.connect(self.extract_shape_factor)
        self.btn_crest_factor.clicked.connect(self.extract_crest_factor)
        self.btn_pulse_factor.clicked.connect(self.extract_pulse_factor)
        self.btn_clearance_factor.clicked.connect(self.extract_clearance_factor)

    # 打开文件选择对话框
    def choose_file(self):
        filename, _ = QFileDialog.getOpenFileName(self, '选择文件', '.', 'Excel files (*.xlsx)')
        if filename:
            self.filename = filename
            self.label_path = QLabel(filename)
            self.layout.addWidget(self.label_path)
            self.df = pd.read_excel(self.filename, index_col=0, header=[0, 1])
            self.ax.clear()
            self.ax.plot(self.df)
            self.canvas.draw()

    # 提取均值
    def extract_mean(self):
        if hasattr(self, 'df'):
            means = self.df.mean()
            self.ax.clear()
            self.ax.plot(means)
            self.canvas.draw()
        # 提取最大值
    def extract_max(self):
        if hasattr(self, 'df'):
            max = data_X1.nlargest(1).mean()
            self.ax.clear()
            self.ax.plot(max)
            self.canvas.draw()
    # 提取标准差
    def extract_std(self):
        if hasattr(self, 'df'):
            stds = self.df.std()
            self.ax.clear()
            self.ax.plot(stds)
            self.canvas.draw()
    # 提取最小值
    def extract_min(self):
        if hasattr(self, 'df'):
            min = data_X1.nsmallest(1).mean()
            self.ax.clear()
            self.ax.plot(min)
            self.canvas.draw()
    # 提取峰峰值
    def extract_max_min(self):
        if hasattr(self, 'df'):
            max_min = max - min
            self.ax.clear()
            self.ax.plot(max_min)
            self.canvas.draw()
    # 提取绝对均值
    def extract_absolute_mean_value(self):
        if hasattr(self, 'df'):
            absolute_mean_value = np.sum(np.fabs(data_X1)) / size_X1
            self.ax.clear()
            self.ax.plot(absolute_mean_value)
            self.canvas.draw()
    # 提取标准差
    def extract_standard_deviation(self):
        if hasattr(self, 'df'):
            standard_deviation = np.sqrt(np.sum(np.square(data_X1 - mean_value)) / size_X1)
            self.ax.clear()
            self.ax.plot(standard_deviation)
            self.canvas.draw()
    # 提取均方根值
    def extract_root_mean_score(self):
        if hasattr(self, 'df'):
            root_mean_score = np.sqrt(np.sum(np.square(data_X1)) / size_X1)
            self.ax.clear()
            self.ax.plot(root_mean_score)
            self.canvas.draw()
    # 提取方根幅值
    def extract_Root_amplitude(self):
        if hasattr(self, 'df'):
            Root_amplitude = np.square(np.sum(np.sqrt(np.fabs(data_X1))) / size_X1)
            self.ax.clear()
            self.ax.plot(Root_amplitude)
            self.canvas.draw()
    # 提取偏态指标
    def extract_skewness_value(self):
        if hasattr(self, 'df'):
            skewness_value = np.sum(np.power((data_X1 - mean_value) / standard_deviation, 3)) / size_X1
            self.ax.clear()
            self.ax.plot(skewness_value)
            self.canvas.draw()
    # 提取峭度指标
    def extract_Kurtosis_value(self):
        if hasattr(self, 'df'):
            Kurtosis_value = np.sum(np.power((data_X1)/standard_deviation, 4))/size_X1
            self.ax.clear()
            self.ax.plot(Kurtosis_value)
            self.canvas.draw()
    # 提取波形因子
    def extract_shape_factor(self):
        if hasattr(self, 'df'):
            shape_factor = root_mean_score / absolute_mean_value
            self.ax.clear()
            self.ax.plot(shape_factor)
            self.canvas.draw()
    # 提取峰值因子
    def extract_crest_factor(self):
        if hasattr(self, 'df'):
            crest_factor = max / root_mean_score
            self.ax.clear()
            self.ax.plot(crest_factor)
            self.canvas.draw()
    # 提取脉冲因子
    def extract_pulse_factor(self):
        if hasattr(self, 'df'):
            pulse_factor = max / absolute_mean_value
            self.ax.clear()
            self.ax.plot(pulse_factor)
            self.canvas.draw()
    # 提取裕度因子
    def extract_clearance_factor(self):
        if hasattr(self, 'df'):
            clearance_factor = max / Root_amplitude
            self.ax.clear()
            self.ax.plot(clearance_factor)
            self.canvas.draw()

# 启动应用程序
if __name__ == '__main__':
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec_()
