""" Program that calculates the Net Present Value (NPV) of a bond.
the bond can be a zero coupon bond (offered at a discount) or 
a bond offering a coupon annually/semi-annually. """

def bond_npv(coupon,par, time, ty, rate):

	""" this function calculates the NPV of the bond. It takes in the following arguments;
	coupon --> amount that will be paid to the buyer either annually or semi-annually.
	         we will be providing the coupon rate and then calculating the amount based on the face value.
	time --> This is the number of years to the maturiity of the bond.
	ty --> This will be used to show if the coupon payments are annual or semi-annual. The value is either 1...
	         for annual payments bonds or 0 for semi-annual payments
	par --> this is the face value of the bond. 
	rate --> prevailing interest rate of the bond.
	"""

	#initializing payment periods
	payment_periods = 0

	#Initializing the sum of all coupon payments discounted with the prevailing interest rate.
	coupons = 0

	if (ty == 1):
		payment_periods = int(time)
		cpn = coupon 

	else:
		payment_periods = int(time*2)
		cpn = coupon/2

	for i in range(1,payment_periods+1):
		value = ((cpn/100)*par) / ((1+(rate/100))**i)
		coupons = coupons + value
	#Calculating the npv of the face value of the bond.
	par_npv = par / ((1+(rate/100))**payment_periods)

	Net_Present_Value = coupons + par_npv

	return int(Net_Present_Value)



def mc_duration(coupon, par, time, ty, rate):
	""" this function is used to calculate the Macaulay Duration of a bond. 
	This shows how the price of a bond changes given a change in interest rates.
	Duration is measured in years, so it doesn't directly measure the change in bond prices...
	with respect to change in yield.

	This function takes in the same arguments as the bond_npv() function """

	# getting the price of the bond.
	price = bond_npv(coupon, par, time, ty, rate)

	#initializing payment periods
	payment_periods = 0
	

	#Initializing the sum of all coupon payments discounted with the prevailing interest rate.
	# The coupons will be time weighted, same with the present value of the face value of the bond.
	coupons = 0

	if (ty == 1):
		payment_periods = int(time)
		cpn = coupon

	else:
		payment_periods = int(time*2)
		cpn = coupon/2

	for i in range(1,payment_periods+1):
		value = ((cpn/100)*par) / ((1+(rate/100))**i)
		time_weighted = value*i
		coupons = coupons + time_weighted
	#Calculating the time weigthed npv of the face value of the bond.
	par_npv = (par / ((1+(rate/100))**payment_periods))
	tw = par_npv * payment_periods

	duration = (coupons + tw)/ price
	return duration


def mod_duration(coupon, par, time, ty, rate):
	""" this function is used to calculate the modified duration of a bond.
	unlike the macaulay duration which is in years, the modified duration shows how sensitive 
	bond prices are to changes in their yield/interest rates. """

	# getting the macaulay duration.
	md = mc_duration(coupon,par,time,ty,rate)

	# calculating the modified duration
	duration = md/(1+(rate/100))

	return duration # Expressed in % terms


def change_in_prices(coupon,par,time,ty,rate,y):
	"""Shows the % change in prices given the change in the interest rate.
	Arguments:
	y--> change in the interest rates. 
	"""
	#getting modified duration

	md = mod_duration(coupon,par,time,ty,rate)

	db = -1*md*(-y/100)
	return db*100 # change in bond prices


bbb = change_in_prices(8,1000,10,1,7.25,0.8)
print(bbb)







