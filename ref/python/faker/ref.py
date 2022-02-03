from faker import Faker
import pandas as pd
import random
from datetime import date
from json import dumps

pd.set_option("display.max_columns", 20)
# region faker and random to pandas df
faker = Faker()


def create_rows(num=1):
    output = [
        {
            "name": faker.name(),
            "address": faker.address(),
            "name": faker.name(),
            "email": faker.email(),
            "bs": faker.bs(),
            "address": faker.address(),
            "city": faker.city(),
            "state": faker.state(),
            "date_time": faker.date_between(date(2021, 8, 1), date(2021, 12, 1)),
            "paragraph": faker.paragraph(),
            "Conrad": faker.catch_phrase(),
            "randomdata": random.randint(1000, 2000),
            "randomfloat": round(random.uniform(10.1, 15.2), 2),
        }
        for x in range(num)
    ]
    return output


df = pd.DataFrame(create_rows(10))
print(df)
# endregion

# region abstract
# df = pd.DataFrame(faker.profile())
# print(df)
# endregion

# region numbers
print(f"Random int: {faker.random_int()}")
print(f"Random int: {faker.random_int(0, 100)}")
print(f"Random digit: {faker.random_digit()}")
print("\n")
# endregion

# region strings
# buzz words, catch_phrase is also buzz wordy
print(f"a word: {faker.bs()}") 
print(f"a word: {faker.word()}")
print(f"six words: {faker.words(6)}")
words = ["forest", "blue", "cloud", "sky", "wood", "falcon"]
print(f"customized unique words: {faker.words(3, words, True)}")
print("\n")
# endregion

# region date
print("minumum age 18, maximum age 90")
for _ in range(5):
    print(f"Date of Birth: {faker.date_of_birth(minimum_age=18, maximum_age=90)}")
print("minimum age 63, maximum age 110")
for _ in range(5):
    print(f"Date of Birth: {faker.date_of_birth(minimum_age=63, maximum_age=110)}")
print("Date between")
for _ in range(5):
    print(f"Date of Birth: {faker.date_between(date(2021,8,1),date(2021,12,1))}")


print("\n")
# endregion

# region id
print(f"md5: {faker.md5()}")
print(f"sha1: {faker.sha1()}")
print(f"sha256: {faker.sha256()}")
print(f"uuid4: {faker.uuid4()}")
print("\n")
# endregion

# region names
print(f"Name: {faker.name()}")
print(f"First name: {faker.first_name()}")
print(f"Last name: {faker.last_name()}")
print(f"Male name: {faker.name_male()}")
print(f"Female name: {faker.name_female()}")
print("\n")
# endregion

# region contact
print(f"Email: {faker.email()}")
print(f"Phone: {faker.phone_number()}")
print("\n")
# endregion

# region location
print(f"Address: {faker.address()}")
print(f"lat, long: {faker.latlng()}")
print("\n")
# endregion

# region internet
print(f"IPv4: {faker.ipv4()}")
print(f"IPv6: {faker.ipv6()}")
print(f"MAC address: {faker.mac_address()}")
print("\n")
# endregion

# region job
print("\n")
for _ in range(6):
    print(faker.job())
print("\n")
# endregion

# region switching locale
faker = Faker("cz_CZ")
for i in range(3):
    name = faker.name()
    address = faker.address()
    phone = faker.phone_number()
    print(f"{name}, {address}, {phone}")
print("\n")
# endregion
