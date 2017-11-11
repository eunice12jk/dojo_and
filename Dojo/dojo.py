
def start():
		arguments = docopt(__doc__)
		"""Creating an instance of DOJO"""


		create_room=arguments.get('create_room')
		add_person=arguments.get('add_person')
        print_room=arguments.get('print_room')