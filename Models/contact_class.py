from sys import maxsize


class Contact:
    def __init__(self, first_name_value=None, middle_name_value=None, last_name_value=None, nickname_value=None,
                 title_value=None, company_value=None, address_value=None, home_phone_value=None,
                 mobile_phone_value=None, work_phone_value=None, fax_value=None, email_value=None,
                 email2_value=None, email3_value=None, homepage_value=None,
                 bday_value=None, bmonth_value=None, byear_value=None, aday_value=None,
                 amonth_value=None, ayear_value=None, secondary_address_value=None,
                 secondary_home_value=None, secondary_notes_value=None, contact_id_value=None):
        self.contact_id = contact_id_value
        self.first_name = first_name_value
        self.middle_name = middle_name_value
        self.last_name = last_name_value
        self.nickname = nickname_value
        self.title = title_value
        self.company = company_value
        self.address = address_value
        self.home_phone = home_phone_value
        self.mobile_phone = mobile_phone_value
        self.work_phone = work_phone_value
        self.fax = fax_value
        self.email = email_value
        self.email2 = email2_value
        self.email3 = email3_value
        self.homepage = homepage_value
        self.bday = bday_value
        self.bmonth = bmonth_value
        self.byear = byear_value
        self.aday = aday_value
        self.amonth = amonth_value
        self.ayear = ayear_value
        self.secondary_address = secondary_address_value
        self.secondary_home = secondary_home_value
        self.secondary_notes = secondary_notes_value

    def __repr__(self):
        return "%s:%s" % (self.contact_id, self.first_name)

    def __eq__(self, other):
        return self.contact_id is None or other.contact_id is None or self.contact_id == other.contact_id  # \
        # and self.first_name == other.first_name

    def id_or_max(self):
        if self.contact_id:
            return int(self.contact_id)
        else:
            return maxsize
