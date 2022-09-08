# 作业一
# 3^4*5^2*11^7*13^8
# 因子:
#     1, 3, 3^2, 3^3, 3^4     5个
#     1, 5, 5^2               3个
#     1, 11, 11^2 ... 11^7    8个
#     1, 13, 13^2 ... 13^8    9个
# 共计 5 x 3 x 8 x 9 = 1080个


# 作业二    直接运行即可

##################################################################
# 获胜策略：
#   将每堆石子数转成2进制
#   将所有数进行异或运算
#   结果为0则为后手胜状态（Next Win），非0则为先手胜状态（First Win）
# 获胜操作:
#   先手胜状态时，每次操作使得各堆石子数异或结果为0
##################################################################

from functools import reduce

# 进行nim游戏并判断输赢程序

def Read_and_Move(nums, player):
    # 计算异或结果
    xor_result = reduce(lambda x, y: x^y, nums)
    if xor_result:
        # 计算各个元素的异或结果
        xor_nums = [xor_result^i for i in nums]
        # 取得异或结果小于原数的索引位置作为操作位
        move_index = list(map(lambda x, y: x<y, xor_nums, nums)).index(True)
        # 计算拿石子个数
        move = nums[move_index] - xor_nums[move_index]
        # 进行操作
        nums, player = Move(nums, move_index, move, player)
    else:
        # 异或结果为0时为必输状态，取走最大一堆加快游戏进度
        # 计算最大值索引
        move_index = nums.index(max(nums))
        # 选取最大值
        move = nums[move_index]
        # 进行操作
        nums, player = Move(nums, move_index, move, player)
    return nums, player


def Move(nums, index, move, player):
    # 拿取石子
    nums[index] -= move
    # 删除石子数为0的堆
    if nums[index]==0:
        nums.remove(0)

    if player:
        print(f"先手方从第{index+1}堆中拿走{move}颗石子")
    else:
        print(f"后手方从第{index+1}堆中拿走{move}颗石子")

    for i in range(len(nums)):
        print(f"第{i+1}堆石子剩余{nums[i]}个")

    player  = not player
    return nums, player


def nim_play(nums, player):
    if len(nums)==1:
        if player:
            print(f"先手方从第1堆中拿取{nums[0]}颗石子")
            print("First Win")
        else:
            print(f"后手方从第1堆中拿取{nums[0]}颗石子")
            print("Next Win")
    else:
        nums, player = Read_and_Move(nums, player)
        nums, player = nim_play(nums, player)
    return nums, player


def nim_game():
    heaps = 0
    nums = []
    # True为先手方，False为后手方，通过取反来进行来回操作
    player = True

    heaps = int(input("请输入堆数:"))

    if heaps<1:
        print("Input Error")
        return False
    else:
        for i in range(heaps):
            temp_num = int(input(f"请输入第{i+1}堆的石子数:"))
            if temp_num>0:
                nums.append(temp_num)
            else:
                print("Input Error")
                return False

    if heaps==1:
        print(f"先手方从第1堆中拿取{nums[0]}颗石子")
        print("First Win")
        return True
    else: nim_play(nums, player)


# nim游戏，双方都为最优操作
nim_game()

