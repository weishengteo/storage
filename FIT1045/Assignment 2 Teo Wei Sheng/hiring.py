#Name = Teo Wei Sheng
#Student ID = 29800668
#Date = 24 April 2019
#Assignment 2
#Task 1: Talent Acquisition

jess = (["php", "java"], 200)
clark = (["php", "c++", "go"], 1000)
john = (["lua"], 500)
cindy = (["php", "go", "word"], 240)

candidates = [jess, clark, john, cindy]
project = ["php", "java", "c++", "lua","go"]



def cost(candidates):
    cost = 0
    for i in candidates:
        cost = cost + i[-1]
    return cost

def skills(candidates):
    skill = []
    tskill = []
    for i in candidates:
        tskill = i[0]
        for j in tskill:
            if j not in skill:
                skill.append(j)
    return skill

def uncovered(project, skills):
    uncov = []
    for i in project:
        if i not in skills:
            uncov.append(i)
    return uncov

def best_individual_candidate(project, candidates):
    skillpd = []
    for i in candidates:
        slength = 0
        for j in range(len(i[0])):
            if i[0][j] in project:
                slength = slength + 1
        skillpd.append(slength/i[1])

    return(skillpd.index(max(skillpd)))

def team_of_best_individuals(project, candidates):
    bestc = []
    lengthp = len(project)
    
    while len(project) != 0:
        covered = 0
        cand = best_individual_candidate(project, candidates)
        cskill = skills([candidates[cand]])
        ucproject = uncovered(project, skills([candidates[cand]]))

        for i in cskill:
            if i in project:
                project.remove(i)
                covered = covered + 1

        if covered != 0:
            bestc.append(candidates[cand])
            candidates.remove(candidates[cand])
            project = ucproject
        elif covered == 0:
            continue

    return bestc

def best_team(project,candidates):
    team = []
    finallist= []
    costlist = []
    finalteam = []

    def bitlists(n):
        first = (len(n))*[0]
        last = n
        res = [first]
        while res[-1] != last:
            res += [lex_suc(res[-1],n)]
        return res


    def lex_suc(bitlst,n):
        res = bitlst[:]
        i = len(res) - 1
        while res[i] == n[i]:
            res[i] = 0
            i -= 1
        res[i] += 1
        return res

# Codes for bitlists and lex_suc obtained from
# Week 6 Lecture 11 slide 26
# Citation:
# Monash (n.d.). Lec11_Brute_Force, week 6, slide 26. Retrieved from https://lms.monash.edu/pluginfile.php/8757727/mod_resource/content/1/Lec11_Brute_Force.pdf

# Generates numbers based on number of candidates from 0000 to 1*(number of candidates)
# In this case, 0000 to 1111, where 0 means the candidate is not chosen and 1 means that the candidate is chosen

    candp = bitlists([1]*len(candidates))
    print(candp)
    for i in range(len(candp)):
        templist = []
        for j in range(len(candp[0])):
            if candp[i][j] == 1:
                templist.append(candidates[j])
                print(candidates[j])
        finallist.append(templist)

# Finds the teams out of all possible combinations that covers all the skills needed

    for i in range(len(finallist)):
        if uncovered(project,skills(finallist[i])) == []:
            finalteam.append(finallist[i])
            costlist.append(cost(finallist[i]))

# Finds the final team that has the lowest cost required and fulfils all required needs            
    minindex = costlist.index(min(costlist))       
    return finalteam[minindex]
