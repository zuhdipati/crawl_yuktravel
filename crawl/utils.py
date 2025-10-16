import pandas as pd

def save_to_excel(data):
    df = pd.DataFrame(data)
    df.to_excel("products.xlsx", index=False, sheet_name="YukTravel")
    
    
def auto_scroll(page, scrolls=10, delay=500):
    for _ in range(scrolls):
        page.mouse.wheel(0, 15000)
        page.wait_for_timeout(delay)
