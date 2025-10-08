def text_read(str):
    words = len(str.split())
    time = (words / 200) * 60
    result = f"{int(time)} seconds"
    return result
