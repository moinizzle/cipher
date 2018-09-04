# Functions for running an encryption or decryption.

# The values of the two jokers.
JOKER1 = 27
JOKER2 = 28

def clean_message(one_line_text):
  '''(str) -> str
  Return a string which only contains uppercase letters 
  and no spaces. Given string might contain lowercase 
  letters, numbers, punctation, and whitespaces. 
  REQ: cannot be empty if non-empty output is expected
  >>> clean_message('moinIrfan')
  'MOINIRFAN'  
  >>> clean_message('My cat is huge!!')
  'MYCATISHUGE'
  >>> clean_message('980m34092350235023o392358230i3950952305n932509!!!????..')
  'MOIN'
  >>> clean_message('messi10')
  'MESSI'
  >>> clean_message('??????????????????????????????????')
  ''
  >>> clean_message('')
  ''
  '''  
  # convert the raw input into uppercase letters
  only_uppercase_chars = one_line_text.upper()
  # Get rid of the whitespaces by replacing it with no spaces
  only_uppercase_chars = only_uppercase_chars.replace(" ", "")
  # Get rid of the numbers by looping through the string, if it finds
  # a number between 0-9, it replaces it with no spaces
  for i in range(9):
    only_uppercase_chars = only_uppercase_chars.replace(str(i), '')
    # Get rid of the punctation by also looping and splitting and then
    # joining the char with the rest of the string if there's no punctuation
    only_uppercase_chars = ''.join([a for a in only_uppercase_chars if a not 
                                    in ('!', '?', '=', ',', '.', '/',
                                        '(',')', '{', '}', '@', '#',
                                        '%', '^',  '*', '-', '_', '+',
                                        '~', ':', ';', '|', '<', '>')])
    return only_uppercase_chars

def encrypt_letter(single_uppercase_char, keystream_value):
  '''(str, int) -> str
  Given an uppercase character and keystream value,
  return the encrypted letter by processing the 
  uppercase letter with the keystream value.
  REQ: keystream_value >= 0
  REQ: keystream_value <= 26
  REQ: single_uppercase_char = must be char
  REQ: single_uppercase_char = must be uppercase
  REQ: single_uppercase_char = between A-Z
  >>> encrypt_letter('A', 1)
  'B'
  >>> encrypt_letter('K', 0)
  'K'
  >>> encrypt_letter('Z', 26)
  'Z'
  >>> encrypt_letter('M', 14)
  'A'
  >>> encrypt_letter('V', 19)
  'O'
  '''
  # Store all alphabet in one variable for later access
  alphabet_string = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
  # Cover the single string to a list of strings 
  alphabet_string_list = list(alphabet_string)
  # Convert the given alphabet character to number by obtaining the
  # index of the list where it's stored
  # Add the converted number to keystream_value
  encrypted_number = alphabet_string_list.index(single_uppercase_char) + \
  keystream_value
  # Subtract 26 if the encrypted number is larger than 26 since
  # the list of alphabet cannot be longer than 26 letters
  if encrypted_number > 25:
    encrypted_number = encrypted_number - 26
  # Obtain the encrypted letter by using the encrypted number
  # as an index for the alphabet list
  encrypted_letter = alphabet_string_list[encrypted_number]
  return encrypted_letter


def decrypt_letter(single_uppercase_char, keystream_value):
  ''' (str, int) -> str
  Given an uppercase character and keystream value,
  return the decrypted letter by processing the 
  uppercase letter with the keystream value.
  REQ: keystream_value >= 0
  REQ: keystream_value <= 26
  REQ: single_upper_char = must be char
  REQ: single_upper_char = must be uppercase
  REQ: single_upper_char = between A-Z
  >>> decrypt_letter('A',0)
  'A'
  >>> decrypt_letter('A',26)
  'A'
  >>>decrypt_letter('Z',0)
  'Z'
  >>> decrypt_letter('Z',0)
  'Z'
  >>> decrypt_letter('M',2)
  'K'
  >>> decrypt_letter('S',18)
  'A'
  '''
  # Store all alphabet in one variable for later access
  alphabet_string = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
  # Cover the single string to a list of strings 
  alphabet_string_list = list(alphabet_string)
  # Convert the given alphabet character to number by obtaining the
  # index of the list where it's stored
  # Subtract the converted number from keystream_value  
  decrypted_number = alphabet_string_list.index(single_uppercase_char) - \
  keystream_value
  # Add 26 if the encrypted number is smaller than 0 since
  # we subtracted 26 in encrypt_letter
  if decrypted_number < 0:
    decrypted_number = decrypted_number + 26
  # Obtain the decrypted letter by using the decrypted number
  # as an index for the alphabet list
  decrypted_letter = alphabet_string_list[decrypted_number]
  return decrypted_letter


def swap_cards(deck_of_cards, index_of_deck):
  '''(list of int, int) -> NoneType
  Given a list of integers which contain values in
  arbitrary indexes (deck of cards), and an index, 
  swap the value located at the given index with 
  the index which follows it, whilst treating 
  the deck of cards as circular. The list is
  mutated, and nothing is returned. 
  REQ: deck_of_cards has to be a list
  REQ: index_of_deck >= 0
  REQ: index_of_deck < len(deck_of_cards) (length of list)
  >>> deck = [1,2,3]
  >>> swap_cards(deck, 2)
  >>> deck == [3,2,1]
  True
  >>> cool_deck = [9,99,999,9999,99999, 999999, 9999999]
  >>> swap_cards(cool_deck, 0)
  >>> cool_deck == [99, 9, 999, 9999, 99999, 999999, 9999999]
  True
  >>> deck_of_cards = [1,4,7,10,13,16,19,22,25,28,3,6,9,12,15,18,21,24,27,2,5]
  >>>swap_cards(deck_of_cards, 6)
  >>> deck_of_cards == [1, 4, 7, 10, 13, 16, 22, 19, 25, 28, 3, 6, 9, 12, 
  15, 18, 21, 24, 27, 2, 5] 
  True
  >>> deck = [1,2,3]
  >>> swap_cards(deck, 0)
  >>> deck == [3,2,1]
  False
  '''
  # Assign a variable to the given index, and the following index
  a, b = index_of_deck, index_of_deck + 1
  # Since this list is being treated as a circular deck of cards,
  # if the card being switched is at the end, we automcatically
  # go back to the beginning of the deck, thus setting the 
  # index of the following card to 0.
  if a == (len(deck_of_cards)-1):
    b = 0
  # Switch the values using the indexes of the list stored in the 
  # variables, a and b.
  deck_of_cards[b], deck_of_cards[a] = deck_of_cards[a], deck_of_cards[b]    


def move_joker_1(deck_of_cards):
  '''(list of int) -> NoneType
  Given a list of integers which contain values in
  arbitrary indexes (deck of cards), switch the 
  JOKER1 value with the value following 
  it, whilst treating the deck of cards as 
  circular. The list is mutated, and 
  nothing is returned. 
  REQ: deck_of_cards has to be a list
  REQ: cannot be empty if non-empty output is expected
  REQ: list values have to be integers
  >>> deck = [1, 2, 27]
  >>> move_joker_1(deck)
  >>> deck == [27,2,1]
  True
  >>> deck_of_cards = [1,4,7,10,13,16,19,22,25,28,3,6,9,12,15,18,21,24,27,2,5]
  >>>move_joker_1(deck_of_cards)
  >>> deck_of_cards == [1, 4, 7, 10, 13, 16, 22, 19, 25, 28, 3, 6, 9, 12, 
  15, 18, 21, 24, 2, 27, 5] 
  True
  '''
  # Find the index of JOKER1 and store it in a variable
  joker_1_index = deck_of_cards.index(JOKER1)
  # Call the swap_cards to switch the JOKER1 card with
  # the card following it
  swap_cards(deck_of_cards, joker_1_index)
  

def move_joker_2(deck_of_cards):
  ''' (list of int) -> NoneType
  Given a list of integers which contain values in
  arbitrary indexes (deck of cards), move the 
  JOKER2 value two cards down, whilst 
  treating the deck of cards as 
  circular. The list is mutated, 
  and nothing is returned. 
  REQ: deck_of_cards has to be a list
  REQ: cannot be empty if non-empty output is expected
  REQ: list values have to be integers
  >>> deck = [1, 2, 28]
  >>> move_joker_2(deck)
  >>> deck == [2, 28, 1]
  True
  >>> deck_of_cards = [1,4,7,10,13,16,19,22,25,28,3,6,9,12,15,18,21,24,27,2,5]
  >>>move_joker_2(deck_of_cards)
  >>> deck_of_cards == [1, 4, 7, 10, 13, 16, 19, 22, 25, 3, 6, 28, 9, 12, 15, 
  18, 21, 24, 27, 2, 5]
  True
  '''
  # Get the index of JOKER2
  joker_2_index = deck_of_cards.index(JOKER2)
  # Call swap_cards to move it one card down
  swap_cards(deck_of_cards, joker_2_index)
  # Get the new index of JOKER2
  joker_2_index_2 = deck_of_cards.index(JOKER2)
  # Call swap_cards to move it one card down again, thus
  # JOKER2 gets moved down twice
  swap_cards(deck_of_cards, joker_2_index_2)
    

def triple_cut(deck_of_cards):
  '''(list of int) -> NoneType
  Given a list of integers which contain values in
  arbitrary indexes (deck of cards), move everything
  that's above the first joker (can be JOKER1 or 
  JOKER2) to the bottom of the deck. Everything 
  under the second joker (can be JOKER1 or 
  JOKER2) goes to the top of the deck.The 
  list is mutated, and nothing is returned. 
  REQ: deck_of_cards has to be a list
  REQ: cannot be empty if non-empty output is expected
  REQ: list values have to be integers
  >>> deck1 = [1, 2, 3, 27, 28]
  >>> triple_cut(deck1)
  >>> deck1 == [27, 28, 1, 2, 3]
  True
  >>> deck2 = [28, 1, 2, 3, 4, 27]
  >>> triple_cut(deck2)
  >>> deck2 == [28, 1, 2, 3, 4, 27]
  True
  >>> deck = [1,4,7,10,13,16,19,22,25,28,3,6,9,12,15,18,21,24,27,2,5
  >>> triple_cut(deck)
  >>> deck == [2, 5, 28, 3, 6, 9, 12, 15, 18, 21, 24, 27, 1, 4, 7, 10, 13, 
  16, 19, 22, 25]
  '''
  # Get the index of JOKER1
  joker_1_index = deck_of_cards.index(JOKER1)
  # Get the index of JOKER2
  joker_2_index = deck_of_cards.index(JOKER2)
  # Check which joker comes first  
  if joker_1_index < joker_2_index:
    # If JOKER1 comes first, then add 2 to JOKER2 index
    # and assign both of the indexes to variables   
    a, b = joker_1_index, joker_2_index + 1
    # Do the triple cut by switching the values above 
    # the first joker with the values under the second
    # joker, thus the triple cut
    deck_of_cards[b:], deck_of_cards[:a] = deck_of_cards[:a],deck_of_cards[b:]
  elif joker_1_index > joker_2_index:
    a, b = joker_2_index, joker_1_index + 1
    # If JOKER2 comes first, then add 1 to JOKER1 index
    # and assign both of the indexes to variables
    # Do the triple cut by switching the values above 
    # the first joker with the values under the second
    # joker, thus the triple cut
    deck_of_cards[b:], deck_of_cards[:a] = deck_of_cards[:a],deck_of_cards[b:]
    
def insert_top_to_bottom(deck_of_cards):
  '''(list of int) -> NoneType
  Given a list of integers which contain values in
  arbitrary indexes (deck of cards), use the value
  located in the highest index of the list. The
  value dictates how many cards from the top
  of the deck should be moved to the bottom,
  placing it right above the highest index
  (bottom card).The list is mutated, and 
  nothing is returned. 
  REQ: deck_of_cards has to be a list
  REQ: cannot be empty if non-empty output is expected
  REQ: list values have to be integers
  >>> deck = [1,2,3,2]
  >>> insert_top_to_bottom(deck)
  >>> deck == [3, 1, 2, 2]
  True
  >>> deck1 = [1,2,3,4,5,6,7,8,8]
  >>> insert_top_to_bottom(deck1)
  >>> deck1 == [1,2,3,4,5,6,7,8,8]
  True
  >>> deck2 = [1,4,7,10,13,16,19,22,25,28,3,6,9,12,15,18,21,24,27,2,5]
  >>> insert_top_to_bottom(deck2)
  >>> deck2 == [16, 19, 22, 25, 28, 3, 6, 9, 12, 15, 18, 21, 24, 27, 2, 1, 4, 
  7, 10, 13, 5]
  True
  '''
  # Find the value of the bottom card
  bottom_card = deck_of_cards[-1]
  # Assign a variable to the values which will be moved to the 
  # bottom of the deck
  move_to_bottom = deck_of_cards[:bottom_card]
  # delete the same values which are currently on the top
  del deck_of_cards[:bottom_card]
  # Add those same value to the bottom
  deck_of_cards.extend(move_to_bottom)
  # Remove the bottom card which is not currently
  # present at the bottom
  deck_of_cards.remove(bottom_card)
  # Add the same previously deleted card to the bottom,
  # where it's suppose to be
  deck_of_cards.append(bottom_card)    
    

def get_card_at_top_index(deck_of_cards):
  '''(list of int) -> int
  Given a list of integers which contain values in
  arbitrary indexes (deck of cards), return the card
  which is present in the lowest index. If the value
  of the card located at the lowest index is 
  JOKER2 (28), return JOKER1 (27) instead.
  REQ: deck_of_cards has to be a list
  REQ: cannot be empty if non-empty output is expected
  REQ: list values have to be integers
  >>> deck1 = [1,2,3,4,5,1]
  >>> get_card_at_top_index(deck1)
  2
  >>> deck2 = [28,4,7,10,13,16,19,22,25,28,3,6,9,12,15,18,21,24,27,2,
  5,8,11,14,17,20,23,26]
  >>> get_card_at_top_index(deck2)
  26
  >>> deck3 = [27,4,7,10,13,16,19,22,25,28,3,6,9,12,15,18,21,24,27,2, 
  5,8,11,14,17,20,23,26]
  >>> get_card_at_top_index(deck2)
  26
  '''
  # Get the value of the top card using index 0
  top_card = deck_of_cards[0]
  # If the value of the top card is JOKER2 (28),
  # then set it to JOKER1 (27)
  if top_card == JOKER2:
    top_card = JOKER1
  # Take the value of the top card as an index
  # and return the value located at that 
  # particular index
  return deck_of_cards[top_card]
    

def get_next_value(deck_of_cards):
  '''(list of int) -> int
  Given a list of integers which contain values in
  arbitrary indexes (deck of cards), return the 
  next potential keystream value associated with
  the particular deck.
  REQ: deck_of_cards has to be a list
  REQ: cannot be empty if non-empty output is expected
  REQ: list values have to be integers 
  REQ: deck_of_cards must have a 27 and 28 value inside it
  >>> deck = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,
  25,26,27,28]
  >>> get_next_value(deck)
  28
  >>> deck1 = [27,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,
  25,26,28,1]
  >>> get_next_value(deck1)
  6
  >>> deck2 = [27,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,
  25,26,1,28]
  >>> get_next_value(deck2)
  6 
  '''
  # This function perform 5 different functions to obtain
  # the keystream value
  # The first four mutate the list
  # This function switch the index of JOKER1 with
  # the card which follows it
  move_joker_1(deck_of_cards)
  # Moves joker two cards over
  move_joker_2(deck_of_cards)
  # Performs the triple cut where the values above the first
  # joker switched with the values which are under the second
  # joker 
  triple_cut(deck_of_cards)
  # Uses the value of the bottom card as an index for moving
  # that many cards from the top of the deck to the bottom, 
  # but placing it over the bottom card.
  insert_top_to_bottom(deck_of_cards)
  # The potential key value is determined by using the top 
  # card value as an index and returning that value.
  # That is the keystream value. 
  potential_key_value = get_card_at_top_index(deck_of_cards)
  return potential_key_value
    

def get_next_keystream_value(deck_of_cards):
  '''(list of int) -> int
  Given a list of integers which contain values in
  arbitrary indexes (deck of cards), return the 
  next keystream value associated with
  the particular deck. If the keystream values
  turns out to be JOKER1 (27) or JOKER2 (28),
  run the function again until a value between 
  1-26 is produced. 
  REQ: deck_of_cards has to be a list
  REQ: deck_of_cards cannot be empty if non-empty output is expected
  REQ: deck_of_card list values have to be integers 
  REQ: deck_of_cards must have a 27 and 28 value inside it 
  >>> deck = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,
  25,26,27,28]
  >>> get_next_keystream_value(deck)
  8
  >>> deck1 = [27,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,
  25,26,28,1]
  >>> get_next_keystream_value(deck1)
  6
  >>> deck2 = [27,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,
  25,26,1,28]
  >>> get_next_keystream_value(deck2)
  6 
  '''
  # call get_next_value to run the five stages of the
  # algorithm
  keystream_value = get_next_value(deck_of_cards)
  # If the key stream value turns out to be 
  # JOKER1 (27) or JOKER2(28), run the five
  # stages of the algorithm again!
  while keystream_value in {JOKER1, JOKER2}:
    keystream_value = get_next_value(deck_of_cards)
  return keystream_value
    

def process_message(deck_of_cards, message_to_process, encrypt_or_decrypt):
  '''(list of int, list str, str) ->  list of str
  Given a list of integers(deck of cards), string to process, and
  a string instructing whether to encrypt or decrypt the  given string,
  (message_to_process), return the encrypted or decrypted string as a list.
  REQ: deck_of_cards has to be a list
  REQ: deck_of_cards cannot be empty if non-empty output is expected
  REQ: deck_of_cards list values have to be integers 
  REQ: deck_of_cards must have a 27 and 28 value inside it 
  REQ: encrypt_or_decrypt = 'e' or 'd'
  REQ: message_to_process must be a string
  '''
  # make the message readable
  cleaned_message = clean_message(message_to_process) 
  # place the content of the message inside a list
  # for better accessibility
  cleaned_message_list = list(cleaned_message)
  encrypted_letter = ''
  decrypted_letter = ''
  # if the message is said to be encrypted or decryted, generate 
  # keystream values and use encrypt_letter function or 
  # decrypt_letter function and return the full
  # processed message
  for char in cleaned_message_list:
    keystream_value = get_next_keystream_value(deck_of_cards)
    if encrypt_or_decrypt == 'e':
      encrypted_letter = encrypted_letter + encrypt_letter(char, keystream_value
                                                           )
    elif encrypt_or_decrypt == 'd':
      decrypted_letter = decrypted_letter + decrypt_letter(char, keystream_value
                                                           ) 
  return encrypted_letter or decrypted_letter
    

def process_messages(deck_of_cards, list_of_messages_to_process,
                     encrypt_or_decrypt):
  '''(file open for reading) -> list of str
  Returns the contents of the file as a encrypted or decrypted
  list of strings. 
  REQ: deck_of_cards has to be a list
  REQ: deck_of_cards cannot be empty if non-empty output is expected
  REQ: deck_of_cards list values have to be integers 
  REQ: deck_of_cards must have a 27 and 28 value inside it 
  REQ: encrypt_or_decrypt = 'e' or 'd'
  '''
  # Use list comprehension to process each list value, which
  # contains string values to be encrypted or decryped
  list_of_messages_to_process = [process_message(deck_of_cards, i, 
                                                   encrypt_or_decrypt) for i in
                                   list_of_messages_to_process]
  # return the full processed message as a list
  return list_of_messages_to_process
    

def read_messages(read_open_file):
  '''(io.TextIOWrapper) -> list of str
  Return the values of the open file as a list of strings.
  REQ: file must be open
  '''
  list_of_deck_messages = ''
  # reads each line
  message = read_open_file.readline()
  # places the contents of the file in a string, separating them
  # by lines breaks.
  while message:
      list_of_deck_messages = list_of_deck_messages + message
        
      message = read_open_file.readline()
  return list_of_deck_messages.splitlines()

def read_deck(read_open_file):
  ''' (io.TextIOWrapper) -> list of int
  Return the values of the open file as a list of strings.
  REQ: file must be open
  '''
  list_of_deck_ints = [] #create an empty list
  line = read_open_file.readline() # read the file, line by line
  while line: # place the integers inside a list
      list_of_deck_ints = list_of_deck_ints + line.split() # use line breaks
      line = read_open_file.readline()                     # as separator
  # use list comprehension to convert values into ints
  return [int(i) for i in list_of_deck_ints] # values should be ints 


    