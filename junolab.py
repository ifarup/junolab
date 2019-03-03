#!/usr/bin/env python3

import sys
import mido
from PyQt5 import QtWidgets, uic
from PyQt5.QtCore import QRegExp
from PyQt5.QtGui import QRegExpValidator

qtCreatorFile = 'junolab.ui'
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)


class JunoLab(QtWidgets.QMainWindow, Ui_MainWindow):

    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        # Set up MIDI connection
        ports = mido.get_ioport_names()
        self.midi_port_combo.addItems(ports)
        self.midi_port_combo.currentIndexChanged.connect(self.on_midi_port_changed)
        self.midi_port = None
        self.on_midi_port_changed()

        # Connect the DCO Controls
        self.dco_range_4_rbutton.pressed.connect(
            lambda: self.sysex_send_ipr(6, 0))
        self.dco_range_8_rbutton.pressed.connect(
            lambda: self.sysex_send_ipr(6, 1))
        self.dco_range_16_rbutton.pressed.connect(
            lambda: self.sysex_send_ipr(6, 2))
        self.dco_range_32_rbutton.pressed.connect(
            lambda: self.sysex_send_ipr(6, 3))
        self.dco_pw_slider.valueChanged.connect(
            lambda: self.sysex_send_ipr(14, self.dco_pw_slider.value()))
        self.dco_pwm_slider.valueChanged.connect(
            lambda: self.sysex_send_ipr(15, self.dco_pwm_slider.value()))
        self.dco_pulse_off_rbutton.pressed.connect(
            lambda: self.sysex_send_ipr(3, 0))
        self.dco_pulse_sq_rbutton.pressed.connect(
            lambda: self.sysex_send_ipr(3, 1))
        self.dco_pulse_pw_fix_rbutton.pressed.connect(
            lambda: self.sysex_send_ipr(3, 2))
        self.dco_pulse_pwpwm_rbutton.pressed.connect(
            lambda: self.sysex_send_ipr(3, 3))
        self.dco_saw_off_rbutton.pressed.connect(
            lambda: self.sysex_send_ipr(4, 0))
        self.dco_saw_saw_rbutton.pressed.connect(
            lambda: self.sysex_send_ipr(4, 1))
        self.dco_saw_pw_fix_rbutton.pressed.connect(
            lambda: self.sysex_send_ipr(4, 2))
        self.dco_saw_pwpwm_rbutton.pressed.connect(
            lambda: self.sysex_send_ipr(4, 3))
        self.dco_saw_saw_alt1_rbutton.pressed.connect(
            lambda: self.sysex_send_ipr(4, 4))
        self.dco_saw_saw_alt2_rbutton.pressed.connect(
            lambda: self.sysex_send_ipr(4, 5))
        self.dco_sub_sq_rbutton.pressed.connect(
            lambda: self.sysex_send_ipr(5, 0))
        self.dco_sub_pw_fix_rbutton.pressed.connect(
            lambda: self.sysex_send_ipr(5, 1))
        self.dco_sub_sq_alt1_rbutton.pressed.connect(
            lambda: self.sysex_send_ipr(5, 2))
        self.dco_sub_sq_alt2_rbutton.pressed.connect(
            lambda: self.sysex_send_ipr(5, 3))
        self.dco_sub_sub_sq_rbutton.pressed.connect(
            lambda: self.sysex_send_ipr(5, 4))
        self.dco_sub_sub_pw_fix_rbutton.pressed.connect(
            lambda: self.sysex_send_ipr(5, 5))
        self.dco_sub_lvl_slider.valueChanged.connect(
            lambda: self.sysex_send_ipr(7, self.dco_sub_lvl_slider.value()))
        self.dco_noise_lvl_slider.valueChanged.connect(
            lambda: self.sysex_send_ipr(8, self.dco_noise_lvl_slider.value()))
        self.dco_lfo_slider.valueChanged.connect(
            lambda: self.sysex_send_ipr(11, self.dco_lfo_slider.value()))
        self.dco_after_slider.valueChanged.connect(
            lambda: self.sysex_send_ipr(13, self.dco_after_slider.value()))
        self.dco_env_slider.valueChanged.connect(
            lambda: self.sysex_send_ipr(12, self.dco_env_slider.value()))
        self.dco_env_mode_env_rbutton.pressed.connect(
            lambda: self.sysex_send_ipr(0, 0))
        self.dco_env_mode_inv_rbutton.pressed.connect(
            lambda: self.sysex_send_ipr(0, 1))
        self.dco_env_mode_denv_rbutton.pressed.connect(
            lambda: self.sysex_send_ipr(0, 2))
        self.dco_env_mode_dinv_rbutton.pressed.connect(
            lambda: self.sysex_send_ipr(0, 3))

        # Connect the VCF controls
        self.vcf_hpf_slider.valueChanged.connect(
            lambda: self.sysex_send_ipr(9, self.vcf_hpf_slider.value()))
        self.vcf_freq_slider.valueChanged.connect(
            lambda: self.sysex_send_ipr(16, self.vcf_freq_slider.value()))
        self.vcf_res_slider.valueChanged.connect(
            lambda: self.sysex_send_ipr(17, self.vcf_res_slider.value()))
        self.vcf_lfo_slider.valueChanged.connect(
            lambda: self.sysex_send_ipr(18, self.vcf_lfo_slider.value()))
        self.vcf_key_flw_slider.valueChanged.connect(
            lambda: self.sysex_send_ipr(20, self.vcf_key_flw_slider.value()))
        self.vcf_after_slider.valueChanged.connect(
            lambda: self.sysex_send_ipr(21, self.vcf_after_slider.value()))
        self.vcf_env_slider.valueChanged.connect(
            lambda: self.sysex_send_ipr(19, self.vcf_env_slider.value()))
        self.vcf_env_mode_env_rbutton.pressed.connect(
            lambda: self.sysex_send_ipr(1, 0))
        self.vcf_env_mode_inv_rbutton.pressed.connect(
            lambda: self.sysex_send_ipr(1, 1))
        self.vcf_env_mode_denv_rbutton.pressed.connect(
            lambda: self.sysex_send_ipr(1, 2))
        self.vcf_env_mode_dyn_rbutton.pressed.connect(
            lambda: self.sysex_send_ipr(1, 3))

        # Connect the ENV controls
        self.env_t1_slider.valueChanged.connect(
            lambda: self.sysex_send_ipr(26, self.env_t1_slider.value()))
        self.env_l1_slider.valueChanged.connect(
            lambda: self.sysex_send_ipr(27, self.env_l1_slider.value()))
        self.env_t2_slider.valueChanged.connect(
            lambda: self.sysex_send_ipr(28, self.env_t2_slider.value()))
        self.env_l2_slider.valueChanged.connect(
            lambda: self.sysex_send_ipr(29, self.env_l2_slider.value()))
        self.env_t3_slider.valueChanged.connect(
            lambda: self.sysex_send_ipr(30, self.env_t3_slider.value()))
        self.env_l3_slider.valueChanged.connect(
            lambda: self.sysex_send_ipr(31, self.env_l3_slider.value()))
        self.env_t4_slider.valueChanged.connect(
            lambda: self.sysex_send_ipr(32, self.env_t4_slider.value()))
        self.env_key_flw_slider.valueChanged.connect(
            lambda: self.sysex_send_ipr(33, self.env_key_flw_slider.value()))

        # Connect the VCA controls
        self.vca_level_slider.valueChanged.connect(
            lambda: self.sysex_send_ipr(22, self.vca_level_slider.value()))
        self.vca_after_slider.valueChanged.connect(
            lambda: self.sysex_send_ipr(23, self.vca_after_slider.value()))
        self.vca_env_mode_env_rbutton.pressed.connect(
            lambda: self.sysex_send_ipr(2, 0))
        self.vca_env_mode_gt_rbutton.pressed.connect(
            lambda: self.sysex_send_ipr(2, 1))
        self.vca_env_mode_denv_rbutton.pressed.connect(
            lambda: self.sysex_send_ipr(2, 2))
        self.vca_env_mode_dgt_rbutton.pressed.connect(
            lambda: self.sysex_send_ipr(2, 3))

        # Connect the LFO controls
        self.lfo_rate_slider.valueChanged.connect(
            lambda: self.sysex_send_ipr(24, self.lfo_rate_slider.value()))
        self.lfo_delay_slider.valueChanged.connect(
            lambda: self.sysex_send_ipr(25, self.lfo_delay_slider.value()))

        # Connect the CHORUS controls
        self.chorus_checkBox.stateChanged.connect(
            lambda: self.sysex_send_ipr(10, self.chorus_checkBox.isChecked()))
        self.chorus_rate_slider.valueChanged.connect(
            lambda: self.sysex_send_ipr(34, self.chorus_rate_slider.value()))

        # Set up validation and connect the patch name editor
        name_reg_ex = QRegExp("[A-Za-z0-9 -]*")
        input_validator = QRegExpValidator(name_reg_ex, self.patch_name_lineEdit)
        self.patch_name_lineEdit.setValidator(input_validator)
        self.patch_name_lineEdit.editingFinished.connect(
            lambda: self.sysex_send_ipr(36, self.patch_name_lineEdit.text()))

        # File menu
        self.action_quit.triggered.connect(
            lambda: sys.exit())


    # Slots

    def on_midi_port_changed(self):
        if self.midi_port is not None:
            self.midi_port.close()
        self.midi_port = mido.open_ioport(self.midi_port_combo.currentText(), callback=self.on_midi_receive)

    def on_midi_receive(self, msg):
        print(msg)

    def sysex_send_ipr(self, parameter, value):
        data = [0b01000001,
                0b00110110,
                self.midi_channel_spinBox.value() - 1,
                0b00100011,
                0b00100000,
                0b00000001]
        if parameter != 36:
            data.append(parameter)
            data.append(value)
        else:
            alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789 -"
            value = value.ljust(10)
            for i in range(10):
                data.append(parameter + i)
                data.append(alpha.find(value[i]))
        msg = mido.Message('sysex', data=data)
        if self.midi_port is not None:
            self.midi_port.send(msg)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = JunoLab()
    window.show()
    sys.exit(app.exec_())
