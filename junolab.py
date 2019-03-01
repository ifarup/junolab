#!/usr/bin/env python

import sys
import mido
from PyQt5 import QtWidgets, uic

qtCreatorFile = 'junolab.ui'
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)


class JunoLab(QtWidgets.QMainWindow, Ui_MainWindow):

    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        # MIDI connection
        ports = mido.get_output_names()
        self.midi_port_combo.addItems(ports)
        self.midi_port = mido.open_output(ports[0])
        self.midi_port_combo.currentIndexChanged.connect(self.on_midi_port_changed)

        # Connect the DCO Controls
        self.dco_range_4_rbutton.pressed.connect(
            lambda: self.on_button_press(6, 0))
        self.dco_range_8_rbutton.pressed.connect(
            lambda: self.on_button_press(6, 1))
        self.dco_range_16_rbutton.pressed.connect(
            lambda: self.on_button_press(6, 2))
        self.dco_range_32_rbutton.pressed.connect(
            lambda: self.on_button_press(6, 3))
        self.dco_pw_slider.valueChanged.connect(
            lambda: self.on_slider_change(14, self.dco_pw_slider))
        self.dco_pwm_slider.valueChanged.connect(
            lambda: self.on_slider_change(15, self.dco_pwm_slider))
        self.dco_pulse_off_rbutton.pressed.connect(
            lambda: self.on_button_press(3, 0))
        self.dco_pulse_sq_rbutton.pressed.connect(
            lambda: self.on_button_press(3, 1))
        self.dco_pulse_pw_fix_rbutton.pressed.connect(
            lambda: self.on_button_press(3, 2))
        self.dco_pulse_pwpwm_rbutton.pressed.connect(
            lambda: self.on_button_press(3, 3))
        self.dco_saw_off_rbutton.pressed.connect(
            lambda: self.on_button_press(4, 0))
        self.dco_saw_saw_rbutton.pressed.connect(
            lambda: self.on_button_press(4, 1))
        self.dco_saw_pw_fix_rbutton.pressed.connect(
            lambda: self.on_button_press(4, 2))
        self.dco_saw_pwpwm_rbutton.pressed.connect(
            lambda: self.on_button_press(4, 3))
        self.dco_saw_saw_alt1_rbutton.pressed.connect(
            lambda: self.on_button_press(4, 4))
        self.dco_saw_saw_alt2_rbutton.pressed.connect(
            lambda: self.on_button_press(4, 5))
        self.dco_sub_sq_rbutton.pressed.connect(
            lambda: self.on_button_press(5, 0))
        self.dco_sub_pw_fix_rbutton.pressed.connect(
            lambda: self.on_button_press(5, 1))
        self.dco_sub_sq_alt1_rbutton.pressed.connect(
            lambda: self.on_button_press(5, 2))
        self.dco_sub_sq_alt2_rbutton.pressed.connect(
            lambda: self.on_button_press(5, 3))
        self.dco_sub_sub_sq_rbutton.pressed.connect(
            lambda: self.on_button_press(5, 4))
        self.dco_sub_sub_pw_fix_rbutton.pressed.connect(
            lambda: self.on_button_press(5, 5))
        self.dco_sub_lvl_slider.valueChanged.connect(
            lambda: self.on_slider_change(7, self.dco_sub_lvl_slider))
        self.dco_noise_lvl_slider.valueChanged.connect(
            lambda: self.on_slider_change(8, self.dco_noise_lvl_slider))
        self.dco_lfo_slider.valueChanged.connect(
            lambda: self.on_slider_change(11, self.dco_lfo_slider))
        self.dco_after_slider.valueChanged.connect(
            lambda: self.on_slider_change(13, self.dco_after_slider))
        self.dco_env_slider.valueChanged.connect(
            lambda: self.on_slider_change(12, self.dco_env_slider))
        self.dco_env_mode_env_rbutton.pressed.connect(
            lambda: self.on_button_press(0, 0))
        self.dco_env_mode_inv_rbutton.pressed.connect(
            lambda: self.on_button_press(0, 1))
        self.dco_env_mode_denv_rbutton.pressed.connect(
            lambda: self.on_button_press(0, 2))
        self.dco_env_mode_dinv_rbutton.pressed.connect(
            lambda: self.on_button_press(0, 3))

        # Connect the VCF controls
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

        # Connect the ENV controls
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

        # Connect the VCA controls
        self.vca_level_slider.valueChanged.connect(
            lambda: self.on_slider_change(22, self.vca_level_slider))
        self.vca_after_slider.valueChanged.connect(
            lambda: self.on_slider_change(23, self.vca_after_slider))
        self.vca_env_mode_env_rbutton.pressed.connect(
            lambda: self.on_button_press(2, 0))
        self.vca_env_mode_gt_rbutton.pressed.connect(
            lambda: self.on_button_press(2, 1))
        self.vca_env_mode_denv_rbutton.pressed.connect(
            lambda: self.on_button_press(2, 2))
        self.vca_env_mode_dgt_rbutton.pressed.connect(
            lambda: self.on_button_press(2, 3))

        # Connect the LFO controls
        self.lfo_rate_slider.valueChanged.connect(
            lambda: self.on_slider_change(24, self.lfo_rate_slider))
        self.lfo_delay_slider.valueChanged.connect(
            lambda: self.on_slider_change(25, self.lfo_delay_slider))

        # Connect the CHORUS controls
        self.chorus_checkBox.stateChanged.connect(
            lambda: self.on_button_press(10, self.chorus_checkBox.isChecked()))
        self.chorus_rate_slider.valueChanged.connect(
            lambda: self.on_slider_change(34, self.chorus_rate_slider))

    # Slots

    def on_midi_port_changed(self):
        self.midi_port = mido.open_output(self.midi_port_combo.currentText())

    def on_slider_change(self, parameter, slider):
        self.sysex_send_ipr(parameter, slider.value(), self.midi_channel_spinBox.value() - 1)

    def on_button_press(self, parameter, value):
        self.sysex_send_ipr(parameter, value, self.midi_channel_spinBox.value() - 1)

    # Send MIDI

    def sysex_send_ipr(self, parameter, value, channel=0):
        msg = mido.Message('sysex', data=[0b01000001,
                                          0b00110110,
                                          channel,
                                          0b00100011,
                                          0b00100000,
                                          0b00000001,
                                          parameter,
                                          value])
        print(msg.hex())
        self.midi_port.send(msg)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = JunoLab()
    window.show()
    sys.exit(app.exec_())
