#!/usr/bin/env python3
# Small program to display precious metal future prices on polybar. Written by Zeb.

import argparse
import requests.exceptions
from yahoo_fin import stock_info as si

ROUND_BY = 1

# Ticker symbol -> (display symbol, unit label)
METALS = {
    'silver':    ('SI=F', 'Ag', '/oz'),
    'gold':      ('GC=F', 'Au', '/oz'),
    'platinum':  ('PL=F', 'Pt', '/oz'),
    'palladium': ('PA=F', 'Pd', '/oz'),
    'copper':    ('HG=F', 'Cu', '/lb'),
}


def get_price(ticker):
    try:
        return round(si.get_live_price(ticker), ROUND_BY)
    except (requests.exceptions.RequestException, KeyError, ValueError, AssertionError):
        return None


def display_metals():
    parser = argparse.ArgumentParser(description='Display precious metal futures prices in Polybar.')
    parser.add_argument('-s', '--silver',    help='display the price of silver (troy oz)',    action='store_true')
    parser.add_argument('-g', '--gold',      help='display the price of gold (troy oz)',      action='store_true')
    parser.add_argument('-p', '--platinum',  help='display the price of platinum (troy oz)',  action='store_true')
    parser.add_argument('-a', '--palladium', help='display the price of palladium (troy oz)', action='store_true')
    parser.add_argument('-c', '--copper',    help='display the price of copper (per lb)',      action='store_true')
    args = parser.parse_args()

    selected = [k for k in METALS if getattr(args, k)]

    if not selected:
        print("No metal chosen to display! Use --help for more information.")
        return

    parts = []
    for metal in selected:
        ticker, symbol, unit = METALS[metal]
        price = get_price(ticker)
        parts.append(f"{symbol}: ${price}{unit}" if price is not None else f"{symbol}: N/A")

    print(" | ".join(parts))


if __name__ == '__main__':
    display_metals()

