# paper-implementations
Collection of AI, ML and robotics paper reproducibility work


## 1. Introduction
This project is a personal collection of reproducibility experiments covering a selection of milestone papers from 
the fields of machine learning and robotics. The **purpose** of this work is to **facilitate human learning**: 
re-implementing important algorithms and techniques is an excellent mechanism for developing a deeper, internalised 
understanding of the technology. It's also a great way to exercise the **brain's plasticity**: like going to the gym,
but for the mind.

I think of this as the equivalent of doing maths exercises in school: you don't do them because you'll be doing
the same calculations in a job. You do them in order to develop a working **understanding** of mathematics, which in 
turn is a pre-requisite for developing the sort of understanding of science and engineering domains that is actually
required in order to do useful work.

By line count, the majority of the code in this repository will obviously be written by AI. However, the key rule of
this project is that **whatever you want to truly understand, you must do yourself**. Having AI write those parts for me
would defeat the purpose of this pedagogical exercise. Therefore, while boilerplate code like training infrastructure
is in the remit of coding agents, the following are strictly written by me:

1. The core training and evaluation steps that are unique to each paper's contribution
2. The brief analysis of the outcomes of each reproducibility exercise

This repository is **not** a software library intended for reuse (although you are free to use it as such).


## 2. Setup
This project's dependencies are managed using `uv`. In order to get started, ensure `uv` is available, then:

```shell
uv venv
make setup
```

You can then either activate the virtual environment with `source .venv/bin/activate` and run `python` commands, or
use the `uv run` command as per your own preference.


## 3. Quickstart

Create a new paper directory and README from the repository template with:

```shell
make new-paper PAPER=2015-residual-learning
```

Each paper's README documents its own setup, training and evaluation commands. Run `make check` to verify repository
formatting and linting.


## 4. Structure
```
papers/<year>-<slug>/   independent, self-contained implementation of a single paper
common/                 infrastructure shared across papers
notebooks/              scratchpad for exploration and quick tests
resources/templates/    reusable documentation templates
```

Generally each paper's directory contains the core algorithm, training and evaluation entry points, and 
a `README.md` with a brief description and reproduction analysis. A local `paper.pdf` may be placed beside the
implementation for reference; it is ignored by Git, so the README should link to an immutable version of the paper.

Notebooks are plain `jupyter` since the GitHub web interface renders them natively.


## 5. Role of Coding Agents
In order to facilitate the pedagogical aims mentioned in the [introduction](#1-introduction), a few self-imposed
limitations in the use of coding agents should be followed.

AI **should** be used for:
1. Repository scaffolding and maintenance
2. Shared boilerplate code such as training infrastructure
3. Learning assistance, such as finding errors or quizzing the user

AI **should not** be used for:
1. Writing the core steps of the algorithms being re-implemented
2. Understanding the outcomes of the re-implementation attempt

In other words: the 5% of code implementing what you want to *learn* should be written by hand; delegate the remaining
95% to AI.


## 6. Citation
The code in this repository is available under the MIT License (see [LICENSE](LICENSE)). If using this work in
a publication such as a blog or paper, please cite this repository:

```bibtex
@software{,
  author = {De Bernardi, Marcello},
  title = {Paper Implementations: A collection of learning-oriented paper reproducibility experiments},
  year = {2026},
  publisher = {GitHub},
  howpublished = {\url{https://github.com/marcellodebernardi/paper-implementations}},
}
```
