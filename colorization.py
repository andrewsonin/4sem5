from random import randint

r = lambda: randint(0, 255)
colorize = lambda: '#%02X%02X%02X' % (r(), r(), r())
