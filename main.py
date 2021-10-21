from flashtext import KeywordProcessor
#documentation of many use cases https://github.com/vi3k6i5/flashtext

keyword_processor = KeywordProcessor()
keyword_processor = KeywordProcessor(case_sensitive=False)
keyword_dict = {
    "follow_up": ["FU", "Follow up", "follow up"],
    "book_appt": ["appt"],
    "email": ["send", "email", "lab req"],
    "call": ["book", "contact"],
    "fax": ["fax", "pharmacy"]
}

keyword_processor.add_keywords_from_dict(keyword_dict)


def parse_line(line):
    print(keyword_processor.extract_keywords(line))
    print("------------------------------------------")

if __name__ == '__main__':
    # print_hi('PyCharm')
    ticklers = open(r"ticklers.txt")
    for line in ticklers:
        single_tickler = ticklers.readline()
        print(single_tickler)
        parse_line(single_tickler)


