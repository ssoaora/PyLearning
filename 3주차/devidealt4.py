p = int(input('분자를 입력하시오: '))
q = int(input('분모를 입력하시오: '))

a = p / q
s = "나눗셈의 결과"

print("%s :  %E" % (s,a))
# %s 대신 %c 로 입력한다면 문자 하나의 형식변환자 이므로 오류가 난다
