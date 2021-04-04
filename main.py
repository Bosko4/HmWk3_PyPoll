# First import two necessary modules for path (os) and data file (csv)
import os
import csv

#Create refernce path for data file
datapath=os.path.join('.','Resources','election_data.csv')

#open file using dynamic path (should work on Mac or Windows)
with open(datapath) as datafile:
    data = csv.reader(datafile, delimiter=',')
    
    # skip headers row 
    header = next(data)

    #create blank dictonary
    votetally = dict()
    votes = []
    #create variables
    totalvotes = int(0)
    votesfor = int(0)
    votepercent = float(0)
    hivotes = int(0)
    winner = str()


    #extract candidates receiving votes as seperate list
    
    for lines in data:
        votes.append(lines[2])
    #print(votes)

        #Loop thru votes counting results for each candidate into created dictonary
    for vote in votes:

        #count total number of votes 
        totalvotes = totalvotes +1
    
        if vote not in votetally:
                votetally[vote]=1
        else:
               votetally[vote] = votetally[vote]+1
    
    for k in votetally:
        votepercent = votetally[k]/totalvotes
        votetally[k]=(votetally[k],votepercent)         #<-- Had to get some help from BCS learning assistant after spinning my wheels going thru google. 
        
        votesfor = votetally[k][0]
        if votesfor > hivotes:
            hivotes = votesfor
            winner = k

    #Terminal output
    print("ELECTION RESULTS")
    print("------------------------------------------------------------")
    print(f"The total votes cast in the election were {totalvotes}.")
    print("------------------------------------------------------------")
    print()
    for k in votetally:
            print(k,votetally[k][0],"{0:.0%}".format(votetally[k][1]))  #<-- Had to do some googling to get the % formatting
    print("------------------------------------------------------------")
    print()
    print(f"The winner of the election was {winner} with {hivotes} votes received.")


#Create output text file
output_path = os.path.join('.','Analysis','Findings.txt')

#write to output summary text file
with open(output_path, 'w', newline='') as txtfile:
       
    txtfile.write("ELECTION RESULTS" +'\n')
    txtfile.write("------------------------------------------------------------" +'\n')
    txtfile.write(f"The total votes cast in the election were {totalvotes}." +'\n')
    txtfile.write("------------------------------------------------------------" +'\n')
    txtfile.write("" +'\n')
    txtfile.write(str(votetally) +'\n')
    txtfile.write("------------------------------------------------------------" +'\n')
    txtfile.write("" +'\n')
    txtfile.write(f"The winner of the election was {winner} with {hivotes} votes received." +'\n')
