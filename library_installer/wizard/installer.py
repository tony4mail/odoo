# -*- coding: utf-8 -*-
##################################################
#                                                #
#    Cyb3rSky Corp. (A group for freelancers)    #
#    Copyright (C) 2021 onwards                  #
#                                                #
#    Email: cybersky25@gmail.com                 #
#                                                #
##################################################

from odoo import models, fields
import sys
import subprocess
from odoo.exceptions import UserError


class Installer(models.TransientModel):
    _name = "library_installer.installer"
    _description = "Python3 Library installer using"

    lib_data = fields.Text(
        help="Type the python libraries name separated by comma (,)")

    def install(self):

        lib_data = " ".join(self.lib_data.split(','))
        cmd = sys.executable + " -m pip install --upgrade --user " + lib_data

        ps = subprocess.Popen(cmd, shell=True)
        exitcode = ps.wait()

        if exitcode != 0:
            raise UserError(
                "Went into an error while installing one or more libraries. The following could be the reasons:\n1) Misspelled library name.\n2) Library version not availabe.\n3) Library not available.")
