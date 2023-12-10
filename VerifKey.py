import urllib.request as request, os, hashlib, random, string
print('DO NOT USE THIS. IT WAS BROKEN, ITS STILL BROKEN AND WILL BE BROKEN FOREVER BECAUSE I DONT WANT TO UPDATE IT. THE MODULE ISNT BROKEN ITSELF, JUST THE INSTALLER. BUT I DONT WANT TO SUPPORT THIS. THIS WAS MADE LESS THAN A YEAR AGO (when i wrote that) BUT I EVOLVED AND THIS SHOULD NOT BE USED ANYMORE. CODE RELEASED UNDER THE UNLICENSE. FOR MORE INFO, GOTO https://github.com/HGStyle/VerifKey/')
def getPB(pb):
    return "https://pastebin.com/raw/" + str(pb)

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
    return False

def keyGenerator(amount):
    charset = string.ascii_letters + string.digits
    hashedkeys = []
    keys = []
    for x in range(amount):
        key = ""
        for y in range(20):
            key += random.choice(charset)
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
