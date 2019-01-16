#  File: PhoneBook.py

#  Description: The purpose of this assignment is to build a phone book that
#  will store contact information of people that the user knows.

#  Student Name: Jorge Caviedes

#  Student UT EID: jac9773

#  Course Name: CS 313E

#  Unique Number: 51350

#  Date Created: 9/18/2018

#  Date Last Modified: 9/21/2018

class ContactInfo (object):
  # constructor
  def __init__ (self, street = ' ', city = ' ', state = ' ', zip = ' ', country = ' ', phone = ' ', email = ' '):
      self.street = street
      self.city = city
      self.state = state
      self.zip = zip
      self.country = country
      self.phone = phone
      self.email = email

  # string representation of Contact Info
  def __str__ (self):
      return str(self.street) + '\n' + str(self.city) + '\n' + str(self.state) + '\n' + str(self.zip) + '\n' + str(self.country) + '\n' + str(self.phone) + '\n' + str(self.email)

# Define global dictionary to hold all the contact information
phone_book = {}

# This function adds the contact information of a new person in the
# dictionary
def add_person():
  # Prompt the user to enter the name of the new person
  name = input('Enter name: ')
  if name == "":
      menu()
      return
  # Check if name exists in phone book. If it does print a message
  # to that effect and return
  if name in phone_book:
      print('{} exists in the phone book.'.format(name))
      return
  # Prompt the user to enter the required contact information
  street = input('Enter street: ')
  city = input('Enter city: ')
  state = input('Enter state: ')
  zip = input('Enter zip: ')
  country = input('Enter country: ')
  phone = input('Enter phone number: ')
  email = input('Enter e-mail address: ')
  # Create the ContactInfo object
  contactObj = ContactInfo (street, city, state, zip, country, phone, email)
  # Add the name and the contact information to the phone dictionary
  phone_book[name] = contactObj
  # Print message that the information was added successfully
  print('The contact has been added successfully.')

# This function deletes an existing person from the phone dictionary
def delete_person():
  # Prompt the user to enter the name of the person
  name = input('Enter name: ')
  # If the name exists in phone book delete it.
  # Print message as to the action.
  if name in phone_book:
      del phone_book[name]
      print('{} was deleted from the phone book.'.format(name))
      return
  else:
      print('{} does not exist in the phone book.'.format(name))
      return

# This function updates the information of an existing person
def update_person():
  # Prompt the user to enter the name of the person
  name = input('Enter name: ')
  # Check if name exists in phone book. If it does prompt
  # the user to enter the required information.
  if name in phone_book:
      contact = phone_book[name]
      street = input('Enter street: ')
      if street != "":
          contact.street = street
      city = input('Enter city: ')
      if city != "":
          contact.city = city
      state = input('Enter state: ')
      if state != "":
          contact.state = state
      zip = input('Enter zip: ')
      if zip != "":
          contact.zip = zip
      country = input('Enter country: ')
      if country != "":
          contact.country = country
      phone = input('Enter phone number: ')
      if phone != "":
          contact.phone = phone
      email = input('Enter e-mail address: ')
      if email != "":
          contact.email = email

      print('Information has been updated.')
      return
  # If the name does not exist print a message to that effect.
  else:
      print('{} does not exist in the phone book.'.format(name))
      return

# This function prints the contact information of an existing person
def search_person():
  # Prompt the user to enter the name of the person
  name = input('Enter name: ')
  # Check if name exists in phone book. If it does print the
  # information in a neat format.
  if name in phone_book:
      print('Contact information for {} - '.format(name))
      print(phone_book[name])
      return
  # If the name does not exist print a message to that effect.
  else:
      print('{} does not exist in the phone book.'.format(name))
      return

# This function open the file for writing and writes out the contents
# of the dictionary.
def save_quit():
  # Open file for writing
  out_file = open ('./phone.txt', 'w')
  # Iterate through the dictionary and write out the items in the file
  for key in phone_book:
      out_file.write(str(key) + '\n')
      out_file.write(str(phone_book[key]) + '\n')
      out_file.write('\n')
  # Close file
  out_file.close()
  # Print  message
  #print('Thank you for using the phone book.')
  return

# This function prints the menu, prompts the user for his/her selection
# and returns it. The function will prompt again and again
# until the user types 5 to quit.
def menu():
    while True:
        try:
            print('\n1. Add a Person\n')
            print('2. Delete a Person\n')
            print('3. Search for a Person\n')
            print('4. Update Information on a Person\n')
            print('5. Quit\n')
            num = int(input('Enter your selection: '))

            if num == 1:
                add_person ()
            elif num == 2:
                delete_person ()
            elif num == 3:
                search_person ()
            elif num == 4:
                update_person ()
            elif num == 5:
                return False
            else:
                raise ValueError
        except:
            print('This is an invalid selection. Please select again.')
    return

# This function opens the file for reading, reads the contact information
# for each person and adds it to the dictionary.
def create_phone_book():
  # Open file for reading
  in_file = open ("./phone.txt", "r")

  # Read first line (name)
  line = in_file.readline()
  line = line.strip()

  # Loop through the entries for each person
  while (line != ""):
    name = line

    # Read street
    line = in_file.readline()
    street = line.strip()
    # Read city
    line = in_file.readline()
    city = line.strip()
    # Read state
    line = in_file.readline()
    state = line.strip()
    # Read zip
    line = in_file.readline()
    zip = line.strip()
    # Read country
    line = in_file.readline()
    country = line.strip()
    # Read phone number
    line = in_file.readline()
    phone = line.strip()
    # Read e-mail address
    line = in_file.readline()
    email = line.strip()
    # Read blank line
    line = in_file.readline()
    blank = line
    # Read first line of the next block of data
    line = in_file.readline()
    line = line.strip()

    # Create ContactInfo object
    new_contact = ContactInfo (street, city, state, zip, country, phone, email)
    # Add to phone dictionary
    phone_book[name] = new_contact
  # Close file
  in_file.close()

def main():
  # Read file and create phone book dictionary
  create_phone_book()

  # Print logo
  print ("Phone Book")

  # Print menu and get selection
  selection = menu()

  # Save and quit
  save_quit ()
  # Goodbye message
  print ()
  print ("Thank you for using the Phone Book.\n")

# This line above main is for grading purposes. It will not affect how
# your code will run while you develop and test it.
# DO NOT REMOVE THE LINE ABOVE MAIN
if __name__ == "__main__":
  main()
