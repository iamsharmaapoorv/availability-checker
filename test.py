from profiles.profile import *
from clients.client import *
from subscriptions.subscription import *
from products.amazon_product import *
from products.shopatsc_product import *
from notifications.email_notification import EmailNotification

ps5_url = "https://www.amazon.in/Sony-CFI-1008A01R-PlayStation-5-console/dp/B08FV5GC28/ref=sr_1_1?crid=P99RKF8O9NCK&dchild=1&keywords=playstation+5&qid=1623180606&refinements=p_n_availability%3A1318485031&rnid=1318483031&sprefix=play%2Caps%2C333&sr=8-1"
ps5 = AmazonProduct(ps5_url)

test_url = "https://www.amazon.in/Certified-Protective-Bacterial-Filtration-Efficiency/dp/B08B1TVYT1/?_encoding=UTF8&pd_rd_w=teKY0&pf_rd_p=53d67038-493a-4b7a-bd3b-21b47bfb9ce1&pf_rd_r=ARH0P1YRPZYGNKCDE5X3&pd_rd_r=98ade321-5e29-4118-a8e4-624255b39191&pd_rd_wg=FxOzi&ref_=pd_gw_unk"
test = AmazonProduct(test_url)

ps5_subscription = Subscription(ps5, 1)
test_subscription = Subscription(test, 1)

ps5_subscription.add_notification(EmailNotification)
test_subscription.add_notification(EmailNotification)


ps5_shopatsc_url = 'https://shopatsc.com/collections/playstation-5/products/playstation-5-console-store'
test_shopatsc_url = 'https://shopatsc.com/products/ps4-1tb-gts-r-c-spiderman-ps-3m?variant=34152199389323'

ps5_shopatsc = ShopAtSCProduct(ps5_shopatsc_url)
test_shopatsc = ShopAtSCProduct(test_shopatsc_url)

ps5_shopatsc_subscription = Subscription(ps5_shopatsc, 1)
test_shopatsc_subscription = Subscription(test_shopatsc, 1)

ps5_shopatsc_subscription.add_notification(EmailNotification)
test_shopatsc_subscription.add_notification(EmailNotification)

apoorv = Client('Apoorv', "9629770677", 'appycoolme@gmail.com',  "110078")

apoorv_profile = Profile(apoorv)
apoorv_profile.add_subscription(ps5_subscription)
#apoorv_profile.add_subscription(test_subscription)
#apoorv_profile.add_subscription(ps5_shopatsc_subscription)
apoorv_profile.add_subscription(test_shopatsc_subscription)

apoorv_profile.ping()
