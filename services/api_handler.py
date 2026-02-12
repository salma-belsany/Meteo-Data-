import requests
from config.settings import CONFIG
import time

class ApiHandler:
    """Gestionnaire des appels API Toulouse Métropole"""
    
    def __init__(self):
        self.base_url = CONFIG["api"]["base_url"]
        self.session = requests.Session()
        self.session.headers.update({
            "User-Agent": "ToulouseMeteoApp/1.0"
        })
    
    def get_all_stations(self):
        """Récupère toutes les stations météo"""
        endpoint = CONFIG["api"]["endpoint_stations"]
        params = CONFIG["api"]["params"]
        
        try:
            url = f"{self.base_url}{endpoint}"
            print(f"🌐 Appel API: {url}")
            response = self.session.get(url, params=params, timeout=10)
            response.raise_for_status()
            
            data = response.json()
            stations = data.get("results", [])
            print(f"✅ {len(stations)} stations récupérées")
            return stations
        except requests.RequestException as e:
            print(f"❌ Erreur API: {e}")
            return []
    
    def get_station_data(self, station_id):
        """Récupère les DONNÉES MÉTÉO d'une station spécifique"""
        try:
            # NOUVELLE LOGIQUE : utiliser l'id_nom comme nom du dataset
            endpoint = f"{station_id}/records" 
            params = {
                "select": "humidite,pression,temperature_en_degre_c,heure_de_paris",
                "limit": 5,  
                "order_by": "heure_de_paris DESC"
            }
            url = f"{self.base_url}{endpoint}"
            
            print(f"🌡️  Récupération données: {url}")
            response = self.session.get(url, params=params, timeout=10)
            response.raise_for_status()
            
            data = response.json()
            results = data.get("results", [])
            if results:
                return results[0] 
            return {}
        except requests.RequestException as e:
            print(f"❌ Erreur station {station_id}: {e}")
            return {}
