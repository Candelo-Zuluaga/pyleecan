from matplotlib.patches import Patch, FancyArrowPatch
import matplotlib.pyplot as plt
from swat_em import datamodel
from numpy import sqrt

from ....Functions.labels import decode_label, WIND_LAB, BAR_LAB
from ....Functions.Winding.find_wind_phase_color import find_wind_phase_color
from ....Functions.Winding.gen_phase_list import gen_name
from ....Functions.Plot import dict_2D
from ....Functions.init_fig import init_fig
from ....definitions import config_dict
from ....Classes.WindingSC import WindingSC
from ....Classes.WindingUD import WindingUD
from ....Functions.Plot.get_color_legend_from_surface import (
    get_color_legend_from_surface,
)

PHASE_COLORS = config_dict["PLOT"]["COLOR_DICT"]["PHASE_COLORS"]
PLUS_HATCH = "++"
MINUS_HATCH = ".."

def plot(
    self,
    fig=None,
    ax=None,
    is_lam_only=False,
    sym=1,
    alpha=0,
    delta=0,
    is_edge_only=False,
    edgecolor=None,
    is_add_arrow=False,
    is_display=True,
    is_add_sign=True,
    is_show_fig=True,
    save_path=None,
    win_title=None,
    is_legend=True,
    is_clean_plot=False,
    is_winding_connection=False,
    is_winding_connection_phase_A=False,
):
    """Plot the Lamination LamSlotMultiMagWind with Winding and Magnets in the specified slots or empty if not specified

    Parameters
    ----------
    self : LamSlotMultiMagWind
        A LamSlotMulti object
    fig : Matplotlib.figure.Figure
        existing figure to use if None create a new one
    ax : Matplotlib.axes.Axes object
        Axis on which to plot the data
    is_lam_only : bool
        True to plot only the lamination (remove the Winding)
    sym : int
        Symmetry factor (1= full machine, 2= half of the machine...)
    alpha : float
        Angle for rotation [rad]
    delta : complex
        Complex value for translation
    is_edge_only: bool
        To plot transparent Patches
    edgecolor:
        Color of the edges if is_edge_only=True
    is_display : bool
        False to return the patches
    is_add_sign : bool
        True to Add + / - on the winding
    is_show_fig : bool
        To call show at the end of the method
    save_path : str
        full path including folder, name and extension of the file to save if save_path is not None
    win_title : str
        Title for the window
    is_legend : bool
        True to add the legend
    is_clean_plot : bool
        True to remove title, legend, axis (only machine on plot with white background)
    is_winding_connection : bool
        True to display winding connections (plot based on plot_polar_layout method of swat-em)
    is_winding_connection : bool
        True to display winding connections on phase A only
    Returns
    -------
    patches : list
        List of Patches
    fig : Matplotlib.figure.Figure
        Figure containing the plot
    ax : Matplotlib.axes.Axes object
        Axis containing the plot
    """

    (fig, ax, patch_leg, label_leg) = init_fig(fig=fig, ax=ax, shape="rectangle")

    surf_list = self.build_geometry(sym=sym, alpha=alpha, delta=delta)
    patches = list()
    head = None
    
    # getting the number of phases and winding connection matrix
    if self.winding is not None:
        if isinstance(self.winding, WindingSC):  # plot only one phase for WindingSC
            wind_mat = None
            qs = 1
        else:
            try:
                wind_mat = self.winding.get_connection_mat()
                qs = self.winding.qs
                
                if is_winding_connection:
                    # generate a datamodel for the winding
                    wdg = datamodel()
                    # generate winding from inputs
                    wdg.genwdg(
                        Q=self.get_Zs(),
                        P=2 * self.get_pole_pair_number(),
                        m=qs,
                        layers=self.winding.Nlayer,
                        turns=self.winding.Ntcoil,
                        w=self.winding.coil_pitch,
                    )
                    head = wdg.get_wdg_overhang(optimize_overhang=False)
            except:
                wind_mat = None
                qs = 1
    else:
        wind_mat = None
        qs = 1
    patch_leg, label_leg = list(), list()
    for surf in surf_list:
        label_dict = decode_label(surf.label)
        if WIND_LAB in label_dict["surf_type"] or BAR_LAB in label_dict["surf_type"]:
            if not is_lam_only:
                color, sign = find_wind_phase_color(wind_mat=wind_mat, label=surf.label)
                if sign == "+" and is_add_sign:
                    hatch = PLUS_HATCH
                elif sign == "-" and is_add_sign:
                    hatch = MINUS_HATCH
                else:
                    hatch = None
                patches.extend(
                    surf.get_patches(
                        color=color,
                        is_edge_only=is_edge_only,
                        hatch=hatch,
                        edgecolor=edgecolor,
                    )
                )
        else:
            color, legend = get_color_legend_from_surface(surf, is_lam_only)

            if color is not None:
                patches.extend(
                    surf.get_patches(
                        color=color,
                        is_edge_only=is_edge_only,
                        edgecolor=edgecolor,
                    )
                )
            if not is_edge_only and legend is not None and legend not in label_leg:
                label_leg.append(legend)
                patch_leg.append(Patch(color=color))
    
    # Display the result
    if is_display:
        # Display the result
        (fig, ax, patch_leg_1, label_leg_1) = init_fig(
            fig=fig, ax=ax, shape="rectangle"
        )

        # Merge patch_leg, label_leg
        for l, p in zip(label_leg_1, patch_leg_1):
            if l not in label_leg:
                label_leg.append(l)
                patch_leg.append(p)

        ax.set_xlabel("[m]")
        ax.set_ylabel("[m]")
        for patch in patches:
            ax.add_patch(patch)
        # Axis Setup
        ax.axis("equal")

        # Window title
        if is_winding_connection:
            if self.is_stator:
                prefix = "Stator winding radial pattern "
            else:
                prefix = "Rotor winding radial pattern "
        else:
            if self.is_stator:
                prefix = "Stator "
            else:
                prefix = "Rotor "
        if (
            win_title is None
            and self.parent is not None
            and self.parent.name not in [None, ""]
        ):
            win_title = self.parent.name + " " + prefix[:-1]
        elif win_title is None:
            win_title = prefix[:-1]
        manager = plt.get_current_fig_manager()
        if manager is not None:
            manager.set_window_title(win_title)

        # The Lamination is centered in the figure
        Lim = self.Rext * 1.5
        ax.set_xlim(-Lim, Lim)
        ax.set_ylim(-Lim, Lim)

        title = None

        # Add the legend
        if not is_edge_only:
            if is_winding_connection:
                if self.is_stator and "Stator" not in label_leg:
                    title = "Stator winding radial pattern"
                elif not self.is_stator and "Rotor" not in label_leg:
                    title = "Rotor winding radial pattern"
            elif is_lam_only:
                if self.is_stator and "Stator" not in label_leg:
                    title = "Stator Lamination"
                elif not self.is_stator and "Rotor" not in label_leg:
                    title = "Rotor Lamination"
            else:
                if self.is_stator and "Stator" not in label_leg:
                    title = "Stator with winding"
                elif not self.is_stator and "Rotor" not in label_leg:
                    title = "Rotor with winding"

            ax.set_title(title)

            # Add the winding legend only if needed
            if not is_lam_only and self.winding is not None:
                if is_add_sign:
                    if "Phase +" not in label_leg:
                        # Adding + and - in the legend as separate patch
                        patch_leg.append(Patch(color="w", hatch=PLUS_HATCH))
                        patch_leg[-1].set_edgecolor("k")
                        label_leg.append("Phase +")

                    if "Phase -" not in label_leg:
                        # Adding + and - legend
                        patch_leg.append(Patch(color="w", hatch=MINUS_HATCH))
                        patch_leg[-1].set_edgecolor("k")
                        label_leg.append("Phase -")

                phase_name = [prefix + n for n in gen_name(qs, is_add_phase=True)]
                for ii in range(qs):
                    if not phase_name[ii] in label_leg:
                        # Avoid adding twice the same label
                        index = ii % len(PHASE_COLORS)
                        patch_leg.append(Patch(color=PHASE_COLORS[index]))
                        label_leg.append(phase_name[ii])

            if is_legend:
                ax.legend(
                    patch_leg,
                    label_leg,
                    prop={
                        "family": dict_2D["font_name"],
                        "size": dict_2D["font_size_legend"],
                    },
                )

            for item in (
                [ax.xaxis.label, ax.yaxis.label]
                + ax.get_xticklabels()
                + ax.get_yticklabels()
            ):
                item.set_fontname(dict_2D["font_name"])
                item.set_fontsize(dict_2D["font_size_label"])
            ax.title.set_fontname(dict_2D["font_name"])
            ax.title.set_fontsize(dict_2D["font_size_title"])

        if save_path is not None:
            fig.savefig(save_path)
            plt.close(fig=fig)
        # Clean figure
        if is_clean_plot:
            ax.set_axis_off()
            ax.axis("equal")
            if ax.get_legend() is not None:
                ax.get_legend().remove()
            ax.set_title("")

        if is_show_fig:
            fig.show()
        return fig, ax
    else:
        return patches