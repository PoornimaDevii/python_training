
#python manage.py shell < updating,filter_db.py ( to run a file)
# python3 manage.py createsuperuser ( creating super user)

from myapp.models import Publisher

# p1 = Publisher(name='Addison-Wesley',address='5 Arlington St.',city='Boston',state_province='MA',country='USA',
#                website="http://www.addison-wesley.com/")
# p1.save()
#
# p2 = Publisher(name="O'Reilly", address='10Fawcett str', city='Cambridge', state_province='MA',
#                website='http://www.oreilly.com/')
# p2.save()
# publishers_list = Publisher.objects.all()
# print(publishers_list)
# print(Publisher.objects.filter(name="'O'Reilly"))
# print(Publisher.objects.filter(country='USA'))
# print(Publisher.objects.get(country='USA'))
# print(Publisher.objects.order_by('name'))
#

p1 = Publisher(name='wesley22',address='5 Arlington St.',city='Boston',state_province='MA',country='USA',
               website="http://www.addison-wesley.com/")
p1.save()









