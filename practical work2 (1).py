def read_file(filename):
    with open(filename, 'r') as file:
        return file.read()

# Test the function
content = read_file('sample.txt')
print(content[:100])  # Print the first 100 characters


def count_lines(content):
    return len(content.split('\n'))

# Test the function
num_lines = count_lines(content)
print(f"Number of lines: {num_lines}")

def count_words(content):
    return len(content.split())

# Test the function
num_words = count_words(content)
print(f"Number of words: {num_words}")

def count_unique_words(content):
    return len(set(content.lower().split()))   #converts the text to lowercase and splits it into words. set emsures only unique words

#test the function
num_unique_words = count_unique_words(content)
print(f"Number of unique words: {num_unique_words}")


def find_longest_word(content):
    words = content.split()
    return max(words, key=len) if words else ""  #to find words with max length
#test the func
longest_word = find_longest_word(content)
print(f"Longest word: {longest_word}")


def word_count_occurrences(content, target_word):
    words = content.lower().split()   #
    target_word = target_word.lower()
    return words.count(target_word)

#test
target_word = input("Enter the word to count: ")
word_count_occurrences = word_count_occurrences(content, target_word)
print(f"the word '{target_word}' appears {word_count_occurrences} times.")

def percentage_longer_than_average(content):
    words = content.split()
    if not words:
        return 0.0
    
    ave_length = sum(len(word) for word in words) / len(words)
    longer_words = [word for word in words if len(word) > ave_length]
    percentage = (len(longer_words) / len(words)) * 100

    return percentage
percentage = percentage_longer_than_average(content)
print(f"percentage of words longer than average: {percentage:.2f}%")