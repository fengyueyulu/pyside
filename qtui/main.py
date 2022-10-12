import sys
from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
import pyqtgraph as pg
from mainSystem import Ui_Form as main_ui
from chartWin import Ui_Form as chart_ui
from systemSetting import Ui_Form as setting_ui


class MainWin(QWidget, main_ui):

    def __init__(self):
        super(MainWin, self).__init__()
        self.setupUi(self)
        self.search_btn.clicked.connect(self.gotoChart)
        self.jump_btn.clicked.connect(self.gotoSetting)

    def gotoChart(self):
        self.chartwin = ChartWin()
        self.chartwin.show()
        self.close()

    def gotoSetting(self):
        self.settingwin = SettingWin()
        self.settingwin.show()
        self.close()


class ChartWin(QWidget, chart_ui):

    def __init__(self):
        super(ChartWin, self).__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.gotoMain)
        self.pushButton_2.clicked.connect(self.gotoSetting)
        self.pw = pg.PlotWidget()
        self.pw.setTitle('数据动态曲线', color='black', size='12pt')
        self.pw.setLabel('left', '温度、湿度、甲烷', color='black')
        self.pw.setLabel('bottom', '时间(最近30秒(x轴单位/0.1s))', color='black')
        self.pw.setBackground('#f0ffff')
        self.pw.showGrid(x=True, y=True)
        self.horizontalLayout.addWidget(self.pw)
        self.draw_lines()

    def draw_lines(self, times=None, temperature=None, humidity=None, ch4=None):
        # 通过调用该方法，传递参数，来实现动态更新
        # 下面是默认的测试数据，删除就行
        times = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
        temperature = [30, 32, 24, 31, 19, 12, 20, 28, 38, 30]
        humidity = [10, 12, 13, 9, 3, 14, 17, 12, 11, 10]
        ch4 = [1, 2, 2.4, 1.2, 1.8, 1.3, 2.5, 3.1, 4.6, 3.4]
        self.pw.plot(times, temperature, pen=pg.mkPen(width=3, color='#3fc5c6'))
        self.pw.plot(times, humidity, pen=pg.mkPen(width=3, color='#35d0a6'))
        self.pw.plot(times, ch4, pen=pg.mkPen(width=3, color='#bce49e'))

    def gotoMain(self):
        self.mainwin = MainWin()
        self.mainwin.show()
        self.close()

    def gotoSetting(self):
        self.settingwin = SettingWin()
        self.settingwin.show()
        self.close()


class SettingWin(QWidget, setting_ui):

    def __init__(self):
        super(SettingWin, self).__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.gotoMain)
        self.pushButton_6.clicked.connect(self.gotoChart)

    def gotoMain(self):
        self.mainwin = MainWin()
        self.mainwin.show()
        self.close()

    def gotoChart(self):
        self.chartwin = ChartWin()
        self.chartwin.show()
        self.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    mywin = MainWin()
    mywin.show()
    sys.exit(app.exec_())