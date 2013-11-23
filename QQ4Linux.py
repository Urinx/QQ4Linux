#! /usr/bin/env python
import sys,thread
from PyQt4 import QtGui,QtCore,QtWebKit
class Login(QtGui.QWidget):
	def __init__(self):
		super(Login, self).__init__()
		self.initUI()

	def initUI(self):
		self.setWindowTitle('QQ4Linux')
		#hide titleBar
		self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
		self.setWindowIcon(QtGui.QIcon('img/LinuxQQ.png'))
		#self.setMinimumSize(200,260)
		#self.setMaximumSize(200,260)
		self.setFixedSize(200,260)
		#self.setStyleSheet('background-color:rgba(190,190,190,255)')
		self.setFocus()
		self.center()
		self.loginLayout()
		self.trigger()

	def center(self):
		screen=QtGui.QDesktopWidget().screenGeometry()
		size=self.geometry()
		self.move((screen.width()-size.width())/2,(screen.height()-size.height())/2)

	def loginLayout(self):
		headphoto=QtGui.QLabel(self)
		headphoto.setPixmap(QtGui.QPixmap('img/head.png'))
		headphoto.resize(150,150)
		headphoto.move(25,20)

		self.accout=QtGui.QLineEdit(self)
		self.accout.setPlaceholderText('UserName')
		self.accout.setStyleSheet("background:transparent;border:0px;font-size:12px;padding-left:18px;padding-right:15px;")
		self.pas=QtGui.QLineEdit(self)
		self.pas.setPlaceholderText('PassWord')
		self.pas.setEchoMode(QtGui.QLineEdit.Password)
		self.pas.setStyleSheet("background:transparent;border:0px;font-size:12px;padding-left:18px;padding-right:15px;")

		size=self.geometry()
		w=size.width()
		lw=100
		self.accout.resize(lw,20)
		self.accout.move((w-lw)/2,190)
		self.pas.resize(lw,20)
		self.pas.move((w-lw)/2,220)

	def trigger(self):
		quit=QtGui.QAction(QtGui.QIcon(''),'Exit',self)
		quit.setShortcut('Ctrl+Q')
		quit.setStatusTip('quit the login.')
		quit.triggered.connect(QtGui.qApp.quit)
		self.addAction(quit)

		# submit=QtGui.QAction(QtGui.QIcon(''),'Submit',self)
		# submit.setShortcut(QtCore.Qt.Key_Return)
		# submit.setStatusTip('submit the name&password')
		# submit.triggered.connect(self.check)
		# self.addAction(submit)

	def moveEvent(self,e):
		self.center()

	def keyPressEvent(self,event):
		keyEvent=QtGui.QKeyEvent(event)
		if keyEvent.key()==QtCore.Qt.Key_Return:
			self.check()

	def check(self):
		if not self.accout.text() or not self.pas.text():
			mb=QtGui.QMessageBox.warning(self,'Warning','UserName or PassWord is Idle!',QtGui.QMessageBox.Yes,QtGui.QMessageBox.No)
			if mb==QtGui.QMessageBox.No:
				sys.exit()
		else:
			self.checkpas(self.accout.text(),self.pas.text())
		

	def checkpas(self,acc,pas):
		if self.checkInSQL(acc,pas):
			self.close()
			qq.show()
			qq.initUI()

	def checkInSQL(self,acc,pas):
		return True

	def test(self):
		QtGui.QMessageBox.question(self,'Message','test',QtGui.QMessageBox.Yes,QtGui.QMessageBox.No)

class Splash(QtGui.QSplashScreen):
	def __init__(self):
		super(Splash, self).__init__()
		self.setPixmap(QtGui.QPixmap("img/apple.png"))
		self.show()

		self.timer=QtCore.QBasicTimer()
		self.step=0
		self.timer.start(30,self)

	def timerEvent(self,event):
		if self.step>=30:
			self.timer.stop()
			self.finish(login)
			login.show()
		self.step+=1

class QQ(QtGui.QWidget):
	def __init__(self):
		super(QQ,self).__init__()
		self.initWin()
		self.trigger()
		self.setPosition()
		self.setFocus()
		#self.initUI()

	def initWin(self):
		self.setWindowTitle('QQ For Linux')
		self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
		self.setWindowIcon(QtGui.QIcon('img/LinuxQQ.png'))
		pix=QtGui.QPixmap("img/iphone-big-image.png","0")
		#pix=QtGui.QPixmap("iphone-big-image.png","0",QtCore.Qt.AvoidDither|QtCore.Qt.ThresholdDither|QtCore.Qt.ThresholdAlphaDither)
		self.resize(pix.size())
		self.setMask(pix.mask())
		self.dragPosition=None

	def initUI(self):
		webqq=QtWebKit.QWebView()
		webqq.load(QtCore.QUrl('http://paiplace.5gbfree.com/QQ/Introduction.html'))
		webqq.setFixedSize(264,454)
		
		vbox=QtGui.QVBoxLayout()
		vbox.addSpacing(25)

		hbox=QtGui.QHBoxLayout()
		hbox.addSpacing(6)
		hbox.addWidget(webqq)

		vbox.addLayout(hbox)
		self.setLayout(vbox)

	def mousePressEvent(self,event):
		if event.button()==QtCore.Qt.LeftButton:
			self.dragPosition=event.globalPos()-self.frameGeometry().topLeft()
			event.accept()
		if event.button()==QtCore.Qt.RightButton:
			self.close()

	def mouseMoveEvent(self,event):
		if event.buttons() & QtCore.Qt.LeftButton:
			self.move(event.globalPos()-self.dragPosition)
			event.accept()

	def paintEvent(self,event):
		painter=QtGui.QPainter(self)
		painter.drawPixmap(0,0,QtGui.QPixmap("img/iphone-big-image.png"))

	def trigger(self):
		quit=QtGui.QAction(QtGui.QIcon(''),'Exit',self)
		quit.setShortcut('Ctrl+Q')
		quit.setStatusTip('quit the login.')
		quit.triggered.connect(QtGui.qApp.quit)
		self.addAction(quit)

	def setPosition(self):
		screen=QtGui.QDesktopWidget().screenGeometry()
		size=self.geometry()
		self.move(screen.width()-size.width(),(screen.height()-size.height())/2)		

if __name__=='__main__':
	app=QtGui.QApplication(sys.argv)
	splash=Splash()
	app.processEvents()
	login=Login()
	qq=QQ()
	sys.exit(app.exec_())