
class Query:

    def __init__(self, query):
        self.query = query

    def get_query(self, parser, searcher, number_docs_result_search):
        my_query = parser.parse(self.query)
        results = searcher.search(my_query, limit=number_docs_result_search)

        docs = []
        for x in list(results):
            doc_name = x['path']
            docs.append(doc_name)
        return docs
