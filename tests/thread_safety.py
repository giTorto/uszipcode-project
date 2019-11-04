from uszipcode import SearchEngine
from multiprocessing import Pool

zip_search_ng = SearchEngine(simple_zipcode=True, db_file_dir="here")


def search_by_city(city):

    return zip_search_ng.by_city(city)


if __name__ == '__main__':
    p = Pool(5)

    city_results = p.map(search_by_city, ["boston", "new york", "somerville", "cambridge", "seattle", "san francisco"])

    for zip_codes in city_results:
        for zip_code in zip_codes:
            print(zip_code.major_city, zip_code.zipcode)
