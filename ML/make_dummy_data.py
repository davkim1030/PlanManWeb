# 1. work table을 사용하여 1일 뒤, 2일 뒤 completetion_rate 예측
# 1. completion_rate(work.complete_time/plan.object_time), work_instance.date
# 2. plan table을 사용하여 iteration_type에 따라 일정 기간의 통계를 통해 object_time 재설정 권유
# 2. date, work.completion_rate, plan.object_time

import numpy
import csv

if __name__ == '__main__':
    f = open('output1.csv', 'w', encoding='utf-8', newline='')
    wr = csv.writer(f)
    wr.writerow(['date', 'object_time', 'complete_time', 'completion_rate']) # data set 1 header
    # wr.writerow(['date', 'completion_rate', 'object_time']) # data set 2 hedaer

    object_time = 0

    for i in range(1000):
        """ for data set 1"""
        # round(numpy.random.uniform(0, 2), 2)
        object_time = numpy.random.random_integers(1, 100)
        complete_time = numpy.random.random_integers(0, 100)
        wr.writerow([i, object_time, complete_time, round(complete_time / object_time, 2)])
        """ for data set 2"""
        # if i % 7 == 0:
        #     object_time = numpy.random.random_integers(1, 100)
        # wr.writerow([i,
        #              round(numpy.random.random_integers(0, object_time) / object_time, 2),
        #              object_time])

    f.close()
