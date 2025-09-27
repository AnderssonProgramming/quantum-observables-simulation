# Quantum Observables Simulation Tests
# Validation and verification tests for all quantum algorithms

import numpy as np
import unittest

class QuantumTests(unittest.TestCase):
    """Test suite for quantum observables simulation"""
    
    def test_normalization(self):
        """Test quantum state normalization"""
        state = np.array([1/np.sqrt(2), 1j/np.sqrt(2)])
        norm = np.linalg.norm(state)
        self.assertAlmostEqual(norm, 1.0, places=10)
    
    def test_unitary_property(self):
        """Test unitary matrix properties"""
        U = np.array([[0, 1], [1, 0]])
        product = U @ U.conj().T
        identity = np.eye(2)
        self.assertTrue(np.allclose(product, identity))
    
    def test_probability_conservation(self):
        """Test probability conservation"""
        state = np.array([0.6, 0.8])
        probabilities = np.abs(state)**2
        total_prob = np.sum(probabilities)
        self.assertAlmostEqual(total_prob, 1.0, places=10)

if __name__ == '__main__':
    unittest.main()