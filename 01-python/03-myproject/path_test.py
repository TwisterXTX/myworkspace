import os


def get_all_sub(path):
    _dir_list = []
    _file_list = []
    for root, dirs, files in os.walk(path):
        # get all sub dirs
        for d_name in dirs:
            _dir_list.append(os.path.join(root, d_name))
        # get all sub files
        for f_name in files:
            _file_list.append(os.path.join(root, f_name))

    return _dir_list, _file_list


def get_all_file_keyword(path, file_type='py', keyword1=None, keyword2=None, un_keyword=None, un_keyword2=None):
    _file_keyword_list = []
    _file_list = []
    for root, dirs, files in os.walk(path):
        for fn in files:
            if os.path.join(root, fn).endswith(file_type):
                _file_list.append(os.path.join(root, fn))

    _file_keyword_list = [x for x in _file_list if os.path.isfile(x)]

    if keyword1 is not None:
        _file_keyword_list = [x for x in _file_keyword_list if keyword1 in os.path.basename(x)]

    if un_keyword is not None:
        _file_keyword_list = [x for x in _file_keyword_list if un_keyword not in os.path.basename(x)]

    return _file_keyword_list

if __name__ == '__main__':

    root_path = r'D:\02-githubtest\Lector'

    # dir_list, file_list = get_all_sub(root_path)
    #
    # for dir_name in dir_list:
    #     print(dir_name)

    py_file_list = get_all_file_keyword(root_path, file_type='py', keyword1='setup')

    print(py_file_list)
