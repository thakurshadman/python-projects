#!/usr/bin/python3.6
#Shadman Thakur
from collections import deque
import sys


class Process:
    processNum = 1
    def __init__(self, ptype, size):
        self.pid = Process.processNum
        self.ptype = ptype 
        self.status = 'waiting'
        self.size = size
        self.startAddress = None
        self.endAddress = None
        Process.processNum += 1

class Memory:
    def __init__(self,capacity):
        self.totalSize = capacity
        self.freeSpace = capacity
        self.pcb = []

class HardDisk:
    def __init__(self):
        self.ioQueue = deque()
        
    def hdServe(self):  
        if self.ioQueue:
            self.ioQueue[0].status = 'serving'

    def hdInfo(self):
        for process in self.ioQueue:
            print(f'PID: {process.pid}    Status: {process.status}\n')

class CPUScheduler:
    def __init__(self,hdObjlist,memory):
        self.rtQueue = deque()
        self.comQueue = deque()
        self.hdList = hdObjlist
        self.memRef = memory

    def run(self):
        rtQempty = not self.rtQueue
        comQempty = not self.comQueue
        if rtQempty and not comQempty:
            self.comQueue[0].status = 'running'
        elif comQempty and not rtQempty:
            self.rtQueue[0].status = 'running'
        elif not rtQempty and not comQempty:
            self.comQueue[0].status = 'waiting' 
            self.rtQueue[0].status = 'running'

    def createPCB(self,process): #return bool 
        pcbEmpty = not self.memRef.pcb
        if pcbEmpty or process.size <= self.memRef.pcb[0].startAddress:
            self.memRef.pcb.insert(0,process)
            self.memRef.pcb[0].startAddress = 0 # 
            self.memRef.pcb[0].endAddress = process.size - 1
            self.memRef.freeSpace -= process.size 
            return  True
        elif not pcbEmpty: 
            for i in range(1,len(self.memRef.pcb)): 
                if (self.memRef.pcb[i].startAddress - (self.memRef.pcb[i-1].endAddress + 1)) >= process.size:
                    self.memRef.pcb.insert(i,process)
                    self.memRef.pcb[i].startAddress = self.memRef.pcb[i-1].endAddress + 1
                    self.memRef.pcb[i].endAddress = self.memRef.pcb[i].startAddress + (self.memRef.pcb[i].size - 1)
                    self.memRef.freeSpace -= process.size
                    return True
            if self.memRef.totalSize - (self.memRef.pcb[-1].endAddress + 1) >= process.size:
                         self.memRef.pcb.append(process)
                         self.memRef.pcb[-1].startAddress = self.memRef.pcb[-2].endAddress + 1
                         self.memRef.pcb[-1].endAddress = self.memRef.pcb[-1].startAddress + (self.memRef.pcb[-1].size - 1)
                         self.memRef.freeSpace -= process.size
                         return True
            else:
                print('ERROR:PROCESS SIZE TOO BIG FOR CURRENT STATE OF MEMORY\n')
                return False

    def rtProcessCreator(self,size): # AR size
        if size <= self.memRef.freeSpace and size > 0:
            process = Process('RT', size)
            if self.createPCB(process):
                self.rtQueue.append(process)
                self.run()
        else:
            print('ERROR:INVALID PROCESS SIZE  FOR CURRENT STATE OF MEMORY\n')

    def comProcessCreator(self,size): # A size
        if size <= self.memRef.freeSpace and size > 0:
            process = Process('common',size)
            if self.createPCB(process):
                self.comQueue.append(process)
                self.run()
        else:
            print('ERROR:INVALID PROCESS SIZE FOR CURRENT STATE OF MEMORY\n')

    def timesplice(self): # Q
        try:
            comQempty = not self.comQueue
            rtQempty = not self.rtQueue
            if not comQempty and rtQempty:
                if self.comQueue[0].status == 'running' :
                    self.comQueue.rotate(-1)
                    self.comQueue[-1].status = 'waiting'
            else:
                self.rtQueue.rotate(-1)
                self.rtQueue[-1].status = 'waiting'
            self.run()
        except IndexError:
            print('There\'s no running process!\n')
        
    def freePCB(self,PID):
        for process in self.memRef.pcb[:]:
            if process.pid == PID and process.status == 'terminated':
                self.memRef.freeSpace += process.size
                self.memRef.pcb.remove(process)
                break

    def terminate(self): # t
        try:
                if self.comQueue and not self.rtQueue:    
                    if self.comQueue[0].status == 'running' :
                        self.comQueue[0].status = 'terminated'
                        self.freePCB(self.comQueue[0].pid)
                        self.comQueue.popleft()
                else:
                    self.rtQueue[0].status = 'terminated'
                    self.freePCB(self.rtQueue[0].pid)
                    self.rtQueue.popleft()
                self.run()
        except IndexError:
            print('There\'s no running process!\n')

    def diskRequest(self, hdNum): # d number
        try:
            if self.comQueue and not self.rtQueue: 
                if self.comQueue[0].status == 'running' :
                    self.hdList[hdNum].ioQueue.append(self.comQueue[0])
                    self.comQueue[0].status = 'waiting'
                    self.comQueue.popleft() 
            else:
                self.hdList[hdNum].ioQueue.append(self.rtQueue[0])
                self.rtQueue[0].status = 'waiting'
                self.rtQueue.popleft()
            self.hdList[hdNum].hdServe()
            self.run()
        except IndexError:
            print(f'The request for HD number: {hdNum}  is invalid!\n')
        
    def  diskReqFinished(self,hdNum): # D number
        try:
            self.hdList[hdNum].ioQueue[0].status = 'waiting'
            if self.hdList[hdNum].ioQueue[0].ptype == 'common':
                self.comQueue.append(self.hdList[hdNum].ioQueue[0])
                self.hdList[hdNum].ioQueue.popleft()
            else:
                self.rtQueue.append(self.hdList[hdNum].ioQueue[0])
                self.hdList[hdNum].ioQueue.popleft()
            self.hdList[hdNum].hdServe()
            self.run()
        except IndexError:
            print(f'The request for HD number: {hdNum}  is invalid!\n')

    def stateOfMemory(self): # S m
        print(f'-------MEMORY STATUS------')
        print(f'Total Capacity: {self.memRef.totalSize} Bytes\n')
        print(f'Free Space: {self.memRef.freeSpace} Bytes\n')
        for process in self.memRef.pcb:
            print (f'PID: {process.pid}   Type: {process.ptype}   StartAddress: {process.startAddress}   EndAddress: {process.endAddress}\n')

    def hardDiskInfo(self): # S i
        for num,hd in enumerate(self.hdList):
            print(f'------HD: {num} I/O Queue------')
            hd.hdInfo()
         

    def cpuInfo(self): # S r
        print ('------RT Queue------')
        if self.rtQueue:# if not empty
            for process in self.rtQueue:
                print(f'PID: {process.pid}   Status: {process.status}\n')
        else:
            print('Queue is empty')
        print ('------Common Queue------')
        if self.comQueue: #if not empty
            for process in self.comQueue:
                print(f'PID: {process.pid}   Status: {process.status}\n')
        else:
            print('Queue is empty.')

def simulationInitializer():
    try:    
        mem = Memory(int(input('How much RAM memory is there on the simulated computer?\n')))
        hdnum = int(input('How many hard disks does the simulated computer have?\n'))
        listOfHDs = []
        for i in range(hdnum):
            listOfHDs.append(HardDisk())
        scheduler = CPUScheduler(listOfHDs,mem)
        while(True):
            args = input().split() 
            if args[0] == 'A':
                scheduler.comProcessCreator(int(args[1]))
            elif args[0] == 'AR':
                scheduler.rtProcessCreator(int(args[1]))
            elif args[0] == 'Q':
                scheduler.timesplice()
            elif args[0] == 't':
                scheduler.terminate()
            elif args[0] == 'd':
                scheduler.diskRequest(int(args[1]))
            elif args[0] == 'D':
                scheduler.diskReqFinished(int(args[1]))
            elif args[0] == 'S':
                if args[1] == 'r':
                    scheduler.cpuInfo()
                elif args[1] == 'i':
                    scheduler.hardDiskInfo()
                elif args[1] == 'm':
                    scheduler.stateOfMemory()
                else:
                    print('Invalid Input!\n')
            else:
                print('Invalid Input!\n')
    except ValueError:
        print('Invalid Input!\n')
    except IndexError:
        print('Invalid Input!\n')
    except KeyboardInterrupt:
        print('\nSimulation has ended!\n')
        sys.exit()
    
if __name__ == '__main__':
    simulationInitializer()




