# pip install faker

from faker import Faker

fake = Faker()

print(fake.name())
print(fake.email())
print(fake.image_url())
print(fake.uri())
print(fake.sentence())
print(fake.password())

print(fake.password(length=16,
                    special_chars=True,
                    digits=True,
                    upper_case=True,
                    lower_case=True))

print(fake.company())
