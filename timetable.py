import csp
import pandas as pd
import time
from utils import F 

#_____________________________________________________________________________________
#

class Timetable(csp.CSP):
    
    def __init__(self, df):
        self.variables = []
        self.full_var = dict()
        self.domains = dict()
        self.neighbors = dict()

        self.counter = 0  #metraei tis fores pou kaleitai h var_constraints


        #take from csv file all the info
        for i in range(50):   #estw oti to arxeio exei mexri 50 grammes
            a = csv_returner(i, df)
            if a!=None:
                self.variables.append((a[1]))     #san variables pernaw to onoma kathe mathimatos
                self.full_var[a[1]]= a              #sto full_var exei key to onoma kai values mia lista me ola ta periexomena ths grammhs
            else:
                break

        #ta domains einai tis morfis x,y opou x=1,2,3 gia ta slots kai y=1,...,21 gia tis hmeres  
        for var in self.variables:
            self.domains[var]=[]
            for y in range(1,22):
                for x in range(1,4):
                    self.domains[var].append((x,y))

        #efoson kathe slot prepei na exei mono ena mathima ola ta mathimata exoun neighbors ola ta ypoloipa
        for var in self.variables:
            self.neighbors[var]=[]
            for varx in self.variables:
                if varx!=var:
                    self.neighbors[var].append(varx)
        

        csp.CSP.__init__(self,self.variables, self.domains, self.neighbors, self.var_constraints)

    def var_constraints(self, A, a, B, b):
        self.counter+=1
        #se ena slot mono ena mathima
        if a==b:
            return False
        #mathimata toy idiou etous se diaforetikh hmera
        if a[1]==b[1] and self.full_var[A][0]==self.full_var[B][0]:
            return False
        #ta dyskola mathimata se diaforetikh hmera 
        if a[1]==b[1] and self.full_var[A][3]==True and self.full_var[B][3]==True:
            return False
        #an ena apo ta dyo mathimata exei argasthrio:
        if a[1]==b[1] and (self.full_var[A][4]==True or self.full_var[B][4]==True):
            #an einai kai ta dyo dyskola apagoreuontai na einai thn idia mera
            if self.full_var[A][3]==True and self.full_var[B][3]==True:
                return  False
            #an exoun kai ta dyo ergasthrio den mporoun na xwresoun se mia hmera me 3 slots
            if self.full_var[A][4]==True and self.full_var[B][4]==True:
                return False
            #an to A exei to ergasthrio
            if self.full_var[A][4]==True:
                i=0
            #an to B exei to ergasthrio
            if self.full_var[B][4]==True:
                i=-1
            if i==0:
                if a[0]==3:   #an einai sto 3o slot den xwraei to ergasthrio na mpei
                    return False
                elif b[0]!=a[0]+1:
                    return True
                else:
                    return False
            elif i==-1:
                if b[0]==3:  
                    return False
                elif a[0]!=b[0]+1:
                    return True
                else:
                    return False                    

        #ta mathimata toy idioy kathigiti se diaforetikh hmera
        if a[1]==b[1] and self.full_var[A][2]==self.full_var[B][2]:
            return False
        #ta dyskola mathimata prepei na apexoyn toulaxiston dyo meres metaksi toys
        if a[1]!=b[1] and self.full_var[A][3]==True and self.full_var[B][3]==True:
                if a[1]<=b[1]-2 or b[1]<=a[1]-2:
                    return True
                else:
                    return False   
        
        return True

    def display_all(self, assignment):
        print("Τhe result is: ")
        if assignment==None:
            print("the limit has been passed")
        else:

            for y in range(1,22):
                for x in range(1,4):
                    for var in self.variables:
                        if assignment[var] == (x,y):
                            if x==1:
                                print("+","--"*len(var), end=' +')
                                print()
                            print('|', assignment[var], var,  end=' |')
                            print()
                            if self.full_var[var][4]==True:
                                print('|', (x+1,y),var+' LAB', end=' |')
                                print()


            print("+","-"*50, "+")


#_________________________________________________________________________________
#

def csv_returner(line, df):    #bazoyme thn grammh toy arxeiou poy theloyme na epistrepsoyme
    line_list =[]
    dict_of_classes = df.to_dict('list')
    keys_tuple = tuple(dict_of_classes.keys())
    for k, v in dict_of_classes.items():
        for i in range(len(keys_tuple)):
            if k == keys_tuple[i]:
                u = tuple(v)            
                if line<len(u):     #check if file ended
                    line_list.append(u[line])
                else:
                    return None 
    return line_list               #return thn lista me ola ta periexomena ths grammhs

#_________________________________________________________________________________
#   main

if __name__ == '__main__':
    df = pd.read_csv('Στοιχεία Μαθημάτων.csv')  #edw bazoume to onoma tou arxeioy csv poy theloyme na diabasoume
    k = Timetable(df)


    begin = time.time()


    
    #m = csp.backtracking_search(k, csp.mrv, csp.lcv, csp.mac)
    
    #m = csp.backtracking_search(k, csp.dom_wdeg, csp.lcv, csp.mac)

    #m=csp.backtracking_search(k, csp.mrv, csp.lcv, csp.forward_checking)

    
    m=csp.backtracking_search(k, csp.dom_wdeg, csp.lcv, csp.forward_checking)
    
    
    #m=csp.backtracking_search(k)

    #m=csp.backtracking_search(k , csp.mrv)

    #m=csp.min_conflicts(k)

    end=time.time()

    k.display_all(m)
    print("number of times var_costrain function: "+str(k.counter))
    print()
    print("the total time is: "+str(end-begin) )
    print()
    print("the total number of assignments is: "+str(k.nassigns))

    

#https://pynative.com/convert-pandas-dataframe-to-dict/