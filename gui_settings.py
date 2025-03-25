

class gameSettings():
    """ Settings for the game """
    perspective = True






class defaultFonts():
    """ font=("FontName", Size, "Style") """
    # style include: "bold", "underline", "italic", "underline", "overstrike"
    default_font = ('Helvatical',10)
    alt_font = ("Arial", 12)
    

def rgb_2_hex(r, g, b):
    return f'#{r:02x}{g:02x}{b:02x}'

class DefaultTheme():
    """ Format: (red, green, blue) ranging from 0-256 """
    name = "default_theme"

    # Background colors
    left_header = rgb_2_hex(150, 150, 150)
    right_header = rgb_2_hex(150, 150, 150)
    opp_header = rgb_2_hex(100, 100, 100)
    game_header = rgb_2_hex(100, 100, 100)
    player_header = rgb_2_hex(100, 100, 100)
    setting_header = rgb_2_hex(150, 150, 150)
    settings_content_frame = rgb_2_hex(100, 100, 100)

    # Button colors
    button_color = rgb_2_hex(150, 150, 150)
    button_highlight_color = rgb_2_hex(120, 120, 120)

    # chess square colors
    light_square = rgb_2_hex(255, 206, 158)
    dark_square = rgb_2_hex(209, 139, 71)

    # Text color
    text_color = rgb_2_hex(0, 0, 0)
