#!/usr/bin/env python3
import argparse

from checkers.manager import get_prepared_checkers


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='tyyp: an internet censorship analyzer.')
    parser.add_argument('domain', type=str, help='Domain to analyze')
    args = parser.parse_args()

    for checker in get_prepared_checkers():
        result = checker.check(args.domain)
