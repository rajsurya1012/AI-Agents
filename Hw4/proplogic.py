import sat_interface

def tt2():
    '''
    Propositions:
        A: Amy is a truth-teller
        B: Bob is a truth-teller
        C: Cal is a truth-teller
        
        Amy says, "Cal and I are truthful."
        Bob says, "Cal is a liar."
        Cal says, "Bob speaks the truth or Amy lies."
        
    return a list containing all entailed propositions or negated propositions
    '''
    print("Truth-tellers and liars II")
    print("-------------------------")
    ttprob = sat_interface.KB(["~A C",
                               "~A A",
                               "~A ~C A",
                               "~B ~C",
                               "C B",
                               "~C B ~A",
                               "~B A C"])

    entailed = []
    if ttprob.test_literal("A") == False:
        entailed.append(False)
        print("Amy is a liar")
    if ttprob.test_literal("~A") == False:
        entailed.append(True)
        print("Amy is a truth-teller")
    if ttprob.test_literal("B") == False:
        entailed.append(False)
        print("Bob is a liar")
    if ttprob.test_literal("~B") == False:
        entailed.append(True)
        print("Bob is a truth-teller")
    if ttprob.test_literal("C") == False:
        entailed.append(False)
        print("Cal is a liar")
    if ttprob.test_literal("~C") == False:
        entailed.append(True)
        print("Cal is a truth-teller")
    print("-------------------------")
    return entailed

def tt3():
    '''
    Propositions:
        A: Amy is a truth-teller
        B: Bob is a truth-teller
        C: Cal is a truth-teller
        
        Amy says, "Cal is not honest."
        Bob says, "Amy and Cal never lie."
        Cal says, "Bob is correct."
        
    return a list containing all entailed propositions or negated propositions
    '''
    print("Truth-tellers and liars III")
    print("-------------------------")
    ttprob = sat_interface.KB(["~A ~C",
                               "C A",
                               "~B A",
                               "~B C",
                               "~A ~C B",
                               "~C B",
                               "~B C"])

    entailed = []
    if ttprob.test_literal("A") == False:
        entailed.append(False)
        print("Amy is a liar")
    if ttprob.test_literal("~A") == False:
        entailed.append(True)
        print("Amy is a truth-teller")
    if ttprob.test_literal("B") == False:
        entailed.append(False)
        print("Bob is a liar")
    if ttprob.test_literal("~B") == False:
        entailed.append(True)
        print("Bob is a truth-teller")
    if ttprob.test_literal("C") == False:
        entailed.append(False)
        print("Cal is a liar")
    if ttprob.test_literal("~C") == False:
        entailed.append(True)
        print("Cal is a truth-teller")
    print("-------------------------")
    return entailed

def salt():
    print("Salt")
    print("-------------------------")
    ttprob = sat_interface.KB(["~A Y",
                               "~Y A",
                               "~C ~Z",
                               "Z C",
                               "A B C",
                               "~A ~B ~C",
                               "~B A",
                               "~A B",
                               "~X ~Y",
                               "~Y ~Z",
                               "~Z ~X",
                               "X Y Z"])

    entailed = {}
    if ttprob.test_literal("A") == False:
        entailed["Caterpillar is truth teller (A)"]=False
        
    if ttprob.test_literal("~A") == False:
        entailed["Caterpillar is truth teller (A)"]=True
        
    if ttprob.test_literal("B") == False:
        entailed["Bill the Lizard is truth teller (B)"]=False
        
    if ttprob.test_literal("~B") == False:
        entailed["Bill the Lizard is truth teller (B)"]=True
        
    if ttprob.test_literal("C") == False:
        entailed["Cheshire Cat is truth teller (C)"]=False
        
    if ttprob.test_literal("~C") == False:
        entailed["Cheshire Cat is truth teller (C)"]=True
        
    if ttprob.test_literal("X") == False:
        entailed["Caterpillar stole the salt (X)"]=False
           
    if ttprob.test_literal("~X") == False:
        entailed["Caterpillar stole the salt (X)"]=True
        
    if ttprob.test_literal("Y") == False:
        entailed["Bill the Lizard stole the salt (Y)"]=False  
           
    if ttprob.test_literal("~Y") == False:
        entailed["Bill the Lizard stole the salt (Y)"]=True
        
    if ttprob.test_literal("Z") == False:
        entailed["Cheshire Cat stole the salt (Z)"]=False  
          
    if ttprob.test_literal("~Z") == False:
        entailed["Cheshire Cat stole the salt (Z)"]=True 
    print("-------------------------")
    return entailed

def golf():
    print("Golf")
    print("-------------------------")
    ttprob = sat_interface.KB(["~HA ~DA",
                               "~HA ~TA",
                               "~DA ~TA",
                               "DA HA TA",
                               "~HB ~DB",
                               "~HB ~TB",
                               "~DB ~TB",
                               "DB HB TB",
                               "~HC ~DC",
                               "~HC ~TC",
                               "~DC ~TC",
                               "DC HC TC",
                               "~HA ~HB",
                               "~HA ~HC",
                               "~HC ~HB",
                               "HA HB HC"
                               "~TA ~TB",
                               "~TA ~TC",
                               "~TB ~TC",
                               "TA TB TC",
                               "~DA ~DB",
                               "~DA ~DC",
                               "~DB ~DC",
                               "DA DB DC",
                               "~DA ~D HB",
                               "~DA D ~HB",
                               
                               "~DA ~D HB",    
                                "~DA D ~HB",    
                                "~TA HB",          
                                "~HA HB"
                                "~HA ~HB",   
                                "~DB D",        
                                "~TB",          
                                "~DC ~D TB",    
                                "~DC D ~TB",     
                                "~HC ~TB",    
                                "~TC TB",   
                                "~DC ~DA"
                                ])

    entailed = {} 
    if ttprob.test_literal("TA") == False:
        entailed["Tom is in first position (TA)"]=False  
    if ttprob.test_literal("~TA") == False:
        entailed["Tom is in first position (TA)"]=True
        
    if ttprob.test_literal("TB") == False:
        entailed["Tom is in second position (TB)"]=False  
    if ttprob.test_literal("~TB") == False:
        entailed["Tom is in second position (TB)"]=True
        
    if ttprob.test_literal("TC") == False:
        entailed["Tom is in third position (TC)"]=False   
    if ttprob.test_literal("~TC") == False:
        entailed["Tom is in third position (TC)"]=True
        
    if ttprob.test_literal("HA") == False:
        entailed["Harry is in first position (HA)"]=False   
    if ttprob.test_literal("~HA") == False:
        entailed["Harry is in first position (HA)"]=True  
        
    if ttprob.test_literal("HB") == False:
        entailed["Harry is in second position (HB)"]=False    
    if ttprob.test_literal("~HB") == False:
        entailed["Harry is in second position (HB)"]=True 
        
    if ttprob.test_literal("HC") == False:
        entailed["Harry is in third position (HC)"]=False    
    if ttprob.test_literal("~HC") == False:
        entailed["Harry is in third position (HC)"]=True 
        
    if ttprob.test_literal("DA") == False:
        entailed["Dick is in first position (DA)"]=False    
    if ttprob.test_literal("~DA") == False:
        entailed["Dick is in first position (DA)"]=True
        
    if ttprob.test_literal("DB") == False:
        entailed["Dick is in second position (DB)"]=False   
    if ttprob.test_literal("~DB") == False:
        entailed["Dick is in second position (DB)"]=True
        
    if ttprob.test_literal("DC") == False:
        entailed["Dick is in third position (DC)"]=False  
    if ttprob.test_literal("~DC") == False:
        entailed["Dick is in third position (DC)"]=True
        
    if ttprob.test_literal("D") == False:
        entailed["Dick is telling truth (D)"]=False   
    if ttprob.test_literal("~D") == False:
        entailed["Dick is telling truth (D)"]=True

    return entailed
def main():
    print(tt2())
    print(tt3())
    print(salt())
    print(golf())

if __name__ == '__main__':
    main()
