def luminance_factor(lightness: float) -> float:
    """
    Calculates the luminance factor (Y) from the lightness (L*)
    using the CIE 15:2018 standard.

    :param lightness: The lightness value (L*) to convert to luminance factor (Y).
    """
    return ((lightness + 16) / 116) ** 3


def calc_opacity(L_white: float, L_black: float) -> float:
    """
    Calculates the opacity percentage based on lightness values (L*) using the ISO 2471 standard.

    :param L_white: The lightness value (L*) of the sample over white reference.
    :param L_black: The lightness value (L*) of the sample over black reference.
    """
    Yw = luminance_factor(L_white)
    Yb = luminance_factor(L_black)
    return (Yb / Yw) * 100


if __name__ == "__main__":
    Lw = 90.91
    Lb = 74.98

    opacity = calc_opacity(Lw, Lb)

    print(f"Opacidade calculada: {opacity:.2f}%")
