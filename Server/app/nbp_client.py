import json
import requests
from .date_util import DateUtil
from .nbp_enums import Period


class NBPClient:
    def __init__(self):
        self.service_host = "api.nbp.pl"
        self.header_content_type_json = {'content-type': 'application/json'}

        self.endpoint_url = {
            'rates': '/api/exchangerates/rates',
            'tables': '/api/exchangerates/tables'
        }

    def build_endpoint(self, path=None):
        url = f"https://{self.service_host}"
        if path is not None:
            url += f"{path}"
        return url

    def get_all_currencies_for_table(self, table_number: str):
        request = self.build_endpoint(self.endpoint_url.get("tables") + '/' + table_number)
        http_response = requests.get(url=request, params=dict(), headers=self.header_content_type_json)
        if http_response.status_code == 200:
            json_response = http_response.json()
            return [{currency.get('code'): currency.get('currency')} for currency in json_response[0].get('rates')]
        else:
            return None

    def get_single_currency_data(self, table_number: str, currency: str, period: Period = None):
        request = self.build_endpoint(self.endpoint_url.get("rates") + f"/{table_number}" + f"/{currency}" + "/")
        if period is None:
            request += "today/"
        else:
            calendar = DateUtil()
            start_date = calendar.get_end_date(period)
            request += str(start_date) + f"/{calendar.end_date.date()}"
        http_response = requests.get(url=request, params=dict(), headers=self.header_content_type_json)
        if http_response.status_code == 200:
            json_result = http_response.json()
            return [{'no': currency.get('no'), 'effectiveDate': currency.get('effectiveDate'), 'rate': currency.get('mid')} for currency in json_result.get('rates')]
        else:
            return None
