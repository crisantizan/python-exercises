from inspect import cleandoc
from os import name, system


def clear_screen():
    # for Windows
    if name == 'nt':
        _ = system('cls')
    # Linux, Mac
    else:
        _ = system('clear')


class Contact:
    def __init__(self, id, name, phone, email):
        self.id = id
        self.name = name
        self.phone = phone
        self.email = email

    # def edit(self, )


class ContactBook:
    def __init__(self):
        self._contacts = []
        pass

    def add(self, name, email, phone):
        if self._email_exists(email):
            raise Exception('Email already exists')

        new_id = self._generate_id()
        contact = Contact(id=new_id, name=name, email=email, phone=phone)
        self._contacts.append(contact)
        clear_screen()
        print('**** --- New contact saved successfully! --- ****\n')

    def _email_exists(self, email):
        for contact in self._contacts:
            if contact.email == email:
                return True
        else:
            return False

    def _generate_id(self):
        length = len(self._contacts)
        return length + 1 if (length > 0) else 1

    def _print(self, contact):
        print('**** ---- **** ---- **** ---- **** ---- ****')
        print('ID: {}'.format(contact.id))
        print('Name: {}'.format(contact.name))
        print('Phone: {}'.format(contact.phone))
        print('Email: {}'.format(contact.email))
        print('**** ---- **** ---- **** ---- **** ---- ****\n')

    def print(self):
        for contact in self._contacts:
            self._print(contact)


def print_menu():
    menu = '''
        SELECT AN OPTION:

        [l]ist contacts
        [s]earch contact
        [a]dd new contact
        [e]dit contact
        [d]elete contact
    '''
    print(cleandoc(menu))


def get_contact_data():
    name = input('Type a name: ')
    email = input('Type a email: ')
    phone = input('Type a phone: ')

    return {'name': name, 'email': email, 'phone': phone}


def main():
    contact_list = ContactBook()
    # contact_list.add(
    #     name='Cristian', email='crisantizan@gmail.com', phone=3456)
    # contact_list.add(
    #     name='José', email='crisantizan@gmail.com', phone=3456)
    # contact_list.print()
    # contact = Contact(name='Cristian', phone=3654,
    #                   email='crisantizan@gmail.com')

    # print(vars(contact))
    # book = ContactBook()
    # book.add(contact)
    # book.print()

    while True:
        print_menu()
        option = input(
            '\nPress the first letter of option you want: \n'
        ).lower()[0]

        if option == 'l':
            contact_list.print()
        elif option == 's':
            print('Search contact...\n')
        elif option == 'a':
            success = False
            while not success:
                try:
                    data = get_contact_data()
                    contact_list.add(
                        data['name'], data['email'], data['phone']
                    )
                    success = True
                except Exception as error:
                    print('\n{}, please try again\n'.format(error))

        elif option == 'e':
            print('Edit contact...\n')
        elif option == 'd':
            print('Delete contact...\n')
        else:
            print('Please, select a valid option\n')


if __name__ == '__main__':
    main()
