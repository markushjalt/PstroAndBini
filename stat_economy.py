import matplotlib.pyplot as plt

# Set variable values
dzw = 6142
dab = 6881
diesel = 8277
car_loan = 2137
car_insurance = 1461
car_service = 1148
car_summed = 14412
loan = 9116
electricity = 1492
other = 567
phones = 1716
house = 2117

# Household
labels_household = ['Cars', 'Loan', 'Elec.', 'Phones', 'House', 'Other']
size_household = [car_summed, loan, electricity, phones, house, other]
colors_household = ['blue', 'red', 'green', 'magenta', 'cyan', 'yellow']

# Cars 
labels_cars = ['DZW', 'DAB', 'Diesel', 'Loans', 'Insur.', 'Service']
size_cars = [dzw, dab, diesel, car_loan, car_insurance, car_service]
colors_cars = ['blue', 'red', 'green', 'magenta', 'cyan', 'yellow']

# S60 VS XC60
vs_label = 'DZW', 'DAB'
vs_cars = [dzw, dab]
colors_vs_cars = ['blue', 'red']

# Plot household
fig, (ax, axx) = plt.subplots(1,2)
fig.set_size_inches(13, 6)
ax.pie(size_household, labels = labels_household,  colors = colors_household, autopct = '%1.1f%%')
axx.bar(labels_household, size_household, color = colors_household)
axx.set_ylabel('kr', fontsize = 12)
fig.suptitle('Household Overview', fontsize = 14, fontweight = 'bold')

# Plot cars
fig2, (ax2, axx2) = plt.subplots(1,2)
fig2.set_size_inches(13, 6)
ax2.pie(size_cars, labels=labels_cars, colors = colors_cars, autopct = '%1.1f%%')
axx2.bar(labels_cars, size_cars, color = colors_cars)
axx2.set_ylabel('kr', fontsize = 12)
fig2.suptitle('Car Costs', fontsize = 14, fontweight = 'bold')

# Plot S60 vs XC60
fig3, (ax3, axx3) = plt.subplots(1,2)
fig3.set_size_inches(10, 6)
ax3.pie(vs_cars, labels=vs_label, colors = colors_vs_cars, autopct = '%1.1f%%')
axx3.bar(vs_label, vs_cars, color = colors_vs_cars)
axx3.set_ylabel('kr', fontsize = 12)
fig3.suptitle('S60 VS XC60', fontsize = 14, fontweight = 'bold')

fig4, axs = plt.subplots(2, 3)
fig4.set_size_inches(15, 7)
axs[0, 0].pie(size_household, labels = labels_household,  colors = colors_household, autopct = '%1.1f%%')
axs[0, 1].pie(size_cars, labels=labels_cars, colors = colors_cars, autopct = '%1.1f%%')
axs[0, 2].pie(vs_cars, labels=vs_label, colors = colors_vs_cars, autopct = '%1.1f%%')
axs[1, 0].bar(labels_household, size_household, color = colors_household)
axs[1, 1].bar(labels_cars, size_cars, color = colors_cars)
axs[1, 2].bar(vs_label, vs_cars, color = colors_vs_cars)
axs[1, 0].set_ylabel('kr', fontsize = 12)
axs[1, 1].set_ylabel('kr', fontsize = 12)
axs[1, 2].set_ylabel('kr', fontsize = 12)
axs[0, 0].set_title('Household Overview', fontsize = 14, fontweight = 'bold')
axs[0, 1].set_title('Cars Overview', fontsize = 14, fontweight = 'bold')
axs[0, 2].set_title('S60 VS XC60', fontsize = 14, fontweight = 'bold')
fig4.suptitle('Complete Overview', fontsize = 18, fontweight = 'bold')


plt.show()
