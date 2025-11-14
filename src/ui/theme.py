"""Theme helpers for the Motor Report App UI.

This module provides a minimal, safe-to-import wrapper around Flet theming.
It intentionally catches errors so importing it in non-GUI/test environments
does not raise hard failures.
"""
from typing import Literal, Optional
import logging

try:
    import flet as ft
except Exception:
    ft = None

logger = logging.getLogger(__name__)

ThemeModeLiteral = Literal["light", "dark", "system"]


def apply_theme(page, default_mode: ThemeModeLiteral = "system") -> None:
    """Apply a conservative theme to the provided Flet `page`.

    - Sets `page.theme` and `page.dark_theme` to default Theme objects.
    - Sets `page.theme_mode` according to `default_mode` or persisted client_storage.
    This is intentionally lightweight so it won't change visual design drastically
    but will allow Flet to use its native light/dark tokens when available.
    """
    if ft is None:
        logger.debug("Flet not available; apply_theme is a no-op.")
        return

    try:
        # Basic theme objects (can be enriched later)
        try:
            page.theme = ft.Theme()
        except Exception:
            # Some Flet runtimes may not allow setting theme object early
            pass

        try:
            page.dark_theme = ft.Theme()
        except Exception:
            pass

        # Decide mode: preference in client_storage overrides default
        mode = default_mode
        try:
            if hasattr(page, "client_storage") and page.client_storage is not None:
                stored = page.client_storage.get("theme")
                if stored in ("light", "dark", "system"):
                    mode = stored
        except Exception:
            # ignore storage problems
            pass

        try:
            if mode == "light":
                page.theme_mode = ft.ThemeMode.LIGHT
            elif mode == "dark":
                page.theme_mode = ft.ThemeMode.DARK
            else:
                page.theme_mode = ft.ThemeMode.SYSTEM
        except Exception:
            # if ThemeMode isn't available, ignore
            pass

        # Try to set a neutral page background (best-effort)
        try:
            if not getattr(page, "bgcolor", None):
                page.bgcolor = ft.Colors.WHITE if mode != "dark" else ft.Colors.GREY_900
        except Exception:
            pass

        try:
            page.update()
        except Exception:
            # update may not be legal during some initialization sequences
            pass

    except Exception as e:
        logger.debug("apply_theme encountered an error: %s", e)


def set_user_theme(page, mode: ThemeModeLiteral) -> None:
    """Persist a user theme preference and apply it.

    mode must be 'light', 'dark' or 'system'. Silently returns if ft is missing.
    """
    if ft is None:
        return
    try:
        if hasattr(page, "client_storage") and page.client_storage is not None:
            try:
                page.client_storage.set("theme", mode)
            except Exception:
                pass
        apply_theme(page, default_mode=mode)
    except Exception:
        pass


def toggle_theme(page) -> None:
    """Toggle page theme mode between light and dark (best-effort)."""
    if ft is None:
        return
    try:
        current = getattr(page, "theme_mode", None)
        if current == ft.ThemeMode.DARK:
            set_user_theme(page, "light")
        else:
            set_user_theme(page, "dark")
    except Exception:
        pass
