import zlib

def compress_data(data):
    return zlib.compress(data.encode())

print(compress_data("Hello, World!"))
