from sys import maxsize

from Utils.string_utils import clear_spaces, clear_spaces_and_hyphens as clear_all


class Contact:
    def __init__(self, first_name_value=None, middle_name_value=None, last_name_value=None, nickname_value=None,
                 title_value=None, company_value=None, address_value=None, home_phone_value=None,
                 mobile_phone_value=None, work_phone_value=None, fax_value=None, email_value=None,
                 email2_value=None, email3_value=None, homepage_value=None,
                 bday_value=None, bmonth_value=None, byear_value=None, aday_value=None,
                 amonth_value=None, ayear_value=None, secondary_address_value=None,
                 secondary_home_value=None, secondary_notes_value=None, contact_id_value=None,
                 all_phones_from_home_page_value=None, all_emails_from_home_page_value=None):
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
        self.all_phones_from_home_page = all_phones_from_home_page_value
        self.all_emails_from_home_page = all_emails_from_home_page_value

    def __repr__(self):
        return "%s:%s %s" % (self.contact_id, self.first_name, self.last_name)

    def __eq__(self, other):
        return (self.contact_id is None or other.contact_id is None or self.contact_id == other.contact_id) \
               and clear_all(self.first_name) == clear_all(other.first_name) and clear_all(self.last_name) == clear_all(
            other.last_name)

    def id_or_max(self):
        if self.contact_id:
            return int(self.contact_id)
        else:
            return maxsize

    def merge_emails_like_on_home_page(self, clear_hyphens):
        return "\n".join(filter(lambda x: x != "",
                                map(lambda x: clear_all(x) if clear_hyphens else clear_spaces(x),
                                    filter(lambda x: x is not None,
                                           [self.email, self.email2,
                                            self.email3]))))

    def merge_phones_like_on_home_page(self):
        return "\n".join(filter(lambda x: x != "",
                                map(lambda x: clear_all(x),
                                    filter(lambda x: x is not None,
                                           [self.home_phone, self.mobile_phone,
                                            self.work_phone, self.secondary_home]))))
