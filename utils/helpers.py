from config.settings import CONFIG

def print_banner():
    """Affiche le banner d'accueil"""
    print("""
╔══════════════════════════════════════╗
║     🌤️ MÉTÉO TOULOUSE MÉTROPOLE 🌤️
║         Stations en temps réel       ║
╚══════════════════════════════════════╝
    """)

def format_station_info(station, weather_data):
    """Affiche les vraies données météo"""
    info = f"\n{'='*60}\n"
    info += f"📍 STATION: {station.get('id_nom', 'N/A')}\n"
    info += f"🏙️  VILLE: {station.get('ville', 'Toulouse')}\n"
    info += f"{'='*60}\n"
    
    if weather_data:
        info += f"🌡️  Température: {weather_data.get('temperature_en_degre_c', 'N/A')}°C\n"
        info += f"💧 Humidité: {weather_data.get('humidite', 'N/A')}% \n"
        info += f"📊 Pression: {weather_data.get('pression', 'N/A')} hPa\n"
        info += f"🕐 Heure: {weather_data.get('heure_de_paris', 'N/A')}\n"
    else:
        info += "📊 Données météo non disponibles\n"
    
    info += f"{'='*60}"
    return info
