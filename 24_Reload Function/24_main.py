from imp import reload
import reload_example


def main():
    try:
        reload(reload_example)
        reload_example.skills()
    except Exception as e:
        print(str(e))


while True:
    '''
    While program runs - you can Edit and Save reload_example and program changed
    '''
    main()
    input('Enter to continue: ')
