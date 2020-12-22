class Student:
	def __init__(self,name):
		self.name = name
		self.exp = 0
		self.lesson = 0
		self.AddEXP(10)

	def Hello(self):
		print('สวัสดีจ้าาา ผมชื่อ{}'.format(self.name))

	def Coding(self):
		print('{} กำลังเขียนโปรแกรม'.format(self.name))
		self.exp += 5
		self.lesson += 1

	def ShowEXP(self):
		print('- {} มีประสบการณ์ {} EXP'.format(self.name,self.exp))
		print('- เรียนไป {} ครั้งแล้ว'.format(self.lesson))

	def AddEXP(self,score):
		self.exp += score
		self.lesson += 1
		

class SpecialStudent(Student):

	def __init__(self,name,farther):
		super().__init__(name)
		self.farther = farther
		mafia = ['Bill Gates','Thomas Edison']
		if farther in mafia:
			self.exp += 100

	def AddEXP(self,score):
		self.exp += (score*3)
		self.lesson += 1


	def Askexp(self,score=10):
		print('ขอเพิ่มคะแนน')
		self.AddEXP(score)



if __name__ == '__main__':
	print('======= 1 Jan 2020 =======')
	stname0 = SpecialStudent('Mark','Bill Gates')
	stname0.ShowEXP()

	stname1 = Student('Albert')
	print(stname1.name)
	stname1.Hello()
	print('-----------------')

	stname2 = Student('Steve')
	print(stname2.name)
	stname2.Hello()

	print('======= 2 Jan 2020 =======')
	print('-----Coding----get 10exp----')

	# stname1.exp += 10
	stname1.AddEXP(10)
	# stname1.lesson += 1


	print('======= 3 Jan 2020 =======')

	print('ตอนนี้ exp ของแต่ละคนมีเท่าไร')
	print(stname1.name,stname1.exp)
	print(stname2.name,stname2.exp)


	print('======= 4 Jan 2020 =======')

	for i in range(5):
		stname2.Coding()
	

	stname1.ShowEXP()
	stname2.ShowEXP()


