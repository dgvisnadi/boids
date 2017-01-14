from setuptools import setup, find_packages

# Setup file
setup(
    name = 'Boids',
    version = '0.1.0',
    description= 'Flying boids simulation',
    packages = find_packages(exclude=['*tests']),
    scripts = ['scripts/boids'],
    install_requires = ['argparse', 'matplotlib', 'numpy', 'pyyaml', 'seaborn']
)
