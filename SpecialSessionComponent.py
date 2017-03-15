from _Framework.SessionComponent import SessionComponent
from _Framework.ButtonElement import ButtonElement
from _Framework.ButtonMatrixElement import ButtonMatrixElement

class SpecialSessionComponent(SessionComponent):
    def __init__(self, width, height, num_decks, track_offsets, scene_offsetsm, \
                    buttons):
        self.width = width
        self.height = height
        self.decks = self._init_decks(num_decks, track_offsets, scene_offsets)


    def _init_decks(self, num_decks, track_offsets, scene_offsets):
        decks = []
        for k in range(num_decks):
            decks[k] = Deck(track_offsets[k], scene_offsets[k])
        return decks


    def _add_deck_select_button(self, button, deck):
        pass


    def select_deck(self, deck):
        self.set_offsets(decks[deck].track_offset, decks[deck].scene_offset)


    def _setup_button_matrix(self):
        pass


    def add_button_to_matrix(self, button, track, scene):
        pass


class Deck(object):
    def __init__(self, track_offset, scene_offset=0):
        self.track_offset
        self.scene_offset


    def set_track_offset(self, offset):
        self.track_offset = offset


    def set_scene_offset(self, offset):
        self.scene_offset = offset
