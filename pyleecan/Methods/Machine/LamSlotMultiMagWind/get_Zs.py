# -*- coding: utf-8 -*-

from numpy import pi, angle, exp
import numpy as np
from ....Classes.Circle import Circle
from ....Classes.SurfLine import SurfLine
from ....Classes.Arc1 import Arc1
from ....Classes.Segment import Segment


def get_Zs(self,type):
    """Return the number of Slot of the Lamination

    Parameters
    ----------
    self : LamSlotMulti
        a LamSlotMulti object

    Returns
    -------
    Zs : float
        Number of Slot

    """
    Zs = None
    for ii in range(0,len(self.slot_list)):
        if self.type_list[ii]==type:
            Zs = self.slot_list[ii].Zs
    return Zs
