#  :bird: Boids

Boids is a package that lets you simulate the flying behavior these birds.

Optionally, you can save the animation as a .mp4 or .gif file.

### Getting Started

The following instructions will guide you how to install the package on your local machine.

### Installing

```
pip install git+https://github.com/dgvisnadi/boids.git
```

### Usuage

The command ```boids --help``` will show you how to use the function:

```
usage: boids [-h] [--number BOIDS] [--speed SPEED] [--out TYPE]

Simulate boids flying behavior

optional arguments:
  -h, --help          show this help message and exit
  --number NUMBER     Number of boids
  --speed SPEED       slow or fast
  --out OUT           If TRUE, .gif file of animation will be saved
```

Example: ```boids --number 50 --speed slow --out gif```

<img src="/img/boids_slow.gif" width=48%/> <img src="/img/boids_fast.gif" width=48%/>

For any distribution, please have a look at [CITATION.md](/CITATION.md) and [LICENSE](/LICENSE)
