# def gen_f(fname):
#     with open(fname) as file:
#         j = 0
#         file_lines = file.readlines()
#         print(file_lines)
#         for each in file_lines:
#             if each != '\n':
#                 j += 1
#             print(j)
#
# gen_f('/home/cisco/PycharmProjects/samp_proj1/day_201118/para.txt')
# # j = 0
# for i in gen_f('/home/cisco/PycharmProjects/samp_proj1/day_201118/para.txt'):
#     print(i)
#
#
# print("No of paras", j)
gen_obj = (each for each in open('/home/cisco/PycharmProjects/samp_proj1/day_201118/para.txt'))
print(next(gen_obj))
print(next(gen_obj))
print(next(gen_obj))
print(next(gen_obj))
