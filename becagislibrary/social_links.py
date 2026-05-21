# -*- coding: utf-8 -*-
"""HTML footer social links using image files (no embedded base64)."""

__author__ = "Thang Quach"
__date__ = "2022-08-25"
__copyright__ = "(L) 2022 by Thang Quach"

import os


def social_bw_html(plugin_root):
    """Return HTML snippet for GitHub and LinkedIn icons in algorithm help footers."""
    github_icon = os.path.join(plugin_root, "images", "github.png")
    linkedin_icon = os.path.join(plugin_root, "images", "linkedin.png")
    return (
        '<a target="_blank" rel="noopener noreferrer" href="https://github.com/thangqd">'
        '<img title="Github" src="' + github_icon + '"></a>'
        '<a target="_blank" rel="noopener noreferrer" href="https://www.linkedin.com/in/thangqd/">'
        '<img title="Linkedin" src="' + linkedin_icon + '"></a> '
    )
