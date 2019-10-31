import random

### CREATE POPULATION

pop = []
print("pop: " + str(pop)) #shows you how the population is empty originally
random.seed()
popSize = 100000 #determine population size here
for i in range(popSize): #adds randomly created agents into the population
   agent = []
   fit = float("-inf")
   agent.append(fit) #sets first argument of agent/agent[0] to negative infinity so that this value can later be replaced by the fitness score and sorted using agent[0]!
   for j in range(2): #adds 2 arguments to the agent for x & y
      agent.append(random.uniform(-10, 10)) #random.uniform makes a list of random floating point numbers between (a,b)
   pop.append(agent) #adding the agent that was just created into the population
print("new pop: " + str(pop)) #shows you the new population without fitness scoring yet

### CREATE FUNCTION

def function(agent):
   x = agent[1]
   y = agent[2]
   return (x+(2*y)-7)**2 + ((2*x)+y-5)**2

### TESTING THE FUNCTION

print("pop[0]: " + str(pop[0])) #test: print out first agent in population
print("test output: " + str(function(pop[0]))) #test: evaluate first agent in pop by running the function on it

### EVOLUTION

for l in range(len(pop)): #this loops as many times as needed to reduce list to one argument

### FITNESS: EVALUATE FUNCTION ON POPULATION

   for k in range(len(pop)):
      pop[k][0] = function(pop[k]) #for agent determined by running a for loop to index into the population at k, the first index of the agent is assigned the value of the function being run on the agent at index k/pop[k]
   print("pop with new agent: " + str(pop))

### FITTEST: SORT POPULATION

   pop.sort() #sorts from least to greatest (based off of the first index of each agent which is also the fitness!
   #pop = pop[::-1] #flips the order of the list from greatest to least
   print("sorted pop: " + str(pop))

### SURVIVAL OF THE FITTEST: SLICING THE LIST

#taking out to test... for l in range(len(pop)): #so this loops through as many times as needed to reduce the list to one argument
   pop = pop[:len(pop)//2] #gets the population from index 0 to half the length
   print("sliced pop: " + str(pop))
   
### MUTATION: MODIFY THE AGENT ARGUMENTS

   mutationRate = .1 #modify rate of mutation here!
   for m in range(int(mutationRate*len(pop))):
      pop[random.randint(1,len(pop)-1)][random.randint(1,2)] += random.uniform(-10,10)
      ######## help how do i mutate it while keeping x and y within -10 and 10
      #argument at random index within an agent at a random index within population gets added or subtracted a number between -10 and 10
   print("mutated pop: " + str(pop))
   #tested in python terminal

### CROSSOVER: RANDOMLY SUFFLE AGENT ARGUMENTS WITH EACH OTHER

   babyList = []
   for n in range(1,len(pop)): #take the 1, out if problems
      baby = []
      baby.extend([pop[n][0],pop[n][1],pop[n][2]])
      print(baby)
      babyList.append(baby)
   pop = [pop[0]]
   pop.extend(babyList)
   print(pop)  
 
### MAXIMUM FOUND: STOP
   
   if len(pop) == 1: #stops when list found max
      break
print("function min: " + str(pop[0][0]))
