from sys import maxsize


class Contact:
    def __init__(self, firstname=None, middlename=None, lastname=None, nickname=None, photo=None, title=None,
                 company=None, address=None, home=None, mobile=None, work=None, fax=None, email=None,
                 email2=None, email3=None, homepage=None, bday=None, bmonth=None, byear=None, aday=None, amonth=None,
                 ayear=None, address2=None, phone2=None, notes=None, id=None, all_phones_from_home_page=None,
                 all_emails_from_home_page=None):
        self.firstname = firstname
        self.middlename = middlename
        self.lastname = lastname
        self.nickname = nickname
        self.photo = photo
        self.title = title
        self.company = company
        self.address = address
        self.home = home
        self.mobile = mobile
        self.work = work
        self.fax = fax
        self.email = email
        self.email2 = email2
        self.email3 = email3
        self.homepage = homepage
        self.bday = bday
        self.bmonth = bmonth
        self.byear = byear
        self.aday = aday
        self.amonth = amonth
        self.ayear = ayear
        self.address2 = address2
        self.phone2 = phone2
        self.notes = notes
        self.id = id
        self.all_phones_from_home_page = all_phones_from_home_page
        self.all_emails_from_home_page = all_emails_from_home_page

    def __repr__(self):
        return "%s:%s:%s" % (self.id, self.firstname, self.lastname)

    def __eq__(self, other):
        return (self.id is None or other.id is None or self.id == other.id) and \
            (self.firstname is None or other.firstname is None or self.firstname == other.firstname) and \
            (self.middlename is None or other.middlename is None or self.middlename == other.middlename) and \
            (self.lastname is None or other.lastname is None or self.lastname == other.lastname) and \
            (self.nickname is None or other.nickname is None or self.nickname == other.nickname) and \
            (self.photo is None or other.photo is None or self.photo == other.photo) and \
            (self.title is None or other.title is None or self.title == other.title) and \
            (self.company is None or other.company is None or self.company == other.company) and \
            (self.address is None or other.address is None or self.address == other.address) and \
            (self.home is None or other.home is None or self.home == other.home) and \
            (self.mobile is None or other.mobile is None or self.mobile == other.mobile) and \
            (self.work is None or other.work is None or self.work == other.work) and \
            (self.fax is None or other.fax is None or self.fax == other.fax) and \
            (self.email is None or other.email is None or self.email == other.email) and \
            (self.email2 is None or other.email2 is None or self.email2 == other.email2) and \
            (self.email3 is None or other.email3 is None or self.email3 == other.email3) and \
            (self.homepage is None or other.homepage is None or self.homepage == other.homepage) and \
            (self.bday is None or other.bday is None or self.bday == other.bday) and \
            (self.bmonth is None or other.bmonth is None or self.bmonth == other.bmonth) and \
            (self.byear is None or other.byear is None or self.byear == other.byear) and \
            (self.aday is None or other.aday is None or self.aday == other.aday) and \
            (self.amonth is None or other.amonth is None or self.amonth == other.amonth) and \
            (self.ayear is None or other.ayear is None or self.ayear == other.ayear) and \
            (self.address2 is None or other.address2 is None or self.address2 == other.address2) and \
            (self.phone2 is None or other.phone2 is None or self.email2 == other.phone2) and \
            (self.notes is None or other.notes is None or self.email2 == other.notes)

    def id_or_max(self):
            if self.id:
                return int(self.id)
            else:
                return maxsize
