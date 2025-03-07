def get_magnet_number(self, sym=1):
    """Return the number of magnet on the Lamination

    Parameters
    ----------
    self : LamSlotM
        A LamSlotM object
    sym : int
        Symmetry factor (1= full machine, 2= half of the machine...)

    Returns
    -------
    N_mag : int
        Number of magnets on the lamination
    """
    for ii in range(0,len(self.type_list)):
        if self.type_list[ii]=='M':
            Zs = self.slot_list[ii].Zs
    return Zs
