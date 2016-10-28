from solidfire.factory import ElementFactory

ef = ElementFactory.create("10.117.61.40", "admin", "admin", version=8.0)

print(type(ef.get_cluster_hardware_info().cluster_hardware_info.drives["1"].uuid))