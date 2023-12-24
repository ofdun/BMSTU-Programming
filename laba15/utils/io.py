import struct
from utils.actions import (isInts)


def inputNums(prompt: str) -> list[int]:
    while True:
        nums = input(prompt).split()
        if not isInts(nums):
            print("Неправильный ввод!")
        else:
            break
    return nums


def printFile(path: str):
    with open(path, "rb") as f:
        print(f"Файл {path}")
        while True:
            line = f.read(4)
            if len(line) != 4:
                break
            num = struct.unpack("<i", line)[0]
            print(f"{num} ", end='')
        print()
        
        
def writeNums(path: str, nums: list[int]) -> None:
    with open(path, "wb") as f:
        for num in nums:
            line = struct.pack("<i", num)
            f.write(line)