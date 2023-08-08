#Exercise
from uagame import Window
from time import sleep

window = Window('hello', 300, 200)

word = window.input_string('Enter string >', 0, 0)

string_width = window.get_string_width(word)
window_width = window.get_width()
string_height = window.get_font_height()
window_height = window.get_height()

line_x = window_width - string_width
line_y = window_height - string_height

window.draw_string(word, line_x, line_y)
window.update()
sleep(2)

window.close()
