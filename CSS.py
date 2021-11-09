#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#
# SPDX-License-Identifier: GPL-3.0
#
# GNU Radio Python Flow Graph
# Title: Cooperative Spectrum Sensing
# Author: Mohammad Hallaq
# GNU Radio version: v3.8.2.0-57-gd71cd177

from distutils.version import StrictVersion

if __name__ == '__main__':
    import ctypes
    import sys
    if sys.platform.startswith('linux'):
        try:
            x11 = ctypes.cdll.LoadLibrary('libX11.so')
            x11.XInitThreads()
        except:
            print("Warning: failed to XInitThreads()")

from PyQt5 import Qt
from gnuradio import qtgui
from gnuradio.filter import firdes
import sip
from gnuradio import analog
from gnuradio import blocks
from gnuradio import filter
from gnuradio import gr
import sys
import signal
from argparse import ArgumentParser
from gnuradio.eng_arg import eng_float, intx
from gnuradio import eng_notation
import bloc3_0
import bloc3_0_0
import bloc3_0_1
import osmosdr
import time

from gnuradio import qtgui

class CSS(gr.top_block, Qt.QWidget):

    def __init__(self):
        gr.top_block.__init__(self, "Cooperative Spectrum Sensing")
        Qt.QWidget.__init__(self)
        self.setWindowTitle("Cooperative Spectrum Sensing")
        qtgui.util.check_set_qss()
        try:
            self.setWindowIcon(Qt.QIcon.fromTheme('gnuradio-grc'))
        except:
            pass
        self.top_scroll_layout = Qt.QVBoxLayout()
        self.setLayout(self.top_scroll_layout)
        self.top_scroll = Qt.QScrollArea()
        self.top_scroll.setFrameStyle(Qt.QFrame.NoFrame)
        self.top_scroll_layout.addWidget(self.top_scroll)
        self.top_scroll.setWidgetResizable(True)
        self.top_widget = Qt.QWidget()
        self.top_scroll.setWidget(self.top_widget)
        self.top_layout = Qt.QVBoxLayout(self.top_widget)
        self.top_grid_layout = Qt.QGridLayout()
        self.top_layout.addLayout(self.top_grid_layout)

        self.settings = Qt.QSettings("GNU Radio", "CSS")

        try:
            if StrictVersion(Qt.qVersion()) < StrictVersion("5.0.0"):
                self.restoreGeometry(self.settings.value("geometry").toByteArray())
            else:
                self.restoreGeometry(self.settings.value("geometry"))
        except:
            pass

        ##################################################
        # Variables
        ##################################################
        self.samp_rate = samp_rate = 2e6
        self.freq = freq = 450e6
        self.Smoothing_Factor = Smoothing_Factor = 32
        self.Samples_Number = Samples_Number = 4500

        ##################################################
        # Blocks
        ##################################################
        self.qtgui_time_sink_x_0 = qtgui.time_sink_f(
            1024, #size
            samp_rate, #samp_rate
            "", #name
            1 #number of inputs
        )
        self.qtgui_time_sink_x_0.set_update_time(1)
        self.qtgui_time_sink_x_0.set_y_axis(-5, 5)

        self.qtgui_time_sink_x_0.set_y_label('Amplitude', "")

        self.qtgui_time_sink_x_0.enable_tags(True)
        self.qtgui_time_sink_x_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.0, 0, 0, "")
        self.qtgui_time_sink_x_0.enable_autoscale(False)
        self.qtgui_time_sink_x_0.enable_grid(True)
        self.qtgui_time_sink_x_0.enable_axis_labels(True)
        self.qtgui_time_sink_x_0.enable_control_panel(True)
        self.qtgui_time_sink_x_0.enable_stem_plot(False)


        labels = ['', '', '', '', '',
            '', '', '', '', '']
        widths = [1, 1, 1, 1, 1,
            1, 1, 1, 1, 1]
        colors = ['blue', 'red', 'green', 'black', 'cyan',
            'magenta', 'yellow', 'dark red', 'dark green', 'dark blue']
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
            1.0, 1.0, 1.0, 1.0, 1.0]
        styles = [1, 1, 1, 1, 1,
            1, 1, 1, 1, 1]
        markers = [-1, -1, -1, -1, -1,
            -1, -1, -1, -1, -1]


        for i in range(1):
            if len(labels[i]) == 0:
                self.qtgui_time_sink_x_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_time_sink_x_0.set_line_label(i, labels[i])
            self.qtgui_time_sink_x_0.set_line_width(i, widths[i])
            self.qtgui_time_sink_x_0.set_line_color(i, colors[i])
            self.qtgui_time_sink_x_0.set_line_style(i, styles[i])
            self.qtgui_time_sink_x_0.set_line_marker(i, markers[i])
            self.qtgui_time_sink_x_0.set_line_alpha(i, alphas[i])

        self._qtgui_time_sink_x_0_win = sip.wrapinstance(self.qtgui_time_sink_x_0.pyqwidget(), Qt.QWidget)
        self.top_grid_layout.addWidget(self._qtgui_time_sink_x_0_win)
        self.osmosdr_source_0_0_0_0 = osmosdr.source(
            args="numchan=" + str(1) + " " + 'hackrf=2'
        )
        self.osmosdr_source_0_0_0_0.set_time_unknown_pps(osmosdr.time_spec_t())
        self.osmosdr_source_0_0_0_0.set_sample_rate(samp_rate)
        self.osmosdr_source_0_0_0_0.set_center_freq(freq, 0)
        self.osmosdr_source_0_0_0_0.set_freq_corr(0, 0)
        self.osmosdr_source_0_0_0_0.set_dc_offset_mode(0, 0)
        self.osmosdr_source_0_0_0_0.set_iq_balance_mode(0, 0)
        self.osmosdr_source_0_0_0_0.set_gain_mode(False, 0)
        self.osmosdr_source_0_0_0_0.set_gain(10, 0)
        self.osmosdr_source_0_0_0_0.set_if_gain(20, 0)
        self.osmosdr_source_0_0_0_0.set_bb_gain(20, 0)
        self.osmosdr_source_0_0_0_0.set_antenna('', 0)
        self.osmosdr_source_0_0_0_0.set_bandwidth(0, 0)
        self.osmosdr_source_0_0_0 = osmosdr.source(
            args="numchan=" + str(1) + " " + 'hackrf=1'
        )
        self.osmosdr_source_0_0_0.set_time_unknown_pps(osmosdr.time_spec_t())
        self.osmosdr_source_0_0_0.set_sample_rate(samp_rate)
        self.osmosdr_source_0_0_0.set_center_freq(freq, 0)
        self.osmosdr_source_0_0_0.set_freq_corr(0, 0)
        self.osmosdr_source_0_0_0.set_dc_offset_mode(0, 0)
        self.osmosdr_source_0_0_0.set_iq_balance_mode(0, 0)
        self.osmosdr_source_0_0_0.set_gain_mode(False, 0)
        self.osmosdr_source_0_0_0.set_gain(10, 0)
        self.osmosdr_source_0_0_0.set_if_gain(20, 0)
        self.osmosdr_source_0_0_0.set_bb_gain(20, 0)
        self.osmosdr_source_0_0_0.set_antenna('', 0)
        self.osmosdr_source_0_0_0.set_bandwidth(0, 0)
        self.osmosdr_source_0_0 = osmosdr.source(
            args="numchan=" + str(1) + " " + "hackrf='0'"
        )
        self.osmosdr_source_0_0.set_time_unknown_pps(osmosdr.time_spec_t())
        self.osmosdr_source_0_0.set_sample_rate(samp_rate)
        self.osmosdr_source_0_0.set_center_freq(freq, 0)
        self.osmosdr_source_0_0.set_freq_corr(0, 0)
        self.osmosdr_source_0_0.set_dc_offset_mode(0, 0)
        self.osmosdr_source_0_0.set_iq_balance_mode(0, 0)
        self.osmosdr_source_0_0.set_gain_mode(False, 0)
        self.osmosdr_source_0_0.set_gain(10, 0)
        self.osmosdr_source_0_0.set_if_gain(20, 0)
        self.osmosdr_source_0_0.set_bb_gain(20, 0)
        self.osmosdr_source_0_0.set_antenna('', 0)
        self.osmosdr_source_0_0.set_bandwidth(0, 0)
        self.dc_blocker_xx_0_0_0 = filter.dc_blocker_cc(1024, True)
        self.dc_blocker_xx_0_0 = filter.dc_blocker_cc(1024, True)
        self.dc_blocker_xx_0 = filter.dc_blocker_cc(1024, True)
        self.blocks_threshold_ff_0_1_0_0 = blocks.threshold_ff(1.4451, 1.4451, 0)
        self.blocks_threshold_ff_0_1_0 = blocks.threshold_ff(1.4451, 1.4451, 0)
        self.blocks_threshold_ff_0_1 = blocks.threshold_ff(1.4451, 1.4451, 0)
        self.blocks_threshold_ff_0_0_0 = blocks.threshold_ff(1.0573, 1.0573, 0)
        self.blocks_threshold_ff_0_0 = blocks.threshold_ff(1.0573, 1.0573, 0)
        self.blocks_threshold_ff_0 = blocks.threshold_ff(1.0573, 1.0573, 0)
        self.blocks_sub_xx_0_0_0 = blocks.sub_ff(1)
        self.blocks_sub_xx_0_0 = blocks.sub_ff(1)
        self.blocks_sub_xx_0 = blocks.sub_ff(1)
        self.blocks_or_xx_1_0_0_1 = blocks.or_ii()
        self.blocks_or_xx_1_0_0_0 = blocks.or_ii()
        self.blocks_or_xx_1_0_0 = blocks.or_ii()
        self.blocks_or_xx_1_0 = blocks.or_ii()
        self.blocks_multiply_xx_0_0_0 = blocks.multiply_vcc(1)
        self.blocks_multiply_xx_0_0 = blocks.multiply_vcc(1)
        self.blocks_multiply_xx_0 = blocks.multiply_vcc(1)
        self.blocks_moving_average_xx_0_0_0 = blocks.moving_average_ff(1000, 1, 4000, 1)
        self.blocks_moving_average_xx_0_0 = blocks.moving_average_ff(1000, 1, 4000, 1)
        self.blocks_moving_average_xx_0 = blocks.moving_average_ff(1000, 1, 4000, 1)
        self.blocks_float_to_complex_0_0_0_0_0 = blocks.float_to_complex(1)
        self.blocks_float_to_complex_0_0_0_0 = blocks.float_to_complex(1)
        self.blocks_float_to_complex_0_0_0 = blocks.float_to_complex(1)
        self.blocks_complex_to_mag_squared_0_0_0 = blocks.complex_to_mag_squared(1)
        self.blocks_complex_to_mag_squared_0_0 = blocks.complex_to_mag_squared(1)
        self.blocks_complex_to_mag_squared_0 = blocks.complex_to_mag_squared(1)
        self.blocks_and_xx_0_0_0 = blocks.and_ii()
        self.blocks_and_xx_0_0 = blocks.and_ii()
        self.blocks_and_xx_0 = blocks.and_ii()
        self.bloc3_0_1 = bloc3_0_1.blk(N=Samples_Number, L=Smoothing_Factor, inp=[])
        self.bloc3_0_0 = bloc3_0_0.blk(N=Samples_Number, L=Smoothing_Factor, inp=[])
        self.bloc3_0 = bloc3_0.blk(N=Samples_Number, L=Smoothing_Factor, inp=[])
        self.analog_const_source_x_0_0_0_0 = analog.sig_source_f(0, analog.GR_CONST_WAVE, 0, 0, 1)
        self.analog_const_source_x_0_0_0 = analog.sig_source_f(0, analog.GR_CONST_WAVE, 0, 0, 1)
        self.analog_const_source_x_0_0 = analog.sig_source_f(0, analog.GR_CONST_WAVE, 0, 0, 1)



        ##################################################
        # Connections
        ##################################################
        self.connect((self.analog_const_source_x_0_0, 0), (self.blocks_sub_xx_0, 0))
        self.connect((self.analog_const_source_x_0_0_0, 0), (self.blocks_sub_xx_0_0, 0))
        self.connect((self.analog_const_source_x_0_0_0_0, 0), (self.blocks_sub_xx_0_0_0, 0))
        self.connect((self.bloc3_0, 0), (self.blocks_threshold_ff_0_1_0, 0))
        self.connect((self.bloc3_0_0, 0), (self.blocks_threshold_ff_0_1, 0))
        self.connect((self.bloc3_0_1, 0), (self.blocks_threshold_ff_0_1_0_0, 0))
        self.connect((self.blocks_and_xx_0, 0), (self.blocks_or_xx_1_0_0_0, 0))
        self.connect((self.blocks_and_xx_0_0, 0), (self.blocks_or_xx_1_0_0_0, 2))
        self.connect((self.blocks_and_xx_0_0_0, 0), (self.blocks_or_xx_1_0_0_0, 1))
        self.connect((self.blocks_complex_to_mag_squared_0, 0), (self.blocks_moving_average_xx_0, 0))
        self.connect((self.blocks_complex_to_mag_squared_0_0, 0), (self.blocks_moving_average_xx_0_0, 0))
        self.connect((self.blocks_complex_to_mag_squared_0_0_0, 0), (self.blocks_moving_average_xx_0_0_0, 0))
        self.connect((self.blocks_float_to_complex_0_0_0, 0), (self.blocks_multiply_xx_0, 1))
        self.connect((self.blocks_float_to_complex_0_0_0_0, 0), (self.blocks_multiply_xx_0_0, 1))
        self.connect((self.blocks_float_to_complex_0_0_0_0_0, 0), (self.blocks_multiply_xx_0_0_0, 1))
        self.connect((self.blocks_moving_average_xx_0, 0), (self.blocks_threshold_ff_0, 0))
        self.connect((self.blocks_moving_average_xx_0_0, 0), (self.blocks_threshold_ff_0_0, 0))
        self.connect((self.blocks_moving_average_xx_0_0_0, 0), (self.blocks_threshold_ff_0_0_0, 0))
        self.connect((self.blocks_multiply_xx_0, 0), (self.bloc3_0_0, 0))
        self.connect((self.blocks_multiply_xx_0_0, 0), (self.bloc3_0, 0))
        self.connect((self.blocks_multiply_xx_0_0_0, 0), (self.bloc3_0_1, 0))
        self.connect((self.blocks_or_xx_1_0, 0), (self.blocks_and_xx_0, 0))
        self.connect((self.blocks_or_xx_1_0, 0), (self.blocks_and_xx_0_0_0, 0))
        self.connect((self.blocks_or_xx_1_0_0, 0), (self.blocks_and_xx_0, 1))
        self.connect((self.blocks_or_xx_1_0_0, 0), (self.blocks_and_xx_0_0, 0))
        self.connect((self.blocks_or_xx_1_0_0_0, 0), (self.qtgui_time_sink_x_0, 0))
        self.connect((self.blocks_or_xx_1_0_0_1, 0), (self.blocks_and_xx_0_0, 1))
        self.connect((self.blocks_or_xx_1_0_0_1, 0), (self.blocks_and_xx_0_0_0, 1))
        self.connect((self.blocks_sub_xx_0, 0), (self.blocks_float_to_complex_0_0_0, 0))
        self.connect((self.blocks_sub_xx_0_0, 0), (self.blocks_float_to_complex_0_0_0_0, 0))
        self.connect((self.blocks_sub_xx_0_0_0, 0), (self.blocks_float_to_complex_0_0_0_0_0, 0))
        self.connect((self.blocks_threshold_ff_0, 0), (self.blocks_or_xx_1_0, 1))
        self.connect((self.blocks_threshold_ff_0, 0), (self.blocks_sub_xx_0, 1))
        self.connect((self.blocks_threshold_ff_0_0, 0), (self.blocks_or_xx_1_0_0, 1))
        self.connect((self.blocks_threshold_ff_0_0, 0), (self.blocks_sub_xx_0_0, 1))
        self.connect((self.blocks_threshold_ff_0_0_0, 0), (self.blocks_or_xx_1_0_0_1, 1))
        self.connect((self.blocks_threshold_ff_0_0_0, 0), (self.blocks_sub_xx_0_0_0, 1))
        self.connect((self.blocks_threshold_ff_0_1, 0), (self.blocks_or_xx_1_0, 0))
        self.connect((self.blocks_threshold_ff_0_1_0, 0), (self.blocks_or_xx_1_0_0, 0))
        self.connect((self.blocks_threshold_ff_0_1_0_0, 0), (self.blocks_or_xx_1_0_0_1, 0))
        self.connect((self.dc_blocker_xx_0, 0), (self.blocks_complex_to_mag_squared_0, 0))
        self.connect((self.dc_blocker_xx_0, 0), (self.blocks_multiply_xx_0, 0))
        self.connect((self.dc_blocker_xx_0_0, 0), (self.blocks_complex_to_mag_squared_0_0, 0))
        self.connect((self.dc_blocker_xx_0_0, 0), (self.blocks_multiply_xx_0_0, 0))
        self.connect((self.dc_blocker_xx_0_0_0, 0), (self.blocks_complex_to_mag_squared_0_0_0, 0))
        self.connect((self.dc_blocker_xx_0_0_0, 0), (self.blocks_multiply_xx_0_0_0, 0))
        self.connect((self.osmosdr_source_0_0, 0), (self.dc_blocker_xx_0, 0))
        self.connect((self.osmosdr_source_0_0_0, 0), (self.dc_blocker_xx_0_0, 0))
        self.connect((self.osmosdr_source_0_0_0_0, 0), (self.dc_blocker_xx_0_0_0, 0))


    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "CSS")
        self.settings.setValue("geometry", self.saveGeometry())
        event.accept()

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.osmosdr_source_0_0.set_sample_rate(self.samp_rate)
        self.osmosdr_source_0_0_0.set_sample_rate(self.samp_rate)
        self.osmosdr_source_0_0_0_0.set_sample_rate(self.samp_rate)
        self.qtgui_time_sink_x_0.set_samp_rate(self.samp_rate)

    def get_freq(self):
        return self.freq

    def set_freq(self, freq):
        self.freq = freq
        self.osmosdr_source_0_0.set_center_freq(self.freq, 0)
        self.osmosdr_source_0_0_0.set_center_freq(self.freq, 0)
        self.osmosdr_source_0_0_0_0.set_center_freq(self.freq, 0)

    def get_Smoothing_Factor(self):
        return self.Smoothing_Factor

    def set_Smoothing_Factor(self, Smoothing_Factor):
        self.Smoothing_Factor = Smoothing_Factor
        self.bloc3_0.L = self.Smoothing_Factor
        self.bloc3_0_0.L = self.Smoothing_Factor
        self.bloc3_0_1.L = self.Smoothing_Factor

    def get_Samples_Number(self):
        return self.Samples_Number

    def set_Samples_Number(self, Samples_Number):
        self.Samples_Number = Samples_Number
        self.bloc3_0.N = self.Samples_Number
        self.bloc3_0_0.N = self.Samples_Number
        self.bloc3_0_1.N = self.Samples_Number





def main(top_block_cls=CSS, options=None):

    if StrictVersion("4.5.0") <= StrictVersion(Qt.qVersion()) < StrictVersion("5.0.0"):
        style = gr.prefs().get_string('qtgui', 'style', 'raster')
        Qt.QApplication.setGraphicsSystem(style)
    qapp = Qt.QApplication(sys.argv)

    tb = top_block_cls()

    tb.start()

    tb.show()

    def sig_handler(sig=None, frame=None):
        Qt.QApplication.quit()

    signal.signal(signal.SIGINT, sig_handler)
    signal.signal(signal.SIGTERM, sig_handler)

    timer = Qt.QTimer()
    timer.start(500)
    timer.timeout.connect(lambda: None)

    def quitting():
        tb.stop()
        tb.wait()

    qapp.aboutToQuit.connect(quitting)
    qapp.exec_()

if __name__ == '__main__':
    main()
