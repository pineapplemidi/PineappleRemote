from __future__ import with_statement
import sys
import time
import Live

from _Framework.ControlSurface import ControlSurface
from _Framework.SessionComponent import SessionComponent
from _Framework.ButtonElement import ButtonElement
from _Framework.TransportComponent import TransportComponent
from _Framework.InputControlElement import InputControlElement, \
                                        MIDI_CC_TYPE, MIDI_NOTE_TYPE

from SpecialSessionComponent import SpecialSessionComponent


class Pineapple(ControlSurface):
    def __init__(self, c_instance):
        ControlSurface.__init__(self, c_instance)
        self._setup_session_box(4, 4)
        self._setup_transport()


    def log(self, message):
        sys.stderr.write("LOG: " + message.encode("utf-8"))


    def handle_sysex(self, midi_bytes):
        for k in range(midi_bytes):
            self.log(midi_bytes[k])


    def make_button(self, is_momentary, channel, cc, name):
        button = ButtonElement(is_momentary, MIDI_CC_TYPE, channel, cc)
        button.name = name
        return button


    def _configure_hardware_functions(self):
        pass


    def _request_hardware_functions(self):
        pass


    def _handle_hardware_function_calls(self):
        pass


    def _setup_session_box(self, width, length):
        with self.component_guard():
            self.session = SessionComponent(width, length)
            # self.session = SpecialSessionComponent(width, length, 1, [0], [0])
            self.set_highlighting_session_component(self.session)


    def _setup_transport(self):
        with self.component_guard():
            transport = TransportComponent()
            play_button = self.make_button(False, 10, 0, "Play Button")
            stop_button = self.make_button(False, 10, 1, "Stop Button")
            record_button = self.make_button(True, 10, 2, "Record Button")
            transport.set_play_button(play_button)
            transport.set_stop_button(stop_button)
            transport.set_record_button(record_button)
