# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'd:/GIT/nodes/PyFlow/GraphEditor_ui.ui'
#
# Created: Wed Feb 21 14:51:09 2018
#      by: pyside2-uic 2.0.0 running on PySide2 2.0.0~alpha0
#
# WARNING! All changes made in this file will be lost!

from Qt import QtCompat, QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(1608, 875)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/resources/LogoBpApp.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setDocumentMode(False)
        MainWindow.setDockOptions(QtWidgets.QMainWindow.AllowTabbedDocks)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_3.setSpacing(1)
        self.gridLayout_3.setContentsMargins(1, 1, 1, 1)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.horizontal_splitter = QtWidgets.QSplitter(self.centralwidget)
        self.horizontal_splitter.setStyleSheet("")
        self.horizontal_splitter.setOrientation(QtCore.Qt.Horizontal)
        self.horizontal_splitter.setObjectName("horizontal_splitter")
        self.SceneWidget = QtWidgets.QWidget(self.horizontal_splitter)
        self.SceneWidget.setObjectName("SceneWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.SceneWidget)
        self.gridLayout.setContentsMargins(1, 1, 1, 1)
        self.gridLayout.setObjectName("gridLayout")
        self.SceneLayout = QtWidgets.QGridLayout()
        self.SceneLayout.setSizeConstraint(QtWidgets.QLayout.SetMaximumSize)
        self.SceneLayout.setContentsMargins(0, 0, 0, 0)
        self.SceneLayout.setObjectName("SceneLayout")
        self.gridLayout.addLayout(self.SceneLayout, 0, 0, 1, 1)
        self.gridLayout_3.addWidget(self.horizontal_splitter, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 1608, 26))
        self.menuBar.setObjectName("menuBar")
        self.menuEdit = QtWidgets.QMenu(self.menuBar)
        self.menuEdit.setObjectName("menuEdit")
        self.menuView = QtWidgets.QMenu(self.menuBar)
        self.menuView.setObjectName("menuView")
        self.menuFile = QtWidgets.QMenu(self.menuBar)
        self.menuFile.setObjectName("menuFile")
        self.menuHelp = QtWidgets.QMenu(self.menuBar)
        self.menuHelp.setObjectName("menuHelp")
        self.menuPlugins = QtWidgets.QMenu(self.menuBar)
        self.menuPlugins.setObjectName("menuPlugins")
        MainWindow.setMenuBar(self.menuBar)
        self.toolBar = QtWidgets.QToolBar(MainWindow)
        self.toolBar.setObjectName("toolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.dockWidgetVariables = QtWidgets.QDockWidget(MainWindow)
        self.dockWidgetVariables.setMinimumSize(QtCore.QSize(150, 113))
        self.dockWidgetVariables.setFloating(False)
        self.dockWidgetVariables.setFeatures(QtWidgets.QDockWidget.AllDockWidgetFeatures)
        self.dockWidgetVariables.setObjectName("dockWidgetVariables")
        self.dockWidgetContents_5 = QtWidgets.QWidget()
        self.dockWidgetContents_5.setObjectName("dockWidgetContents_5")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.dockWidgetContents_5)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.scrollArea_2 = QtWidgets.QScrollArea(self.dockWidgetContents_5)
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollArea_2.setObjectName("scrollArea_2")
        self.scrollAreaWidgetContents_2 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_2.setGeometry(QtCore.QRect(0, 0, 148, 756))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.scrollAreaWidgetContents_2.sizePolicy().hasHeightForWidth())
        self.scrollAreaWidgetContents_2.setSizePolicy(sizePolicy)
        self.scrollAreaWidgetContents_2.setObjectName("scrollAreaWidgetContents_2")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.scrollAreaWidgetContents_2)
        self.gridLayout_5.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.leftDockGridLayout = QtWidgets.QGridLayout()
        self.leftDockGridLayout.setObjectName("leftDockGridLayout")
        self.gridLayout_5.addLayout(self.leftDockGridLayout, 0, 0, 1, 1)
        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_2)
        self.verticalLayout_2.addWidget(self.scrollArea_2)
        self.dockWidgetVariables.setWidget(self.dockWidgetContents_5)
        MainWindow.addDockWidget(QtCore.Qt.DockWidgetArea(2), self.dockWidgetVariables)
        self.statusBar = QtWidgets.QStatusBar(MainWindow)
        self.statusBar.setObjectName("statusBar")
        MainWindow.setStatusBar(self.statusBar)
        self.dockWidgetNodeView = QtWidgets.QDockWidget(MainWindow)
        self.dockWidgetNodeView.setMinimumSize(QtCore.QSize(500, 166))
        self.dockWidgetNodeView.setAllowedAreas(QtCore.Qt.AllDockWidgetAreas)
        self.dockWidgetNodeView.setObjectName("dockWidgetNodeView")
        self.dockWidgetContents = QtWidgets.QWidget()
        self.dockWidgetContents.setObjectName("dockWidgetContents")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.dockWidgetContents)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.scrollArea = QtWidgets.QScrollArea(self.dockWidgetContents)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents_3 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_3.setGeometry(QtCore.QRect(0, 0, 498, 594))
        self.scrollAreaWidgetContents_3.setObjectName("scrollAreaWidgetContents_3")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.scrollAreaWidgetContents_3)
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setObjectName("formLayout")
        self.gridLayout_4.addLayout(self.formLayout, 0, 0, 1, 1)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents_3)
        self.verticalLayout.addWidget(self.scrollArea)
        self.dockWidgetNodeView.setWidget(self.dockWidgetContents)
        MainWindow.addDockWidget(QtCore.Qt.DockWidgetArea(1), self.dockWidgetNodeView)
        self.dockWidgetUndoStack = QtWidgets.QDockWidget(MainWindow)
        self.dockWidgetUndoStack.setEnabled(True)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/icons/resources/history.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.dockWidgetUndoStack.setWindowIcon(icon1)
        self.dockWidgetUndoStack.setObjectName("dockWidgetUndoStack")
        self.dockWidgetContents_3 = QtWidgets.QWidget()
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.dockWidgetContents_3.sizePolicy().hasHeightForWidth())
        self.dockWidgetContents_3.setSizePolicy(sizePolicy)
        self.dockWidgetContents_3.setObjectName("dockWidgetContents_3")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.dockWidgetContents_3)
        self.gridLayout_6.setSpacing(1)
        self.gridLayout_6.setContentsMargins(1, 1, 1, 1)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.dockWidgetUndoStack.setWidget(self.dockWidgetContents_3)
        MainWindow.addDockWidget(QtCore.Qt.DockWidgetArea(1), self.dockWidgetUndoStack)
        self.actionDelete = QtWidgets.QAction(MainWindow)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/icons/resources/delete_icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionDelete.setIcon(icon2)
        self.actionDelete.setObjectName("actionDelete")
        self.actionSave = QtWidgets.QAction(MainWindow)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/icons/resources/save_icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionSave.setIcon(icon3)
        self.actionSave.setObjectName("actionSave")
        self.actionLoad = QtWidgets.QAction(MainWindow)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/icons/resources/folder_open_icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionLoad.setIcon(icon4)
        self.actionLoad.setObjectName("actionLoad")
        self.actionSave_as = QtWidgets.QAction(MainWindow)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/icons/resources/save_as_icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionSave_as.setIcon(icon5)
        self.actionSave_as.setObjectName("actionSave_as")
        self.actionPlot_graph = QtWidgets.QAction(MainWindow)
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(":/icons/resources/plot_icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionPlot_graph.setIcon(icon6)
        self.actionPlot_graph.setObjectName("actionPlot_graph")
        self.actionScreenshot = QtWidgets.QAction(MainWindow)
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap(":/icons/resources/screenshot_icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionScreenshot.setIcon(icon7)
        self.actionScreenshot.setObjectName("actionScreenshot")
        self.actionShortcuts = QtWidgets.QAction(MainWindow)
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap(":/icons/resources/shortcuts_icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionShortcuts.setIcon(icon8)
        self.actionShortcuts.setObjectName("actionShortcuts")
        self.actionAlignLeft = QtWidgets.QAction(MainWindow)
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap(":/icons/resources/alignleft.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionAlignLeft.setIcon(icon9)
        self.actionAlignLeft.setObjectName("actionAlignLeft")
        self.actionAlignUp = QtWidgets.QAction(MainWindow)
        icon10 = QtGui.QIcon()
        icon10.addPixmap(QtGui.QPixmap(":/icons/resources/aligntop.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionAlignUp.setIcon(icon10)
        self.actionAlignUp.setObjectName("actionAlignUp")
        self.actionPropertyView = QtWidgets.QAction(MainWindow)
        icon11 = QtGui.QIcon()
        icon11.addPixmap(QtGui.QPixmap(":/icons/resources/property_icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionPropertyView.setIcon(icon11)
        self.actionPropertyView.setObjectName("actionPropertyView")
        self.actionAlignBottom = QtWidgets.QAction(MainWindow)
        icon12 = QtGui.QIcon()
        icon12.addPixmap(QtGui.QPixmap(":/icons/resources/alignbottom.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionAlignBottom.setIcon(icon12)
        self.actionAlignBottom.setObjectName("actionAlignBottom")
        self.actionAlignRight = QtWidgets.QAction(MainWindow)
        icon13 = QtGui.QIcon()
        icon13.addPixmap(QtGui.QPixmap(":/icons/resources/alignright.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionAlignRight.setIcon(icon13)
        self.actionAlignRight.setObjectName("actionAlignRight")
        self.actionNew_Node = QtWidgets.QAction(MainWindow)
        icon14 = QtGui.QIcon()
        icon14.addPixmap(QtGui.QPixmap(":/icons/resources/brick.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionNew_Node.setIcon(icon14)
        self.actionNew_Node.setObjectName("actionNew_Node")
        self.actionNew_Command = QtWidgets.QAction(MainWindow)
        icon15 = QtGui.QIcon()
        icon15.addPixmap(QtGui.QPixmap(":/icons/resources/script.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionNew_Command.setIcon(icon15)
        self.actionNew_Command.setObjectName("actionNew_Command")
        self.actionFunction_Library = QtWidgets.QAction(MainWindow)
        icon16 = QtGui.QIcon()
        icon16.addPixmap(QtGui.QPixmap(":/icons/resources/function.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionFunction_Library.setIcon(icon16)
        self.actionFunction_Library.setObjectName("actionFunction_Library")
        self.actionClear_history = QtWidgets.QAction(MainWindow)
        icon17 = QtGui.QIcon()
        icon17.addPixmap(QtGui.QPixmap(":/icons/resources/clear_icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionClear_history.setIcon(icon17)
        self.actionClear_history.setObjectName("actionClear_history")
        self.actionVariables = QtWidgets.QAction(MainWindow)
        icon18 = QtGui.QIcon()
        icon18.addPixmap(QtGui.QPixmap(":/icons/resources/variable.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionVariables.setIcon(icon18)
        self.actionVariables.setObjectName("actionVariables")
        self.actionHistory = QtWidgets.QAction(MainWindow)
        self.actionHistory.setIcon(icon1)
        self.actionHistory.setObjectName("actionHistory")
        self.actionNew_pin = QtWidgets.QAction(MainWindow)
        icon19 = QtGui.QIcon()
        icon19.addPixmap(QtGui.QPixmap(":/icons/resources/pin.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionNew_pin.setIcon(icon19)
        self.actionNew_pin.setObjectName("actionNew_pin")
        self.menuEdit.addAction(self.actionDelete)
        self.menuEdit.addSeparator()
        self.menuEdit.addAction(self.actionClear_history)
        self.menuView.addAction(self.actionVariables)
        self.menuView.addAction(self.actionHistory)
        self.menuView.addAction(self.actionPropertyView)
        self.menuFile.addAction(self.actionSave)
        self.menuFile.addAction(self.actionLoad)
        self.menuFile.addAction(self.actionSave_as)
        self.menuHelp.addAction(self.actionPlot_graph)
        self.menuHelp.addAction(self.actionShortcuts)
        self.menuPlugins.addAction(self.actionNew_Node)
        self.menuPlugins.addAction(self.actionNew_Command)
        self.menuPlugins.addAction(self.actionFunction_Library)
        self.menuPlugins.addAction(self.actionNew_pin)
        self.menuBar.addAction(self.menuFile.menuAction())
        self.menuBar.addAction(self.menuEdit.menuAction())
        self.menuBar.addAction(self.menuView.menuAction())
        self.menuBar.addAction(self.menuPlugins.menuAction())
        self.menuBar.addAction(self.menuHelp.menuAction())
        self.toolBar.addAction(self.actionPropertyView)
        self.toolBar.addAction(self.actionVariables)
        self.toolBar.addAction(self.actionHistory)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionPlot_graph)
        self.toolBar.addAction(self.actionScreenshot)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionAlignLeft)
        self.toolBar.addAction(self.actionAlignUp)
        self.toolBar.addAction(self.actionAlignBottom)
        self.toolBar.addAction(self.actionAlignRight)
        self.toolBar.addSeparator()

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtCompat.translate("MainWindow", "PyFlow", None, -1))
        self.menuEdit.setTitle(QtCompat.translate("MainWindow", "Edit", None, -1))
        self.menuView.setTitle(QtCompat.translate("MainWindow", "View", None, -1))
        self.menuFile.setTitle(QtCompat.translate("MainWindow", "File", None, -1))
        self.menuHelp.setTitle(QtCompat.translate("MainWindow", "Help", None, -1))
        self.menuPlugins.setTitle(QtCompat.translate("MainWindow", "Plugins", None, -1))
        self.toolBar.setWindowTitle(QtCompat.translate("MainWindow", "toolBar", None, -1))
        self.dockWidgetVariables.setWindowTitle(QtCompat.translate("MainWindow", "Variables", None, -1))
        self.dockWidgetNodeView.setWindowTitle(QtCompat.translate("MainWindow", "PropertyView", None, -1))
        self.dockWidgetUndoStack.setWindowTitle(QtCompat.translate("MainWindow", "History", None, -1))
        self.actionDelete.setText(QtCompat.translate("MainWindow", "Delete", None, -1))
        self.actionSave.setText(QtCompat.translate("MainWindow", "Save", None, -1))
        self.actionLoad.setText(QtCompat.translate("MainWindow", "Load", None, -1))
        self.actionSave_as.setText(QtCompat.translate("MainWindow", "Save as", None, -1))
        self.actionPlot_graph.setText(QtCompat.translate("MainWindow", "Plot graph", None, -1))
        self.actionScreenshot.setText(QtCompat.translate("MainWindow", "Screenshot", None, -1))
        self.actionShortcuts.setText(QtCompat.translate("MainWindow", "Shortcuts", None, -1))
        self.actionAlignLeft.setText(QtCompat.translate("MainWindow", "AlignLeft", None, -1))
        self.actionAlignLeft.setToolTip(QtCompat.translate("MainWindow", "Align selected nodes by the left most", None, -1))
        self.actionAlignUp.setText(QtCompat.translate("MainWindow", "AlignUp", None, -1))
        self.actionAlignUp.setToolTip(QtCompat.translate("MainWindow", "Align selected nodes by the up most", None, -1))
        self.actionPropertyView.setText(QtCompat.translate("MainWindow", "PropertyView", None, -1))
        self.actionPropertyView.setToolTip(QtCompat.translate("MainWindow", "toggle property view", None, -1))
        self.actionAlignBottom.setText(QtCompat.translate("MainWindow", "AlignBottom", None, -1))
        self.actionAlignRight.setText(QtCompat.translate("MainWindow", "alignRight", None, -1))
        self.actionNew_Node.setText(QtCompat.translate("MainWindow", "New node", None, -1))
        self.actionNew_Node.setToolTip(QtCompat.translate("MainWindow", "New node", None, -1))
        self.actionNew_Command.setText(QtCompat.translate("MainWindow", "New editor command", None, -1))
        self.actionNew_Command.setToolTip(QtCompat.translate("MainWindow", "New editor command", None, -1))
        self.actionFunction_Library.setText(QtCompat.translate("MainWindow", "New function library", None, -1))
        self.actionFunction_Library.setToolTip(QtCompat.translate("MainWindow", "New function library", None, -1))
        self.actionClear_history.setText(QtCompat.translate("MainWindow", "Clear history", None, -1))
        self.actionVariables.setText(QtCompat.translate("MainWindow", "Variables", None, -1))
        self.actionHistory.setText(QtCompat.translate("MainWindow", "History", None, -1))
        self.actionNew_pin.setText(QtCompat.translate("MainWindow", "New pin", None, -1))

import nodes_res_rc
