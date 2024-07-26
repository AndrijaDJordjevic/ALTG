import sources.MyClass

def parse_first_page(text):
    first_page = FirstPage()
    lines = text.split("\n")
    for line in lines:
        if "Total brut" in line:
            first_page.total_brut = float(re.search(r"Total brut\s+(\d+\.\d+)", line).group(1))
        elif "Prorata" in line:
            first_page.prorata = float(re.search(r"Prorata\(\%\)\s+(\d+\.\d+)", line).group(1))
        elif "Total hors TVA" in line:
            first_page.total_hors_tva = float(re.search(r"Total hors TVA\s+(\d+\.\d+)", line).group(1))
        elif "TVA" in line:
            first_page.tva = float(re.search(r"TVA\s+(\d+\.\d+)", line).group(1))
        elif "Total TTC" in line:
            first_page.total_ttc = float(re.search(r"Total TTC\s+(\d+\.\d+)", line).group(1))
    return first_page

def parse_last_page(text):
    last_page = LastPage()
    lines = text.split("\n")
    for line in lines:
        if "Total net HT" in line:
            last_page.total_net_ht = float(re.search(r"Total net HT\s+(\d+\.\d+)", line).group(1))
        elif "TVA" in line:
            last_page.total_tva = float(re.search(r"TVA\s+(\d+\.\d+)", line).group(1))
        elif "Total net TTC" in line:
            last_page.total_net_ttc = float(re.search(r"Total net TTC\s+(\d+\.\d+)", line).group(1))
    return last_page

def parse_middle_pages(text):
    middle_page = MiddlePage()
    lines = text.split("\n")
    for line in lines:
        match = re.match(r"(.+?)\s+(\d+,\d+)\s+[a-z]+\s+(\d+\.\d+)\s+CHF\s+(\d+\.\d+)\s+CHF", line)
        if match:
            description = match.group(1).strip()
            quantity = float(match.group(2).replace(',', '.'))
            unit_price = float(match.group(3))
            total_price = float(match.group(4))
            item = LineItem(description, quantity, unit_price, total_price)
            middle_page.add_item(item)
    return middle_page

def ParseAndStructPagesText(pages_text, debug_state):
    first_page_text = pages_text[0]
    last_page_text = pages_text[-1]
    middle_pages_text = pages_text[1:-1]

    first_page = parse_first_page(first_page_text)
    last_page = parse_last_page(last_page_text)
    middle_pages = [parse_middle_pages(page_text) for page_text in middle_pages_text]

    if debug_state:
        print("First Page:", first_page)
        print("Last Page:", last_page)
        for i, middle_page in enumerate(middle_pages):
            print(f"Middle Page {i+1}:", middle_page)

    return first_page, middle_pages, last_page