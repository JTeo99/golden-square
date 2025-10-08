def make_snippet(str):
    words = str.split()
    if len(words) > 4:
        snippet = " ".join(words[:5]) + "..."
        
    else:
        snippet = str

    return snippet