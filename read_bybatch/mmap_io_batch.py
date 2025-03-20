import itertools
import mmap

BATCH_SIZE = 2048

def mmap_io_batch(filename):
    with open(filename, mode="r", encoding="utf8") as file_obj:
        with mmap.mmap(file_obj.fileno(), length=0, access=mmap.ACCESS_READ) as mmap_obj:
            file_size = mmap_obj.size()
            offset = 0
            while offset < file_size:
                chunk = mmap_obj[offset:offset + BATCH_SIZE]
                yield chunk
                offset += BATCH_SIZE