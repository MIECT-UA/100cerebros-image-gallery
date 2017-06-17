import hashlib
import glob

paths = glob.glob("*.jpg")
png = glob.glob("*.png")

for i in png:
    paths.append(i)

#paths.append("AwesomePenguin.jpg")
#paths.append("Ballon.jpg")
#paths.append("Flower.jpg")
#paths.append("GreenLeaf.jpg")

for i in paths:
    file = open(i, "rb")
    hash = hashlib.sha256()
    while True:
        buf = file.read(4096) # 128 is smaller than the typical filesystem block
        if not buf:
            break
        hash.update(buf)
    hashDigest = hash.hexdigest()
    print(i + " -> " + str(hashDigest))
