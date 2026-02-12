"""
Configuration centralisée du projet (Principe Open/Closed)
"""
CONFIG = {
    "api": {
        "base_url": "https://data.toulouse-metropole.fr/api/explore/v2.1/catalog/datasets/",
        "endpoint_stations": "stations-meteo-en-place/records",
        "params": {
            "select": "id_nom,id_numero,ville",
            "order_by": "id_numero",
            "limit": 80
        }
    },
    "display": {
        "max_stations": 20,
        "format": "table"
    },
    "cache": {
        "enabled": True,
        "ttl_seconds": 3600
    }
}
