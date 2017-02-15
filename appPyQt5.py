#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
This program creates a simple window in PyQt5.

Author: Batuto
Website: github.com/Batuto
Last edited: February 2017
"""

import sys
from PyQt5.QtWidgets import QApplication, QWidget

def main():
    app = QApplication(sys.argv)

    window = QWidget()
    window.setWindowTitle('My First App')
    window.resize(600, 300)
    window.move(300, 300)
    window.show()
    
    sys.exit(app.exec_())
    

if __name__ == '__main__':
    main()