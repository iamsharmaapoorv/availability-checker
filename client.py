import re
from exceptions import AvailabilityCheckerException


class Client:
    def __init__(self, name, mobile, email, pincode):
        self.name = name
        self.mobile = mobile
        self.email = email
        self.pincode = pincode

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name

    @property
    def mobile(self):
        return self._mobile

    @mobile.setter
    def mobile(self, mobile_number):
        mobile_pattern = re.compile('[6-9]\d{9}')
        if mobile_pattern.match(mobile_number):
            self._mobile = mobile_number
        else:
            raise AvailabilityCheckerException("Invalid mobile number.")

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, email_id):
        email_pattern = re.compile(
            '^(\w|\.|\_|\-)+[@](\w|\_|\-|\.)+[.]\w{2,3}$')
        if email_pattern.match(email_id):
            self._email = email_id
        else:
            raise AvailabilityCheckerException("Invalid Email ID.")

    @property
    def pincode(self):
        return self._pincode

    @pincode.setter
    def pincode(self, pincode_candidate):
        pincode_pattern = re.compile('\d{6}')
        if re.match(pincode_pattern, pincode_candidate):
            self._pincode = pincode_candidate
        else:
            raise AvailabilityCheckerException("Invalid pincode.")
