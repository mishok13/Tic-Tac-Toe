#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""Tic-tac-toe game implementation"""


import argparse
import sys
import traceback
from ttt import engine


def pretty_print(board):
    view = {engine.CROSS: 'X', engine.DRAUGHT: 'O', engine.EMPTY: ' '}
    for y in xrange(3):
        print ' | '.join(map(str, (view[board[(x, y)]] for x in xrange(3))))
        if y != 2:
            print '-' * 9


def process(args):
    try:
        eng = engine.Engine()
        while True:
            try:
                eng.move()
                pretty_print(eng.board)
                print
            except engine.Victory:
                pretty_print(eng.board)
                print 'Victory for %s' % {-1: 'crosses',
                                          1: 'draughts'}[eng.current_mark]
                break
            except engine.Draw:
                pretty_print(eng.board)
                print 'Draw'
                break
    except Exception:
        traceback.print_exc()
        return 2
    except BaseException:
        traceback.print_exc()
        return 1


def main(args):
    sys.exit(process(args))


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    main(parser.parse_args())
