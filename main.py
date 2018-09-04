
"""
Encrypt or decrypt the contents of a message file using a deck of cards.
"""
import cipher

DECK_FILENAME = 'deck.txt'
MSG_FILENAME = 'encrypt.txt'
MODE = 'e'  # 'e' for encryption, 'd' for decryption.


def main():
    """ () -> NoneType

    Perform the encryption using the deck from a file called DECK_FILENAME and
    the messages from a file called MSG_FILENAME. If MODE is 'e', encrypt;
    otherwise, decrypt. Print the decrypted message to the screen.
    """
    # opens the file which contains the deck
    open_deck_file = open(DECK_FILENAME, 'r') 
    # opens the file which contains the message t
    # encrypt or decrypt
    open_message_file= open(MSG_FILENAME,'r')
    # reads deck
    DECK_LIST = cipher.read_deck(open_deck_file)
    # read message
    MSG_LIST = cipher.read_messages(open_message_file)
    # process the message to be encrypted or decrypted
    LIST_ENCRYPT_DECRYPT = cipher.process_messages(DECK_LIST,MSG_LIST, MODE)
    # join the list values together to form a string
    STR_ENCRYPT_DECRYPT = " ".join(LIST_ENCRYPT_DECRYPT)
    # break lines, thus replace whitespaces
    STR_ENCRYPT_DECRYPT = STR_ENCRYPT_DECRYPT.replace(' ', '\n')
    print(STR_ENCRYPT_DECRYPT)
    open_message_file.close()
    open_deck_file.close()
    
main()

