# -*- coding: utf-8 -*-
# File generated according to Generator/ClassesRef/Machine/LamSlotMultiMagWind.csv
# WARNING! All changes made in this file will be lost!
"""Method code available at https://github.com/Eomys/pyleecan/tree/master/pyleecan/Methods/Machine/LamSlotMultiMagWind
"""

from os import linesep
from sys import getsizeof
from logging import getLogger
from ._check import set_array, check_var, raise_
from ..Functions.get_logger import get_logger
from ..Functions.save import save
from ..Functions.load import load_init_dict
from ..Functions.Load.import_class import import_class
from copy import deepcopy
from .LamSlotMulti import LamSlotMulti

# Import all class method
# Try/catch to remove unnecessary dependencies in unused method
try:
    from ..Methods.Machine.LamSlotMultiMagWind.plot import plot
except ImportError as error:
    plot = error

try:
    from ..Methods.Machine.LamSlotMultiMagWind.build_geometry import build_geometry
except ImportError as error:
    build_geometry = error

try:
    from ..Methods.Machine.LamSlotMultiMagWind.get_pole_pair_number import get_pole_pair_number
except ImportError as error:
    get_pole_pair_number = error

try:
    from ..Methods.Machine.LamSlotMultiMagWind.comp_mmf_dir import comp_mmf_dir
except ImportError as error:
    comp_mmf_dir = error

try:
    from ..Methods.Machine.LamSlotMultiMagWind.plot_mmf_unit import plot_mmf_unit
except ImportError as error:
    plot_mmf_unit = error

try:
    from ..Methods.Machine.LamSlotMultiMagWind.comp_mmf_unit import comp_mmf_unit
except ImportError as error:
    comp_mmf_unit = error

try:
    from ..Methods.Machine.LamSlotMultiMagWind.comp_wind_function import comp_wind_function
except ImportError as error:
    comp_wind_function = error

try:
    from ..Methods.Machine.LamSlotMultiMagWind.comp_angle_d_axis import comp_angle_d_axis
except ImportError as error:
    comp_angle_d_axis = error

try:
    from ..Methods.Machine.LamSlotMultiMagWind.get_dim_active import get_dim_active
except ImportError as error:
    get_dim_active = error


from numpy import array, array_equal
from numpy import isnan
from ._check import InitUnKnowClassError


class LamSlotMultiMagWind(LamSlotMulti):
    """Lamination with list of Slot filled with winding"""

    VERSION = 1

    # Check ImportError to remove unnecessary dependencies in unused method
    # cf Methods.Machine.LamSlotMultiMagWind.plot
    if isinstance(plot, ImportError):
        plot = property(
            fget=lambda x: raise_(
                ImportError("Can't use LamSlotMultiMagWind method plot: " + str(plot))
            )
        )
    else:
        plot = plot
    # cf Methods.Machine.LamSlotMultiMagWind.build_geometry
    if isinstance(build_geometry, ImportError):
        build_geometry = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use LamSlotMultiMagWind method build_geometry: "
                    + str(build_geometry)
                )
            )
        )
    else:
        build_geometry = build_geometry
    # cf Methods.Machine.LamSlotMultiMagWind.get_pole_pair_number
    if isinstance(get_pole_pair_number, ImportError):
        get_pole_pair_number = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use LamSlotMultiMagWind method get_pole_pair_number: "
                    + str(get_pole_pair_number)
                )
            )
        )
    else:
        get_pole_pair_number = get_pole_pair_number
    # cf Methods.Machine.LamSlotMultiMagWind.comp_mmf_dir
    if isinstance(comp_mmf_dir, ImportError):
        comp_mmf_dir = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use LamSlotMultiMagWind method comp_mmf_dir: "
                    + str(comp_mmf_dir)
                )
            )
        )
    else:
        comp_mmf_dir = comp_mmf_dir
    # cf Methods.Machine.LamSlotMultiMagWind.plot_mmf_unit
    if isinstance(plot_mmf_unit, ImportError):
        plot_mmf_unit = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use LamSlotMultiMagWind method plot_mmf_unit: "
                    + str(plot_mmf_unit)
                )
            )
        )
    else:
        plot_mmf_unit = plot_mmf_unit
    # cf Methods.Machine.LamSlotMultiMagWind.comp_mmf_unit
    if isinstance(comp_mmf_unit, ImportError):
        comp_mmf_unit = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use LamSlotMultiMagWind method comp_mmf_unit: "
                    + str(comp_mmf_unit)
                )
            )
        )
    else:
        comp_mmf_unit = comp_mmf_unit
    # cf Methods.Machine.LamSlotMultiMagWind.comp_wind_function
    if isinstance(comp_wind_function, ImportError):
        comp_wind_function = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use LamSlotMultiMagWind method comp_wind_function: "
                    + str(comp_wind_function)
                )
            )
        )
    else:
        comp_wind_function = comp_wind_function
    # cf Methods.Machine.LamSlotMultiMagWind.comp_angle_d_axis
    if isinstance(comp_angle_d_axis, ImportError):
        comp_angle_d_axis = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use LamSlotMultiMagWind method comp_angle_d_axis: "
                    + str(comp_angle_d_axis)
                )
            )
        )
    else:
        comp_angle_d_axis = comp_angle_d_axis
    # cf Methods.Machine.LamSlotMultiMagWind.get_dim_active
    if isinstance(get_dim_active, ImportError):
        get_dim_active = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use LamSlotMultiMagWind method get_dim_active: "
                    + str(get_dim_active)
                )
            )
        )
    else:
        get_dim_active = get_dim_active
    # generic save method is available in all object
    save = save
    # get_logger method is available in all object
    get_logger = get_logger

    def __init__(self, Ksfill=None, winding=-1, magnet=-1, type_list=None, mur_lin_matrix=None, Brm20_matrix=None, slot_list=-1, alpha=None, sym_dict_enforced=None, L1=0.35, mat_type=-1, Nrvd=0, Wrvd=0, Kf1=0.95, is_internal=True, Rint=0, Rext=1, is_stator=True, axial_vent=-1, notch=-1, skew=None, bore=None, yoke=None, init_dict = None, init_str = None):
        """Constructor of the class. Can be use in three ways :
        - __init__ (arg1 = 1, arg3 = 5) every parameters have name and default values
            for pyleecan type, -1 will call the default constructor
        - __init__ (init_dict = d) d must be a dictionary with property names as keys
        - __init__ (init_str = s) s must be a string
        s is the file path to load

        ndarray or list can be given for Vector and Matrix
        object or dict can be given for pyleecan Object"""

        if init_str is not None:  # Load from a file
            init_dict = load_init_dict(init_str)[1]
        if init_dict is not None:  # Initialisation by dict
            assert type(init_dict) is dict
            # Overwrite default value with init_dict content
            if "Ksfill" in list(init_dict.keys()):
                Ksfill = init_dict["Ksfill"]
            if "winding" in list(init_dict.keys()):
                winding = init_dict["winding"]
            if "magnet" in list(init_dict.keys()):
                magnet = init_dict["magnet"]
            if "type_list" in list(init_dict.keys()):
                type_list = init_dict["type_list"]
            if "mur_lin_matrix" in list(init_dict.keys()):
                mur_lin_matrix = init_dict["mur_lin_matrix"]
            if "Brm20_matrix" in list(init_dict.keys()):
                Brm20_matrix = init_dict["Brm20_matrix"]
            if "slot_list" in list(init_dict.keys()):
                slot_list = init_dict["slot_list"]
            if "alpha" in list(init_dict.keys()):
                alpha = init_dict["alpha"]
            if "sym_dict_enforced" in list(init_dict.keys()):
                sym_dict_enforced = init_dict["sym_dict_enforced"]
            if "L1" in list(init_dict.keys()):
                L1 = init_dict["L1"]
            if "mat_type" in list(init_dict.keys()):
                mat_type = init_dict["mat_type"]
            if "Nrvd" in list(init_dict.keys()):
                Nrvd = init_dict["Nrvd"]
            if "Wrvd" in list(init_dict.keys()):
                Wrvd = init_dict["Wrvd"]
            if "Kf1" in list(init_dict.keys()):
                Kf1 = init_dict["Kf1"]
            if "is_internal" in list(init_dict.keys()):
                is_internal = init_dict["is_internal"]
            if "Rint" in list(init_dict.keys()):
                Rint = init_dict["Rint"]
            if "Rext" in list(init_dict.keys()):
                Rext = init_dict["Rext"]
            if "is_stator" in list(init_dict.keys()):
                is_stator = init_dict["is_stator"]
            if "axial_vent" in list(init_dict.keys()):
                axial_vent = init_dict["axial_vent"]
            if "notch" in list(init_dict.keys()):
                notch = init_dict["notch"]
            if "skew" in list(init_dict.keys()):
                skew = init_dict["skew"]
            if "bore" in list(init_dict.keys()):
                bore = init_dict["bore"]
            if "yoke" in list(init_dict.keys()):
                yoke = init_dict["yoke"]
        # Set the properties (value check and convertion are done in setter)
        self.Ksfill = Ksfill
        self.winding = winding
        self.magnet = magnet
        self.type_list = type_list
        self.mur_lin_matrix = mur_lin_matrix
        self.Brm20_matrix = Brm20_matrix
        # Call LamSlotMulti init
        super(LamSlotMultiMagWind, self).__init__(slot_list=slot_list, alpha=alpha, sym_dict_enforced=sym_dict_enforced, L1=L1, mat_type=mat_type, Nrvd=Nrvd, Wrvd=Wrvd, Kf1=Kf1, is_internal=is_internal, Rint=Rint, Rext=Rext, is_stator=is_stator, axial_vent=axial_vent, notch=notch, skew=skew, bore=bore, yoke=yoke)
        # The class is frozen (in LamSlotMulti init), for now it's impossible to
        # add new properties

    def __str__(self):
        """Convert this object in a readeable string (for print)"""

        LamSlotMultiMagWind_str = ""
        # Get the properties inherited from LamSlotMulti
        LamSlotMultiMagWind_str += super(LamSlotMultiMagWind, self).__str__()
        LamSlotMultiMagWind_str += "Ksfill = " + str(self.Ksfill) + linesep
        if self.winding is not None:
            tmp = self.winding.__str__().replace(linesep, linesep + "\t").rstrip("\t")
            LamSlotMultiMagWind_str += "winding = "+ tmp
        else:
            LamSlotMultiMagWind_str += "winding = None" + linesep + linesep
        if self.magnet is not None:
            tmp = self.magnet.__str__().replace(linesep, linesep + "\t").rstrip("\t")
            LamSlotMultiMagWind_str += "magnet = "+ tmp
        else:
            LamSlotMultiMagWind_str += "magnet = None" + linesep + linesep
        LamSlotMultiMagWind_str += "type_list = " + linesep + str(self.type_list).replace(linesep, linesep + "\t") + linesep + linesep
        LamSlotMultiMagWind_str += "mur_lin_matrix = " + linesep + str(self.mur_lin_matrix).replace(linesep, linesep + "\t") + linesep + linesep
        LamSlotMultiMagWind_str += "Brm20_matrix = " + linesep + str(self.Brm20_matrix).replace(linesep, linesep + "\t") + linesep + linesep
        return LamSlotMultiMagWind_str

    def __eq__(self, other):
        """Compare two objects (skip parent)"""

        if type(other) != type(self):
            return False

        # Check the properties inherited from LamSlotMulti
        if not super(LamSlotMultiMagWind, self).__eq__(other):
            return False
        if other.Ksfill != self.Ksfill:
            return False
        if other.winding != self.winding:
            return False
        if other.magnet != self.magnet:
            return False
        if not array_equal(other.type_list, self.type_list):
            return False
        if not array_equal(other.mur_lin_matrix, self.mur_lin_matrix):
            return False
        if not array_equal(other.Brm20_matrix, self.Brm20_matrix):
            return False
        return True

    def compare(self, other, name='self', ignore_list=None, is_add_value=False):
        """Compare two objects and return list of differences"""

        if ignore_list is None:
            ignore_list = list()
        if type(other) != type(self):
            return ['type('+name+')']
        diff_list = list()

        # Check the properties inherited from LamSlotMulti
        diff_list.extend(super(LamSlotMultiMagWind, self).compare(other,name=name, ignore_list=ignore_list, is_add_value=is_add_value))
        if other._Ksfill is not None and self._Ksfill is not None and isnan(other._Ksfill) and isnan(self._Ksfill):
            pass
        elif other._Ksfill != self._Ksfill:
            if is_add_value:
                val_str = ' (self='+str(self._Ksfill)+', other='+str(other._Ksfill)+')'
                diff_list.append(name+'.Ksfill'+val_str)
            else:
                diff_list.append(name+'.Ksfill')
        if (other.winding is None and self.winding is not None) or (other.winding is not None and self.winding is None):
            diff_list.append(name+'.winding None mismatch')
        elif self.winding is not None:
            diff_list.extend(self.winding.compare(other.winding,name=name+'.winding',ignore_list=ignore_list,is_add_value=is_add_value))
        if (other.magnet is None and self.magnet is not None) or (other.magnet is not None and self.magnet is None):
            diff_list.append(name+'.magnet None mismatch')
        elif self.magnet is not None:
            diff_list.extend(self.magnet.compare(other.magnet,name=name+'.magnet',ignore_list=ignore_list,is_add_value=is_add_value))
        if not array_equal(other.type_list, self.type_list):
            diff_list.append(name+'.type_list')
        if not array_equal(other.mur_lin_matrix, self.mur_lin_matrix):
            diff_list.append(name+'.mur_lin_matrix')
        if not array_equal(other.Brm20_matrix, self.Brm20_matrix):
            diff_list.append(name+'.Brm20_matrix')
        # Filter ignore differences
        diff_list = list(filter(lambda x : x not in ignore_list, diff_list))
        return diff_list

    def __sizeof__(self):
        """Return the size in memory of the object (including all subobject)"""

        S = 0  # Full size of the object

        # Get size of the properties inherited from LamSlotMulti
        S += super(LamSlotMultiMagWind, self).__sizeof__()
        S += getsizeof(self.Ksfill)
        S += getsizeof(self.winding)
        S += getsizeof(self.magnet)
        S += getsizeof(self.type_list)
        S += getsizeof(self.mur_lin_matrix)
        S += getsizeof(self.Brm20_matrix)
        return S

    def as_dict(self, type_handle_ndarray=0, keep_function=False, **kwargs):
        """
        Convert this object in a json serializable dict (can be use in __init__).
        type_handle_ndarray: int
            How to handle ndarray (0: tolist, 1: copy, 2: nothing)
        keep_function : bool
            True to keep the function object, else return str
        Optional keyword input parameter is for internal use only 
        and may prevent json serializability.
        """

        # Get the properties inherited from LamSlotMulti
        LamSlotMultiMagWind_dict = super(LamSlotMultiMagWind, self).as_dict(type_handle_ndarray=type_handle_ndarray, keep_function=keep_function, **kwargs)
        LamSlotMultiMagWind_dict["Ksfill"] = self.Ksfill
        if self.winding is None:
            LamSlotMultiMagWind_dict["winding"] = None
        else:
            LamSlotMultiMagWind_dict["winding"] = self.winding.as_dict(type_handle_ndarray=type_handle_ndarray, keep_function=keep_function, **kwargs)
        if self.magnet is None:
            LamSlotMultiMagWind_dict["magnet"] = None
        else:
            LamSlotMultiMagWind_dict["magnet"] = self.magnet.as_dict(type_handle_ndarray=type_handle_ndarray, keep_function=keep_function, **kwargs)
        if self.type_list is None:
            LamSlotMultiMagWind_dict["type_list"] = None
        else:
            if type_handle_ndarray==0:
                LamSlotMultiMagWind_dict["type_list"] = self.type_list.tolist()
            elif type_handle_ndarray==1:
                LamSlotMultiMagWind_dict["type_list"] = self.type_list.copy()
            elif type_handle_ndarray==2:
                LamSlotMultiMagWind_dict["type_list"] = self.type_list
            else:
                raise Exception ('Unknown type_handle_ndarray: '+str(type_handle_ndarray))
        if self.mur_lin_matrix is None:
            LamSlotMultiMagWind_dict["mur_lin_matrix"] = None
        else:
            if type_handle_ndarray==0:
                LamSlotMultiMagWind_dict["mur_lin_matrix"] = self.mur_lin_matrix.tolist()
            elif type_handle_ndarray==1:
                LamSlotMultiMagWind_dict["mur_lin_matrix"] = self.mur_lin_matrix.copy()
            elif type_handle_ndarray==2:
                LamSlotMultiMagWind_dict["mur_lin_matrix"] = self.mur_lin_matrix
            else:
                raise Exception ('Unknown type_handle_ndarray: '+str(type_handle_ndarray))
        if self.Brm20_matrix is None:
            LamSlotMultiMagWind_dict["Brm20_matrix"] = None
        else:
            if type_handle_ndarray==0:
                LamSlotMultiMagWind_dict["Brm20_matrix"] = self.Brm20_matrix.tolist()
            elif type_handle_ndarray==1:
                LamSlotMultiMagWind_dict["Brm20_matrix"] = self.Brm20_matrix.copy()
            elif type_handle_ndarray==2:
                LamSlotMultiMagWind_dict["Brm20_matrix"] = self.Brm20_matrix
            else:
                raise Exception ('Unknown type_handle_ndarray: '+str(type_handle_ndarray))
        # The class name is added to the dict for deserialisation purpose
        # Overwrite the mother class name
        LamSlotMultiMagWind_dict["__class__"] = "LamSlotMultiMagWind"
        return LamSlotMultiMagWind_dict


    def copy(self):
        """Creates a deepcopy of the object"""

        # Handle deepcopy of all the properties
        Ksfill_val = self.Ksfill
        if self.winding is None:
            winding_val = None
        else:
            winding_val = self.winding.copy()
        if self.magnet is None:
            magnet_val = None
        else:
            magnet_val = self.magnet.copy()
        if self.type_list is None:
            type_list_val = None
        else:
            type_list_val = self.type_list.copy()
        if self.mur_lin_matrix is None:
            mur_lin_matrix_val = None
        else:
            mur_lin_matrix_val = self.mur_lin_matrix.copy()
        if self.Brm20_matrix is None:
            Brm20_matrix_val = None
        else:
            Brm20_matrix_val = self.Brm20_matrix.copy()
        if self.slot_list is None:
            slot_list_val = None
        else:
            slot_list_val = list()
            for obj in self.slot_list:
                slot_list_val.append(obj.copy())
        if self.alpha is None:
            alpha_val = None
        else:
            alpha_val = self.alpha.copy()
        if self.sym_dict_enforced is None:
            sym_dict_enforced_val = None
        else:
            sym_dict_enforced_val = self.sym_dict_enforced.copy()
        L1_val = self.L1
        if self.mat_type is None:
            mat_type_val = None
        else:
            mat_type_val = self.mat_type.copy()
        Nrvd_val = self.Nrvd
        Wrvd_val = self.Wrvd
        Kf1_val = self.Kf1
        is_internal_val = self.is_internal
        Rint_val = self.Rint
        Rext_val = self.Rext
        is_stator_val = self.is_stator
        if self.axial_vent is None:
            axial_vent_val = None
        else:
            axial_vent_val = list()
            for obj in self.axial_vent:
                axial_vent_val.append(obj.copy())
        if self.notch is None:
            notch_val = None
        else:
            notch_val = list()
            for obj in self.notch:
                notch_val.append(obj.copy())
        if self.skew is None:
            skew_val = None
        else:
            skew_val = self.skew.copy()
        if self.bore is None:
            bore_val = None
        else:
            bore_val = self.bore.copy()
        if self.yoke is None:
            yoke_val = None
        else:
            yoke_val = self.yoke.copy()
        # Creates new object of the same type with the copied properties
        obj_copy = type(self)(Ksfill=Ksfill_val,winding=winding_val,magnet=magnet_val,type_list=type_list_val,mur_lin_matrix=mur_lin_matrix_val,Brm20_matrix=Brm20_matrix_val,slot_list=slot_list_val,alpha=alpha_val,sym_dict_enforced=sym_dict_enforced_val,L1=L1_val,mat_type=mat_type_val,Nrvd=Nrvd_val,Wrvd=Wrvd_val,Kf1=Kf1_val,is_internal=is_internal_val,Rint=Rint_val,Rext=Rext_val,is_stator=is_stator_val,axial_vent=axial_vent_val,notch=notch_val,skew=skew_val,bore=bore_val,yoke=yoke_val)
        return obj_copy

    def _set_None(self):
        """Set all the properties to None (except pyleecan object)"""

        self.Ksfill = None
        if self.winding is not None:
            self.winding._set_None()
        if self.magnet is not None:
            self.magnet._set_None()
        self.type_list = None
        self.mur_lin_matrix = None
        self.Brm20_matrix = None
        # Set to None the properties inherited from LamSlotMulti
        super(LamSlotMultiMagWind, self)._set_None()

    def _get_Ksfill(self):
        """getter of Ksfill"""
        return self._Ksfill

    def _set_Ksfill(self, value):
        """setter of Ksfill"""
        check_var("Ksfill", value, "float", Vmin=0, Vmax=1)
        self._Ksfill = value

    Ksfill = property(
        fget=_get_Ksfill,
        fset=_set_Ksfill,
        doc=u"""Imposed Slot Fill factor (if None, will be computed according to the winding and the slot)

        :Type: float
        :min: 0
        :max: 1
        """,
    )

    def _get_winding(self):
        """getter of winding"""
        return self._winding

    def _set_winding(self, value):
        """setter of winding"""
        if isinstance(value, str):  # Load from file
            try:
                value = load_init_dict(value)[1]
            except Exception as e:
                self.get_logger().error('Error while loading '+value+', setting None instead')
                value = None
        if isinstance(value, dict) and '__class__' in value:
            class_obj = import_class('pyleecan.Classes', value.get('__class__'), 'winding')
            value = class_obj(init_dict=value)
        elif type(value) is int and value == -1:  # Default constructor
            Winding = import_class('pyleecan.Classes', 'Winding', 'winding')
            value = Winding()
        check_var("winding", value, "Winding")
        self._winding = value

        if self._winding is not None:
            self._winding.parent = self
    winding = property(
        fget=_get_winding,
        fset=_set_winding,
        doc=u"""Lamination's Winding

        :Type: Winding
        """,
    )

    def _get_magnet(self):
        """getter of magnet"""
        return self._magnet

    def _set_magnet(self, value):
        """setter of magnet"""
        if isinstance(value, str):  # Load from file
            try:
                value = load_init_dict(value)[1]
            except Exception as e:
                self.get_logger().error('Error while loading '+value+', setting None instead')
                value = None
        if isinstance(value, dict) and '__class__' in value:
            class_obj = import_class('pyleecan.Classes', value.get('__class__'), 'magnet')
            value = class_obj(init_dict=value)
        elif type(value) is int and value == -1:  # Default constructor
            Magnet = import_class('pyleecan.Classes', 'Magnet', 'magnet')
            value = Magnet()
        check_var("magnet", value, "Magnet")
        self._magnet = value

        if self._magnet is not None:
            self._magnet.parent = self
    magnet = property(
        fget=_get_magnet,
        fset=_set_magnet,
        doc=u"""Lamination's Magnet

        :Type: Magnet
        """,
    )

    def _get_type_list(self):
        """getter of type_list"""
        return self._type_list

    def _set_type_list(self, value):
        """setter of type_list"""
        if type(value) is int and value == -1:
            value = array([])
        elif type(value) is list:
            try:
                value = array(value)
            except:
                pass
        check_var("type_list", value, "ndarray")
        self._type_list = value

    type_list = property(
        fget=_get_type_list,
        fset=_set_type_list,
        doc=u"""List indicating if the lamination is winding 'W' mag 'M' or empty 'E'

        :Type: ndarray
        """,
    )

    def _get_mur_lin_matrix(self):
        """getter of mur_lin_matrix"""
        return self._mur_lin_matrix

    def _set_mur_lin_matrix(self, value):
        """setter of mur_lin_matrix"""
        if type(value) is int and value == -1:
            value = array([])
        elif type(value) is list:
            try:
                value = array(value)
            except:
                pass
        check_var("mur_lin_matrix", value, "ndarray")
        self._mur_lin_matrix = value

    mur_lin_matrix = property(
        fget=_get_mur_lin_matrix,
        fset=_set_mur_lin_matrix,
        doc=u"""Matrix to enforce a different relative magnetic permeability for each magnet layer (shape: [Nrad, Ntan, Zs])

        :Type: ndarray
        """,
    )

    def _get_Brm20_matrix(self):
        """getter of Brm20_matrix"""
        return self._Brm20_matrix

    def _set_Brm20_matrix(self, value):
        """setter of Brm20_matrix"""
        if type(value) is int and value == -1:
            value = array([])
        elif type(value) is list:
            try:
                value = array(value)
            except:
                pass
        check_var("Brm20_matrix", value, "ndarray")
        self._Brm20_matrix = value

    Brm20_matrix = property(
        fget=_get_Brm20_matrix,
        fset=_set_Brm20_matrix,
        doc=u"""Matrix to enforce a different magnet remanence induction at 20degC for each magnet layer (shape: [Nrad, Ntan, Zs])

        :Type: ndarray
        """,
    )
