from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5 import QtCore,uic

import Rresource,icons
import sys
import random

class Welcome(QMainWindow):
	playsignal=QtCore.pyqtSignal()
	def __init__(self,*args,**kwargs):
		super(Welcome,self).__init__()
		uic.loadUi('Welcome.ui',self)
		self.setWindowTitle("Welcome to RPS")
		self.Playbutton.clicked.connect(self.PlaySignal)

	def PlaySignal(self):
		print("Signal Emitted from Play")
		self.playsignal.emit()

class Name(QMainWindow):
	gosignal=QtCore.pyqtSignal(str)
	def __init__(self,*args,**kwargs):
		super(Name,self).__init__()
		uic.loadUi('Name.ui',self)
		self.setWindowTitle("Name")
		
		self.go.clicked.connect(self.GoSignal)

	def GoSignal(self):
		print("Signal Emitted from Go")
		nm=self.name.text()
		if(nm==""):
			nm="You"
		self.gosignal.emit(str(nm))

class RockPaperScissors(QMainWindow):
	rsignal=QtCore.pyqtSignal()
	psignal=QtCore.pyqtSignal()
	ssignal=QtCore.pyqtSignal()
	nsignal=QtCore.pyqtSignal()
	resetsignal=QtCore.pyqtSignal()
	l=["Rock","Paper","Scissors"]
	sscore=0
	yscore=0
    

	def __init__(self,*args,**kwargs):
		super(RockPaperScissors,self).__init__()
		uic.loadUi('RPS.ui',self)
		self.setWindowTitle("Rock Paper Scissors")

		#self.Yourname.setText(self.nm)

		self.rock.clicked.connect(self.RockSignal)
		self.paper.clicked.connect(self.PaperSignal)
		self.scissors.clicked.connect(self.ScissorsSignal)
		self.next.clicked.connect(self.NextSignal)
		self.reset.clicked.connect(self.ResetSignal)

	def RockSignal(self):
		print("Signal emitted from Rock")
		self.rsignal.emit()
		comp=random.choice(self.l)
		self.choosen.setText("Rock")
		self.comp_choice.setText(comp)
		self.paper.setEnabled(False)
		self.scissors.setEnabled(False)

		if(comp=="Paper"):
			self.sscore=self.sscore+1
			self.sys_score.setText(str(self.sscore))
			self.your_score.setText(str(self.yscore))
		elif(comp=="Scissors"):
			self.yscore=self.yscore+1
			self.your_score.setText(str(self.yscore))
			self.sys_score.setText(str(self.sscore))
		elif(comp=="Rock"):
			self.sscore=self.sscore
			self.yscore=self.yscore

	def PaperSignal(self):
		print("Signal emitted from Paper")
		self.psignal.emit()
		comp=random.choice(self.l)
		self.choosen.setText("Paper")
		self.comp_choice.setText(comp)
		self.scissors.setEnabled(False)
		self.rock.setEnabled(False)

		if(comp=="Scissors"):
			self.sscore=self.sscore+1
			self.sys_score.setText(str(self.sscore))
			self.your_score.setText(str(self.yscore))
		elif(comp=="Rock"):
			self.yscore=self.yscore+1
			self.your_score.setText(str(self.yscore))
			self.sys_score.setText(str(self.sscore))
		elif(comp=="Paper"):
			self.sscore=self.sscore
			self.yscore=self.yscore


	def ScissorsSignal(self):
		print("Signal emitted from Scissors")
		self.ssignal.emit()
		comp=random.choice(self.l)
		self.choosen.setText("Scissors")
		self.comp_choice.setText(comp)
		self.rock.setEnabled(False)
		self.paper.setEnabled(False)

		if(comp=="Rock"):
			self.sscore=self.sscore+1
			self.sys_score.setText(str(self.sscore))
			self.your_score.setText(str(self.yscore))
		elif(comp=="Paper"):
			self.yscore=self.yscore+1
			self.your_score.setText(str(self.yscore))
			self.sys_score.setText(str(self.sscore))
		elif(comp=="Scissors"):
			self.sscore=self.sscore
			self.yscore=self.yscore

	def NextSignal(self):
		print("Signal emitted from Next")
		self.nsignal.emit()
		if((self.sscore==5)|(self.yscore==5)):
			if(self.sscore==5):
				self.rock.setEnabled(False)
				self.paper.setEnabled(False)
				self.scissors.setEnabled(False)
				self.result.setText("The System has won this game. Better luck next time")
				
				
			else:
				self.rock.setEnabled(False)
				self.paper.setEnabled(False)
				self.scissors.setEnabled(False)
				self.result.setText("Congratulations...You have Won this game")
				

			

		self.rock.setEnabled(True)
		self.paper.setEnabled(True)
		self.scissors.setEnabled(True)
		self.choosen.setText("")
		self.comp_choice.setText("")

	def ResetSignal(self):
		print("Signal emitted from Reset")
		self.sscore=0
		self.yscore=0
		self.rock.setEnabled(True)
		self.paper.setEnabled(True)
		self.scissors.setEnabled(True)
		self.choosen.setText("")
		self.comp_choice.setText("")
		self.result.setText("")
		self.sys_score.setText("")
		self.your_score.setText("")

class Controller:

	def welcome(self):
		self.w=Welcome()
		self.w.playsignal.connect(self.name)
		self.w.show()

	def name(self):
		self.w.close()
		self.n=Name()
		self.n.gosignal.connect(self.game)
		self.n.show()


	def game(self,nm):
		self.n.close()
		self.a=RockPaperScissors()
		
		self.a.Yourname.setText(nm)
		self.a.show()


if __name__=="__main__":
	app=QApplication(sys.argv)
	ctrl=Controller()
	ctrl.welcome()
	sys.exit(app.exec_())
