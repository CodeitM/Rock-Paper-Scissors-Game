from PyQt5.QtWidgets import QMainWindow,QApplication
from PyQt5 import QtCore,uic
import sys
class MyWindow2(QMainWindow):
	def __init__(self,*args,**kwargs):
		super(MyWindow2,self).__init__()
		uic.loadUi('main.ui',self)
		self.setWindowTitle("My app2")
class MyWindow(QMainWindow):
	signal=QtCore.pyqtSignal()
	def __init__(self,*args,**kwargs):
		super(MyWindow,self).__init__()
		uic.loadUi('main.ui',self)
		self.setWindowTitle("My app")
		self.start.clicked.connect(self.show_hello)
	def show_hello(self):
		print("emitting signal")
		self.signal.emit()

class controller:
	def show_main(self):
		self.a=MyWindow()
		self.a.signal.connect(self.next_window)
		self.a.show()
		
	def next_window(self):
		self.a.close()
		self.b=MyWindow2()
		self.b.show()

if __name__ == '__main__':
	app=QApplication(sys.argv)
	ctrl=controller()
	ctrl.show_main()
	sys.exit(app.exec_())
