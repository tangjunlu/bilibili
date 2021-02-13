from process import process
if __name__ == '__main__':
    sess_data = input('输入SESSDATA值:')
    bili_jct = input('输入bili_jct值:')
    my_info = process.get_my_info(sess_data,bili_jct)
    print(my_info)