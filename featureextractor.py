import numpy as np

class FeatureExtractor:
    def __init__(self):
        pass

    def calculate_mean(self, data):
        # Calculate the mean of the data
        mean = np.mean(data)
        return mean

    def calculate_std(self, data):
        # Calculate the standard deviation of the data
        std = np.std(data)
        return std

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
            Kurtosis_value = np.sum(np.power((data_X1) / standard_deviation, 4)) / size_X1
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

    def extract_features(self, data):
        # Calculate the mean and standard deviation of the data
        mean = self.calculate_mean(data)
        std = self.calculate_std(data)

        # Return the results as a dictionary
        results = {
            'mean': mean,
            'std': std
        }
        return results

