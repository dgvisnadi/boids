from setuptools import setup, find_packages

# Setup file
setup(
    name = 'Boids',
    version = '0.1.0',
    description= 'XXX',
    packages = find_packages(exclude=['*tests']),
    scripts = ['scripts/boids'],
    # install_requires = ['argparse', 'geopy', 'matplotlib', 'numpy', 'requests', 'seaborn']
)
