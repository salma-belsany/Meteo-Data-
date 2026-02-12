"""Tests unitaires File"""
from utils.helpers import print_banner, format_station_info

def test_print_banner():
    print_banner()  # Teste l'affichage banner
    assert True

def test_format_station_info():
    station = {"id_nom": "42-compans", "ville": "Toulouse"}
    data = {"temperature_en_degre_c": 14.1}
    result = format_station_info(station, data)
    assert "14.1°C" in result  # Teste formatage données
    assert "Toulouse" in result
    
def test_format_no_data():
    """Test format sans données"""
    station = {"ville": "Toulouse"}
    result = format_station_info(station, {})
    assert "non disponibles" in result  # Couvre ligne 25
