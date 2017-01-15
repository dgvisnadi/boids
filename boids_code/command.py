#!/usr/bin/env python
from argparse import ArgumentParser
from boids_code.mkgraph import make_graph

def load_boids():
    parser = ArgumentParser(description = 'Visualize boids flying around')
    parser.add_argument('--number', help='Number of boids', dest='number', type=int)
    # parser.add_argument('--to', help='End Location', dest='end', type=str)
    # parser.add_argument('--steps', help='Steps between the two locations', dest='steps', type=int)
    parser.add_argument('--out', help='Type 'mp4' or 'gif' to save the animation', dest='out', type=str)
    arguments = parser.parse_args()

    make_graph(arguments.number, arguments.out)

if __name__ == "__main__":
    load_boids()
