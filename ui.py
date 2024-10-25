import sys
from PySide6.QtWidgets import (QApplication, QMainWindow, QMenu, QToolBar, QLabel, QStatusBar)
from PySide6.QtGui import QIcon, QAction
from PySide6.QtCore import QTimer, Qt


class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Жук Никита Сергеевич №8")
        self.counter = 0

        self.counter_label = QLabel(f"Current Score: {self.counter}", self)
        self.counter_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.setCentralWidget(self.counter_label)

        self.statusBar = QStatusBar()
        self.setStatusBar(self.statusBar)

        menubar = self.menuBar()
        menu = None
        for i in range(3):
            menu = QMenu(f"Add {i * 3 + 1} - {i * 3 + 3}", self)
            menubar.addMenu(menu)
            for j in range(1, 4):
                action = QAction(f"Add {i * 3 + j}", self)
                action.triggered.connect(lambda checked, jl=j, il=i: self.changeCounter(il * 3 + jl))
                menu.addAction(action)

        exit_action = QAction("Exit", self)
        exit_action.triggered.connect(self.close)
        menu.addAction(exit_action)

        toolbar = QToolBar("Main Toolbar")
        icon_paths = [
            QIcon.fromTheme("document-new"),
            QIcon.fromTheme("document-open"),
            # QIcon.fromTheme("document-save"),
            # QIcon.fromTheme("document-properties")
        ]
        toolbar_action_name = [
            'New Game', 'Open Game',  # 'Save Game', 'Settings'
        ]

        for i in range(len(icon_paths)):
            action = QAction(icon_paths[i], toolbar_action_name[i], self)
            toolbar.addAction(action)

            action.triggered.connect(
                lambda checked, display_time=i + 1, button_name=toolbar_action_name[i]:
                    self.displayStatus(f"Action {button_name} executed!", display_time)
            )

        self.addToolBar(toolbar)

    def changeCounter(self, amount):
        self.counter += amount
        self.counter_label.setText(f"Current Score: {self.counter}")

    def displayStatus(self, text, time_to_display):
        self.statusBar.showMessage(text, time_to_display * 1000)


def main():
    app = QApplication(sys.argv)

    window = MyWindow()
    window.resize(1200, 900)
    window.show()

    sys.exit(app.exec())
