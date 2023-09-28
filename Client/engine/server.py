from engine.request import get


class Server():

    client_name = None

    def get_name(self):
        params = {'method': 'get_client_name'}
        response = get(params)
        self.client_name = response['client_name']

    def update(self):
        if self.client_name != None:
            params = {'method': 'update', 'client_name': self.client_name}
            response = get(params)
            return response
        else:
            raise Exception('Server not found, maybe Server.get_name()  ?')
