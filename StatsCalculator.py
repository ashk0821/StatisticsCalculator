import math

def read_numbers():
    nums = []
    lines = input("Enter your numbers.")
    r
    while lines != "":
        line_lists = lines.split()
        for s in line_lists:
            nums.append(float(s))
        lines = input()

    return nums


def get_mean(my_list):
    total = 0

    for n in my_list:
        total += n

    return total / len(my_list)


def get_range(my_list):
    return max(my_list) - min(my_list)


def get_median(my_list):
    my_list.sort()

    if len(my_list) % 2 == 0:
        pos = len(my_list) // 2
        return (my_list[pos] + my_list[pos - 1]) / 2
    else:
        pos = len(my_list) // 2
        return my_list[pos]


def get_std_dev (my_list):
    total = 0
    for x in range (len(my_list)):
        total += (get_mean(my_list) - my_list[x]) ** 2
    return math.sqrt(total/len(my_list))


def main ():
    my_list = read_numbers()
    print ("Mean: %.2f" % get_mean(my_list))
    print ("Std Dev: %.2f" % get_std_dev(my_list))
    print ("Median: ", get_median(my_list))
    print ("Min: ", min(my_list))
    print ("Max: ", max(my_list))
    print ("Range: ", get_range(my_list))

main()