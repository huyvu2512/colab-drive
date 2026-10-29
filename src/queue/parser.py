# Bộ bóc tách và phân tích liên kết đầu vào
def extract_urls(raw_text):
    if not raw_text or not raw_text.strip():
        return []
    cleaned = raw_text.replace(',', '\n').replace(';', '\n').replace('|', '\n')
    urls_list = []
    for line in cleaned.split('\n'):
        line = line.strip()
        if not line:
            continue
        for token in line.split():
            token = token.strip()
            if token:
                urls_list.append(token)
    return urls_list
