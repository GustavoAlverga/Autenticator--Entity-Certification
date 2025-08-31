from service_unknown import service
from entity_certifying import entity_certifying
import hashlib
import random

def generate_services(number_of_services, certifyer):
    services = []

    for i in range(number_of_services):
        name= f"Service {i}"
        private_key= hashlib.sha256(f"private_key_{i}".encode()).hexdigest()

        new_service = service(name, private_key)
        services.append(new_service)
        certifyer.add_key(name, private_key)

        print(f"Name = {name} created with private key: {private_key}")
    
    return services

def generate_intruders(number_of_intruders, certifyer):
    intruders = []
    for i in range(number_of_intruders):
        name= f"Service {i} XXXX Intruder"
        private_key= hashlib.sha256(str(random.randint(1,100000)).encode()).hexdigest()

        new_service = service(name, private_key)
        intruders.append(new_service)

        print(f"Name = {name} created with private key: {private_key}")
    return intruders

def validator_of_service(certifier, service1, service2, message):
    hash1 = service1.generate_hash(message)
    hash2 = service2.generate_hash(message)
    return service1.verify_hash(certifyer, message, hash2) and service2.verify_hash(certifyer, message, hash1)


if __name__ == "__main__":

    number_of_services = int(input("Enter the number of services: "))
    number_of_intruders = int(input("Enter the number of intruders: "))

    certifyer = entity_certifying()

    services = generate_services(number_of_services, certifyer)
    intruders = generate_intruders(number_of_intruders, certifyer)

    print("\n\n\nServices and intruders generated successfully.\n\n\n")

    bag_of_services = services + intruders
    random.shuffle(bag_of_services)
    print("Bag of services created and shuffled successfully.\n\n\n")

    print("Starting validation process...\n\n\n")
    mensage = input("Enter the message to validate: ")
    number_of_loops = int(input("Enter the number of validations to perform: "))

    while number_of_loops > 0:
        while True:
            number1 = random.randint(0, len(bag_of_services) - 1)
            number2 = random.randint(0, len(bag_of_services) - 1)

            if number1 != number2:
                service1 = bag_of_services[number1]
                service2 = bag_of_services[number2]
                break
            
        result = validator_of_service(certifyer, service1, service2, mensage)
        print(f"\nResolt of validation: {"Sucefuly" if result else "Fail"}")
        number_of_loops -= 1
    


    



        