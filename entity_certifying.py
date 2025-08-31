import hashlib

class entity_certifying:
    def __init__(self):
        self.bd_keys = {}

    def add_key(self, service_name, service_key):
        self.bd_keys[service_name] = service_key


    def get_key(self, mensagem, hashed_mensagem):

        for key in self.bd_keys.values():
            test_hash = hashlib.sha256((mensagem + key).encode()).hexdigest()
            if test_hash == hashed_mensagem:
                return True

        return False