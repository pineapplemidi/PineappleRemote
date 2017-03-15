from _Framework.Capabilities import controller_id, inport, outport, \
                                CONTROLLER_ID_KEY, PORTS_KEY, NOTES_CC, SCRIPT

from Pineapple import Pineapple


def get_capabilities():
    return {CONTROLLER_ID_KEY: controller_id(vendor_id=0x04D8, \
                                product_ids=[59], model_name='BERRYHILL'), \
                                PORTS_KEY: [inport(props=[NOTES_CC, SCRIPT]), \
                                outport(props=[NOTES_CC, SCRIPT])]}


def create_instance(c_instance):
    return Pineapple(c_instance)
