#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""Tic-tac-toe game implementation"""


import argparse
import sys
import traceback
from ttt import engine


def process(args):
    try:
        eng = engine.Engine()
        while True:
            eng.move()
            print eng.board
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
