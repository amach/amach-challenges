import sys

# This function merges two sorted lists by iteratively appending the smallest element of the lists
def merge_sorted_lists(list1, list2):
    result = []
    i, j = 0, 0

    while i < len(list1) and j < len(list2):
        if list1[i] <= list2[j]:
            result.append(list1[i])
            i += 1
        else:
            result.append(list2[j])
            j += 1

    result = result + list1[i:] + list2[j:]

    return result

# Testing the merging function with a file where each line is a pair of lists
#   in the format list1, list2
#   e.g.: [1,2,3], [4,5,6]
def main():

    file_name = raw_input("Enter your test file: ")

    f = open(file_name, 'r')

    for line in f:
        list1, list2 = eval(line)
        print "list1:", list1
        print "list2:", list2
        print merge_sorted_lists(list1, list2)

    f.close()

# Standard boilerplate to call the main() function to begin
# the program.
if __name__ == '__main__':
      main()
