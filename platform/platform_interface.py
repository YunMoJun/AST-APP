# coding:utf-8
import sys

from PyQt6.QtCore import Qt, QUrl
from PyQt6.QtGui import QIcon, QDesktopServices
from PyQt6.QtWidgets import QApplication, QFrame, QHBoxLayout
from qfluentwidgets import (NavigationItemPosition, MessageBox, setTheme, Theme, FluentWindow,
                            NavigationAvatarWidget, qrouter, SubtitleLabel, setFont, InfoBadge,
                            InfoBadgePosition, FluentBackgroundTheme)
from qfluentwidgets import FluentIcon as FIF


class Widget(QFrame):

    def __init__(self, text: str, parent=None):
        super().__init__(parent=parent)
        self.label = SubtitleLabel(text, self)
        self.hBoxLayout = QHBoxLayout(self)

        setFont(self.label, 24)
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.hBoxLayout.addWidget(self.label, 1, Qt.AlignmentFlag.AlignCenter)
        self.setObjectName(text.replace(' ', '-'))


class Window(FluentWindow):

    def __init__(self):
        super().__init__()

        # create sub interface
        self.homeInterface = Widget('Search Interface', self)
        self.globeInterface = Widget('Wifi Interface', self)
        self.fingerprintInterface = Widget('Media Interface', self)
        self.accountInterface = Widget('Account Interface', self)
        self.qrcodeInterface = Widget('Qrcode Interface', self)


        self.settingInterface = Widget('Setting Interface', self)

        self.alignmentInterface = Widget('Album Interface', self)
        self.alignmentInterface1 = Widget('Album Interface 1', self)
        self.alignmentInterface2 = Widget('Album Interface 2', self)
        self.alignmentInterface3 = Widget('Album Interface 3', self)
        self.alignmentInterface3_1 = Widget('Album Interface 3-1', self)
        self.alignmentInterface3_2 = Widget('Album Interface 3-2', self)
        self.alignmentInterface4 = Widget('Album Interface 4', self)
        self.alignmentInterface5 = Widget('Album Interface 5', self)
        self.alignmentInterface6 = Widget('Album Interface 6', self)

        self.initNavigation()
        self.initWindow()

    def initNavigation(self):
        self.addSubInterface(self.homeInterface, FIF.HOME, '主页')
        self.addSubInterface(self.qrcodeInterface, FIF.QRCODE, '二维码生成')

        self.navigationInterface.addSeparator()

        self.addSubInterface(self.globeInterface, FIF.GLOBE, '链接服务器')
        self.addSubInterface(self.fingerprintInterface, FIF.FINGERPRINT, '账户密码管理')
        self.addSubInterface(self.accountInterface, FIF.PIE_SINGLE, '收支系统')

        self.navigationInterface.addSeparator()

        self.addSubInterface(self.alignmentInterface, FIF.ALIGNMENT, '导航页', NavigationItemPosition.SCROLL)
        self.addSubInterface(self.alignmentInterface1, FIF.ALIGNMENT, '收藏网址', parent=self.alignmentInterface)
        self.addSubInterface(self.alignmentInterface2, FIF.ALIGNMENT, '官网', parent=self.alignmentInterface)
        self.addSubInterface(self.alignmentInterface3, FIF.ALIGNMENT, '金融', parent=self.alignmentInterface)
        self.addSubInterface(self.alignmentInterface3_1, FIF.ALIGNMENT, '银行', parent=self.alignmentInterface3)
        self.addSubInterface(self.alignmentInterface3_2, FIF.ALIGNMENT, '证券', parent=self.alignmentInterface3)
        self.addSubInterface(self.alignmentInterface4, FIF.ALIGNMENT, '网址4', parent=self.alignmentInterface)
        self.addSubInterface(self.alignmentInterface5, FIF.ALIGNMENT, '网址5', parent=self.alignmentInterface)
        self.addSubInterface(self.alignmentInterface6, FIF.ALIGNMENT, '网址6', parent=self.alignmentInterface)





        # add custom widget to bottom
        self.navigationInterface.addWidget(
            routeKey='avatar',
            widget=NavigationAvatarWidget('AST-APP', 'resource/logo.png'),
            onClick=self.showMessageBox,
            position=NavigationItemPosition.BOTTOM,
        )

        self.addSubInterface(self.settingInterface, FIF.SETTING, 'Settings', NavigationItemPosition.BOTTOM)

        # add badge to navigation item
        # item = self.navigationInterface.widget(self.alignmentInterface.objectName())
        # InfoBadge.attension(
        #     text=9,
        #     parent=item.parent(),
        #     target=item,
        #     position=InfoBadgePosition.NAVIGATION_ITEM
        # )

        # NOTE: enable acrylic effect
        # self.navigationInterface.setAcrylicEnabled(True)

        # disable pop animation
        # self.stackedWidget.setAnimationEnabled(False)

    def initWindow(self):
        self.resize(900, 700)
        self.setWindowIcon(QIcon(':/qfluentwidgets/images/logo.png'))
        self.setWindowTitle('AST-APP')

        desktop = QApplication.screens()[0].availableGeometry()
        w, h = desktop.width(), desktop.height()
        self.move(w//2 - self.width()//2, h//2 - self.height()//2)

        # set the minimum window width that allows the navigation panel to be expanded
        # self.navigationInterface.setMinimumExpandWidth(900)
        # self.navigationInterface.expand(useAni=False)

    def showMessageBox(self):
        w = MessageBox(
            'AST-APP',
            '继续开发，后续支持个人登录，登录后可以个性化导航页',
            self
        )
        w.yesButton.setText('支持')
        w.cancelButton.setText('加油')

        if w.exec():
            QDesktopServices.openUrl(QUrl("https://github.com/yunmojun/ast-app"))




if __name__ == '__main__':
    # setTheme(Theme.DARK)

    app = QApplication(sys.argv)
    w = Window()
    w.show()
    app.exec()
