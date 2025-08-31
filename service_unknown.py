import hashlib
from entity_certifying import entity_certifying
class service:
    def __init__(self, name, private_key):
        self.name = name
        self.private_key = private_key
    
    def generate_hash(self, message):
        return hashlib.sha256((message + self.private_key).encode()).hexdigest()
    
    def verify_hash(self, certifier, message, hash_to_verify): 
        return certifier.get_key(message, hash_to_verify)