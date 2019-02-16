import numpy as np
import matplotlib.pyplot as plt


def plot_data(x_array, y_array, x_label='X', y_label='Y', title=None):
    
    def x_mean():
        return np.mean(x_array)

    def y_mean():
        return np.mean(y_array)

    def x_std():
        return np.std(x_array)

    def y_std():
        return np.std(y_array)

    def pears():
        """Calculate the Pearson correlation coefficient"""
        quad_1 = x_array - x_mean()
        quad_2 = y_array - y_mean()
        top = sum(quad_1 * quad_2)
        quad_3 = sum(quad_1 ** 2)
        quad_4 = sum(quad_2 ** 2)
        bottom = np.sqrt(quad_3 * quad_4)
        pears = top / bottom
        return pears
   
    def slope():
        return pears() * (y_std() / x_std())

    def y_intercept():
        return y_mean() - slope() * x_mean()
    
    def plot_regression_line():
        """Plot a line from slope and intercept"""
        axes = plt.gca()
        x_vals = np.array(axes.get_xlim())
        y_vals = y_intercept() + slope() * x_vals
        plt.plot(x_vals, y_vals)    

    # plotting data points and linear regression
    plt.scatter(x_array, y_array)
    plot_regression_line()
    
    # labeling axis and graph title if provided
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.title(title)
    
    # display graph
    plt.show()