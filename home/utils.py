from django.contrib.auth.tokens import PasswordResetTokenGenerator
from six import text_type
import uuid

def get_random_code():
	code = str(uuid.uuid4())[:8].replace('-', '').lower()
	return code

class AppTokenGenerator(PasswordResetTokenGenerator):
	
	def _make_hash_value(self, myuser, timestamp):
		return (text_type(myuser.is_active)+text_type(myuser.pk)+text_type(timestamp))	


token_generator	= AppTokenGenerator()	