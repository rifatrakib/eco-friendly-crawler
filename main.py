import csv
import json
import subprocess
import pandas as pd
from xlsxwriter.workbook import Workbook


def invoke_spider(spider_name):
    full_command = f'scrapy crawl {spider_name} '
    print(full_command)
    subprocess.run(full_command, shell=True)


def prepare_excel(name):
    csvfile = f'data/csv/{name}-data.csv'
    workbook = Workbook(f'data/excel/{name}-data.xlsx')
    worksheet = workbook.add_worksheet()
    with open(csvfile, 'rt', encoding='utf8') as f:
        reader = csv.reader(f)
        for r, row in enumerate(reader):
            for c, col in enumerate(row):
                worksheet.write(r, c, col)
    workbook.close()


def prepare_flattened_excel(name):
    jsonfile = f'data/json/{name}-data.json'
    workbook = f'data/excel/flattened-{name}-data.xlsx'
    with open(jsonfile, 'r') as f:
        json_data = f.read()[:-3] + '\n]'
        data = json.loads(json_data)
        if name == 'raepak':
            for doc in data:
                if 'product_information' in doc:
                    doc['product_information'] = json.loads(doc['product_information'])
                if 'dimension_sku' in doc:
                    doc['dimension_sku'] = json.loads(doc['dimension_sku'])
    
    df = pd.json_normalize(data, sep='_')
    df.to_excel(workbook, index=False)
    df.to_json(jsonfile, orient='records', indent=4)


if __name__ == '__main__':
    spiders = {
        'toiletry': True,
        'fusion': True,
        'raepak': True,
        'aptar': True,
    }
    
    for spider_name, crawl in spiders.items():
        if crawl:
            invoke_spider(f'{spider_name}_spider')
            prepare_excel(spider_name)
            prepare_flattened_excel(spider_name)
