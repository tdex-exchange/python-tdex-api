import json
import requests
import hashlib
import time
import hmac


class Configs(object):
    def __init__(self):
        self.url = 'https://www.tdex.com/openapi/v1'
        self.headers = {
            'Content-Type': 'application/json',
        }

    def hmac_sign(self, path, expires, data=None):
        if data is None:
            data = ''
        msg = path + expires + data
        res = hmac.new(bytes(self.apiSecret, 'utf-8'), bytes(msg, 'utf-8'), digestmod=hashlib.sha256).hexdigest()
        return res

    def verification(self, data, path):
        expires = str(int(int(round(time.time() * 1000)) / 100000))
        input = data
        curPath = path
        sign = self.hmac_sign(curPath, expires, input)
        self.headers['api-signature'] = sign;
        self.headers['api-expires'] = expires;

    def request(self, data, path, type):
        if(type == 'get'):
            res = requests.post(self.url + path, data, headers=self.headers).json()
        else:
            res = requests.put(self.url + path, data, headers=self.headers).json()
        return res


configs = Configs()


class Tdex(object):
    def __init__(self, options):
        self.apiKey = options['apiKey']
        self.apiSecret = options['apiSecret']
        configs.apiSecret = options['apiSecret']
        configs.headers['api-key'] = options['apiKey']

    def requestApi(self, input, path, type=None):
        configs.verification(input, path)
        res = configs.request(input, path, type)
        return res

    def userInfo(self):
        input = json.dumps({})
        path = '/user/info'
        res = self.requestApi(input, path)
        return res

    def walletBalances(self):
        input = json.dumps({})
        path = '/wallet/balances'
        res = self.requestApi(input, path)
        return res

    def walletBalance(self, data={}):
        input = json.dumps(data)
        path = '/wallet/balance'
        res = self.requestApi(input, path)
        return res

    def walletWithDraw(self, data={}):
        input = json.dumps(data)
        path = '/wallet/withdraw'
        res = self.requestApi(input, path)
        return res

    def walletSwitch(self, data={}):
        input = json.dumps(data)
        path = '/wallet/switch'
        res = self.requestApi(input, path)
        return res

    def futuresOpen(self, data={}):
        input = json.dumps(data)
        path = '/futures/open'
        res = self.requestApi(input, path)
        return res

    def futuresClose(self, data={}):
        input = json.dumps(data)
        path = '/futures/close'
        res = self.requestApi(input, path)
        return res

    def futuresCloseAll(self, data={}):
        input = json.dumps(data)
        path = '/futures/closeAll'
        res = self.requestApi(input, path)
        return res

    def futuresSetSl(self, data={}):
        input = json.dumps(data)
        path = '/futures/setsl'
        res = self.requestApi(input, path)
        return res

    def futuresSetTp(self, data={}):
        input = json.dumps(data)
        path = '/futures/settp'
        res = self.requestApi(input, path)
        return res

    def futuresMerge(self, data={}):
        input = json.dumps(data)
        path = '/futures/merge'
        res = self.requestApi(input, path)
        return res

    def futuresSplit(self, data={}):
        input = json.dumps(data)
        path = '/futures/split'
        res = self.requestApi(input, path)
        return res

    def setup(self, data={}):
        input = json.dumps(data)
        path = '/futures/setup'
        res = self.requestApi(input, path)
        return res

    def futuresScheme(self, data={}, type='get'):
        input = json.dumps(data)
        path = '/futures/scheme'
        res = self.requestApi(input, path, type)
        return res

    def futuresGetOrders(self):
        input = json.dumps({})
        path = '/futures/orders'
        res = self.requestApi(input, path, type)
        return res

    def futuresGetPosition(self):
        input = json.dumps({})
        path = '/futures/position'
        res = self.requestApi(input, path, type)
        return res

    def futuresGetContract(self, data={}):
        input = json.dumps(data)
        path = '/futures/contract'
        res = self.requestApi(input, path)
        return res

    def futuresGetHistory(self, data={}):
        input = json.dumps(data)
        path = '/futures/history'
        res = self.requestApi(input, path)
        return res

    def spotBuy(self, data={}):
        input = json.dumps(data)
        path = '/spot/buy'
        res = self.requestApi(input, path)
        return res

    def spotSell(self, data={}):
        input = json.dumps(data)
        path = '/spot/sell'
        res = self.requestApi(input, path)
        return res

    def spotHistory(self, data={}):
        input = json.dumps(data)
        path = '/spot/history'
        res = self.requestApi(input, path)
        return res

    def spotStat(self, data={}):
        input = json.dumps(data)
        path = '/spot/stat'
        res = self.requestApi(input, path)
        return res

    def getToken(self, data={}):
        input = json.dumps(data)
        path = '/user/token'
        res = self.requestApi(input, path)
        return res

    def futureLastOrder(self, data={}):
        input = json.dumps(data)
        path = '/futures/orders'
        res = self.requestApi(input, path)
        return res




