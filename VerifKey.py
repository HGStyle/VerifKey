import urllib.request as request, os, hashlib, random, string

def getPB(pb):
    return "https://pastebin.com/raw/" + pb

def verify(link, userkey):
    req = request.urlopen(link)
    text = req.read()
    text = text.decode()
    keys = text.split("\r")
    temp = []
    for x in range(0, len(keys)):
        keys[x] = str(keys[x]).replace("\n", "")
    for x in range(0, len(keys)):
        if x != len(keys):
            temp.append(keys[x])
    keys = temp
    hashedUserKey = hashlib.sha512(userkey.encode()).hexdigest()
    for hashedKey in keys:
        if hashedKey == hashedUserKey:
            req = text = keys = hashedKey = userkey = hashedUserKey = temp = None
            return True
    req = text = keys = hashedKey = userkey = hashedUserKey = temp = None
    return False

def keyGenerator(amount):
    charset = string.ascii_letters + string.digits
    for x in range(amount):
        key = ""
        for y in range(20):
            key += random.choice(charset)
        hashedKey = hashlib.sha512(key.encode()).hexdigest()
        print(key, ":", hashedKey)
        with open("keys.txt", "a") as f:
            f.write(hashedKey + "\n")
    print("Finished !")
