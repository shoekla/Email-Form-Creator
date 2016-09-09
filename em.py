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



