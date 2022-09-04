import requests
import json


class Logging:
    def __init__(self, logger_server: str, reference: str, apikey: str):
        self.logger_server = logger_server
        self.reference = reference
        self.apikey = apikey

    def debug(self, message):
        requests.post(
            url=self.logger_server,
            data=json.dumps({'reference': self.reference, 'typ': 'debug', 'message': message}),
            headers={'apikey': self.apikey}
        )

    def info(self, message):
        requests.post(
            url=self.logger_server,
            data=json.dumps({'reference': self.reference, 'typ': 'info', 'message': message}),
            headers={'apikey': self.apikey}
        )

    def error(self, message):
        requests.post(
            url=self.logger_server,
            data=json.dumps({'reference': self.reference, 'typ': 'error', 'message': message}),
            headers={'apikey': self.apikey}
        )



def _log():
    import conf
    try:
        return conf.logger
    except:
        pass


log = _log()
