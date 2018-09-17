def missing_numbers(num_list):
      original_list = [i for i in range(num_list[0], num_list[-1] + 1)]
      num_list = set(num_list)
      return (list(num_list ^ set(original_list)))

print(missing_numbers([1,2,3,6,4,7,10]))
print(missing_numbers([10,14,20]))

