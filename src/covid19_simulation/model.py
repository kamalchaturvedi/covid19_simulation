from numpy.random import lognormal
from math import log, sqrt, erf, exp, pi
from matplotlib import pyplot as plt

class CovidModel:
    r0_range=[1.5,2.5,3.5]
    prob_asymptomatic_individuals = 0.4
    i_individual = [0.1]
    incubation_mean = 1.644
    incubation_st_deviation = 0.363
    environmental_factor = 3
    asymptomic_to_symptomaic_ratio = 0.1
    i_asymptomatic = []
    i_pre_symptomatic = []
    i_symptomatic = []
    i_environmental = []
    i_total = []
    time = 0

    def incubationPeriodProbCDF(self):
        temp = (log(self.time+0.01) - self.incubation_mean)/sqrt(2*self.incubation_st_deviation**2)
        prob = 0.5 + 0.5*erf(temp)
        print("prob",prob)
        return prob
    
    def incubationPeriodProbPDF(self):
        time = self.time + 0.01
        temp = exp(-(log(time) - self.incubation_mean)**2/(2*self.incubation_st_deviation**2))
        prob = (1/(time*self.incubation_st_deviation*sqrt(2*pi)))*temp
        print("prob",prob)
        return prob

    def environmental_infectiousness(self):
        i_environmental = 0;
        for i in range(0, self.time):
            i_environmental += self.i_individual[i]*self.environmental_factor
        return i_environmental

    def infectiousnessModel(self):
        i_asymptomatic = self.prob_asymptomatic_individuals*self.asymptomic_to_symptomaic_ratio*self.i_individual[self.time]
        i_pre_symptomatic = (1-self.prob_asymptomatic_individuals)*(1-self.incubationPeriodProbCDF())*self.i_individual[self.time]
        i_symptomatic = (1-self.prob_asymptomatic_individuals)*self.incubationPeriodProbCDF() *self.i_individual[self.time]
        i_environmental = 0
        print(i_asymptomatic, i_pre_symptomatic, i_symptomatic, i_environmental)
        infectiousness = i_asymptomatic + i_pre_symptomatic + i_symptomatic + i_environmental
        # set infectiousness of individual for current time instant
        self.i_individual.append(i_pre_symptomatic+i_symptomatic)
        self.time += 1
        self.i_asymptomatic.append(i_asymptomatic)
        self.i_pre_symptomatic.append(i_pre_symptomatic)
        self.i_symptomatic.append(i_symptomatic)
        self.i_environmental.append(i_environmental)
        self.i_total.append(infectiousness)
        return infectiousness

    def plotInfectiousness(self):
        plt.plot(self.i_asymptomatic, label='Asymptomatic')
        plt.plot(self.i_pre_symptomatic, label='Presymptomatic')
        plt.plot(self.i_symptomatic, label='Symptomatic')
        plt.plot(self.i_total, label='Total Infectiousness')
        plt.plot(self.i_individual, label='Individual')
        plt.xlabel("Time (days)")
        plt.ylabel("Infectiousness")
        plt.legend()
        plt.show()