"""Дополнить проект фикстурой, которая после каждого шага 
теста дописывает в заранее созданный файл stat.txt строку вида:
время, кол-во файлов из конфига, размер файла из конфига, 
статистика загрузки процессора из файла /proc/loadavg 
(можно писать просто всё содержимое этого файла).
"""


@pytest.fixture()
def create_file_txt():
    if checkout_positive("ls {}".format(data['folder_tst']), data['filename']):
        return True
    else:
        res = checkout_positive("cd {} ../; touch {}".format(data['folder_tst'], data['filename']), "")
        return res


def func_test(cmd):
    return subprocess.run(f'{cmd}', shell=True, stdout=subprocess.PIPE, encoding='utf-8').stdout


@pytest.fixture()
def write_stat_file(print_time, create_file_txt):
    if create_file_txt:

        file = open('{}/{}'.format(data['folder_tst'], data['filename']), 'a')
        file.writelines('Test time:  ')
        file.write(str(print_time))
        file.write('Files quantity:  ')
        file.write(str(data['count']))
        file.write('Size of file:  ')
        file.write(str(data['size_of_file']))
        file.write(' ')
        file.write(func_test(f'cd /proc | cat loadavg'))
