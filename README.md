# Quantum Observables Simulation

## Basic Quantum Theory, Observables and Measurements Workshop

**Author**: Andersson Programming


**Course**: Quantum Computing and Information Theory (CNYT)  
**Institution**: Escuela Colombiana de Ingeniería Julio Garavito  
**Repository**: https://github.com/AnderssonProgramming/quantum-observables-simulation

## Project Overview

This project implements a comprehensive quantum system simulator based on fundamental quantum mechanics principles from Chapter 4. The simulator addresses quantum observables, measurements, and system dynamics through practical implementations of theoretical concepts.

### Key Features

### Section 4.1 Basic Quantum System
- **Discrete Position Modeling**: Particle confined to discrete positions on a line
- **Position Probability Calculation**: Find probability of particle at specific position
- **State Transition Probability**: Calculate transition probability between quantum states

### Chapter 4 Programming Challenges
- **Transition Amplitude Calculation**: Compute amplitude and probability between two state vectors
- **Observable Analysis**: Hermitian verification, mean value, and variance calculations
- **Eigenvalue Probabilities**: Calculate probabilities of transitioning to eigenvector states
- **System Dynamics**: Evolution through series of unitary transformations

### Specific Exercise Solutions
- **Exercise 4.3.1**: Post-measurement state transitions and eigenvector analysis
- **Exercise 4.3.2**: Probability calculations and statistical distributions
- **Exercise 4.4.1**: Unitary matrix verification and composition properties
- **Exercise 4.4.2**: Quantum system evolution over multiple time steps
- **Exercise 4.5.2**: Multi-particle state vector generalization
- **Exercise 4.5.3**: Quantum state separability analysis

## Getting Started

### Prerequisites

```bash
# Required Python packages
numpy>=1.20.0
scipy>=1.7.0
matplotlib>=3.4.0
jupyter>=1.0.0
sympy>=1.8.0
```

### Installation

1. Clone the repository:
```bash
git clone https://github.com/AnderssonProgramming/quantum-observables-simulation.git
cd quantum-observables-simulation
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Launch Jupyter notebook:
```bash
jupyter notebook quantum_observables_simulation.ipynb
```

## Usage

### Running the Complete Simulation

Execute all notebook cells sequentially to run the complete quantum observables simulation:

1. **Environment Setup**: Install and configure required packages
2. **Library Imports**: Load scientific computing libraries
3. **Section 4.1 Basic System**: Test discrete quantum system with position probabilities
4. **Programming Challenges**: Execute all four Chapter 4 programming challenges
5. **Specific Exercises**: Run exercises 4.3.1, 4.3.2, 4.4.1, 4.4.2, 4.5.2, 4.5.3
6. **Results Analysis**: Review comprehensive outputs and mathematical explanations

### Individual Exercise Execution

Each exercise is implemented as a complete section in the notebook and can be run independently.

## Mathematical Framework

### Quantum State Representation

States are represented as complex-valued vectors in Hilbert space:
```
|ψ⟩ = Σᵢ cᵢ|i⟩, where Σᵢ |cᵢ|² = 1
```

### Observable Measurements

Observables are Hermitian matrices with real eigenvalues:
```
Ω = Ω†, Ω|eᵢ⟩ = λᵢ|eᵢ⟩
```

### Quantum Dynamics

Evolution is governed by unitary transformations:
```
|ψ(t+1)⟩ = U|ψ(t)⟩, where U†U = I
```

## File Structure

```
quantum-observables-simulation/
├── quantum_observables_simulation.ipynb  # Main notebook with all solutions
├── transcription_quantum_chapter.py      # Theory content and exercise descriptions
├── requirements.txt                      # Python dependencies
├── README.md                           # Project documentation
└── LICENSE                             # GNU GPL v3 license
```

## Built With

* **Python 3.8+** - Core programming language
* **NumPy** - Numerical computing and linear algebra
* **SciPy** - Advanced mathematical functions
* **Matplotlib** - Data visualization and plotting
* **Jupyter** - Interactive notebook environment
* **SymPy** - Symbolic mathematics

## License

This project is licensed under the GNU General Public License v3.0 - see the [LICENSE](LICENSE) file for details.

## Authors

* **Andersson Programming** - *Complete implementation* - [AnderssonProgramming](https://github.com/AnderssonProgramming)

## Acknowledgments

* Quantum Computing and Information Theory course materials
* Chapter 4 theoretical framework from course textbook
* NumPy and SciPy communities for scientific computing tools

---

*For questions or support, please open an issue in the GitHub repository.*
