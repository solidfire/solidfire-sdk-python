from solidfire.factory import ElementFactory
from uuid import UUID
from solidfire.custom.models import CHAPSecret


ef = ElementFactory.create("10.117.61.40", "admin", "admin", version=9.0)

print(ef.get_storage_conatiners())
