from PyQt5.QtWidgets import QMessageBox


class ErrorMessageBox(QMessageBox):
    def __init__(self, parent, text, informative, detailed):
        super().__init__(parent=parent)
        self.setText(text)
        self.setInformativeText(informative)
        self.setDetailedText(detailed)
        self.setIcon(QMessageBox.Critical)