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

    def calculate_max(self, data):
        # Calculate the standard deviation of the data
        max = np.max(data)
        return max

    def calculate_min(self, data):
        # Calculate the standard deviation of the data
        min = np.min(data)
        return min

    def calculate_max_min(self, data):
        # Calculate the standard deviation of the data
        max_min = np.max_min(data)
        return max_min

    def calculate_absolute_mean_value(self, data):
        # Calculate the standard deviation of the data
        absolute_mean_value = np.absolute_mean_value(data)
        return absolute_mean_value

    def calculate_standard_deviation(self, data):
        # Calculate the standard deviation of the data
        standard_deviation = np.standard_deviation(data)
        return standard_deviation

    def calculate_root_mean_score(self, data):
        # Calculate the standard deviation of the data
        root_mean_score = np.root_mean_score(data)
        return root_mean_score

    def calculate_Root_amplitude(self, data):
        # Calculate the standard deviation of the data
        Root_amplitude = np.Root_amplitude(data)
        return Root_amplitude

    def calculate_skewness_value(self, data):
        # Calculate the standard deviation of the data
        skewness_value = np.skewness_value(data)
        return skewness_value

    def calculate_Kurtosis_value(self, data):
        # Calculate the standard deviation of the data
        Kurtosis_value = np.Kurtosis_value(data)
        return Kurtosis_value

    def calculate_shape_factor(self, data):
        # Calculate the standard deviation of the data
        shape_factor = np.shape_factor(data)
        return shape_factor

    def calculate_crest_factor(self, data):
        # Calculate the standard deviation of the data
        crest_factor = np.crest_factor(data)
        return crest_factor

    def calculate_pulse_factor(self, data):
        # Calculate the standard deviation of the data
        pulse_factor = np.pulse_factor(data)
        return pulse_factor

    def calculate_clearance_factor(self, data):
        # Calculate the standard deviation of the data
        clearance_factor = np.clearance_factor(data)
        return clearance_factor


    def extract_mean(self):
        if hasattr(self, 'df'):
            means = self.df.mean()
            self.ax.clear()
            self.ax.plot(means)
            self.canvas.draw()

    # 提取最大值
    def extract_max(self):
        if hasattr(self, 'df'):
            max = self.df.max()
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
            min = self.df.min()
            self.ax.clear()
            self.ax.plot(min)
            self.canvas.draw()

    # 提取峰峰值
    def extract_max_min(self):
        if hasattr(self, 'df'):
            max_min = self.df.max_min()
            self.ax.clear()
            self.ax.plot(max_min)
            self.canvas.draw()

    # 提取绝对均值
    def extract_absolute_mean_value(self):
        if hasattr(self, 'df'):
            absolute_mean_value = self.df.absolute_mean_value()
            self.ax.clear()
            self.ax.plot(absolute_mean_value)
            self.canvas.draw()

    # 提取标准差
    def extract_standard_deviation(self):
        if hasattr(self, 'df'):
            standard_deviation = self.df.standard_deviation()
            self.ax.clear()
            self.ax.plot(standard_deviation)
            self.canvas.draw()

    # 提取均方根值
    def extract_root_mean_score(self):
        if hasattr(self, 'df'):
            root_mean_score = self.df.root_mean_score()
            self.ax.clear()
            self.ax.plot(root_mean_score)
            self.canvas.draw()

    # 提取方根幅值
    def extract_Root_amplitude(self):
        if hasattr(self, 'df'):
            Root_amplitude = self.df.Root_amplitude()
            self.ax.clear()
            self.ax.plot(Root_amplitude)
            self.canvas.draw()

    # 提取偏态指标
    def extract_skewness_value(self):
        if hasattr(self, 'df'):
            skewness_value = self.df.skewness_value()
            self.ax.clear()
            self.ax.plot(skewness_value)
            self.canvas.draw()

    # 提取峭度指标
    def extract_Kurtosis_value(self):
        if hasattr(self, 'df'):
            Kurtosis_value = self.df.Kurtosis_value()
            self.ax.clear()
            self.ax.plot(Kurtosis_value)
            self.canvas.draw()

    # 提取波形因子
    def extract_shape_factor(self):
        if hasattr(self, 'df'):
            shape_factor = self.df.shape_factor()
            self.ax.clear()
            self.ax.plot(shape_factor)
            self.canvas.draw()

    # 提取峰值因子
    def extract_crest_factor(self):
        if hasattr(self, 'df'):
            crest_factor = self.df.crest_factor()
            self.ax.clear()
            self.ax.plot(crest_factor)
            self.canvas.draw()

    # 提取脉冲因子
    def extract_pulse_factor(self):
        if hasattr(self, 'df'):
            pulse_factor = self.df.pulse_factor()
            self.ax.clear()
            self.ax.plot(pulse_factor)
            self.canvas.draw()

    # 提取裕度因子
    def extract_clearance_factor(self):
        if hasattr(self, 'df'):
            clearance_factor = self.df.clearance_factor()
            self.ax.clear()
            self.ax.plot(clearance_factor)
            self.canvas.draw()

    def extract_features(self, data):
        # Calculate the mean and standard deviation of the data
        mean = self.calculate_mean(data)
        std = self.calculate_std(data)
        max = self.calculate_max(data)
        min = self.calculate_min(data)
        max_min = self.calculate_max_min(data)
        absolute_mean_value = self.calculate_absolute_mean_value(data)
        standard_deviation = self.calculate_standard_deviation(data)
        root_mean_score = self.calculate_root_mean_score(data)
        Root_amplitude = self.calculate_Root_amplitude(data)
        skewness_value = self.calculate_skewness_value(data)
        Kurtosis_value = self.calculate_Kurtosis_value(data)
        shape_factor = self.calculate_shape_factor(data)
        crest_factor = self.calculate_crest_factor(data)
        pulse_factor = self.calculate_pulse_factor(data)
        clearance_factor = self.calculate_clearance_factor(data)

        # Return the results as a dictionary
        results = {
            'mean': mean,
            'std': std,
            'max': max,
            'min': min,
            'max_min': max_min,
            'absolute_mean_value': absolute_mean_value,
            'standard_deviation': standard_deviation,
            'root_mean_score': root_mean_score,
            'Root_amplitude': Root_amplitude,
            'skewness_value': skewness_value,
            'Kurtosis_value': Kurtosis_value,
            'shape_factor': shape_factor,
            'crest_factor': crest_factor,
            'pulse_factor': pulse_factor,
            'clearance_factor': clearance_factor
        }
        return results
