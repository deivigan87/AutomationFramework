import configparser
import logging
import os
import sys

from d14_service_framework.utils.json_parser import JsonParser

"""Class with helper functions which will parse the values from test data configuration files"""


class ConfigParser(object):
    def __init__(self, journey_name, env, protocol):

        self.journey_name = journey_name
        self.env = env
        self.protocol = protocol
        self.config = configparser.ConfigParser()
        self.path = ""

        if __name__ == '__main__':
            path = os.path.split(sys.argv[0])[0]
        else:
            path = os.path.split(__file__)[0]

        self.path = path

        self.config.read(os.path.join(path, self.journey_name + '_test_data.conf'))

    def get_data_validation_file(self, data_key, name_of_file):
        data = JsonParser.read_json_file_to_dict_for_validation(os.path.dirname(os.path.abspath(__file__)),
                                                                "test_data_validation", name_of_file)
        for key in data_key.split(":"):
            data = data[key]
        return data

    def path_env(self):
        return self.path

    def build_headers(self, headertype):

        global username, api_key, centrasite_apikey, gateway_apikey, centrasite_for, accept_language, \
            accept_language_sas, user_token, api_key_capital, postman_token, cache_control, api_key_caps, \
            basic_authorization, api_key_first_capital, client_id
        try:
            basic_authorization = self.config.get(self.env, "Authorization")
        except configparser.NoOptionError:
            pass
        try:
            username = self.config.get(self.env, "username")
        except configparser.NoOptionError:
            pass
        try:
            api_key = self.config.get(self.env, "apikey")
        except configparser.NoOptionError:
            pass
        try:
            centrasite_apikey = self.config.get(self.env, "x-CentraSite-APIKey")
        except configparser.NoOptionError:
            pass
        try:
            cache_control = self.config.get(self.env, "cache-control")
        except configparser.NoOptionError:
            pass
        try:
            api_key_caps = self.config.get(self.env, "API-KEY")
        except configparser.NoOptionError:
            pass
        try:
            api_key_capital = self.config.get(self.env, "Api-Key")
        except configparser.NoOptionError:
            pass
        try:
            api_key_first_capital = self.config.get(self.env, "API-Key")
        except configparser.NoOptionError:
            pass
        try:
            centrasite_for = self.config.get(self.env, "x-Forwarded-For")
        except configparser.NoOptionError:
            pass
        try:
            gateway_apikey = self.config.get(self.env, "x-Gateway-APIKey")
        except configparser.NoOptionError:
            pass
        try:
            postman_token = self.config.get(self.env, "Postman-Token")
        except configparser.NoOptionError:
            pass
        try:
            accept_language = self.config.get(self.env, "Accept-Language")
        except configparser.NoOptionError:
            pass
        try:
            accept_language_sas = self.config.get(self.env, "Accept-Language-SAS")
        except configparser.NoOptionError:
            pass
        try:
            client_id = self.config.get(self.env, ".CLIENTID")
        except configparser.NoOptionError:
            pass
        try:
            user_token = self.config.get(self.env, "UserToken")
        except configparser.NoOptionError:
            logging.info("No accept user token headers")

        if headertype == "core_header":
            headers = {
                "Accept": "application/json",
                "Content-Type": "application/json",
                "API-Key": api_key_first_capital,
                "x-Gateway-APIKey": gateway_apikey
            }
        elif headertype == "core_header_with_forward_key":
            headers = {
                "Accept": "application/json",
                "Content-Type": "application/json",
                "API-Key": api_key_first_capital,
                "x-Gateway-APIKey": gateway_apikey,
                "x-Forwarded-For": centrasite_for
            }
        elif headertype == "core_header_with_client_id":
            headers = {
                "Accept": "application/json",
                "Content-Type": "application/json",
                "API-Key": api_key_first_capital,
                "x-Gateway-APIKey": gateway_apikey,
                ".CLIENTID": client_id
            }
        elif headertype == "build_header":
            headers = {
                "Content-Type": "application/json",
                "API-Key": api_key_first_capital,
                "x-Gateway-APIKey": gateway_apikey
            }
        elif headertype == "aldar_header":
            headers = {
                "Accept": "application/json",
                "Content-Type": "application/json",
                "Authorization": basic_authorization,
                "API-Key": api_key_first_capital,
                "x-Gateway-APIKey": gateway_apikey,
            }
        elif headertype == "microservices_water_bills":
            headers = {
                "Accept": "application/json",
                "Content-Type": "application/json",
                "API-Key": api_key_first_capital,
                "x-Forwarded-For": centrasite_for,
                "x-Gateway-APIKey": gateway_apikey
            }
        elif headertype == "ad_locker":
            headers = {
                "Accept": "application/json",
                "Content-Type": "application/json",
                "API-Key": api_key_first_capital,
                "x-Gateway-APIKey": gateway_apikey
            }
        elif headertype == "electricity_bill_list":
            headers = {
                "x-Gateway-APIKey": gateway_apikey,
                "Api-Key": api_key_caps,
                "Accept": "application/json",
                "Content-Type": "application/json",
                "x-Forwarded-For": centrasite_for,
            }
        elif headertype == "emptyheaders":
            headers = {}
        elif headertype == "Invalidheaders":
            headers = {
                "Username": username,
                "Content-Type": "application/pdf",
                "apikey": api_key
            }
        else:
            headers = {
                "Username": "test_user",
                "Content-Type": "application/json",
                "apikey": "test_api"
            }
        return headers

    def endpoint_parser(self, endpoint_name):
        end_point = self.config.get("url", endpoint_name)
        return end_point

    def main_url(self):
        protocol = self.config.get(self.protocol, "protocol")
        domain = self.config.get(self.env, "domain")
        main_url = protocol + domain
        return main_url
