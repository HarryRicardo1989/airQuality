import requests
import json


class POSTDB:
    def __init__(self):
        self.url_tx = 'http://10.8.0.150:9000/api/insert'

    def post_DB(self, hostname, data_hora, temperatura_ar=0, temperatura_orvalho=0, umidade=0, pressao_local=0, pressao_nivel_mar=0, altitude=0, uva=0, uvb=0, wind_speed=0, wind_direction=0, pluviometro=0, co2=0, tvoc=0, relampago=0):
        json_to_tx = {
            "hostname": hostname,
            "data_hora": data_hora,
            "temperatura_ar": temperatura_ar,
            "temperatura_orvalho": temperatura_orvalho,
            "umidade": umidade,
            "pressao_local": pressao_local,
            "pressao_nivel_mar": pressao_nivel_mar,
            "altitude": altitude,
            "uva": uva,
            "uvb": uvb,
            "wind_speed": wind_speed,
            "wind_direction": wind_direction,
            "pluviometro": pluviometro,
            "co2": co2,
            "tvoc": tvoc,
            "relampago": relampago,
        }
        post = ''
        try:
            requests.post(self.url_tx, json=json_to_tx).text
            post = 'ok'
        except:
            post = 'fault'
            pass
        return post
