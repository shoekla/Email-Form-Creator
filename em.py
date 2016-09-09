import math
def getForm(email):
	email = """ <form action="http://abirshukla.pythonanywhere.com/emailUser/" method="POST">
             <!-- Your Email -->
              <input type="hidden" name="to" value="""+str(email)+""">
                  <!-- Email of User -->
                    <input type="email" name="fromEmail" class="form-control" id="email" placeholder="E-mail" autocomplete="off">
 				<!-- Subject -->
                    <input type="text" name="sub" class="form-control" id="name" placeholder="Subject" autocomplete="off">
               <!-- Message -->
                  <textarea name="mess" class="form-control" rows="9" id="message" placeholder="Message"></textarea>
                  <button type="submit"> Send message </button>
                 <button type="reset">Clear</button>
            </form>
            """
	return email
"""
a = int(raw_input("Enter side a: "))
b = int(raw_input("Enter side b: "))
angle = float(raw_input("Enter angle: "))

c = (((a ** 2)+(b ** 2)-(2*a*b*math.cos(angle))) ** (.5))
print "C: "+str(c)
"""
numRows = int(raw_input("Enter number of rows: "))
lastRow = numRows +numRows -1
numStars = 1
half = (lastRow - 1)/2
for i in range(0,numRows):
	print( (half) * ' ' + numStars * '*' + (half) * ' ')
	numStars +=2
	half -=1



