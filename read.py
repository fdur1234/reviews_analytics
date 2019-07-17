data = []
count = 0
with open('reviews.txt','r') as f:
	for line in f:
		data.append(line)
		count += 1 #count = count + 1
		#if count % 1000 == 0:
		    #print(len(data))# 'print' use time 
#print('檔案讀取完，總共有',len(data),'筆資料')

sum_len = 0
for d in data:
	sum_len = sum_len + len(d)
	
print('字元的平均長度是', sum_len / len(data))

#篩選清單
new = []
for d in data:
	if len(d) < 100:
		new. append(d)
print('一共有', len(new), '長度小於100')
print(new[0])
print(new[1])

print(len(new[0]))

print('第一筆小於100的資料有', len(new[0]), '個字元')

#
good = []
for d in data:
	if 'good' in d:
		good.append(d)
print('總共有', len(good), '筆資料提到good')

# 清單快寫法
good = [d for d in data if 'good' in d]


bad = ['bad' in d for d in data if 'bad' in d]
print(len(bad))










