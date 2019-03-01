#!/usr/bin/env python

import sys
import mido
from PyQt5 import QtWidgets, uic

qtCreatorFile = 'junolab.ui'
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
        self.vcf_hpf_slider.valueChanged.connect(
            lambda: self.on_slider_change(9, self.vcf_hpf_slider))
        self.vcf_freq_slider.valueChanged.connect(
            lambda: self.on_slider_change(16, self.vcf_freq_slider))
        self.vcf_res_slider.valueChanged.connect(
            lambda: self.on_slider_change(17, self.vcf_res_slider))
        self.vcf_lfo_slider.valueChanged.connect(
            lambda: self.on_slider_change(18, self.vcf_lfo_slider))
        self.vcf_key_flw_slider.valueChanged.connect(
            lambda: self.on_slider_change(20, self.vcf_key_flw_slider))
        self.vcf_after_slider.valueChanged.connect(
            lambda: self.on_slider_change(21, self.vcf_after_slider))
        self.vcf_env_slider.valueChanged.connect(
            lambda: self.on_slider_change(19, self.vcf_env_slider))
        self.vcf_env_mode_env_rbutton.pressed.connect(
            lambda: self.on_button_press(1, 0))
        self.vcf_env_mode_inv_rbutton.pressed.connect(
            lambda: self.on_button_press(1, 1))
        self.vcf_env_mode_denv_rbutton.pressed.connect(
            lambda: self.on_button_press(1, 2))
        self.vcf_env_mode_dyn_rbutton.pressed.connect(
            lambda: self.on_button_press(1, 3))

        self.env_t1_slider.valueChanged.connect(
            lambda: self.on_slider_change(26, self.env_t1_slider))
        self.env_l1_slider.valueChanged.connect(
            lambda: self.on_slider_change(27, self.env_l1_slider))
        self.env_t2_slider.valueChanged.connect(
            lambda: self.on_slider_change(28, self.env_t2_slider))
        self.env_l2_slider.valueChanged.connect(
            lambda: self.on_slider_change(29, self.env_l2_slider))
        self.env_t3_slider.valueChanged.connect(
            lambda: self.on_slider_change(30, self.env_t3_slider))
        self.env_l3_slider.valueChanged.connect(
            lambda: self.on_slider_change(31, self.env_l3_slider))
        self.env_t4_slider.valueChanged.connect(
            lambda: self.on_slider_change(32, self.env_t4_slider))
        self.env_key_flw_slider.valueChanged.connect(
            lambda: self.on_slider_change(33, self.env_key_flw_slider))

    # Slots

    def on_slider_change(self, parameter, slider):
        sysex_send_ipr(parameter, slider.value())

    def on_button_press(self, parameter, value):
        sysex_send_ipr(parameter, value)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = JunoLab()
    window.show()
    sys.exit(app.exec_())
