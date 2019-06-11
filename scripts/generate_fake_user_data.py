# pip3 install Faker
from faker import Faker

faker = Faker()

# print fake user data in CSV format
print("name,address,email")
for _ in range(1, 100):
    print("\"{}\",\"{}\",\"{}\"".format(faker.name(), repr(faker.address()), faker.email()))
