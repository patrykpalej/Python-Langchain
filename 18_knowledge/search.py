import re


def search_docs(docs, keywords):
    def is_keyword_in_doc(doc):
        for keyword in keywords:
            keyword = re.sub(r"[.,\/#!$%\^&\*;:{}=\-?`~()]", "", keyword)
            if keyword.lower() in doc.page_content.lower() and len(keyword) > 3:
                print(f'Found: {keyword}')
                return True
        return False

    return [doc for doc in docs if is_keyword_in_doc(doc)]
