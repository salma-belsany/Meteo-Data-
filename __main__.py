from data_structures.linked_list import LinkedList
from data_structures.queue import Queue
from services.api_handler import ApiHandler
from config.settings import CONFIG
from utils.helpers import print_banner, format_station_info

def main():
    print_banner()
    
    # 1. Récupération des stations
    print("📡 Récupération des stations météo de Toulouse...")
    api_handler = ApiHandler()
    stations = api_handler.get_all_stations()
    
    if not stations:
        print("❌ Aucune station trouvée")
        return
    
    # 2. Affichage des stations via Liste Chaînée
    stations_list = LinkedList()
    for station in stations:
        stations_list.append(station)
    
    print("\n📋 Stations météo disponibles :")
    stations_list.display()
    
    # 3. Choix utilisateur et extraction via File
    extraction_queue = Queue()
    choice = input("\n🎯 Numéro de station à consulter (ex: 44) : ").strip()
    
    # Priorité aux stations SANS "point-frais"
    selected_station = next(
        (s for s in stations 
        if str(s.get('id_numero', '')) == choice 
        and 'point-frais' not in s.get('id_nom', '')),
        None
    )
    # Si pas trouvé, prend la première qui match
    if not selected_station:
        selected_station = next(
            (s for s in stations if str(s.get('id_numero', '')) == choice), 
            None
        )

    
    if selected_station:
        station_id = selected_station['id_nom']
        extraction_queue.enqueue(station_id)
        print(f"\n⏳ Extraction des données pour {station_id}...")
        
        while not extraction_queue.is_empty():
            station_to_fetch = extraction_queue.dequeue()
            weather_data = api_handler.get_station_data(station_to_fetch)
            print(format_station_info(selected_station, weather_data))
    else:
        print("❌ Station introuvable")

if __name__ == "__main__":
    main()
