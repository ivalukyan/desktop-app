import logging

from database.db import Traffic, Products, SessionMaker
from sqlalchemy import ExceptionContext


db = SessionMaker()


def get_all_traffic():
    return db.query(Traffic).all()


def add_traffic(material_name: str, possible_delivery: str):
    traffic = Traffic(material_name=material_name, possible_delivery=possible_delivery)
    try:
        db.add(traffic)
        db.commit()
    except ExceptionContext as e:
        logging.info(e)
        db.rollback()
    finally:
        db.close()
        
        
def get_products_all():
    return db.query(Products).all()


def add_products(material_name: str, material_type: str, material_img: str | None, material_price: str,
                 quantity_in_stoke: str, min_quantity: int, quantity_in_box: int, measurement: str):
    products = Products(material_name=material_name, material_type=material_type, material_img=material_img,
                        material_price=material_price, quantity_in_stoke=quantity_in_stoke, min_quantity=min_quantity,
                        quantity_in_box=quantity_in_box, measurement=measurement)
    try:
        db.add(products)
        db.commit()
    except ExceptionContext as e:
        logging.info(e)
        db.rollback()
    finally:
        db.close()