#  -*- coding: utf-8 -*-
#################################################################################
#
#   Copyright (c) 2019-Present Webkul Software Pvt. Ltd. (<https://webkul.com/>)
#   See LICENSE URL <https://store.webkul.com/license.html/> for full copyright and licensing details.
#################################################################################

#################################################################################
{
  "name"                 :  "Website Coupons & Vouchers",
  "summary"              :  "The module allows you to create discount coupons and vouchers for Odoo website. The voucher code can be used by the customer to obtain discount on orders.",
  "category"             :  "Website",
  "version"              :  "6.0.1",
  "sequence"             :  1,
  "author"               :  "Webkul Software Pvt. Ltd.",
  "license"              :  "Other proprietary",
  "website"              :  "https://store.webkul.com/Odoo-Website-Voucher.html",
  "description"          :  """Odoo Website Coupons & Vouchers
Website coupons
Website vouchers
Voucher code
Coupon code
Manage vouchers
Discount coupons
Discount vouchers
Sale vouchers
Coupons & vouchers
POS discount sale
coupon discount
Give discount on Website
Website discount coupons
Odoo Website discount
Discount code Website""",
  "live_test_url"        :  "http://odoodemo.webkul.com/?module=website_voucher",
  "depends"              :  [
                             'wk_coupons',
                             'website_sale_delivery',
                            ],
  "data"                 :  [
                             'views/coupon_inherited_view.xml',
                             'views/templates.xml',
                             'views/inherited_sale_order_view.xml',
                             'wizard/voucher_wizard_view.xml',
                            ],
  "images"               :  ['static/description/Banner.png'],
  "application"          :  True,
  "installable"          :  True,
  "auto_install"         :  False,
  "price"                :  124,
  "currency"             :  "EUR",
  "pre_init_hook"        :  "pre_init_check",
}