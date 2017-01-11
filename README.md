#  :bird: Boids

Boids is a package that lets you visualize the number of green pixels between two location.
It uses Google API to retrieve the image and counts the green pixels.


### Getting Started

The following instructions will guide you how to install the package on your local machine.

### Installing

```
pip install git+https://github.com/dgvisnadi/boids.git
```

### Usuage

The command ```greengraph --help``` will show you how to use the function:

```
usage: greengraph [-h] [--from START] [--to END] [--steps STEPS] [--out OUT]

Visualize amount of green pixels between two locations

optional arguments:
  -h, --help     show this help message and exit
  --from START   Start Location
  --to END       End Location
  --steps STEPS  Steps between the two locations
  --out OUT      Save as: (i.e. image.png)
```

Example: ```greengraph --from London --to Paris --steps 10 --out London_Paris.png```

<img src="/img/boids.gif" width=80% height=80%/>

For any distribution, please have a look at [CITATION.md](/CITATION.md) and [LICENSE](/LICENSE)
