import win32gui, time

def positions(filename, delay = 0.1, period=3):
    p = []
    start = time.time()
    while True:
        p.append(win32gui.GetCursorPos())
        time.sleep(delay)
        if time.time() - start > period:
            start = time.time()
            with open(filename, 'a+') as f:
                f.write('\n'.join(map(lambda (x,y): '{} {}'.format(x,y), p)))
                f.write('\n')
            p = []
            
positions('cursor_positions.txt')