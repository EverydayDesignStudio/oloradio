def init():
    # pin configuration
    global switch1
    switch1 = 23
    global switch2
    switch2 = 24
    global mEnable
    mEnable = 6
    global mLeft
    mLeft = 13
    global mRight
    mRight = 12
    # Software SPI configuration:
    global CLK
    CLK  = 11
    global MISO
    MISO = 9
    global MOSI
    MOSI = 10
    global CS
    CS   = 8
    global yesorno
    yesorno = col.none + '[ ' + col.gre + 'Y' + col.none + ' / ' + col.red + 'N' + col.none + " ] "
    global values
    global timeframe
    timeframe = ''
    global prevtimeframe
    prevtimeframe = ''
    # Pretty labels
    global labels
    labels = ['swi', 'cap', 'sw1', 'sw2']