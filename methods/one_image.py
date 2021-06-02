from connector import MySQL


def upload_one_img(base64_str: str, extension: str):
    sql = MySQL()

    sql.transaction.start()
    try:
        sql.query('INSERT INTO test_table VALUE (%s, %s)', (base64_str, extension, ))
    except:
        sql.transaction.rollback()
        return False, 'exception_occurred'
    else:
        sql.transaction.commit()
        return True, None


def get_one_img(img_num: int):
    sql = MySQL(dict_cursor=True)
    result = sql.query('SELECT image, extension FROM test_table WHERE id=%s', (img_num, ))

    if len(result) == 0:
        return False, None

    result = result[0]
    result['image'] = result['image'].decode("UTF-8")

    return True, result
