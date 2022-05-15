n = int(input())
lists = list(map(int, input().split()))
print('ss')

all_list = []
left_list = []
for i in [1,3,5,7,9]:
	all_list.append(lists[:].count(i))
	left_list.append(lists[:len(lists)//2].count(i))


def checker(idx): #else용
	global lists
	cc=0
	for i in [0,2,4,6,8]:
		# try:
		# 	if lists[:idx].index(i) != ValueError:
		# 		return True
		# except:
		# 	return False
		try:
			if lists[:idx].index(i) != ValueError:
				return True
		except:
			cc+=1
	if cc==5:
		return False
def checker2(idx): #if용
	global lists
	for i in [0,2,4,6,8]:
		if lists[:idx].index(i) != ValueError:
			return True
	else:
		return False


def rchecker(idx): #else용 짝수용
	global lists
	cc=0
	for i in [1,3,5,7,9]:
		try:
			if lists[idx:].index(i) != ValueError:
				return True
		except:
			cc+=1
	if cc==5:
		return False
		
def rchecker2(idx): #if용
	global lists
	for i in [1,3,5,7,9]:
		if lists[idx:].index(i) != ValueError:
			return True
	else:
		return False

cnt = 0
# print('ss')
if sum(all_list)-sum(left_list) > sum(left_list): #오른쪽에 홀수가 더 많을 때
	hol_yang = sum(all_list)
	jjack_yang = len(lists) - hol_yang
	# print('startif')
	while checker2(hol_yang):
		for i in [0,2,4,6,8]:
			try:
			# if lists[:hol_yang].rindex(i) == None:
			# 	continue
			# else:
				iidx = lists[:hol_yang].rindex(i)
				lists[iidx], lists[iidx+1] = lists[iidx+1], lists[iidx]
				cnt +=1
				continue
			except:
				continue
	while rchecker2(jjack_yang):
		for i in [1,3,5,7,9]:
			try:
			# if lists[jjack_yang:].index(i) == None:
			# 	continue
			# else:
				iidx = lists[jjack_yang:].index(i)
				lists[iidx], lists[iidx-1] = lists[iidx-1], lists[iidx]
				cnt +=1
				continue
			except:
				continue

else: #왼쪽에 홀수가 더 많을 때
	hol_yang = sum(all_list)
	# jjack_yang = len(lists)-hol_yang
	# print('startelse')
	while checker(hol_yang):
		for i in [0,2,4,6,8]:
			try:
			# 	if lists[hol_yang:].index(i) == None:
			# 		continue
			# else:
				iidx = lists[hol_yang:].index(i)
				lists[iidx], lists[iidx-1] = lists[iidx-1], lists[iidx]
				cnt +=1
				continue
			except:
				continue
	# print('jjackfin')
	while rchecker(hol_yang):
		for i in [1,3,5,7,9]:
			try:
			# if lists[:jjack_yang].rindex(i) == None:
			# 	continue
			# else:
				iidx = lists[:jjack_yang].rindex(i)
				lists[iidx], lists[iidx+1] = lists[iidx+1], lists[iidx]
				cnt +=1
				continue
			except:
				continue
print(cnt)