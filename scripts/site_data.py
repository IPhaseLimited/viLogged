#!/usr/bin/env python
# -*- coding: utf-8 -*-

# This file has been automatically generated.
# Instead of changing it, create a file called import_helper.py
# and put there a class called ImportHelper(object) in it.
#
# This class will be specially casted so that instead of extending object,
# it will actually extend the class BasicImportHelper()
#
# That means you just have to overload the methods you want to
# change, leaving the other ones inteact.
#
# Something that you might want to do is use transactions, for example.
#
# Also, don't forget to add the necessary Django imports.
#
# This file was generated with the following command:
# ./manage.py dumpscript core
#
# to restore it, run
# manage.py runscript module_name.this_script_name
#
# example: if manage.py is at ./manage.py
# and the script is at ./some_folder/some_script.py
# you must make sure ./some_folder/__init__.py exists
# and run  ./manage.py runscript some_folder.some_script

from django.db import transaction

class BasicImportHelper(object):

    def pre_import(self):
        pass

    # You probably want to uncomment on of these two lines
    # @transaction.atomic  # Django 1.6
    # @transaction.commit_on_success  # Django <1.6
    def run_import(self, import_data):
        import_data()

    def post_import(self):
        pass

    def locate_similar(self, current_object, search_data):
        # You will probably want to call this method from save_or_locate()
        # Example:
        #   new_obj = self.locate_similar(the_obj, {"national_id": the_obj.national_id } )

        the_obj = current_object.__class__.objects.get(**search_data)
        return the_obj

    def locate_object(self, original_class, original_pk_name, the_class, pk_name, pk_value, obj_content):
        # You may change this function to do specific lookup for specific objects
        #
        # original_class class of the django orm's object that needs to be located
        # original_pk_name the primary key of original_class
        # the_class      parent class of original_class which contains obj_content
        # pk_name        the primary key of original_class
        # pk_value       value of the primary_key
        # obj_content    content of the object which was not exported.
        #
        # You should use obj_content to locate the object on the target db
        #
        # An example where original_class and the_class are different is
        # when original_class is Farmer and the_class is Person. The table
        # may refer to a Farmer but you will actually need to locate Person
        # in order to instantiate that Farmer
        #
        # Example:
        #   if the_class == SurveyResultFormat or the_class == SurveyType or the_class == SurveyState:
        #       pk_name="name"
        #       pk_value=obj_content[pk_name]
        #   if the_class == StaffGroup:
        #       pk_value=8

        search_data = { pk_name: pk_value }
        the_obj = the_class.objects.get(**search_data)
        #print(the_obj)
        return the_obj


    def save_or_locate(self, the_obj):
        # Change this if you want to locate the object in the database
        try:
            the_obj.save()
        except:
            print("---------------")
            print("Error saving the following object:")
            print(the_obj.__class__)
            print(" ")
            print(the_obj.__dict__)
            print(" ")
            print(the_obj)
            print(" ")
            print("---------------")

            raise
        return the_obj


importer = None
try:
    import import_helper
    # We need this so ImportHelper can extend BasicImportHelper, although import_helper.py
    # has no knowlodge of this class
    importer = type("DynamicImportHelper", (import_helper.ImportHelper, BasicImportHelper ) , {} )()
except ImportError as e:
    if str(e) == "No module named import_helper":
        importer = BasicImportHelper()
    else:
        raise

import datetime
from decimal import Decimal
from django.contrib.contenttypes.models import ContentType

try:
    import dateutil.parser
except ImportError:
    print("Please install python-dateutil")
    sys.exit(os.EX_USAGE)

def run():
    importer.pre_import()
    importer.run_import(import_data)
    importer.post_import()

def import_data():
    # Initial Imports
    from django.contrib.auth.models import User

    # Processing model: CompanyDepartments

    from core.models import CompanyDepartments


    # Processing model: UserProfile

    from core.models import UserProfile


    # Processing model: CompanyEntranceNames

    from core.models import CompanyEntranceNames


    # Processing model: VisitorGroup

    from core.models import VisitorGroup


    # Processing model: Visitors

    from core.models import Visitors

    core_visitors_1 = Visitors()
    core_visitors_1.uuid = UUID('1732b8d060c311e496f7c9442a10d21e')
    core_visitors_1.created_at = dateutil.parser.parse("2014-10-31T06:00:04.707558+00:00")
    core_visitors_1.modified_at = dateutil.parser.parse("2014-10-31T09:33:27.386176+00:00")
    core_visitors_1.changed_by = None
    core_visitors_1.first_name = u'Barry'
    core_visitors_1.last_name = u'Abdullai'
    core_visitors_1.visitors_email = u'freefony@gmail.com'
    core_visitors_1.visitors_phone = u'08067886565'
    core_visitors_1.occupation = u''
    core_visitors_1.company_name = u''
    core_visitors_1.company_address = u''
    core_visitors_1.date_of_birth = dateutil.parser.parse("1984-10-19")
    core_visitors_1.nationality = u''
    core_visitors_1.state_of_origin = u'Ankpa'
    core_visitors_1.lga_of_origin = u''
    core_visitors_1.image_url = u''
    core_visitors_1.fingerprint = u''
    core_visitors_1.scanned_signature = u''
    core_visitors_1.visitors_pass_code = u''
    core_visitors_1.group_id = None
    core_visitors_1 = importer.save_or_locate(core_visitors_1)

    core_visitors_2 = Visitors()
    core_visitors_2.uuid = UUID('e3dd7a9e60ca11e496f7c9442a10d21e')
    core_visitors_2.created_at = dateutil.parser.parse("2014-10-31T06:56:53.707472+00:00")
    core_visitors_2.modified_at = dateutil.parser.parse("2014-10-31T06:56:53.707512+00:00")
    core_visitors_2.changed_by = None
    core_visitors_2.first_name = u'James'
    core_visitors_2.last_name = u'Olaide'
    core_visitors_2.visitors_email = u'dfreefony@gmail.com'
    core_visitors_2.visitors_phone = u'08067886500'
    core_visitors_2.occupation = u''
    core_visitors_2.company_name = u''
    core_visitors_2.company_address = u''
    core_visitors_2.date_of_birth = dateutil.parser.parse("1984-10-19")
    core_visitors_2.nationality = u''
    core_visitors_2.state_of_origin = u'Anambra'
    core_visitors_2.lga_of_origin = u''
    core_visitors_2.image_url = u''
    core_visitors_2.fingerprint = u''
    core_visitors_2.scanned_signature = u''
    core_visitors_2.visitors_pass_code = u''
    core_visitors_2.group_id = None
    core_visitors_2 = importer.save_or_locate(core_visitors_2)

    # Processing model: VisitorsLocation

    from core.models import VisitorsLocation

    core_visitorslocation_1 = VisitorsLocation()
    core_visitorslocation_1.uuid = UUID('23e1a23e60ce11e496f7c9442a10d21e')
    core_visitorslocation_1.created_at = dateutil.parser.parse("2014-10-31T07:19:09.935514+00:00")
    core_visitorslocation_1.modified_at = dateutil.parser.parse("2014-10-31T07:19:09.935561+00:00")
    core_visitorslocation_1.changed_by = None
    core_visitorslocation_1.visitor_id = core_visitors_1
    core_visitorslocation_1.state = u'Kano'
    core_visitorslocation_1.residential_lga = u'Ankpa'
    core_visitorslocation_1.contact_address = u'uuen iew oowew'
    core_visitorslocation_1 = importer.save_or_locate(core_visitorslocation_1)

    # Processing model: Appointments

    from core.models import Appointments

    core_appointments_1 = Appointments()
    core_appointments_1.uuid = UUID('0930b90648024a658516057bd839db3e')
    core_appointments_1.created_at = dateutil.parser.parse("2014-10-31T09:41:18.481527+00:00")
    core_appointments_1.modified_at = dateutil.parser.parse("2014-10-31T09:41:18.481574+00:00")
    core_appointments_1.changed_by = None
    core_appointments_1.visitor_id = core_visitors_2
    core_appointments_1.representing = u'Director General'
    core_appointments_1.purpose = u'Marketing'
    core_appointments_1.appointment_date = dateutil.parser.parse("2014-10-30")
    core_appointments_1.visit_start_time = datetime.time(3, 14, 16)
    core_appointments_1.visit_end_time = datetime.time(3, 14, 16)
    core_appointments_1.host_id =  importer.locate_object(User, "id", User, "id", 1, {'username': u'admin', 'first_name': u'', 'last_name': u'', 'is_active': True, 'id': 1, 'is_superuser': True, 'is_staff': True, 'last_login': datetime.datetime(2014, 10, 31, 0, 14, 36, 979798, tzinfo=<UTC>), 'password': u'pbkdf2_sha256$12000$wsEsuF97jGuC$wCLKdqZ53Bb7cc1Tkj0lFngSb5zlXAUHDm3dCqyv7tk=', 'email': u'admin@gmail.com', 'date_joined': datetime.datetime(2014, 10, 30, 17, 54, 33, 929285, tzinfo=<UTC>)} ) 
    core_appointments_1.escort_required = True
    core_appointments_1.is_approved = False
    core_appointments_1.is_expired = False
    core_appointments_1.checked_in = None
    core_appointments_1.checked_out = None
    core_appointments_1.label_code = u''
    core_appointments_1.entrance_id = None
    core_appointments_1 = importer.save_or_locate(core_appointments_1)

    core_appointments_2 = Appointments()
    core_appointments_2.uuid = UUID('24bd41474f60428788a296fe3938296e')
    core_appointments_2.created_at = dateutil.parser.parse("2014-10-31T09:46:06.137630+00:00")
    core_appointments_2.modified_at = dateutil.parser.parse("2014-10-31T09:46:06.137658+00:00")
    core_appointments_2.changed_by = None
    core_appointments_2.visitor_id = core_visitors_1
    core_appointments_2.representing = u'Himself'
    core_appointments_2.purpose = u'what do think'
    core_appointments_2.appointment_date = dateutil.parser.parse("2014-10-30")
    core_appointments_2.visit_start_time = datetime.time(4, 0)
    core_appointments_2.visit_end_time = datetime.time(5, 45, 36)
    core_appointments_2.host_id =  importer.locate_object(User, "id", User, "id", 1, {'username': u'admin', 'first_name': u'', 'last_name': u'', 'is_active': True, 'id': 1, 'is_superuser': True, 'is_staff': True, 'last_login': datetime.datetime(2014, 10, 31, 0, 14, 36, 979798, tzinfo=<UTC>), 'password': u'pbkdf2_sha256$12000$wsEsuF97jGuC$wCLKdqZ53Bb7cc1Tkj0lFngSb5zlXAUHDm3dCqyv7tk=', 'email': u'admin@gmail.com', 'date_joined': datetime.datetime(2014, 10, 30, 17, 54, 33, 929285, tzinfo=<UTC>)} ) 
    core_appointments_2.escort_required = True
    core_appointments_2.is_approved = False
    core_appointments_2.is_expired = False
    core_appointments_2.checked_in = None
    core_appointments_2.checked_out = None
    core_appointments_2.label_code = u''
    core_appointments_2.entrance_id = None
    core_appointments_2 = importer.save_or_locate(core_appointments_2)

    core_appointments_3 = Appointments()
    core_appointments_3.uuid = UUID('0930b90648024a688816057bd839db3e')
    core_appointments_3.created_at = dateutil.parser.parse("2014-10-31T15:17:09.542878+00:00")
    core_appointments_3.modified_at = dateutil.parser.parse("2014-10-31T15:17:09.542937+00:00")
    core_appointments_3.changed_by = None
    core_appointments_3.visitor_id = core_visitors_2
    core_appointments_3.representing = u'Director General'
    core_appointments_3.purpose = u'Marketing'
    core_appointments_3.appointment_date = dateutil.parser.parse("2014-10-30")
    core_appointments_3.visit_start_time = datetime.time(3, 14, 16)
    core_appointments_3.visit_end_time = datetime.time(3, 14, 16)
    core_appointments_3.host_id =  importer.locate_object(User, "id", User, "id", 1, {'username': u'admin', 'first_name': u'', 'last_name': u'', 'is_active': True, 'id': 1, 'is_superuser': True, 'is_staff': True, 'last_login': datetime.datetime(2014, 10, 31, 0, 14, 36, 979798, tzinfo=<UTC>), 'password': u'pbkdf2_sha256$12000$wsEsuF97jGuC$wCLKdqZ53Bb7cc1Tkj0lFngSb5zlXAUHDm3dCqyv7tk=', 'email': u'admin@gmail.com', 'date_joined': datetime.datetime(2014, 10, 30, 17, 54, 33, 929285, tzinfo=<UTC>)} ) 
    core_appointments_3.escort_required = True
    core_appointments_3.is_approved = False
    core_appointments_3.is_expired = False
    core_appointments_3.checked_in = None
    core_appointments_3.checked_out = None
    core_appointments_3.label_code = u''
    core_appointments_3.entrance_id = None
    core_appointments_3 = importer.save_or_locate(core_appointments_3)

    # Processing model: Vehicle

    from core.models import Vehicle


    # Processing model: MessageQueue

    from core.models import MessageQueue


    # Processing model: AppLicenseDuration

    from core.models import AppLicenseDuration


    # Processing model: RestrictedItems

    from core.models import RestrictedItems


