import struct


def isInts(nums: str) -> bool:
    for i, num in enumerate(nums):
        while True:
            try:
                num = float(num)
                if int(num) != num:
                    raise Exception
                nums[i] = int(num)
                break
            except ValueError:
                return False
            except Exception:
                print("Не все элементы являются целыми числами!")
                return False
    return True
            
            
def removeNegatives(path: str, n: int):
    with open(path, "r+b") as f:
        pointer = 0
        count = 0
        for _ in range(n):
            f.seek(pointer)
            num = struct.unpack("<i", f.read(4))[0]
            if num < 0:
                count += 1
            else:
                f.seek(pointer - count * 4)
                f.write(struct.pack("<i", num))
            pointer += 4
        f.truncate(4 * (n - count))
        

def addDoubled(path: str, n: int):
    with open(path, "r+b") as f:
        count = 0
        for _ in range(n):
            num = struct.unpack("<i", f.read(4))[0]
            if num < 0:
                count += 1
        f.seek(0, 2)
        f.write(struct.pack(f"<{count}i", *[0]*count))
        pointer = 4 * (n - 1)
        for _ in range(n):
            if count == 0:
                break
            f.seek(pointer)
            num = struct.unpack("<i", f.read(4))[0]
            if num >= 0:
                f.seek(pointer + count * 4)
                f.write(struct.pack("<i", num))
            else:
                count -= 1
                f.seek(pointer + count * 4)
                f.write(struct.pack("<i", num))
                f.write(struct.pack("<i", num * 2))
            pointer -= 4
            
            
def gnomeSortFile(path: str, n: int) -> None:
    with open(path, "r+b") as f:
        pointer = 0
        for i in range(1, n):
            pointer = (i - 1) * 4
            f.seek(pointer)
            currentNumBytes = f.read(4)
            currentNum = struct.unpack("<i", currentNumBytes)[0]
            nextNumBytes = f.read(4)
            nextNum = struct.unpack("<i", nextNumBytes)[0]
            while nextNum < currentNum and pointer >= 0:
                f.seek(pointer)
                f.write(nextNumBytes)
                f.write(currentNumBytes)
                f.flush()
                pointer -= 4
                if pointer < 0:
                    break
                
                f.seek(pointer)
                currentNumBytes = f.read(4)
                currentNum = struct.unpack("<i", currentNumBytes)[0]