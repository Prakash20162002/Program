import string


def remove_punctuation(input_string):
    return ''.join([char for char in input_string if char not in string.punctuation])


def is_prime(number):
    if number <= 1:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True


input_string =input("Enter a String To Remove Punctuation")
clean_string = remove_punctuation(input_string)
print("String without punctuation:", clean_string)


num =int(input("Enter a Number to Chcek Prime or Not"))
print(f"Is {num} prime? {'Yes' if is_prime(num) else 'No'}")
