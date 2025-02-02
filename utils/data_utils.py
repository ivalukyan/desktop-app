import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


def clean_data_traffic(arr: list) -> list:
    return ([[c.material_name, c.possible_delivery] for c in arr])


def clean_data_product(arr: list) -> list:
    return ([[c.material_name, c.material_type, c.material_img,
              c.material_price, c.quantity_in_stoke, c.min_quantity,
              c.quantity_in_box, c.measurement] for c in arr])    
