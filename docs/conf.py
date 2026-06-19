"""Sphinx configuration for the ibflex documentation."""

from pathlib import Path
import sys

# ``ibflex`` uses a flat layout (the package lives at the repo root) and is
# editable-installed in the docs environment; this insert is belt-and-suspenders
# so autodoc can import it even without the editable install.
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

# --------------------------------------------------------------------------- #
# Project information
# --------------------------------------------------------------------------- #
project = "ibflex"
author = "Monte Hoover"
release = "1.1"
root_doc = "index"

# --------------------------------------------------------------------------- #
# Extensions
# --------------------------------------------------------------------------- #
extensions = [
    "sphinx.ext.autodoc",      # pull API docs from docstrings
    "sphinx.ext.napoleon",     # understand NumPy-style Parameters/Returns
    "sphinx.ext.mathjax",      # render LaTeX math (when docstrings use it)
    "sphinx.ext.intersphinx",  # cross-link to Python stdlib types
    "sphinx.ext.viewcode",     # add "[source]" links next to each object
]

templates_path = ["_templates"]
exclude_patterns = ["_build", ".DS_Store"]

# --------------------------------------------------------------------------- #
# Autodoc / Napoleon
# --------------------------------------------------------------------------- #
# Keep functions in source order (approx -> exact -> simple_vol) rather than
# alphabetical, which matches how the modules are organised.
autodoc_member_order = "bysource"
napoleon_numpy_docstring = True
napoleon_google_docstring = False

# Six ``ibflex.Types`` dataclasses (FlexQueryResponse, SLBActivity, Transfer,
# CorporateAction, CashTransaction, SecurityInfo) each define a field named
# ``type``. When autodoc renders their generated ``__init__`` signatures, Sphinx
# auto-cross-references the ``type`` parameter name and finds all six attribute
# targets, so it can't disambiguate (``<unknown>:1: more than one target found
# for cross-reference 'type'``). There is no narrower Sphinx toggle for this
# parameter-name collision short of renaming the (legitimate) fields, so we
# suppress the single ref.python warning it produces.
suppress_warnings = ["ref.python"]

# --------------------------------------------------------------------------- #
# HTML output
# --------------------------------------------------------------------------- #
html_theme = "furo"
html_title = "ibflex"
html_static_path = ["_static"]
html_css_files = ["rockbound.css"]

# Rockbound Capital brand palette, wired through Furo's CSS variables. Furo emits
# every key here verbatim as a ``--<key>`` custom property, so the brand colors
# (and the ``rockbound-*`` helpers used in rockbound.css) follow the light/dark
# toggle automatically. Typography (Libre Franklin) and the Warm Gold accent rules
# live in _static/rockbound.css. No logo, per the docs brief.
_BODY_STACK = '"Libre Franklin", "Helvetica Neue", Arial, sans-serif'
html_theme_options = {
    "light_css_variables": {
        "color-brand-primary": "#1A2A44",      # Deep Navy
        "color-brand-content": "#317098",      # Button Blue (links)
        "color-brand-visited": "#317098",
        "color-background-primary": "#F7F9FB",  # Cool White (page)
        "color-background-secondary": "#F1F4F7",  # Aqua Haze (sidebar/panels)
        "color-background-hover": "#F1F4F7",
        "color-foreground-primary": "#303F4F",  # body text
        "color-foreground-secondary": "#5D6D7E",  # Steel Blue
        "color-foreground-muted": "#5D6D7E",
        "color-api-name": "#1A2A44",
        "color-api-pre-name": "#5D6D7E",
        "font-stack": _BODY_STACK,
        "rockbound-heading": "#1A2A44",         # Deep Navy headings
        "rockbound-accent": "#D9B38D",          # Warm Gold separator rules
    },
    "dark_css_variables": {
        "color-brand-primary": "#BFD1E4",       # Steel Blue ramp, lightest (subtle nav accent)
        "color-brand-content": "#9AB6E3",        # Deep Navy ramp, lightest (links)
        "color-brand-visited": "#9AB6E3",
        "color-background-primary": "#00081E",   # Deep Navy ramp, darkest -- near-black page
        "color-background-secondary": "#1A2A44",  # Deep Navy anchor -- sidebar/panels
        "color-background-hover": "#415981",     # Deep Navy ramp, stop 3
        "color-foreground-primary": "#F7F9FB",   # Cool White body text
        "color-foreground-secondary": "#BFD1E4",  # Steel Blue ramp, lightest
        "color-foreground-muted": "#8697A9",      # Steel Blue ramp, stop 2
        "color-api-name": "#F7F9FB",             # white function names
        "color-api-pre-name": "#8697A9",
        "font-stack": _BODY_STACK,
        "rockbound-heading": "#F7F9FB",          # Cool White -- white titles
        "rockbound-accent": "#D9B38D",
    },
}

intersphinx_mapping = {"python": ("https://docs.python.org/3", None)}
