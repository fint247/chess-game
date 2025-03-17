class default_fonts():
    """ font=("FontName", Size, "Style") """
    # style include: "bold", "underline", "italic", "underline", "overstrike"
    menu_font = ('Helvatical',10)
    file_header_font = ("Arial", 12)
    editor_font = ("Arial", 12)
    line_num_font = ("Arial", 12)
    output_font = ("Arial", 12)
    setting_font = ("Arial", 12)
    setting_selected_font = ("Arial", 12, "bold")

def rgb_2_hex(r, g, b):
    return f'#{r:02x}{g:02x}{b:02x}'

class DefaultTheme():
    """ Format: (red, green, blue) ranging from 0-256 """
    name = "default_theme"

    # Background colors
    header_color = rgb_2_hex(150, 150, 150)
    file_header_color = rgb_2_hex(180, 180, 180)
    editor_color = rgb_2_hex(200, 200, 200)
    line_num_color = rgb_2_hex(190, 190, 190)
    output_color = rgb_2_hex(100, 100, 100)
    setting_content_color = rgb_2_hex(180, 180, 180)

    # Button colors
    menu_button_color = rgb_2_hex(150, 150, 150)
    menu_button_highlight_color = rgb_2_hex(128, 100, 100)

    file_button_color = rgb_2_hex(170, 170, 170)
    file_button_highlight_color = rgb_2_hex(128, 100, 100)
    file_focus_color = rgb_2_hex(200, 200, 200)

    # Text color
    text_color = rgb_2_hex(0, 0, 0)
