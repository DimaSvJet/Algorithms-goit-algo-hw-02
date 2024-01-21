from collections import deque


def check_text(text):

    chars_deque = deque()

    for char in text:
      chars_deque.append(char)

    while len(chars_deque) > 1:
       first_char = chars_deque.pop()
       last_char =  chars_deque.popleft()
       if first_char != last_char:
          print("It's not a polindrome")
          break
    else:
       print('The word is a polindrome')

check_text("radar")

