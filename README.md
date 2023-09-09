[<img src="./image/README/1694220443343.png" width="250" />](./image/README/1694220443343.png)
[<img src="./Classical Mechanics/N-Body.gif" width="333" />](./Classical Mechanics/N-Body.gi)

# Computational Physics with Python using Jupyter Notebooks ⚛️ <img src="https://i0.wp.com/tinkercademy.com/wp-content/uploads/2018/04/python-icon.png?ssl=1" width=20/> <img src="https://docs.poppy-project.org/fr/img/logo/jupyter.png" width=20>

This repository is a collection of physics problems solutions using Jupyter Notebooks that I was working on them during my degree in Physics Engineering.

## Table of Contents

The repository is divided into the following folders:

* **Classical Mechanics** ~ Problems related to classical mechanics (Newtonian mechanics, Lagrangian mechanics, Hamiltonian mechanics, etc.)
* **Classical Electrodynamics** ~ Problems related to classical electrodynamics (Maxwell's equations, etc.)
* **Quantum Mechanics** ~ Problems related to quantum mechanics (Schrödinger equation, etc.)
* **Thermodynamics** ~ Problems related to thermodynamics (Laws of thermodynamics, etc.)
* **Dynamical Systems** ~ Problems related to dynamical systems (Chaos theory, etc.)

## Requirements
* Python 3.6 or higher

I recommend using [Anaconda](https://www.anaconda.com/) to install all the requirements. You can download Anaconda 
from [here](https://www.anaconda.com/products/individual). Or create a virtual environment using [virtualenv](https://virtualenv.pypa.io/en/latest/).

### Using Anaconda

You can create a new environment using the following commands:

```bash
conda create --name py_physics python=3.8
conda activate py_physics
conda install -c conda-forge notebook
```

### Using virtualenv

First, you need to install virtualenv using the following command:

```bash
pip install virtualenv
```

Then, you can create a new environment using the following commands:

```bash
virtualenv py_physics
source py_physics/bin/activate
pip install notebook
```

### Libraries needed

* Jupyter Notebook
* Numpy
* Matplotlib
* Scipy
* Sympy
* Sklearn
* Numba

## Installation

You can install all the requirements using the following command:

```bash
pip install -r requirements.txt
```

## Usage

You can run the notebooks using the following command:

```bash
jupyter notebook
```

## References

This repository contains some techniques based on the YouTube channel [Mr. P Solver](https://www.youtube.com/@MrPSolver)

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.
