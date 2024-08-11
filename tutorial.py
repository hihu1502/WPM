import curses
from curses import wrapper


def main(stdscr):
    curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_WHITE, curses.COLOR_BLACK)

    stdscr.clear() # wrapper lps run clear terminal jd 0
    stdscr.addstr(1, 4 ,"Hello world!") #add text to screen
    stdscr.refresh()  #ref scr
    key = stdscr.getkey() #lps minta input dr user bru ttp
    print(key)


wrapper(main) #restore prog to init state
