import hid

mouse = hid.device()

for device in hid.enumerate():
    if device["manufacturer_string"] == "SINOWEALTH" and device["product_string"] == "Wired Gaming Mouse" and device["product_id"] == 54:
        mouse.open(device["vendor_id"], device["product_id"])
        break

mouse.set_nonblocking(1)

while True:
    d = mouse.read(64)
    if d:
        print(d)
    else:
        break
