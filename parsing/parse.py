import threading as td
import pandas as pd

from os import getenv
from dotenv import load_dotenv

from utils.db_utils import add_traffic, add_products

load_dotenv()

PATH_FILES = getenv("PATH_EXCEL_FILES")  # Абсолютный путь до файла


def traffic_excel():
    df = pd.read_excel(f"{PATH_FILES}/files/traffic.xlsx")
    for index, data in df.iterrows():
        # Нужно подставлять свои названия колонок
        add_traffic(material_name=data["Наименование материала"], possible_delivery=data["Возможный поставщик"])


def product_csv():
    df = pd.read_csv(f"{PATH_FILES}/files/products.csv", sep=";")
    for index, data in df.iterrows():
        if data["Изображение"] == "нет":
            add_products(data["Наименование материала"], data["Тип материала"], None, data["Цена"],
                         data["Количество на складе"], data["Минимальное количество"], data["Количество в упаковке"],
                         data["Единица измерения"])
        else:
            add_products(data["Наименование материала"], data["Тип материала"], data["Изображение"], data["Цена"],
                         data["Количество на складе"], data["Минимальное количество"], data["Количество в упаковке"],
                         data["Единица измерения"])


def main():
    traffic_excel()
    product_csv()


if __name__ == "__main__":
    main()
