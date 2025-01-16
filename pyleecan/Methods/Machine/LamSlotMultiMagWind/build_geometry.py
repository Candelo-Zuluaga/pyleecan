# -*- coding: utf-8 -*-
from numpy import pi
import numpy as np

from ....Classes.Winding import Winding
from ....Methods import NotImplementedYetError
from ....Classes.LamSlot import LamSlot
from ....Functions.labels import update_RTS_index
from ....Functions.labels import (
    BOUNDARY_PROP_LAB,
    COND_BOUNDARY_PROP_LAB,
    WIND_LAB,
    MAG_LAB,
    YSMR_LAB,
    YSML_LAB,
    LAM_LAB,
    YOKE_LAB,
    decode_label,
)


def build_geometry(self, is_magnet=True, sym=1, alpha=0, delta=0, is_circular_radius=False):
    """Build the geometry of the LamSlotMultiMagWind with Winding and Magnets in the specified slots or empty if not specified

    Parameters
    ----------
    self : LamSlotMultiMagWind
        A LamSlotMultiMagWind object
    is_magnet : bool
        If True build the magnet surfaces
    alpha : float
        Angle for rotation [rad]
    delta : complex
        Complex value for translation
    is_circular_radius : bool
        True to add surfaces to "close" the Lamination radii

    Returns
    -------
    surf_list : list
        list of surfaces needed to draw the lamination

    """
    # getting the Lamination surface
    surf_lam = LamSlot.build_geometry(
        self, sym=sym, alpha=alpha, delta=delta, is_circular_radius=is_circular_radius
    )
    # getting the winding or/and magnet surface
    surf_list = list()    
    for ii in range(len(self.slot_list)): # We loop through the slot list
        # Checking Simmetry 
        assert (self.slot_list[ii].Zs % sym) == 0, (
            "ERROR, Wrong symmetry for "
            + st
            + " "
            + str(self.slot_list[ii].Zs)
            + " slots and sym="
            + str(sym)
        )
        if self.type_list[ii] == 'M':
            Zs = self.slot_list[ii].Zs
            slot_pitch = 2 * pi / Zs
            angle = self.alpha[ii]
            # Add the magnet surface(s)
            if is_magnet and self.magnet is not None:
                # Get the active surface to copy rotate
                Nrad, Ntan = self.get_dim_active()
                mag_layer_surf = self.slot_list[ii].build_geometry_active(
                    Nrad=Nrad,
                    Ntan=Ntan,
                    alpha=alpha,
                    delta=delta,
                )

                # for each magnet to draw
                mag_surf_list = list()
                for jj in range(Zs // sym):
                    for surf in mag_layer_surf:
                        mag_surf = surf.copy()
                        # changing the slot reference number
                        mag_surf.label = update_RTS_index(
                            label=surf.label, S_id=jj, surf_type_label=MAG_LAB
                        )
                        mag_surf.rotate(jj * slot_pitch + self.alpha[ii]) 
                        mag_surf_list.append(mag_surf)
                # Update the magnets BC (if magnet side matches sym lines ex: SlotM18)
                if self.slot_list[ii].is_full_pitch_active() and sym > 1:
                    for surf in mag_surf_list:
                        label_dict = decode_label(surf.label)
                        # Set BC on Right side / Ox
                        if label_dict["S_id"] == 0:
                            # Find the lines to add the BC
                            for line in surf.get_lines():
                                if (
                                    line.prop_dict is not None
                                    and COND_BOUNDARY_PROP_LAB in line.prop_dict
                                    and line.prop_dict[COND_BOUNDARY_PROP_LAB] == YSMR_LAB
                                ):
                                    line.prop_dict.update(
                                        {
                                            BOUNDARY_PROP_LAB: st
                                            + "_"
                                            + YSMR_LAB
                                            + "-"
                                            + str(label_dict["R_id"])
                                        }
                                    )
                        # Set BC on Left side / last active surface
                        if label_dict["S_id"] == Zs // sym - 1:
                            # Find the lines to add the BC
                            for line in surf.get_lines():
                                if (
                                    line.prop_dict is not None
                                    and COND_BOUNDARY_PROP_LAB in line.prop_dict
                                    and line.prop_dict[COND_BOUNDARY_PROP_LAB] == YSML_LAB
                                ):
                                    line.prop_dict.update(
                                        {
                                            BOUNDARY_PROP_LAB: st
                                            + "_"
                                            + YSML_LAB
                                            + "-"
                                            + str(label_dict["R_id"])
                                        }
                                    )
                # Update Magnets BC when no lamination
                if self.Rint == self.Rext and self.Rint != 0:
                    label_yoke = self.get_label() + "_" + LAM_LAB + YOKE_LAB
                    for surf in mag_surf_list:
                        label_dict = decode_label(surf.label)
                        if label_dict["R_id"] == 0:
                            for line in surf.get_lines():
                                if (
                                    line.prop_dict is not None
                                    and COND_BOUNDARY_PROP_LAB in line.prop_dict
                                    and line.prop_dict[COND_BOUNDARY_PROP_LAB] == YOKE_LAB
                                ):
                                    line.prop_dict.update({BOUNDARY_PROP_LAB: label_yoke})

                # Shift to have a tooth center on Ox
                for surf in mag_surf_list:
                    surf.rotate(pi / Zs)
                surf_list.extend(mag_surf_list)
        elif self.type_list[ii] == 'W':
            if self.slot_list[ii] is not None and self.slot_list[ii].Zs != 0:
                # getting number of slot
                Zs = self.slot_list[ii].Zs
                # getting angle between Slot
                slot_pitch = 2 * pi / Zs
                # getting Nrad and Ntan
                if self.winding is None or self.winding.conductor is None:
                    Nrad, Ntan = 1, 1
                    surf_Wind = list()
                else:
                    try:
                        Nrad, Ntan = self.winding.get_dim_wind()
                    except Exception:
                        Nrad, Ntan = 1, 1

                    surf_Wind = self.slot_list[ii].build_geometry_active(
                        Nrad=Nrad,
                        Ntan=Ntan,
                        alpha=alpha,
                        delta=delta,
                    )

                st = self.get_label()
                assert (self.slot_list[ii].Zs % sym) == 0, (
                    "ERROR, Wrong symmetry for "
                    + st
                    + " "
                    + str(self.slot.Zs)
                    + " slots and sym="
                    + str(sym)
                )
                for jj in range(Zs // sym):  # for each slot
                    # for each part of the winding surface in the slot
                    for surf in surf_Wind:
                        new_surf = surf.copy()
                        # changing the slot reference number
                        new_surf.label = update_RTS_index(
                            label=surf.label, S_id=jj, surf_type_label=WIND_LAB
                        )
                        new_surf.rotate(jj * slot_pitch + self.alpha[ii])
                        surf_list.append(new_surf)
                # Update the winding BC (if winding side matches sym lines ex: SlotM18)
                if self.slot_list[ii].is_full_pitch_active() and sym > 1:
                    for surf in surf_list:
                        label_dict = decode_label(surf.label)
                        # Set BC on Right side / Ox
                        if label_dict["S_id"] == 0:
                            # Find the lines to add the BC
                            for line in surf.get_lines():
                                if (
                                    line.prop_dict is not None
                                    and COND_BOUNDARY_PROP_LAB in line.prop_dict
                                    and line.prop_dict[COND_BOUNDARY_PROP_LAB] == YSMR_LAB
                                ):
                                    line.prop_dict.update(
                                        {
                                            BOUNDARY_PROP_LAB: st
                                            + "_"
                                            + YSMR_LAB
                                            + "-"
                                            + str(label_dict["R_id"])
                                        }
                                    )
                        # Set BC on Left side / last active surface
                        if label_dict["S_id"] == Zs // sym - 1:
                            # Find the lines to add the BC
                            for line in surf.get_lines():
                                if (
                                    line.prop_dict is not None
                                    and COND_BOUNDARY_PROP_LAB in line.prop_dict
                                    and line.prop_dict[COND_BOUNDARY_PROP_LAB] == YSML_LAB
                                ):
                                    line.prop_dict.update(
                                        {
                                            BOUNDARY_PROP_LAB: st
                                            + "_"
                                            + YSML_LAB
                                            + "-"
                                            + str(label_dict["R_id"])
                                        }
                                    )
                # Add wedges if any
                if self.slot_list[ii].wedge_mat is not None:
                    wedge_list = self.slot_list[ii].get_surface_wedges()
                    for jj in range(Zs // sym):  # for each slot
                        # for each wedges surface in the slot
                        for surf in wedge_list:
                            new_surf = type(surf)(init_dict=surf.as_dict())
                            # changing the slot reference number
                            new_surf.label = update_RTS_index(label=surf.label, S_id=jj)
                            new_surf.rotate(jj * slot_pitch+self.alpha[ii])
                            surf_list.append(new_surf)
                # Shift to have a tooth center on Ox
                for surf in surf_list:
                    surf.rotate(pi / Zs)
        else:
            pass
                    
    surf_list = surf_lam + surf_list    
    return surf_list

