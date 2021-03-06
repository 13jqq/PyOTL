/*!
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
*/

#pragma once

#include <OTL/Optimizer/SMS-EMOA/XTriple/SMS-EMOA.h>
#include "../MakeHypervolume.h"

namespace pyotl
{
namespace optimizer
{
namespace sms_emoa
{
namespace xtriple
{
template <typename _TReal, typename _TDecision, typename _TRandom>
class SMS_EMOA : public otl::optimizer::sms_emoa::xtriple::SMS_EMOA<_TReal, _TDecision, _TRandom, MakeHypervolume<_TReal> >
{
public:
	typedef _TReal TReal;
	typedef _TDecision TDecision;
	typedef _TRandom TRandom;
	typedef MakeHypervolume<TReal> TMakeHypervolume;
	typedef otl::optimizer::sms_emoa::xtriple::SMS_EMOA<TReal, TDecision, TRandom, TMakeHypervolume> TSuper;
	typedef typename TSuper::TIndividual TIndividual;
	typedef typename TSuper::TSolutionSet TSolutionSet;
	typedef typename TSuper::TProblem TProblem;
	typedef typename TSuper::TCrossover TCrossover;
	typedef typename TSuper::TMutation TMutation;

	SMS_EMOA(TRandom random, TProblem &problem, const std::vector<TDecision> &initial, TCrossover &crossover, TMutation &mutation);
	~SMS_EMOA(void);
};

template <typename _TReal, typename _TDecision, typename _TRandom>
SMS_EMOA<_TReal, _TDecision, _TRandom>::SMS_EMOA(TRandom random, TProblem &problem, const std::vector<TDecision> &initial, TCrossover &crossover, TMutation &mutation)
	: TSuper(random, problem, initial, crossover, mutation, TMakeHypervolume())
{
}

template <typename _TReal, typename _TDecision, typename _TRandom>
SMS_EMOA<_TReal, _TDecision, _TRandom>::~SMS_EMOA(void)
{
}
}
}
}
}
