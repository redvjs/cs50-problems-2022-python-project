import pytest
import re
from megabank import valid_password
# Assuming valid_password function is defined in a module called `your_module`
# from your_module import valid_password

def test_valid_password_success(monkeypatch):
    """Test valid password is accepted."""
    # Mock inputs for the valid password
    mock_inputs = iter(["StrongPass1", "StrongPass1"])
    
    monkeypatch.setattr('builtins.input', lambda _: next(mock_inputs))

    # Call the function
    result = valid_password()

    # Assert that the result is the expected valid password
    assert result == "StrongPass1"

def test_password_mismatch(monkeypatch):
    """Test password mismatch scenario."""
    # Mocking the inputs where the passwords dont match
    mock_inputs = iter(["StrongPass1", "DifferentPass1", "StrongPass1", "StrongPass1"])
    
    monkeypatch.setattr('builtins.input', lambda _: next(mock_inputs))

    # Calling the valid_password function
    result = valid_password()

    # Assert that only the matched password is returned by the function
    assert result == "StrongPass1"

def test_invalid_password(monkeypatch):
    """Test invalid password is rejected."""
    # Mock inputs where the password does not meet the criteria
    mock_inputs = iter([
        "weak",          # Invalid: too short, no digit, no uppercase
        "weak",          # Re-enter (still invalid)
        "better1",       # Invalid: still not meeting the uppercase requirement
        "better1",       # Re-enter (still invalid)
        "BetterPass123",    # Valid
        "BetterPass123"     # Re-enter (valid)
    ])

    monkeypatch.setattr('builtins.input', lambda _: next(mock_inputs))

    # Call the function
    result = valid_password()

    # Assert that the result is the expected valid password
    assert result == "BetterPass123"
