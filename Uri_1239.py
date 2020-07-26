while True:
    try:
        text = input()
        for char in text:
            text = text.replace('_', '<i>',1).replace('_', '</i>',1).replace('*', '<b>',1).replace('*', '</b>',1)
        print(text)
    except:
        break
