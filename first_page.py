from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
import sys
from sign_up_form import Ui_SignUp
from admin_page import Ui_adminpage
from user_page import Ui_userpage
import sqlite3



class Ui_home(object):
    def openSignup(self):
        self.window=QtWidgets.QMainWindow()
        self.ui=Ui_SignUp()
        self.ui.setupUi(self.window)
        #home.hide()#Hides this window when next window opens
        self.window.show()
        home.showMinimized()

    def gotouser(self):
        conn=sqlite3.connect("project.db")
        c=conn.cursor()

        #To input details
        userid=str(self.userid.text())
        userpass=str(self.userpass.text())
        print(userid,userpass)

        #we need to check conditions and SQL here
        c1="SELECT * FROM user WHERE Username=? AND Password=?"
        c2=(userid,userpass)
        c.execute(c1,c2)
        results=c.fetchall()
        if results:
            self.window=QtWidgets.QMainWindow()
            self.ui=Ui_userpage()
            self.ui.setupUi(self.window)
            #home.hide()#Hides this window when next window opens
            self.ui.user_name.setText(userid)
            self.window.show()
            home.close()
        else:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Warning)
            msg.setText("Incorrect username or password.")
            msg.setWindowTitle("Error")
            msg.setStandardButtons(QMessageBox.Ok)
            retval = msg.exec_()
        
        

    def gotoadmin(self):
        conn=sqlite3.connect("project.db")
        c=conn.cursor()

        #To input details
        adminid=str(self.adminid.text())
        adminpass=str(self.adminpass.text())
        print(adminid,adminpass)

        #we need to check conditions and SQL here
        c1="SELECT * FROM admin WHERE Username=? AND Password=?"
        c2=(adminid,adminpass)
        c.execute(c1,c2)
        results=c.fetchall()
        if results:
            self.window=QtWidgets.QMainWindow()
            self.ui=Ui_adminpage()
            self.ui.setupUi(self.window)
            self.ui.admin_name.setText(adminid)
            #home.hide()#Hides this window when next window opens
            self.window.show()
            home.close()
        else:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Warning)
            msg.setText("Incorrect username or password.")
            msg.setWindowTitle("Error")
            msg.setStandardButtons(QMessageBox.Ok)
            retval = msg.exec_()

        
    def setupUi(self, home):
        home.setObjectName("home")
        home.resize(1075, 841)
        home.setStatusTip("")
        self.centralwidget = QtWidgets.QWidget(home)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(170, 60, 221, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(90, 150, 401, 51))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(170, 300, 151, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(750, 310, 171, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label_4.setFont(font)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(40, 370, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_5.setFont(font)
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(610, 370, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_6.setFont(font)
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(50, 450, 91, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_7.setFont(font)
        self.label_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(620, 460, 91, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_8.setFont(font)
        self.label_8.setAlignment(QtCore.Qt.AlignCenter)
        self.label_8.setObjectName("label_8")
        self.userlogin = QtWidgets.QPushButton(self.centralwidget)
        self.userlogin.setGeometry(QtCore.QRect(210, 520, 93, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.userlogin.setFont(font)
        self.userlogin.setStyleSheet("border: 1px solid black;")
        self.userlogin.setObjectName("userlogin")

        #go to user page
        self.userlogin.clicked.connect(self.gotouser)

        self.adminlogin = QtWidgets.QPushButton(self.centralwidget)
        self.adminlogin.setGeometry(QtCore.QRect(790, 520, 93, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.adminlogin.setFont(font)
        self.adminlogin.setStyleSheet("border: 1px solid black;")
        self.adminlogin.setObjectName("adminlogin")

        #go to admin page
        self.adminlogin.clicked.connect(self.gotoadmin)

        self.userid = QtWidgets.QLineEdit(self.centralwidget)
        self.userid.setGeometry(QtCore.QRect(170, 370, 171, 31))
        self.userid.setObjectName("userid")
        self.userpass = QtWidgets.QLineEdit(self.centralwidget)
        self.userpass.setGeometry(QtCore.QRect(170, 450, 171, 31))
        self.userpass.setInputMethodHints(QtCore.Qt.ImhHiddenText|QtCore.Qt.ImhNoAutoUppercase|QtCore.Qt.ImhNoPredictiveText|QtCore.Qt.ImhSensitiveData)
        self.userpass.setEchoMode(QtWidgets.QLineEdit.Password)
        self.userpass.setObjectName("userpass")
        self.adminid = QtWidgets.QLineEdit(self.centralwidget)
        self.adminid.setGeometry(QtCore.QRect(750, 370, 171, 31))
        self.adminid.setObjectName("adminid")
        self.adminpass = QtWidgets.QLineEdit(self.centralwidget)
        self.adminpass.setGeometry(QtCore.QRect(750, 450, 171, 31))
        self.adminpass.setToolTip("")
        self.adminpass.setInputMethodHints(QtCore.Qt.ImhHiddenText|QtCore.Qt.ImhNoAutoUppercase|QtCore.Qt.ImhNoPredictiveText|QtCore.Qt.ImhSensitiveData)
        self.adminpass.setEchoMode(QtWidgets.QLineEdit.Password)
        self.adminpass.setObjectName("adminpass")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(160, 600, 741, 41))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_9.setFont(font)
        self.label_9.setAlignment(QtCore.Qt.AlignCenter)
        self.label_9.setObjectName("label_9")
        self.signup = QtWidgets.QPushButton(self.centralwidget)
        self.signup.setGeometry(QtCore.QRect(480, 670, 101, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.signup.setFont(font)
        self.signup.setStyleSheet("border: 1px solid black;")
        self.signup.setObjectName("signup")

        #calling the function to display signup form
        self.signup.clicked.connect(self.openSignup)

        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(550, 30, 401, 243))
        self.label_10.setText("")
        self.label_10.setPixmap(QtGui.QPixmap("bl3.png"))
        self.label_10.setObjectName("label_10")
        home.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(home)
        self.statusbar.setObjectName("statusbar")
        home.setStatusBar(self.statusbar)

        self.retranslateUi(home)
        QtCore.QMetaObject.connectSlotsByName(home)

    def retranslateUi(self, home):
        _translate = QtCore.QCoreApplication.translate
        home.setWindowTitle(_translate("home", "Home Page"))
        self.label.setText(_translate("home", "Welcome!"))
        self.label_2.setText(_translate("home", "Donate Blood, Donate life!"))
        self.label_3.setText(_translate("home", "User Login"))
        self.label_4.setText(_translate("home", "Admin Login"))
        self.label_5.setText(_translate("home", "Username:"))
        self.label_6.setText(_translate("home", "Username:"))
        self.label_7.setText(_translate("home", "Password:"))
        self.label_8.setText(_translate("home", "Password:"))
        self.userlogin.setText(_translate("home", "Login"))
        self.adminlogin.setText(_translate("home", "Login"))
        self.label_9.setText(_translate("home", "Haven\'t donated yet, sign up and be a part of the community!"))
        self.signup.setText(_translate("home", "Sign Up"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    home = QtWidgets.QMainWindow()
    ui = Ui_home()
    ui.setupUi(home)
    home.show()
    sys.exit(app.exec_())
