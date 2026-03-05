# Test for ExtendedCamelCase from FitLibrary
# Copyright 2004 Rick Mugridge, University of Auckland, NZ
# Released under the terms of the GNU General Public License version 2 or later.
# Python Translation Copyright 2005, John H. Roth Jr.

import unittest
import fitLib.ExtendedCamelCase
ExtendedCamelCase = fitLib.ExtendedCamelCase
def makeExtendedCamelCaseTest():
    theSuite = unittest.makeSuite(Test_ExtendedCamelCase, 'test')
#    theSuite.addTest(unittest.makeSuite(Test_FooBar, 'Test'))
    return theSuite

class Test_ExtendedCamelCase(unittest.TestCase):

    def check(self, input, out):
        self.assertEqual(out, ExtendedCamelCase.camel(input))

    
    def testJustCamel(self):
        self.check("two words","twoWords")
        self.check("three wee words", "threeWeeWords")

    def testExtendedCamel(self):
        self.check("\" hi \"","quoteHiQuote")
        self.check("!#$%age","bangHashDollarPercentAge")
        self.check("&'()*","ampersandSingleQuoteLeftParenthesisRightParenthesisStar")
        self.check("+,-./:","plusCommaMinusDotSlashColon")
        self.check(";=?","semicolonEqualsQuestion")
        self.check("@[]\\","atLeftSquareBracketRightSquareBracketBackslash")
        self.check("^`{}~","caretBackquoteLeftBraceRightBraceTilde")
        self.check("cost $","costDollar")
        self.check("cost$","costDollar")
        self.check("!","bang")
        self.check("!!","bangBang")
        self.check("meet @","meetAt")
        self.check("rick@mugridge.com","rickAtMugridgeDotCom")
        self.check("","blank")
        
    def testLeadingDigit(self):
        self.check("2 words","twoWords")

    def testPythonKeyword(self):
        self.check("return","return_")

    def testUnicode(self):
        self.check("\u216C","u216C")
        self.check("\u216D\uFFFE","u216DuFFFE")
        self.check("\uFFFF","uFFFF")
        self.check("\u0041b","Ab")

if __name__ == '__main__':
    unittest.main(defaultTest='makeExtendedCamelCaseTest')

