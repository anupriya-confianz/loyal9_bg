from xmlrpc import client
class Infusionsoft:

    def __init__(self, name, api_key):
        self.client = client.ServerProxy("https://" + name + ".infusionsoft.com/api/xmlrpc")
        self.client.error = client.Error
        self.key = api_key

    def __getattr__(self, service):
        def function(method, *args):
            call = getattr(self.client, service + '.' + method)
            try:
                return call(self.key, *args)
            except self.client.error as v:
                return v
        return function

    def server(self):
        return self.client

class InfusionsoftOAuth(Infusionsoft):

    def __init__(self, access_token):
        self.client = client.ServerProxy("https://api.infusionsoft.com/crm/xmlrpc/v1?access_token=%s" % access_token)
        self.client.error = client.Error
        self.key = access_token
