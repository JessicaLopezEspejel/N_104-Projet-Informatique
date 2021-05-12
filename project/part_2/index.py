
import time
import sys
from whoosh.index import create_in, open_dir, exists_in

from redefineIndex import RedefineIndex


def create_index(save_index_folder, index_name, num_docs_index, lst_articlesIndex, schema, pool):
    t0 = time.time()
    if not exists_in(save_index_folder, index_name):
        print('*' * 10 + ' Building the index for {} documents '.format(num_docs_index) + '*' * 10)
        ix = create_in(save_index_folder, schema, index_name)  # it returns an index.
        writer = ix.writer(procs=6, multisegment=True, limitmb=4096)  # procs=6, limitmb=4GB## OR 8192

        for idx, path_name_file_index in enumerate(lst_articlesIndex[num_docs_index]):
            if idx % 10000 == 0:
                t1 = time.time()
                print("  {}/{}. elapsed time : {}s".format(idx, num_docs_index, round(t1 - t0, 3)));
                sys.stdout.flush()
            # Object
            redefine_index = RedefineIndex()
            article_content = redefine_index.get_content(path_name_file_index, pool)
            article_content = " ".join(article_content)

            writer.add_document(path=path_name_file_index, content=article_content)  # , time=modtime
        # writer.remove_field("path")
        writer.commit(merge=False)
        t1 = time.time()
        print('*' * 10 + ' Index built in {}s '.format(round(t1 - t0, 3)) + '*' * 10)  # It's CPU seconds elapsed (floating point)

    ix = open_dir(save_index_folder, index_name)

    return ix