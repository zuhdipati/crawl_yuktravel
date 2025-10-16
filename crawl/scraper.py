from bs4 import BeautifulSoup

def scrape_link_list_paket(html: str):
    soup = BeautifulSoup(html, "html.parser")
    links = [a["href"] for a in soup.select("div.div-btnBook a")]
    
    return links

def scrape_detail_join_trip(html: str, link: str):
    soup = BeautifulSoup(html, "html.parser")
    join_trip = []
    
    title_tag = soup.select_one("div.title_detail_tour h1[itemprop='name']")
    title = title_tag.get_text(strip=True) if title_tag else None
    
    desc_tag = soup.select_one("div.title_detail_tour p[itemprop='description']")
    desc = desc_tag.get_text(strip=True) if desc_tag else None
    
    price_tag = soup.select_one("span.price.big-price")
    price = price_tag.get_text(strip=True) if price_tag else None
    
    props = []
    for prop in soup.select(".tourprop"):
        prop_title_tag = prop.select_one("div.item")
        prop_title = prop_title_tag.get_text(strip=True) if prop_title_tag else None
        props.append(prop_title)
    
    itins = []
    for itinerarie in soup.select("div.itinerariesCont"):
        day_tag = itinerarie.select_one(".DayItin")
        desc_tag = itinerarie.select_one(".block-itiner")
        
        day_itin = day_tag.get_text(strip=True) if day_tag else None
        desc_itin = desc_tag.get_text(strip=True) if desc_tag else None

        itins.append({
            "day": day_itin,
            "title": desc_itin
        })
        
    incls = [li.get_text(strip=True) for li in soup.select("#collapseInclusion li")]
    excls = [li.get_text(strip=True) for li in soup.select("#collapseExclusion li")]
    terms = [li.get_text(strip=True) for li in soup.select("#collapseTerm li")]

    join_trip.append({
        "title": title,
        "desc": desc,
        "price": price,
        "props": props,
        "itineraries": itins,
        "inclusions": incls,
        "exclusions": excls,
        "terms": terms,
        "link": link
    })
    
    return join_trip

def scrape_list_join_trip(html: str):   
    soup = BeautifulSoup(html, "html.parser")
    packages = []
    
    for package in soup.select("div.thumbnail-list"):
        
        title_tag = package.select_one("h3.title-des")
        title = title_tag.get_text(strip=True) if title_tag else None
        
        price_tag = package.select_one("span.price.big-price")
        price = price_tag.get_text(strip=False) if price_tag else None
        
        location_tag = package.select_one("div.location")
        location = location_tag.get_text(strip=False) if location_tag else None
        
        link_tag = package.select_one("a[href]")
        link = link_tag["href"] if link_tag and "href" in link_tag.attrs else None
        packages.append({
            "judul": title,
            "harga": price,
            "lokasi": location,
            "link": link
        })
        
    return packages
