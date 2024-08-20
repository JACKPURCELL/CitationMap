from citation_map import generate_citation_map

if __name__ == '__main__':
    # This is my Google Scholar ID. Replace this with your ID.
    scholar_id = '3rDjnykAAAAJ'
    generate_citation_map(scholar_id,use_openai=False)