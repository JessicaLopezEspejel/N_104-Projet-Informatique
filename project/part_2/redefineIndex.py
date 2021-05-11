

class RedefineIndex:

    def __init__(self, content):
        self.content = content

    def process_read(self):
        return self.content

    def get_content(self, path_name_file_index, pool):
        with open(path_name_file_index, 'r', encoding='utf-8') as file_idx:
            content = pool.map(self.process_read, file_idx)
        return content

    def get_keywords(self):
        pass
