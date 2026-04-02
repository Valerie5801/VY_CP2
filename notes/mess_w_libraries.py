from faker import Faker

"""fake = Faker(["it_IT", "en_US", "ja_JP"])

for i in range(10):
    print(fake.name())"""

from faker.providers import DynamicProvider

fake = Faker()
#this allows us to choose a random set of words
words = DynamicProvider(
    provider_name = "omri_names", #this is how we access it
    elements = ["omori", "aubrey", "kel", "hero", "basil", "mari", "mewo", "sunny", "capt. spaceboy", "sweetheart", "doughie", "biscuit"]
)

#adding the provider via variable name
fake.add_provider(words)
#calling it using the provider_name
print(fake.omri_names())