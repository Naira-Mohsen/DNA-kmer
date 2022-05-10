

def count_imers(seq, i):
    counts = {}
    num_imers = len(seq) - i + 1 #num of k-mers
    for k in range(num_imers): #loop through k-mer list
        imer = seq[k:k+i]#num of chars in each k-mer

        if imer not in counts:
            counts[imer] = 0
        counts[imer] += 1
    return counts

def main():
	seq = input("Enter the genome sequence: ")
	i = int(input("Enter the value of i in i-mer: "))
	imers = count_imers(seq,i)
	print("Number of occurences of ",i,"-mers in the genome sequence: \n")
	print(imers)

	names = list(imers.keys())
	values = list(imers.values())




if __name__ == '__main__':
	main()