# ตัวอย่างโปรแกรม

### วิธีติดตั้ง

เปิด CMD / Terminal

```python
pip install testunclepim
```

### วิธีเล่น

เปิด IDLE ขึ้นมาแล้วพิมพ์...

```python
>>> import student
```
```python
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


ปล. ขออภัย version 0.1 ลุงใช้เวลาพัฒนาแค่คืนเดียว เลยไม่ได้สมบูรณ์จ้าาาา
ปล2. ใน Mac เล่นได้ แต่ฟังชั่นคีย์บอร์ดยังติดปัญหา ไฟล์ data.csv อยู่ใน /Users/ชื่อusername


