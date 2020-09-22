import sys

from PyQt5.QtWidgets import QApplication

from screenshot import Screenshot

if __name__ == '__main__':
    app = QApplication(sys.argv)
    s = Screenshot()
    s.app = app
    s.capture('http://chungtoimuontudo2.wordpress.com', 'chungtoimuontudo2.png')
    sys.exit(app.exec_())