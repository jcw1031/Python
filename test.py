guest_book="""김갑,123456789
이을,010-1234-5678
박병,010-5678-111
최은정,111-1111-1111
정무,010-3333-3333"""

guest_book = guest_book.replace('\n', ',')
a = guest_book.split(',')

name = list()
call=list()

for i in range(0, len(a)):
    if i%2==0:
        name.append(a[i])
    else:
        call.append(a[i])

wrong_guest = list()
for i in range(0, len(call)):
    tmp = call[i].split('-')
    if len(tmp)!=3 or tmp[0] != "010" or len(tmp[1])!=4 or len(tmp[2])!=4 :
        wrong_guest.append(i)

for i in wrong_guest:
    print("잘못 쓴 사람 : "+name[i])
    print("잘못 쓴 번호 : "+call[i]+"\n")