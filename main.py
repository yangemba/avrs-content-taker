from openpyxl import load_workbook
import requests
import asyncio
import concurrent.futures
import requests
import time
import bs4
import logging
start = time.time()


def take_value(sheet, row, column):
    return sheet.cell(row=row, column=column).value


def take_ides():
    wb = load_workbook('test-flats.xlsx')
    sheet = wb['Sheetname']
    max_row_index = sheet.max_row
    id_list = [take_value(sheet, x, 1) for x in range(2, max_row_index + 1)]
    return id_list


def parse_info(response):
    first = response.text.split('id="descripRealty">')
    comment = first[1].split('</div>')[0].replace('\n', '').replace('            ', '').replace('          ', '')
    return comment


id_list = take_ides()
response_list = []


async def scrap():
    with concurrent.futures.ThreadPoolExecutor(max_workers=100) as executor:
        loop = asyncio.get_event_loop()
        futures = [
            loop.run_in_executor(executor, requests.get, f'http://avers.in.ua/flat/{i}.htm')
            for i in id_list
        ]
        for response in await asyncio.gather(*futures):
            try:
                logging.warning(response.status_code)
                info = parse_info(response)
            except Exception as e:
                logging.warning(f"error: {e}")
                continue
            if info:
                response_list.append(info)


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(scrap())
    finish = time.time()
    print(len(response_list))
    print(str(finish - start))

# Todo write take_id_in_url, then create dict from responses and re-write.
