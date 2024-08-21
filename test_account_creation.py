import pytest
from megabank import account_creation, account_details, login

@pytest.fixture
def mock_account_details():
    original_details = {
        'dun1': {
            'Name': 'Duncan',
            'Username': 'duncmaster',
            'Password': 'DuncanLikesCoding123',
            'Initial deposit': 300,
            'Account balance': 300,
        },
        'vic2': {
            'Name': 'Vico',
            'Username': 'redvjs',
            'Password': 'NetherlandsW1llW1n',
            'Initial deposit': 5,
            'Account balance': 5,
        },
        'wil3': {
            'Name': 'Wilson',
            'Username': 'wilsonistheman',
            'Password': '1WilsonAndADream',
            'Initial deposit': 250,
            'Account balance': 250,
        },
    }
    return original_details

def test_account_creation(monkeypatch, mock_account_details):
    
    mock_inputs = iter([
    # Account Creation Sequence
    'John', 
    'johndoe',
    'JohnDoe123',
    'JohnDoe123',
    1000,
    1,
    # Login Sequence
    'Joh4', 
    'johndoe',
    'JohnDoe123',
    ])

    monkeypatch.setattr('builtins.input', lambda _: next(mock_inputs))

    # Call the function to test
    account_creation()

    # Check that the account was added correctly
    assert 'joh4' in account_details
    assert account_details['joh4']['Name'] == 'John'
    assert account_details['joh4']['Username'] == 'johndoe'
    assert account_details['joh4']['Password'] == 'JohnDoe123'
    assert account_details['joh4']['Initial deposit'] == 1000
    assert account_details['joh4']['Account balance'] == 1000