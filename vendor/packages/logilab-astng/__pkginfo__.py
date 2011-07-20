# Copyright (c) 2003-2010 LOGILAB S.A. (Paris, FRANCE).
# http://www.logilab.fr/ -- mailto:contact@logilab.fr
#
# This program is free software; you can redistribute it and/or modify it under
# the terms of the GNU Lesser General Public License as published by the Free Software
# Foundation; either version 2 of the License, or (at your option) any later
# version.
#
# This program is distributed in the hope that it will be useful, but WITHOUT
# ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS
# FOR A PARTICULAR PURPOSE. See the GNU Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public License along with
# this program; if not, write to the Free Software Foundation, Inc.,
# 59 Temple Place - Suite 330, Boston, MA  02111-1307, USA.
# copyright 2003-2010 LOGILAB S.A. (Paris, FRANCE), all rights reserved.
# contact http://www.logilab.fr/ -- mailto:contact@logilab.fr
# copyright 2003-2010 Sylvain Thenault, all rights reserved.
# contact mailto:thenault@gmail.com
#
# This file is part of logilab-astng.
#
# logilab-astng is free software: you can redistribute it and/or modify it
# under the terms of the GNU Lesser General Public License as published by the
# Free Software Foundation, either version 2.1 of the License, or (at your
# option) any later version.
#
# logilab-astng is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or
# FITNESS FOR A PARTICULAR PURPOSE.  See the GNU Lesser General Public License
# for more details.
#
# You should have received a copy of the GNU Lesser General Public License along
# with logilab-astng. If not, see <http://www.gnu.org/licenses/>.
"""
logilab.astng packaging information

"""

distname = 'logilab-astng'

modname = 'astng'
subpackage_of = 'logilab'

numversion = (0, 20, 1)
version = '.'.join([str(num) for num in numversion])

install_requires = ['logilab-common >= 0.49.0']

pyversions = ["2.3", "2.4", "2.5", '2.6']

license = 'LGPL'

author = 'Logilab'
author_email = 'python-projects@lists.logilab.org'
mailinglist = "mailto://%s" % author_email
web = "http://www.logilab.org/project/%s" % distname
ftp = "ftp://ftp.logilab.org/pub/%s" % modname

short_desc = "rebuild a new abstract syntax tree from Python's ast"

long_desc = """The aim of this module is to provide a common base \
representation of python source code for projects such as pychecker, pyreverse,
pylint... Well, actually the development of this library is essentially
governed by pylint's needs.

It rebuilds the tree generated by the compiler.ast [1] module (python <= 2.4)
or by the builtin _ast module (python >= 2.5) by recursively walking down the
AST and building an extended ast (let's call it astng ;). The new node classes
have additional methods and attributes for different usages.
Furthermore, astng builds partial trees by inspecting living objects."""


from os.path import join
include_dirs = [join('test', 'regrtest_data'),
                join('test', 'data'), join('test', 'data2')]