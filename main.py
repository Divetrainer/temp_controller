from machine import Pin

board_led = Pin("LED", mode=Pin.OUT, value=1)
button = Pin(15, mode=Pin.IN, pull=Pin.PULL_DOWN)
while True:   
    #read input from button to swap screens
    if button.value() == 1:
        board_led.on()
        #screen logic swap
    else:
        board_led.off()
        #base case for screens
    
    
    
    
