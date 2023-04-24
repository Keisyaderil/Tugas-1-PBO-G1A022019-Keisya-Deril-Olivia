def apply_duakali(func,arg):
	return func(func(arg))

def tambah_lima(x):
	return x + 5

print(apply_duakali(tambah_lima, 10))
