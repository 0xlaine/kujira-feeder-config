#!/usr/bin/env python3

import argparse
import requests


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("--custom", type=str, required=True)
    parser.add_argument("--config", type=str, default="global")

    return parser.parse_args()


def main():
    args = parse_args()

    base_config = open(args.config, "r").read() + "\n"
    config = open(args.custom, "r").read() + "\n"

    print(config + base_config)


if __name__ == "__main__":
    main()
