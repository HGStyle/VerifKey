import urllib.request as request, os, hashlib, random, string

def getPB(pb):
    return f"https://pastebin.com/raw/{str(pb)}"

def verify(link, userkey):
    req = request.urlopen(link)
    text = req.read()
    text = text.decode()
    keys = text.split("\r")
    for x in range(0, len(keys)):
        keys[x] = str(keys[x]).replace("\n", "")
    temp = [keys[x] for x in range(0, len(keys)) if x != len(keys)]
    keys = temp
    hashedUserKey = hashlib.sha512(userkey.encode()).hexdigest()
    for hashedKey in keys:
        if hashedKey == hashedUserKey:
            req = text = keys = hashedKey = userkey = hashedUserKey = temp = None
            return True
    return False

def keyGenerator(amount):
    charset = string.ascii_letters + string.digits
    hashedkeys = []
    keys = []
    for _ in range(amount):
        key = "".join(random.choice(charset) for _ in range(20))
        hashedKey = hashlib.sha512(key.encode()).hexdigest()
        with open("hashedkeys.txt", "a") as f:
            f.write(hashedKey + "\n")
        with open('keys.txt', 'a') as f:
            f.write(key + "\n")
    print("Finished !")
    print('Keys to enter are in the file `keys.txt`.')
    print('Hashed keys (text to upload) are stored in the file `hashedkeys.txt\.')
    
if __name__ == "__main__":
    print('VerifKey v2 by HGStyle')
    print('Launching key generator...')
    amount = input('How many keys you want to generate ? --> ')
    while not amount.isdigit():
        print('Amount must be a digit !')
        amount = input('How many keys you want to generate ? --> ')
    amount = int(amount)
    keyGenerator(amount)
