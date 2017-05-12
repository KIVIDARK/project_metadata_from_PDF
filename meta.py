class PdfMetaData(object):
    def __init__(self, filename):
        self.file = open(filename, 'rb')
        self.result = None
        self.module_checker(ppars=True)
        self.parser = self.PPars(self.file)

    def module_checker(self, ppars=None, pdoc=None):
        if ppars:
            self.PPars = None
            from pdfminer.pdfparser import PDFParser as pars
            self.PPars = pars
        if pdoc:
            self.PDoc = None
            from pdfminer.pdfdocument import PDFDocument as pdoc
            self.PDoc = pdoc

    def parse(self):
        self.module_checker(pdoc=True)
        self.result = self.PDoc(self.parser)
        result_dict = self.result.info[0]
        for key in result_dict.keys():
            print "%s: %s" % (key, result_dict[key])

if __name__ == "__main__":
    pd = PdfMetaData('file.pdf')
    print pd.parse()

