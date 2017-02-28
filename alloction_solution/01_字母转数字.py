# -*- coding:utf-8 -*-

import unittest


def char2num(num_str):
    '''
    将数字串进行二叉树化。左子树：一个字符。右子树：两个字符。
    类似于深度遍历，每次遇到叶子节点，将从跟节点到叶节点的信息全部打印
    举例：123
    -->
        1        12
      2   23   3
    3
    '''
    result = []
    if len(num_str) == 0:
        return result
    char_list = map(lambda x: chr(x + ord('a')), range(0, 26))
    num_char = dict(zip(range(1, 27), list(char_list)))
    stack_tmp = []  # 记录了上次分叉的地方，当失败的时候，弹出，另行处理
    char_tmp = []   # 记录存放的字符串
    
    # [0, 1],0 代表在num_str中的位置。1 代表在字符队列中的位置
    stack_tmp.append([-1,0])
    while len(stack_tmp):
        stack_data = stack_tmp.pop(-1)
        index = stack_data[0]
        char_index = stack_data[1]
        if char_index != -1:
            char_tmp = char_tmp[:char_index]

        while index < len(num_str):
            # 取一位，并将左子树压入栈
            if index != -1:
                char_data = num_str[index]
                char_tmp.append(num_char[int(char_data)])

            new_stack_data = [index + 1, len(char_tmp)]
            stack_tmp.append(new_stack_data)

            index += 1
            # 取两位，优先遍历右子树
            if index >= len(num_str):
                result.append(char_tmp)
                break
            if index + 1 >= len(num_str):
                break
            char_data = num_str[index:index + 2]
            if char_data > "26":
                break
            else:
                char_tmp.append(num_char[int(char_data)])
            index += 2
            if index >= len(num_str):
                result.append(char_tmp)

    return result


class Test(unittest.TestCase):
    '''TestCase'''

    datas = [
        {
            "expected": [['l', 'c'], ['a', 'w'], ['a', 'b', 'c']],
            "input": '123'
        },
        {
            "expected": [],
            "input": ''
        }
    ]

    def test_char2num(self):
        for data in self.datas:
            actual = char2num(data['input'])
            self.assertEqual(actual, data['expected'])


if __name__ == "__main__":
    unittest.main()
