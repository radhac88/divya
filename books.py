books = [{
	"name": None,
	"author": None,
	"read": None
},
	{
		
	}

]

def insert():
	print("Enter book name")
	b_name = input()
	books["name"] = b_name
	print("Enter author name")
	b_author = input()
	books["author"] = b_author
	print("Have you read the book Y/N")
	b_read = input()
	if b_read == "Y":
		books["read"] = True
	else:
		books["read"] = False

	return(books)



print("Select the action you want to perform")
print("1. Insert")
print("1. Delete")
print("1. Mark")
user_input = input()

if user_input == "insert" or "Insert":
	print(insert())

elif user_input == "Delete" or "delete":
	pass
	