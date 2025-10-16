from .browser import get_list_join_trip, get_detail_join_trip
from .scraper import scrape_list_join_trip, scrape_link_list_paket, scrape_detail_join_trip
import json

def detail_join_trip():
    url = "https://www.yuktravel.com/paket-liburan"
    html = get_list_join_trip(url)
    
    join_trip_data = []
    
    links = scrape_link_list_paket(html)
    
    for link in links:
        print(link)
        html = get_detail_join_trip(link)
        data = scrape_detail_join_trip(html, link)
        join_trip_data.extend(data)
        
    if join_trip_data:
        with open("data/detail_join_trip.json", "w", encoding="utf-8") as f:
            json.dump(join_trip_data, f, ensure_ascii=False, indent=2)
        print(f"Data tersimpan ke detail_join_trip.json ({len(join_trip_data)} paket)")
    else:
        print("Tidak ada data ditemukan.")
        

def list_join_trip():
    url = "https://www.yuktravel.com/paket-liburan"
    html = get_list_join_trip(url)
    
    join_trip_data = []
    
    data = scrape_list_join_trip(html)
    join_trip_data.extend(data)
        
    if join_trip_data:
        with open("data/list_join_trip.json", "w", encoding="utf-8") as f:
            json.dump(join_trip_data, f, ensure_ascii=False, indent=2)
        print(f"Data tersimpan ke join_trip2.json ({len(join_trip_data)} paket)")
    else:
        print("Tidak ada data ditemukan.")

def main():
    detail_join_trip()


if __name__ == "__main__":
    main()
