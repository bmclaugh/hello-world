a_list = [1,2,3, 'BEV', [5,6,7], 'WORD']
print a_list
print a_list[0]
#print a_list[len(a_list)]
print a_list[len(a_list)-1]
print a_list[:2]
print a_list[:-1]
print a_list[-1]
print a_list[-1][0]
a_string = 'RASHAD'
print a_string[-1]
print a_list.index('BEV')
a_list.reverse
print a_list
my_list = [ 1, 2.5 ,'BEV', [2,3,4]]
print my_list
print len(my_list)
my_list.append('RICHARD')
print my_list
my_list.remove('RICHARD')
print my_list
my_list[-1][1]
print my_list[-1][1]
print a_list + my_list
big_list = a_list + my_list
a_set = set([1, 'HEY', 1])
print a_set
my_set = {1,'BYE'}
print my_set
my_set.intersection(a_set)
print my_set.intersection(a_set)
if 'HEY' in a_set:
	print 'HEY'
new_list = set([1,2,3,4,5])
num_set = {2,4}
print new_list - num_set
print new_list | num_set
my_dictionary = {1: 'beverly', 2: 'bev', 3: 'b'}
for x, y in my_dictionary.items():
	print x, y
for x,y in my_dictionary.items():
	print x
for x,y in my_dictionary.items():
	print y
my_dictionary[4] = 'bam'
print my_dictionary
new_dictionary ={'T':'a', 'G': 'c', 'A':'t', 'C':'g'}
print new_dictionary
new_string = 'ACGTACAGATACAGATACAGATAGCAGATAGACATAGACATCAGT'
for x,y in new_dictionary.iteritems():
	print x, 'corresponds to' , y
	new_string = new_string.replace(x,y)
	print new_string

#print new_string.upper()


