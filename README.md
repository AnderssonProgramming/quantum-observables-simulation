# Quantum Observables Simulation

## Basic Quantum Theory, Observables and Measurements Workshop

**Author**: Systems Engineering Team  
**Course**: Quantum Computing and Information Theory (CNYT)  
**Institution**: Escuela Colombiana de Ingeniería Julio Garavito  
**Repository**: https://github.com/AnderssonProgramming/quantum-observables-simulation

## Project Overview

This project implements a comprehensive quantum system simulator based on fundamental quantum mechanics principles from Chapter 4. The simulator addresses quantum observables, measurements, and system dynamics through practical implementations of theoretical concepts.

### Key Features

- **Quantum System Modeling**: Discrete particle position simulation with complex state vectors
- **Observable Measurements**: Hermitian matrix analysis with eigenvalue decomposition
- **State Transition Analysis**: Probability calculations for quantum state collapse
- **Unitary Evolution**: Time-based system dynamics with unitary transformations
- **Multi-Particle Systems**: Tensor product construction for composite quantum systems
- **Entanglement Analysis**: Separability detection and quantum correlation analysis

## Technical Implementation

### Core Components

1. **QuantumSystemSimulator**: Base class for quantum state management
2. **ObservableMeasurement**: Observable analysis and measurement simulation
3. **UnitaryTransformation**: Quantum dynamics and evolution operators
4. **QuantumBilliardBall**: Discrete time evolution simulation
5. **MultiParticleQuantumSystem**: Tensor product system construction
6. **QuantumStateSeparabilityAnalyzer**: Entanglement and separability analysis

### Solved Exercises

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

### Installing

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

## Running the Exercises

### Complete Simulation

Execute all notebook cells sequentially to run the complete quantum observables simulation:

1. **Environment Setup**: Install and configure required packages
2. **Library Imports**: Load scientific computing libraries
3. **Core Implementation**: Initialize quantum system classes
4. **Exercise Solutions**: Run specific problem implementations
5. **Visualization**: Generate plots and analysis results

### Individual Exercise Execution

Each exercise can be run independently:

```python
# Exercise 4.3.1: Observable measurements
measurement_system = ObservableMeasurement(observable_matrix)
possible_states = measurement_system.get_possible_states_after_measurement()

# Exercise 4.4.2: Quantum evolution
qbb = QuantumBilliardBall(initial_state, unitary_matrix)
final_state = qbb.evolve_multiple_steps(3)

# Exercise 4.5.3: Separability analysis
analyzer = QuantumStateSeparabilityAnalyzer(2, [2, 2])
result = analyzer.analyze_two_particle_separability(state_vector)
```

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

## Results Summary

- **Exercise 4.3.1**: Identified post-measurement eigenstates
- **Exercise 4.3.2**: Calculated transition probabilities (p₁ = p₂ = 0.5)
- **Exercise 4.4.1**: Verified unitary matrix properties and composition
- **Exercise 4.4.2**: Computed final probability at position 3: 0.500
- **Exercise 4.5.2**: Derived n-particle state vectors with 2ⁿ dimensions
- **Exercise 4.5.3**: Determined state separability using rank analysis

## Built With

* **Python 3.8+** - Core programming language
* **NumPy** - Numerical computing and linear algebra
* **SciPy** - Advanced mathematical functions
* **Matplotlib** - Data visualization and plotting
* **Jupyter** - Interactive notebook environment
* **SymPy** - Symbolic mathematics

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit changes using conventional commits (`git commit -m 'feat: add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## Versioning

This project uses conventional commits for systematic development:

- `feat:` New features and implementations
- `docs:` Documentation updates
- `test:` Testing and validation additions
- `chore:` Maintenance and project setup

## Authors

* **Systems Engineering Team** - *Complete implementation* - [AnderssonProgramming](https://github.com/AnderssonProgramming)

## License

This project is licensed under the MIT License - see the LICENSE.md file for details

## Acknowledgments

* Quantum Computing and Information Theory course materials
* Escuela Colombiana de Ingeniería Julio Garavito
* Chapter 4 theoretical framework from course textbook
* NumPy and SciPy communities for scientific computing tools

---

*For questions or support, please open an issue in the GitHub repository.*
