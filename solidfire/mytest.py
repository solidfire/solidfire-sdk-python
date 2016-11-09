from solidfire.factory import ElementFactory
from uuid import UUID
from solidfire.custom.models import CHAPSecret


ef = ElementFactory.create("10.117.60.15", "admin", "admin", version=9.0, port=442)

#print(ef.create_storage_container("name"))
print(ef.list_storage_containers())