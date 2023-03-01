import textwrap

def wrap(string, max_width):
    wrapper = textwrap.TextWrapper(width=max_width)
  
    word_list = wrapper.wrap(text=string)
  
# Print each line.
    for element in word_list:
        print(element)
    return

if __name__ == '__main__':
    string, max_width = input('enter a sentence:'), int(input('Enter the number of alphabets you want in each line:'))
    result = wrap(string, max_width)
    print(result)