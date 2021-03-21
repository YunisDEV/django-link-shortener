import random
import string

def generateLink():
    dataset = string.ascii_uppercase+string.ascii_lowercase+"0123456789"
    result = random.sample(dataset,8)
    return "".join(result)