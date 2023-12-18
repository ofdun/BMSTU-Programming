import os
import struct


def deleteRowFromDb(path: str, row: int) -> None:
    row -= 1
    filesize = os.path.getsize(path)
    if filesize < 32 * row:
        return
    with open(path, "r+b") as f:
        pointerToRead = 32 * row + 32
        for _ in range(filesize - pointerToRead):
            f.seek(pointerToRead)
            byteToWrite = f.read(1)
            f.seek(pointerToRead - 32)
            f.write(byteToWrite)
            pointerToRead += 1
            
        f.truncate(pointerToRead - 32)
        
        
def writeLine(pathToFile: str, animal: str, height: float, weight: float):
    # little-endian
    line = struct.pack("< 24s f f", animal.encode('cp866'), height, weight)
    with open(pathToFile, "ab") as f:
        f.write(line)
        
        
def insertRowInDb(path: str, rowIndex: int, line: [str, float, float]) -> None:
    rowIndex -= 1
    filesize = os.path.getsize(path)
    writeLine(path, line[0], line[1], line[2])
    if filesize < 32 * rowIndex:
        return
    filesize += 32
    with open(path, "r+b") as f:
        pointerToWrite = filesize - 1
        for _ in range(filesize - rowIndex * 32 - 32):
            f.seek(pointerToWrite - 32)
            byteToWrite = f.read(1)
            f.seek(pointerToWrite)
            f.write(byteToWrite)
            pointerToWrite -= 1
        f.seek(rowIndex * 32)
        line = struct.pack("< 24s f f", line[0].encode('cp866'), line[1], line[2])
        f.write(line)