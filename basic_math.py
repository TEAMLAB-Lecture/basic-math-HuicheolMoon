#######################
# Basic Math          #
#######################

"""
여기서 간단한 수학을 하는 프로그램을 만들것입니다. 
"""


def get_greatest(number_list):
    """
    주어진 리스트에서 가장 큰 숫자를 반환함

        Parameters:
            number_list (list): integer로 값으로만 구성된 list
            ex - [10, 33, 22, 99, 33]

        Returns:
            greatest_number (int): parameter number_list 중 가장 큰 값

        Examples:
            >>> number_list = [39, 54, 32, 11, 99]
            >>> import basic_math as bm
            >>> bm.get_greatest(number_list)
            99
    """
    greatest_number = number_list[0]    # greatest_number의 초깃값 설정

    for number in number_list:          # 주어진 리스트 안의 원소 크기를 반복해서 비교
        if number > greatest_number:
            greatest_number = number

    return greatest_number              # 가장 큰 숫자 반환


def get_smallest(number_list):
    """
    주어진 리스트에서 제일 작은 숫자를 반환함

        Parameters:
            number_list (list): integer로 값으로만 구성된 list
            ex - [10, 33, 22, 99, 33]

        Returns:
            smallest_number (int): parameter number_list 중 가장 작은 값

        Examples:
            >>> number_list = [39, 54, 32, 11, 99]
            >>> import basic_math as bm
            >>> bm.get_smallest(number_list)
            11
    """
    smallest_number = number_list[0]    # smallest_number의 초깃값 설정

    for number in number_list:          # 주어진 리스트 안의 원소 크기를 반복해서 비교
        if number < smallest_number:
            smallest_number = number

    return smallest_number              # 가장 작은 숫자 반환


def get_mean(number_list):
    """
    주어진 리스트 숫자들의 평균을 구함.

        Parameters:
            number_list (list): integer로 값으로만 구성된 list
            ex - [10, 33, 22, 99, 33]

        Returns:
            mean (int): parameter number_list 숫자들의 평균

        Examples:
            >>> number_list = [39, 54, 32, 11, 99]
            >>> import basic_math as bm
            >>> bm.get_mean(number_list)
            47
    """
    sum = 0

    for number in number_list:          # 리스트 원소들의 합 계산
        sum += number

    mean = sum / len(number_list)       # 리스트 원소들의 합을 리스트 원소의 개수로 나누어 평균 계산

    return mean


def quick_selection(number_list, order):
    """
    주어진 리스트에서 Quick selection을 진행.

        Parameters:
            number_list (list): integer로 값으로만 구성된 list
                ex - [10, 33, 22, 99, 33]
            order (int): 찾으려는 숫자의 크기 순서
    """
    mid_num = len(number_list) // 2
    pivot = number_list[mid_num]
    less = []
    more = []

    if len(number_list) == 1:
        return number_list[0]

    for number in number_list:
        if number < pivot:
            less.append(number)
        else:
            more.append(number)

    if len(less) >= order:
        return quick_selection(less, order)
    else:
        return quick_selection(more, order-len(less))


def get_median(number_list):
    """
    주어진 리스트 숫자들의 중간값을 구함.

        Parameters:
            number_list (list): integer로 값으로만 구성된 list
            ex - [10, 33, 22, 99, 33]

        Returns:
            median (int): parameter number_list 숫자들의 중간값

        Examples:
            >>> number_list = [39, 54, 32, 11, 99]
            >>> import basic_math as bm
            >>> bm.get_median(number_list)
            39
            >>> number_list2 = [39, 54, 32, 11, 99, 5]
            >>> bm.get_median(number_list2)
            35.5
    """
    mid_number = len(number_list) // 2 + 1

    if len(number_list) % 2 == 1:
        median = quick_selection(number_list, mid_number)
    else:
        median = (quick_selection(number_list, mid_number - 1) + quick_selection(number_list, mid_number)) / 2
    
    return median
