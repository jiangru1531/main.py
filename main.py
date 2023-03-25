from PyQt5.QtWidgets import (QApplication, QMainWindow, QWidget, QVBoxLayout,
                             QHBoxLayout, QFileDialog, QLabel, QPushButton,
                             QComboBox)
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas


class FeatureExtractor:
    def __init__(self, file_path):
        self.file_path = file_path
        self.data = pd.read_excel(file_path)

    def mean(self):
        return np.mean(self.data, axis=0)


class OscilloscopeWindow(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.fig, self.ax = plt.subplots()
        self.canvas = FigureCanvas(self.fig)
        self.layout = QVBoxLayout()
        self.layout.addWidget(self.canvas)
        self.setLayout(self.layout)

    def plot(self, data):
        self.ax.clear()
        self.ax.plot(data)
        self.canvas.draw()


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("特征提取工具")
        self.setWindowIcon(QIcon("icon.png"))
        self.resize(800, 600)

        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        main_layout = QVBoxLayout()

        # 添加文件选择框
        file_layout = QHBoxLayout()
        self.file_path1 = QLabel()
        self.file_path2 = QLabel()
        self.file_path3 = QLabel()
        file_layout.addWidget(QLabel("文件1："))
        file_layout.addWidget(self.file_path1)
        file_layout.addWidget(QLabel("文件2："))
        file_layout.addWidget(self.file_path2)
        file_layout.addWidget(QLabel("文件3："))
        file_layout.addWidget(self.file_path3)
        select_file_btn = QPushButton("选择文件")
        select_file_btn.clicked.connect(self.select_file)
        file_layout.addWidget(select_file_btn)
        main_layout.addLayout(file_layout)

        # 添加示波器窗口
        osc_layout = QHBoxLayout()
        self.osc1 = OscilloscopeWindow()
        self.osc2 = OscilloscopeWindow()
        self.osc3 = OscilloscopeWindow()
        self.osc4 = OscilloscopeWindow()
        osc_layout.addWidget(self.osc1)
        osc_layout.addWidget(self.osc2)
        osc_layout.addWidget(self.osc3)
        osc_layout.addWidget(self.osc4)
        main_layout.addLayout(osc_layout)

        # 添加特征提取按钮
        extract_layout = QHBoxLayout()
        extract_layout.addWidget(QLabel("选择文件："))
        self.file_combo_box = QComboBox()
        extract_layout.addWidget(self.file_combo_box)
        extract_btn = QPushButton("提取特征")
        extract_btn.clicked.connect(self.extract_feature)
        extract_layout.addWidget(extract_btn)
        main_layout.addLayout(extract_layout)

        central_widget.setLayout(main_layout)

    def select_file(self):
        file_path, _ = QFileDialog.getOpenFileName(
            parent=self,
            caption="选择文件",
            filter="Excel 文件 (*.xlsx *.xls)"
        )
        if file_path:
            if not self.file_path1.text():
                self.file_path1.setText(file_path)
            elif not self.file_path2.text():
                self.file_path2.setText(file_path)
            elif not self.file_path3.text():
                self.file_path3.setText(file_path)

    def extract_feature(self):
        file_paths = [self.file_path1.text(), self.file_path2.text(), self.file_path3.text()]
        feature_extractor = FeatureExtractor(file_paths[self.file_combo_box.currentIndex()])
        mean_values = feature_extractor.mean()
        print(mean_values)

if __name__ == '__main__':
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec_()