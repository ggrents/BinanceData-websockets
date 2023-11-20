import matplotlib.pyplot as plt


class Plotter:
    def __init__(self, symbol):
        self.fig = plt.figure()
        self.ax = self.fig.add_subplot(111)
        self.fig.show()
        self.ax.set_title(f"Binance Price Chart for {symbol}")
        self.ax.set_xlabel("Time")
        self.ax.set_ylabel("Price ($)")
        self.ax.legend()

    def update_graph(self, xdata, ydata):
        self.ax.plot(xdata, ydata, color='g')
        self.ax.legend([f"Last price: {ydata[-1]}$"])
        self.fig.canvas.draw()
        plt.pause(0.1)
        return xdata, ydata
