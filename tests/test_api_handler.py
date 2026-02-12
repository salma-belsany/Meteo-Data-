"""Tests unitaires File"""
import pytest
from unittest.mock import patch, MagicMock 
import requests 
from services.api_handler import ApiHandler
from config.settings import CONFIG

def test_config():
    """Test dictionnaire config → 100%"""
    from config.settings import CONFIG
    assert CONFIG["api"]["base_url"] == "https://data.toulouse-metropole.fr/api/explore/v2.1/catalog/datasets/"
    assert CONFIG["api"]["params"]["limit"] == 80

@patch('requests.Session.get')
def test_get_station_data_success(mock_get):
    """Test API station OK"""
    mock_response = MagicMock()
    mock_response.status_code = 200
    mock_response.json.return_value = {
        "results": [{"temperature_en_degre_c": 14.1}]
    }
    mock_get.return_value = mock_response
    
    handler = ApiHandler()
    data = handler.get_station_data("42-compans")
    assert data["temperature_en_degre_c"] == 14.1

@patch('requests.Session.get')  
def test_get_all_stations_timeout(mock_get):
    """Test timeout API"""
    mock_get.side_effect = requests.exceptions.Timeout
    handler = ApiHandler()
    stations = handler.get_all_stations()
    assert stations == []  # Retourne vide sur timeout
