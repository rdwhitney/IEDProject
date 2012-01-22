import os
import sys
import Graph
import BattleManager

class Master:
    """Provides the start for the file"""
    
    def __init__(self, graphFile, inputFile, log):     
        self.input = inputFile
        self.log = log
        self.startPoint = None
        self.endPoint = None
        ## set up some type of file log
        (graphList,subMap_dict) = self.read_map(graphFile)
        self.myGraph = Graph.Graph(graphList,self.startPoint,self.endPoint)
        self.bm = BattleManager.BattleManager(self.myGraph, inputFile)
        return

    def read_input(self, inputFile):
        
        
        return

    def read_map(self, graphFile):
        """Reads the graph file and creates Map and subMap.
        
The graph file must follow the following format where the first line \
consists of "START: X Y" where X and Y are the x and y coordinates of \
the starting point with (0,0) being located at the bottom left corner.

Returns a tuple where the first item is a tuple representing a 
"""
        fileList = graphFile.read().split()

        if fileList[0] == 'START:' and fileList[3] =='END:':
            fileList.pop(0)
            fileList.pop(2)
        else:   ## Error
            sys.exit()

        self.startPoint = (int(fileList.pop(0)), int(fileList.pop(0)))
        self.endPoint = (int(fileList.pop(0)), int(fileList.pop(0)))
        
        ##  Read in the meta-Map
        graphList = []
        for i in range(len(fileList[0])):
            graphList.insert(0,fileList.pop(0))
        ##  Begining of Subgraph Reading
        subMap_dict = {}
        while True:
            if len(fileList) == 0:
                break
            cordKey = (int(fileList.pop(0)), int(fileList.pop(0)))
            subMap_dict[cordKey] = []
            for i in range(len(fileList[0])):
                subMap_dict[cordKey].insert(0,fileList.pop(0))
        graphFile.close()
        return graphList,subMap_dict

    def run(self):
        return

def main():
    print os.getcwd()
    if len(sys.argv) != 4:
        graph_name = 'map.inp'
        input_name = 'input.inp'
        log_name = 'log.out'
    else:
        graph_name = sys.argv[1]
        input_name = sys.argv[2]
        log_name = sys.argv[3]
    try:
        graph_file = open(graphName, 'r')
        input_file = open(inputName, 'r')
        log_file = open(logName, 'w')
        master = Master(graph_file, input_file, log_file)
    except:
        print 'Invalid Filenames'
        raw_input()

if __name__ == '__main__':
    main()