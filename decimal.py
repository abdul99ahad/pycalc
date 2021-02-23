def decimal(display):

    display = str(display)
    if display.find('.') == -1:
        display = str(display) + '.'

    return display
