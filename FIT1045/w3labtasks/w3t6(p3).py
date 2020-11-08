#Name = Teo Wei Sheng
#Date = 22 March 2019
#Task 6: Tables and matrices
#Task6(3)

cols = ['Energy','Water','Protein','Carbs','Sugars','Fat','Fiber']
rows = ['Apple','Orange','Broccoli','Beef','Lamb','Bread']
nutr_vals = [[229, 84.3, 0.4, 12.0, 11.8, 0.0, 2.3],
             [186, 84.3, 1, 9.5, 8.3, 0.2, 2.1],
             [124, 89.6, 3.2, 2.0, 2.0, 0.1, 4.1],
             [613, 70, 22.8, 0.2, 0.0, 6.0, 0.0],
             [1057, 60.2, 18.6, 0.0, 0.0, 20.2, 0.0],
             [1446, 37.6, 8.4, 43.5, 1.5, 2.6, 6.9]]

my_list = [""]*6
final_list = []

count = 0

while count < 6:
    print(rows[count])
    my_list[count] = int(input("Please input the ammount of food(per 100g) that you have eaten: "))
    count += 1

for i in range(len(nutr_vals[0])):
    totalntr = 0
    for j in range(len(nutr_vals)):
        totalntr += (my_list[j])*(nutr_vals[j][i])
        if j == (len(nutr_vals)-1):
            final_list.append(totalntr)
            print("Ammount of", cols[i], "obtained is:", final_list[i])


    

