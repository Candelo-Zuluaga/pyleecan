from numpy import pi
from ....Functions.Geometry.merge_notch_list import merge_notch_list

def get_slot_desc_list(self, sym=1, is_bore=True):
    """Returns an ordered description of the slot

    Parameters
    ----------
    self : LamSlotMulti
        A LamSlotMulti object
    sym: int
        Number of symmetry
    is_bore : bool
        True generate desc of bore, else yoke

    Returns
    -------
    slot_desc : list
        trigo ordered list of dictionary with key:
            "begin_angle" : float [rad]
            "end_angle" : float [rad]
            "obj" : Slot / None for Radius
            "lines : lines corresponding to the radius part
            "label" : Radius/Notch/Slot
    """
    #

    slot_list_out = list()
    for ii in range(0,len(self.slot_list),1):
        slot_list_aux = list()
        if self.slot_list[ii].is_bore == is_bore:
            op = self.slot_list[ii].comp_angle_opening()
            Zs = self.slot_list[ii].Zs
            for jj in range(Zs // sym):
                slot_dict = dict()
                slot_dict["begin_angle"] = 2 * pi / Zs * jj - op / 2 + pi / Zs + self.alpha[ii]
                slot_dict["end_angle"] = 2 * pi / Zs * jj + op / 2 + pi / Zs + + self.alpha[ii]
                slot_dict["obj"] = self.slot_list[ii]
                slot_dict["lines"] = self.slot_list[ii].build_geometry()
                # Apply rotation
                for line in slot_dict["lines"]:
                    line.rotate((slot_dict["begin_angle"] + slot_dict["end_angle"]) / 2)
                slot_dict["label"] = "Slot"
                slot_list_aux.append(slot_dict)
            
        slot_list_out = merge_notch_list(slot_list_out,slot_list_aux)
    return slot_list_out
