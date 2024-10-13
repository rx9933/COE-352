import numpy as np
import pytest
from linear_spring import solve_spring_mass_system  # Replace with actual module name

def test_spring_mass_system_fixed_fixed():
    # Input parameters for the first test case
    num_springs = 4
    spring_constants = np.ones(num_springs)
    masses = [1, 1, 1]  # Example masses (in kg)
    boundary_condition = "fixed-fixed"  # Boundary condition

    # Call the function
    u, elongations, stresses, cond_num = solve_spring_mass_system(num_springs, spring_constants, masses, boundary_condition)

    # Expected values for fixed-fixed boundary condition
    expected_displacements = np.array([14.715, 19.62, 14.715])
    expected_elongations = np.array([14.715, 4.905, -4.905, -14.715])
    expected_stresses = np.array([14.715, 4.905, -4.905, -14.715])
    expected_cond_num = 5.828427124746192
    # print(elongations)
    # Assertions
    assert np.allclose(u, expected_displacements, atol=1e-3)
    assert np.allclose(elongations, expected_elongations, atol=1e-3)
    assert np.allclose(stresses, expected_stresses, atol=1e-3)
    assert np.isclose(cond_num, expected_cond_num, atol=1e-5)

def test_spring_mass_system_fixed_free():
    # Input parameters for the second test case
    num_springs = 3
    spring_constants = np.ones(num_springs)
    masses = [1, 1, 1]  # Example masses (in kg)
    boundary_condition = "fixed-free"  # Boundary condition

    # Call the function
    u, elongations, stresses, cond_num = solve_spring_mass_system(num_springs, spring_constants, masses, boundary_condition)

    # Expected values for fixed-free boundary condition
    expected_displacements = np.array([29.43, 49.05, 58.86])
    expected_elongations = np.array([29.43, 19.62, 9.81])
    expected_stresses = np.array([29.43, 19.62, 9.81])
    expected_cond_num = 16.393731622284424

    # Assertions
    assert np.allclose(u, expected_displacements, atol=1e-3)
    assert np.allclose(elongations, expected_elongations, atol=1e-3)
    assert np.allclose(stresses, expected_stresses, atol=1e-3)
    assert np.isclose(cond_num, expected_cond_num, atol=1e-5)


def test_spring_mass_system_invalid_fixed_fixed():
    # Invalid case: number of masses does not match springs for fixed-fixed
    num_springs = 4
    spring_constants = np.ones(num_springs)
    masses = [1, 1]  # Incorrect number of masses for fixed-fixed
    boundary_condition = "fixed-fixed"

    # Check if assertion is raised
    with pytest.raises(AssertionError, match="incorrect number of springs or masses for boundary condition"):
        solve_spring_mass_system(num_springs, spring_constants, masses, boundary_condition)

def test_spring_mass_system_invalid_fixed_free():
    # Invalid case: number of masses does not match springs for fixed-free
    num_springs = 3
    spring_constants = np.ones(num_springs)
    masses = [1, 1, 1, 1]  # Incorrect number of masses for fixed-free
    boundary_condition = "fixed-free"
        # Check if assertion is raised
    with pytest.raises(AssertionError, match="incorrect number of springs or masses for boundary condition"):
        solve_spring_mass_system(num_springs, spring_constants, masses, boundary_condition)
def test_invalid_free_free():
    num_springs = 3
    spring_constants = np.ones(num_springs)
    masses = [1, 1]  # Incorrect number of masses for free-free
    boundary_condition = "free-free"

    with pytest.raises(ValueError, match="Cannot evaluate two-free end problem; no solutions available"):
        solve_spring_mass_system(num_springs, spring_constants, masses, boundary_condition)

# If running directly
if __name__ == "__main__":
    pytest.main()
