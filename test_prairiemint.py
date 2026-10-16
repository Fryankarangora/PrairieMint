# test_prairiemint.py
"""
Tests for PrairieMint module.
"""

import unittest
from prairiemint import PrairieMint

class TestPrairieMint(unittest.TestCase):
    """Test cases for PrairieMint class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = PrairieMint()
        self.assertIsInstance(instance, PrairieMint)
        
    def test_run_method(self):
        """Test the run method."""
        instance = PrairieMint()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
