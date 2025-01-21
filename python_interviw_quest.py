
#
def second_array_number(data):
   # Remove duplicates to handle cases where the smallest number occurs multiple times
   unique_data = list(set(data))

   # Sort the list
   unique_data.sort()

   # Check if there are at least two unique numbers
   if len(unique_data) < 2:
      return None  # Or raise an exception if needed

   # Return the second smallest number
   return unique_data[1]


data = [15, 3, 4, 5, 6, 0, 2, 12, 1]
second_smallest = second_array_number(data)
print(second_smallest)

import re
def find_email(value):

   pattern = r'[a-zA-Z0-9._+%-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
   val_a = re.findall(pattern,value)
   print(val_a)

value_string = """
Python is a easy language which is very easy to learn. We have got some enquiries from maild IDs  abc@gmail.com, bvg@yahoo.com, tfg@gmail.com  rtf@yahoo.com and xyz@google.com  regarding the course details.

"""

output =find_email(value_string)
#

def find_duplicate_numbers(p_data):
    print(p_data)
    count_dict = {}
    duplicate= []
    for num in p_data:
       if num in count_dict:
          count_dict[num]+=1
       else:
          count_dict[num]=1


    for num,count in count_dict.items():
       if count >1:
          duplicate.append(num)

    return duplicate
data = [15, 3, 4, 5, 6, 0, 2, 2, 1, 1, 12, 1]
op = find_duplicate_numbers(data)
print(op)



def remove_duplicate(data):
    seen = set()
    unique_data = []
    for num in data:
        if num not in seen:
            unique_data.append(num)
            seen.add(num)
    return unique_data
data = [15, 3, 4, 5, 6, 0, 2, 2, 1, 1, 12, 1]
unique_data = remove_duplicate(data)
print(unique_data)

