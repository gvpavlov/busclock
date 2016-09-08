from RPLCD import CharLCD
import time

cyrillic = {
    'а': 'a',
    'б': chr(160),
    'в': chr(181),
    'г': chr(161),
    'д': chr(162),
    'е': 'e',
    'ж': chr(163),
    'з': chr(178),
    'и': chr(164),
    'й': chr(165),
    'к': chr(182),
    'л': chr(166),
    'м': chr(183),
    'н': chr(184),
    'о': 'o',
    'п': chr(167),
    'р': 'p',
    'с': 'c',
    'т': chr(185),
    'у': chr(179),
    'ф': chr(168),
    'х': 'x',
    'ц': chr(169),
    'ч': chr(170),
    'ш': chr(171),
    'щ': chr(172),
    'ъ': chr(173),
    'ь': chr(180),
    'ю': chr(176),
    'я': chr(177),
    'А': 'A',
    'Б': chr(128),
    'В': 'B',
    'Г': chr(129),
    'Д': chr(130),
    'Е': 'E',
    'Ж': chr(131),
    'З': chr(146),
    'И': chr(132),
    'Й': chr(133),
    'К': 'K',
    'Л': chr(134),
    'М': 'M',
    'Н': 'H',
    'О': 'O',
    'П': chr(135),
    'Р': 'P',
    'С': 'C',
    'Т': 'T',
    'У': chr(147),
    'Ф': chr(136),
    'Х': 'X',
    'Ц': chr(137),
    'Ч': chr(138),
    'Ш': chr(139),
    'Щ': chr(140),
    'Ъ': chr(141),
    'Ь': chr(148),
    'Ю': chr(144),
    'Я': chr(145),
}

def utf8_to_lcd(str):
    lcd_str = ""
    for c in str:
        lcd_str += cyrillic.get(c, c)
    return lcd_str

def screen_write(rows):
    lcd.clear()
    lcd.write_string(utf8_to_lcd(rows[0]))
    lcd.cursor_pos = (1, 0)
    lcd.write_string(utf8_to_lcd(rows[1]))

lcd = CharLCD()
# NOTE: Rows are 16 characters long.
rows = ("абвгд1234567890", "adhjуфхцчшщъьюя")

screen_write((rows[1], rows[1].upper()))

# Loops through the ASCII table on the screen.
#
#for i in range(200, 255):
#    lcd.write_string(str(i) + ' ' + chr(i))
#    input("Press enter!")
#    lcd.clear()

