import tingbot
from tingbot import *

def update():
    screen.fill(color='black')
    screen.brightness = tingbot.app.settings['brightness']
    
    if tingbot.app.settings['brightness'] > 0:
        screen.text('-', font_size=15, xy=(10,15))
        screen.text('off', font_size=15, xy=(50,15))
        screen.text('on', font_size=15, xy=(275,15))
        screen.text('+', font_size=15, xy=(310,15))
        
        screen.text('Brightness\n %i%%' % tingbot.app.settings['brightness'])

@left_button.press
def press():
    if tingbot.app.settings['brightness'] > 0:
        tingbot.app.settings['brightness'] -= 10
    update()
    
@midleft_button.press
def press():
    tingbot.app.settings['brightness'] = 0
    update()
    
@midright_button.press
def press():
    tingbot.app.settings['brightness'] = 100
    update()

@right_button.press
def press():
    if tingbot.app.settings['brightness'] < 100:
        tingbot.app.settings['brightness'] += 10
    update()

update()
tingbot.run()