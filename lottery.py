from random import randint
# 导入randint模块


class Lottery:
    # 用于生成彩票号码的类
    def __init__(self):
        self.numbers = 0

    def da_le_tou(self):
        self.numbers = input("欢迎选择大乐透！您希望生成多少注彩票号码？请输入： ")
        while self.numbers.isdigit() is not True:
            print("\n输入类型有误，请输入数字！")
            self.numbers = input("欢迎选择大乐透！您希望生成多少注彩票号码？请输入： ")
        print("\n")
        times = range(1, int(self.numbers) + 1)

        for n in times:
            local_pool_01 = []
            local_pool_02 = []
            number_01 = randint(1,35)
            local_pool_01.append(number_01)

            number_02 = randint(1,35)
            while number_02 in local_pool_01:
                number_02 = randint(1,35)
            local_pool_01.append(number_02)

            number_03 = randint(1,35)
            while number_03 in local_pool_01:
                number_03 = randint(1,35)
            local_pool_01.append(number_03)

            number_04 = randint(1, 35)
            while number_04 in local_pool_01:
                number_04 = randint(1, 35)
            local_pool_01.append(number_04)

            number_05 = randint(1, 35)
            while number_05 in local_pool_01:
                number_05 = randint(1, 35)
            local_pool_01.append(number_05)

            number_06 = randint(1, 12)
            local_pool_02.append(number_06)

            number_07 = randint(1, 12)
            while number_07 in local_pool_02:
                number_07 = randint(1, 12)
            local_pool_02.append(number_07)

            local_pool_01.sort()
            local_pool_02.sort()

            print("第" + str(n) + "注")
            print(' - 35选5号码为： ' + str(local_pool_01))
            print(' - 12选2号码为： ' + str(local_pool_02))

            print("\n")

    def shuang_se_qiu(self):
        self.numbers = input("欢迎选择双色球！您希望生成多少注彩票号码？请输入： ")
        while self.numbers.isdigit() is not True:
            print("\n输入类型有误，请输入数字！")
            self.numbers = input("欢迎选择双色球！您希望生成多少注彩票号码？请输入： ")
        print("\n")
        times = range(1, int(self.numbers) + 1)
        for n in times:
            red_pool = []
            blue_pool = []
            red_01 = randint(1,3)
            red_pool.append(red_01)

            red_02 = randint(1,33)
            while red_02 in red_pool:
                red_02 = randint(1,33)
            red_pool.append(red_02)

            red_03 = randint(1,33)
            while red_03 in red_pool:
                red_03 = randint(1,33)
            red_pool.append(red_03)

            red_04 = randint(1, 33)
            while red_04 in red_pool:
                red_04 = randint(1, 33)
            red_pool.append(red_04)

            red_05 = randint(1, 33)
            while red_05 in red_pool:
                red_05 = randint(1, 33)
            red_pool.append(red_05)

            red_06 = randint(1, 33)
            while red_06 in red_pool:
                red_06 = randint(1, 33)
            red_pool.append(red_06)

            blue_01 = randint(1, 16)
            blue_pool.append(blue_01)

            red_pool.sort()
            blue_pool.sort()

            print("第" + str(n) + "注")
            print(' - 红色球号码为： ' + str(red_pool))
            print(' - 蓝色球号码为： ' + str(blue_pool))

            print("\n")


# shuliang = input("您希望生成多少注彩票号码？请输入： ")
# while shuliang.isdigit() is not True:
#     print("\n输入类型有误，请输入数字！")
#     shuliang = input("您希望生成多少注彩票号码？请输入： ")
# print("\n")
# lottery_01 = Lottery(int(shuliang))
# lottery_01.da_le_tou()

# 待解决问题：各注彩票间去重







