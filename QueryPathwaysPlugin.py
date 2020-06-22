import sys


class QueryPathwaysPlugin:
   def input(self, inputfile):
      params = open(inputfile, 'r')
      self.parameters = dict()
      for line in params:
         contents = line.strip().split('\t')
         self.parameters[contents[0]] = contents[1]
      self.mypathways = self.parameters['pathways']
      self.myquery = self.parameters['queryfile']

   def run(self):
      pathwaystuff = open(self.mypathways, 'r')
      self.bioelements = []
      self.pathways = []
      for line in pathwaystuff:
         myline = line.strip()
         pathway = myline[:myline.find('INVOLVES:')]
         myline = myline[myline.find('INVOLVES:')+10:]
         elements = myline.split('\t')
         while (elements.count('') != 0):
            elements.remove('')
         self.bioelements.append(elements)
         self.pathways.append(pathway)

      self.items = []
      querystuff = open(self.myquery, 'r')
      for line in querystuff:
         self.items.append(line.strip())

   def output(self, outputfile):
      outfile = open(outputfile, 'w')
      count = 0
      for i in range(0, len(self.bioelements)):
        if (self.items[0] in self.bioelements[i]):
           if (len(self.items) == 1 or self.items[1] in self.bioelements[i]):
              outfile.write("FOUND: "+self.pathways[i])
              outfile.write("     INVOLVES: "+str(self.bioelements[i])+"\n")
              found = True
              count += 1

      if (count == 0):
        print("NO MATCHING PATHWAYS FOUND.")
      else:
        print(count, "MATCHING PATHWAYS FOUND.")

      print("")
      print("")
