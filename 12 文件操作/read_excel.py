import xlrd
import random
import xlwt


def read_and_write_xls():
    wb = xlrd.open_workbook('test.xls')
    sh = wb.sheet_by_index(0)
    print(sh.nrows)
    print(sh.ncols)

    data = sh.col_values(4)
    # data = data[4:-3]
    size = len(data)
    print(data)
    score = []
    for i in range(size):
        mean = data[i]
        if mean > 90:
            random_range = random.randint(1, 2)
        elif mean > 95:
            random_range = random.randint(1, 1)
        else:
            random_range = random.randint(1, 3)
        temp = []
        for j in range(6):
            temp.append(random.randint(mean - random_range, mean + random_range))
        temp.append(int(mean / 10) * 10 + 5)
        a = int(8 * mean - sum(temp))
        temp.append(a)
        random.shuffle(temp)
        score.append(temp.copy())
        print(temp)

    wb_xw = xlwt.Workbook(encoding='utf-8')
    sh_xw = wb_xw.add_sheet('score')
    for i in range(len(score[0])):
        for j in range(len(score)):
            sh_xw.write(j, i, label=score[j][i])

    wb_xw.save('paper_score.xls')

    '''
    # for j in range(len(score[0])):
    #     for i in range(len(score)):
    #         with open('data.txt', 'a') as f:
    #             f.write(str(score[i][j]))
    #             f.write('\n')
    #             if i == len(score) - 1:
    #                 f.write('\n')
    '''


read_and_write_xls()
