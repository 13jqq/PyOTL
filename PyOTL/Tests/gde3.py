"""
Copyright (C) 2014, 申瑞珉 (Ruimin Shen)

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU Lesser General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""

import os
import unittest
import numpy
import scipy.stats
import pyotl.utility
import pyotl.problem.real
import pyotl.initial.real
import pyotl.crossover.real
import pyotl.mutation.real
import pyotl.indicator.real
import pyotl.optimizer.real
import pyotl.optimizer.xtriple.real

class TestCase(unittest.TestCase):
	def setUp(self):
		self.pathData = os.path.join(os.path.dirname(__file__), 'Data')
		self.repeat = 30
	
	def tearDown(self):
		pass
	
	def testGDE3(self):
		random = pyotl.utility.Random(1)
		problemGen = lambda: pyotl.problem.real.DTLZ2(3)
		problem = problemGen()
		pathProblem = os.path.join(self.pathData, type(problem).__name__, str(problem.GetNumberOfObjectives()))
		crossover = pyotl.crossover.real.DifferentialEvolution(random, 0.5, problem.GetBoundary(), 0.5)
		mutation = pyotl.mutation.real.PolynomialMutation(random, 0, problem.GetBoundary(), 20)
		pfList = []
		for _ in range(self.repeat):
			problem = problemGen()
			initial = pyotl.initial.real.PopulationUniform(random, problem.GetBoundary(), 100)
			optimizer = pyotl.optimizer.xtriple.real.GDE3(random, problem, initial, crossover, mutation)
			while optimizer.GetProblem().GetNumberOfEvaluations() < 30000:
				optimizer()
			pf = pyotl.utility.PyListList2VectorVector_Real([list(solution.objective_) for solution in optimizer.GetSolutionSet()])
			pfList.append(pf)
		pathCrossover = os.path.join(pathProblem, type(crossover).__name__)
		pathOptimizer = os.path.join(pathCrossover, type(optimizer).__name__)
		pfTrue = pyotl.utility.PyListList2VectorVector_Real(numpy.loadtxt(os.path.join(pathProblem, 'PF.csv')).tolist())
		#GD
		indicator = pyotl.indicator.real.DTLZ2GD()
		metricList = [indicator(pf) for pf in pfList]
		rightList = numpy.loadtxt(os.path.join(pathOptimizer, 'GD.csv')).tolist()
		self.assertGreater(scipy.stats.ttest_ind(rightList, metricList)[1], 0.05, [numpy.mean(rightList), numpy.mean(metricList), metricList])
		#IGD
		indicator = pyotl.indicator.real.InvertedGenerationalDistance(pfTrue)
		metricList = [indicator(pf) for pf in pfList]
		rightList = numpy.loadtxt(os.path.join(pathOptimizer, 'IGD.csv')).tolist()
		self.assertGreater(scipy.stats.ttest_ind(rightList, metricList)[1], 0.05, [numpy.mean(rightList), numpy.mean(metricList), metricList])

if __name__ == '__main__':
	unittest.main()