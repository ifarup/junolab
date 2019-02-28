#!/usr/bin/env python

import sys
import mido
from PyQt5 import QtWidgets, uic

qtCreatorFile = 'main.ui'
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

def sysex_send_ipr(parameter, value, channel=0):
    msg = mido.Message('sysex', data=[0b01000001,
                                      0b00110110,
                                      channel,
                                      0b00100011,
                                      0b00100000,
                                      0b00000001,
                                      parameter,
                                      value])
    print(msg.hex())

class JunoLab(QtWidgets.QMainWindow, Ui_MainWindow):

    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        # Connect up the controls
        self.vcf_hpf_slider.valueChanged.connect(self.vcf_hpf_slot)
        self.vcf_freq_slider.valueChanged.connect(self.vcf_freq_slot)
        self.vcf_res_slider.valueChanged.connect(self.vcf_res_slot)
        self.vcf_lfo_slider.valueChanged.connect(self.vcf_lfo_slot)
        self.vcf_key_flw_slider.valueChanged.connect(self.vcf_key_flw_slot)
        self.vcf_after_slider.valueChanged.connect(self.vcf_after_slot)
        self.vcf_env_slider.valueChanged.connect(self.vcf_env_slot)
        self.vcf_env_mode_env_rbutton.pressed.connect(self.vcf_env_mode_env_slot)
        self.vcf_env_mode_inv_rbutton.pressed.connect(self.vcf_env_mode_inv_slot)
        self.vcf_env_mode_denv_rbutton.pressed.connect(self.vcf_env_mode_denv_slot)
        self.vcf_env_mode_dyn_rbutton.pressed.connect(self.vcf_env_mode_dyn_slot)

    def vcf_hpf_slot(self):
        val = self.vcf_hpf_slider.value()
        sysex_send_ipr(9, val)

    def vcf_freq_slot(self):
        val = self.vcf_freq_slider.value()
        sysex_send_ipr(16, val)

    def vcf_res_slot(self):
        val = self.vcf_res_slider.value()
        sysex_send_ipr(17, val)

    def vcf_lfo_slot(self):
        val = self.vcf_lfo_slider.value()
        sysex_send_ipr(18, val)

    def vcf_key_flw_slot(self):
        val = self.vcf_key_flw_slider.value()
        sysex_send_ipr(20, val)

    def vcf_after_slot(self):
        val = self.vcf_after_slider.value()
        sysex_send_ipr(21, val)

    def vcf_env_slot(self):
        val = self.vcf_env_slider.value()
        sysex_send_ipr(19, val)

    def vcf_env_mode_env_slot(self):
        sysex_send_ipr(1, 0)

    def vcf_env_mode_inv_slot(self):
        sysex_send_ipr(1, 1)

    def vcf_env_mode_denv_slot(self):
        sysex_send_ipr(1, 2)

    def vcf_env_mode_dyn_slot(self):
        sysex_send_ipr(1, 3)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = JunoLab()
    window.show()
    sys.exit(app.exec_())
