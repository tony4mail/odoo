# -*- coding: utf-8 -*-
##############################################################################
#
#    Jupical Technologies Pvt. Ltd.
#    Copyright (C) 2018-TODAY Jupical Technologies(<http://www.jupical.com>).
#    Author: Jupical Technologies Pvt. Ltd.(<http://www.jupical.com>)
#    you can modify it under the terms of the GNU LESSER
#    GENERAL PUBLIC LICENSE (LGPL v3), Version 3.
#
#    It is forbidden to publish, distribute, sublicense, or sell copies
#    of the Software or modified copies of the Software.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU LESSER GENERAL PUBLIC LICENSE (LGPL v3) for more details.
#
#    You should have received a copy of the GNU LESSER GENERAL PUBLIC LICENSE
#    GENERAL PUBLIC LICENSE (LGPL v3) along with this program.
#    If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

from odoo import models


class ProductTempExt(models.Model):

    _inherit = 'product.template'

    def clear_duplicates(self):
        unique_product = []  # list of set
        duplicate_products = []
        is_first = True
        for product in self:
            temp_unique_partners = unique_product.copy()
            if not unique_product:
                unique_product.append((product.id, product.default_code))
            if not is_first:
                for uni_pro in temp_unique_partners:
                    if product.default_code == uni_pro[1]:
                        duplicate_products.append(product.id)
                    else:
                        unique_product.append((product.id, product.default_code))
            is_first = False
        self.browse(list(dict.fromkeys(duplicate_products))).unlink()
