import pytest
from megabank import login

def test_login_sucess(monkeypatch):
    mock_inputs = iter([
    'dun1',
    'duncmaster',
    'DuncanLikesCoding123',
    ])
    
    monkeypatch.setattr('builtins.input', lambda _: next(mock_inputs))

    result = login()
    assert result is not None

def test_login_wrong_username(monkeypatch):
    mock_inputs = iter([
    'dun1',
    'duncmast',
    'DuncanLikesCoding123',
    ])
    
    monkeypatch.setattr('builtins.input', lambda _: next(mock_inputs))

    result = login()
    assert result is None

def test_login_wrong_password(monkeypatch):
    mock_inputs = iter([
    'dun1',
    'duncmaster',
    'DuncanLikesCoding',
    ])
    
    monkeypatch.setattr('builtins.input', lambda _: next(mock_inputs))

    result = login()
    assert result is None

def test_login_invalid_unique_id(monkeypatch):
    mock_inputs = iter([
    'dun2',
    'dunc1',
    'dun',
    'dun1',
    'duncmaster',
    'DuncanLikesCoding123'
    ])
    
    monkeypatch.setattr('builtins.input', lambda _: next(mock_inputs))

    result = login()
    assert result == 'dun1'

def test_login_capitallized(monkeypatch):
    mock_inputs = iter([
    'DUN1',
    'DUNCMASTER',
    'DuncanLikesCoding123'
    ])
    
    monkeypatch.setattr('builtins.input', lambda _: next(mock_inputs))

    result = login()
    assert result == 'dun1'