def hex_to_rgb(hex_code):
    hex_code = hex_code.lstrip('#')
    return tuple(int(hex_code[i:i+2], 16) for i in (0, 2, 4))

def rgb_to_hsl(r, g, b):
    r /= 255.0
    g /= 255.0
    b /= 255.0
    max_c = max(r, g, b)
    min_c = min(r, g, b)
    l = (max_c + min_c) / 2.0

    if max_c == min_c:
        s = h = 0.0
    else:
        d = max_c - min_c
        s = d / (2.0 - max_c - min_c) if l > 0.5 else d / (max_c + min_c)
        if max_c == r:
            h = (g - b) / d + (6.0 if g < b else 0.0)
        elif max_c == g:
            h = (b - r) / d + 2.0
        elif max_c == b:
            h = (r - g) / d + 4.0
        h /= 6.0

    return round(h * 360), round(s * 100), round(l * 100)

def hex_to_hsl(hex_code):
    def _hsl(h, s, l):
        return "{} {}% {}%".format(h, s, l)

    r, g, b = hex_to_rgb(hex_code)
    h, s, l = rgb_to_hsl(r, g, b)
    return _hsl(h, s, l)
