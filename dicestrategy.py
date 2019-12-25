def find_the_best_dice(dices):
	# you need to use range (height-1)
	height=len(dices)
	dice=[0]*height
	#print(dice)
	for i in range(height-1):
		#print("this is dice number ",i+1)
		# use height
		for j in range(i+1,height):
			#print("comparing dice number ",i+1," with dice number ",j+1)
			check1=0
			check2=0
			for element1 in dices[i]:
				for element2 in dices[j]:
					if element1>element2:
						check1=check1+1
					elif element2>element1: 
						check2=check2+1
					else:
						continue		
			if check1>check2:
				print("the dice number ",i+1,"is better than dice number ",j+1)
				dice[i]=dice[i]+1
			else:
				print("the dice number ",j+1,"is better than dice number ",i+1)
				dice[j]=dice[j]+1
	print(dice)
	maxelement=max(dice)
	maxindex=dice.index(max(dice))
	for i in range(len(dice)):
		if i != maxindex:
			if dice[i]==maxelement:
				return -1
	return maxindex	

dices=[[1, 2, 3, 4, 5, 6], [1, 1, 2, 4, 5, 7], [1, 2, 2, 3, 4, 7]]
print(find_the_best_dice(dices))
