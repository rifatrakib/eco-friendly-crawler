import csv
import subprocess
from xlsxwriter.workbook import Workbook


def invoke_spider(spider_name):
    full_command = f'scrapy crawl {spider_name} '
    print(full_command)
    subprocess.run(full_command, shell=True)


def prepare_excel(name):
    csvfile = f'data/{name}-data.csv'
    workbook = Workbook(f'data/{name}-data.xlsx')
    worksheet = workbook.add_worksheet()
    with open(csvfile, 'rt', encoding='utf8') as f:
        reader = csv.reader(f)
        for r, row in enumerate(reader):
            for c, col in enumerate(row):
                worksheet.write(r, c, col)
    workbook.close()


if __name__ == '__main__':
    spiders = {
        'toiletry': False,
        'fusion': False,
        # 'raepak': True,
    }
    
    for spider_name, crawl in spiders.items():
        if crawl:
            invoke_spider(f'{spider_name}_spider')
            prepare_excel(spider_name)
